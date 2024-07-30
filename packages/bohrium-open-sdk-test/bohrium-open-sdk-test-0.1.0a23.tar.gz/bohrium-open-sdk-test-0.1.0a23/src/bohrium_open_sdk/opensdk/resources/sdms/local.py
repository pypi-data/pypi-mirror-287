import os
import json
import shutil
import uuid
from .response import ErrorCode, SdmsResponse
from .sdms import Sdms


class SdmsLocal(Sdms):
    def __init__(self, client, base_path):
        self.base_path = base_path

    def add_characterization_file(
        self,
        uploader_id: int,
        owner_id: int,
        machine_model: str,
        sample_id: str,
        char_data_name: str,
        char_type: str,
        allowed_suffixes=["xlsx", "pdf", "csv", "xls"],
        description="",
        temp_file_path="",
    ) -> SdmsResponse:

        try:
            # 检查文件后缀
            if not self._check_file_suffix(char_data_name, allowed_suffixes):
                return SdmsResponse(ErrorCode.INVALID_FILE_SUFFIX).json

            # 生成UUID
            file_uuid = str(uuid.uuid4())

            # 构建JSON数据
            data = {
                "uploader_id": uploader_id,
                "owner_id": owner_id,
                "machine_model": machine_model,
                "sample_id": sample_id,
                "char_data_name": char_data_name,
                "char_type": char_type,
                "allowed_suffixes": allowed_suffixes,
                "file_suffix": os.path.splitext(char_data_name)[1][1:].lower(),
                "description": description,
                "uuid": file_uuid,
                "file_path": f"{self.base_path}/raw_data/{owner_id}/{char_data_name}",
            }

            # 确保目录存在
            os.makedirs(f"{self.base_path}/raw_data/{owner_id}", exist_ok=True)
            os.makedirs(f"{self.base_path}/meta/{owner_id}", exist_ok=True)

            # 确保临时文件存在
            if not os.path.exists(temp_file_path):
                return SdmsResponse(ErrorCode.FILE_NOT_FOUND).json

            # 原数据
            meta_file_path = self._get_meta_file_path(owner_id, char_data_name)

            # 如果原数据已存在，则返回错误
            if os.path.exists(meta_file_path):
                return SdmsResponse(ErrorCode.FILE_EXISTS).json

            with open(meta_file_path, "w") as f:
                json.dump(data, f, indent=4)

            # 复制文件
            shutil.copy2(temp_file_path, data["file_path"])

            return SdmsResponse(ErrorCode.SUCCESS).json

        except Exception as e:
            return SdmsResponse(code=ErrorCode.UNKNOWN_ERROR, err_msg=str(e)).json

    def delete_characterization_file(self, user_id, char_data_name) -> SdmsResponse:

        try:
            # 文件不存在, 直接返回成功
            meta_file_path = self._get_meta_file_path(user_id, char_data_name)
            if not os.path.exists(meta_file_path):
                return SdmsResponse(ErrorCode.SUCCESS).json

            # 读取JSON文件
            with open(meta_file_path, "r") as f:
                data = json.load(f)

            # 删除原始数据文件
            os.remove(data["file_path"])

            # 删除JSON文件
            os.remove(meta_file_path)

            return SdmsResponse(ErrorCode.SUCCESS).json
        except Exception as e:
            return SdmsResponse(code=ErrorCode.UNKNOWN_ERROR, err_msg=str(e)).json

    def query_characterization_files(self, user_id, key_name) -> SdmsResponse:

        try:
            # 获取用户目录下的所有文件
            meta_dir = f"{self.base_path}/meta/{user_id}"
            if not os.path.exists(meta_dir):
                return SdmsResponse(ErrorCode.SUCCESS, []).json

            files = os.listdir(meta_dir)
            result = []
            for file in files:
                if key_name in file:
                    with open(f"{meta_dir}/{file}", "r") as f:
                        data = json.load(f)
                        result.append(data)

            return SdmsResponse(ErrorCode.SUCCESS, result).json
        except Exception as e:
            return SdmsResponse(code=ErrorCode.UNKNOWN_ERROR, err_msg=str(e)).json

    def get_characterization_file(self, owner_id, char_data_name) -> SdmsResponse:

        try:
            # 读取JSON文件
            meta_file_path = self._get_meta_file_path(owner_id, char_data_name)
            with open(meta_file_path, "r") as f:
                meta_data = json.load(f)

            # 判断文件是否存在
            raw_data_path = meta_data["file_path"]

            if not os.path.exists(raw_data_path):
                return SdmsResponse(ErrorCode.FILE_NOT_FOUND).json

            # 读取原始数据文件
            data = self.read_in_chunks(raw_data_path)

            result = {"meta_data": meta_data, "raw_data": data}
            return SdmsResponse(ErrorCode.SUCCESS, result).json
        except FileNotFoundError:
            return SdmsResponse(ErrorCode.FILE_NOT_FOUND).json
        except Exception as e:
            return SdmsResponse(code=ErrorCode.UNKNOWN_ERROR, err_msg=str(e)).json
