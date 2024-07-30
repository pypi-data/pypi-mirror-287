import os
import json
import shutil
import uuid
from .response import ErrorCode, SdmsResponse
from .sdms import Sdms
from datetime import datetime
import time
from operator import itemgetter


class SdmsLocal(Sdms):
    def __init__(self, client, base_path):
        self.base_path = base_path

    def _add_characterization_preare(
        self,
        uploader_user_id: int,
        owner_id: int,
        char_techs: str,
        sample_id: str,
        name: str,
        type: str,
        allowed_suffixes=["xlsx", "pdf", "csv", "xls"],
        suffix="",
        description="",
    ):
        # 生成UUID
        file_uuid = str(uuid.uuid4())

        # 构建JSON数据
        data = {
            "uploader_user_id": uploader_user_id,
            "owner_id": owner_id,
            "char_techs": char_techs,
            "sample_id": sample_id,
            "name": name,
            "type": type,
            "allowed_suffixes": allowed_suffixes,
            "file_suffix": suffix,
            "description": description,
            "uuid": file_uuid,
            "file_path": f"{self.base_path}/raw_data/{owner_id}/{name}.{suffix}",
            "create_timestamp": int(time.time()),
            "create_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }

        # 确保目录存在
        os.makedirs(f"{self.base_path}/raw_data/{owner_id}", exist_ok=True)
        os.makedirs(f"{self.base_path}/meta/{owner_id}", exist_ok=True)

        # 原数据
        meta_file_path = self._get_meta_file_path(owner_id, name)

        return data, meta_file_path

    def add_characterization_buffer(
        self,
        uploader_user_id: int,
        owner_id: int,
        char_techs: str,
        sample_id: str,
        name: str,
        type: str,
        allowed_suffixes=["xlsx", "pdf", "csv", "xls"],
        description="",
        buffer="",
        suffix="",
    ) -> SdmsResponse:

        try:
            # 检查文件后缀
            res = self._check_file_suffix("", suffix, allowed_suffixes)
            if not res[1]:
                return SdmsResponse(ErrorCode.INVALID_FILE_SUFFIX).json

            data, meta_file_path = self._add_characterization_preare(
                uploader_user_id,
                owner_id,
                char_techs,
                sample_id,
                name,
                type,
                allowed_suffixes,
                res[0],
                description,
            )

            # 如果原数据已存在，则返回错误
            if os.path.exists(meta_file_path):
                return SdmsResponse(ErrorCode.FILE_EXISTS).json

            with open(meta_file_path, "w") as f:
                json.dump(data, f, indent=4)

            # 写入文件
            # 检查数据类型
            if isinstance(buffer, str):
                # 如果是字符串，使用文本写入模式
                with open(data["file_path"], "w", encoding="utf-8") as file:
                    file.write(buffer)
            elif isinstance(buffer, bytes):
                # 如果是二进制数据，使用二进制写入模式
                with open(data["file_path"], "wb") as file:
                    file.write(buffer)
            else:
                raise ValueError("不支持的数据类型。数据必须是字符串或二进制。")

            return SdmsResponse(ErrorCode.SUCCESS).json

        except Exception as e:
            return SdmsResponse(code=ErrorCode.UNKNOWN_ERROR, err_msg=str(e)).json

    def add_characterization_file(
        self,
        uploader_user_id: int,
        owner_id: int,
        char_techs: str,
        sample_id: str,
        name: str,
        type: str,
        allowed_suffixes=["xlsx", "pdf", "csv", "xls"],
        description="",
        temp_file_path="",
        suffix="",
    ) -> SdmsResponse:

        try:
            # 检查文件后缀
            res = self._check_file_suffix(temp_file_path, suffix, allowed_suffixes)
            if not res[1]:
                return SdmsResponse(ErrorCode.INVALID_FILE_SUFFIX).json

            # 确保临时文件存在
            if not os.path.exists(temp_file_path):
                return SdmsResponse(ErrorCode.FILE_NOT_FOUND).json

            data, meta_file_path = self._add_characterization_preare(
                uploader_user_id,
                owner_id,
                char_techs,
                sample_id,
                name,
                type,
                allowed_suffixes,
                res[0],
                description,
            )

            # 原数据
            meta_file_path = self._get_meta_file_path(owner_id, name)

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

    def delete_characterization_file(self, user_id, name) -> SdmsResponse:

        try:
            # 文件不存在, 直接返回成功
            meta_file_path = self._get_meta_file_path(user_id, name)
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

    def get_characterization_file(self, owner_id, name) -> SdmsResponse:

        try:
            # 读取JSON文件
            meta_file_path = self._get_meta_file_path(owner_id, name)
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

    def result_add(self, owner_id: int, name: str, context: str) -> SdmsResponse:

        result_file_path = self._get_result_file_path(owner_id, name)
        if os.path.exists(result_file_path):
            return SdmsResponse(ErrorCode.FILE_EXISTS).json

        timestamp = int(time.time())
        yyyymmdd = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # 构建JSON数据
        data = {
            "owner_id": owner_id,
            "name": name,
            "result": context,
            "create_timestamp": timestamp,
            "create_time": yyyymmdd,
            "update_timestamp": timestamp,
            "update_time": yyyymmdd,
        }

        # 确保目录存在
        os.makedirs(f"{self.base_path}/result/{owner_id}", exist_ok=True)

        try:
            # 写入文件
            with open(result_file_path, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)

            return SdmsResponse(ErrorCode.SUCCESS).json
        except Exception as e:
            return SdmsResponse(code=ErrorCode.UNKNOWN_ERROR, err_msg=str(e)).json

    def result_put(self, owner_id: int, name: str, context: str) -> SdmsResponse:

        result_file_path = self._get_result_file_path(owner_id, name)
        if not os.path.exists(result_file_path):
            return SdmsResponse(ErrorCode.FILE_NOT_FOUND).json

        # 读取现有数据
        datastr = self.read_in_chunks(result_file_path)
        data = json.loads(datastr)
        data["update_timestamp"] = int(time.time())
        data["update_time"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data["result"] = context

        try:
            # 写入文件
            with open(result_file_path, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)

            return SdmsResponse(ErrorCode.SUCCESS).json
        except Exception as e:
            return SdmsResponse(code=ErrorCode.UNKNOWN_ERROR, err_msg=str(e)).json

    def result_delete(self, owner_id: int, name: str) -> SdmsResponse:

        result_file_path = self._get_result_file_path(owner_id, name)
        if not os.path.exists(result_file_path):
            return SdmsResponse(ErrorCode.SUCCESS).json

        try:
            os.remove(result_file_path)
            return SdmsResponse(ErrorCode.SUCCESS).json
        except Exception as e:
            return SdmsResponse(code=ErrorCode.UNKNOWN_ERROR, err_msg=str(e)).json

    def result_query(self, owner_id: int, key_name: str) -> SdmsResponse:

        try:
            # 获取用户目录下的所有文件
            result_dir = f"{self.base_path}/result/{owner_id}"
            if not os.path.exists(result_dir):
                return SdmsResponse(ErrorCode.SUCCESS, []).json

            # 获取文件列表并添加修改时间
            files = []
            for file in os.listdir(result_dir):
                if key_name in file:
                    file_path = os.path.join(result_dir, file)
                    update_time = os.path.getmtime(file_path)
                    files.append((file, update_time))
            # 按修改时间倒序排序
            files.sort(key=itemgetter(1), reverse=True)
            result = []
            # 剔除文件后缀
            for file, _ in files:
                result.append(os.path.splitext(file)[0])

            return SdmsResponse(ErrorCode.SUCCESS, result).json
        except Exception as e:
            return SdmsResponse(code=ErrorCode.UNKNOWN_ERROR, err_msg=str(e)).json

    def result_get(self, owner_id: int, name: str) -> SdmsResponse:

        try:
            result_file_path = self._get_result_file_path(owner_id, name)
            if not os.path.exists(result_file_path):
                return SdmsResponse(ErrorCode.FILE_NOT_FOUND).json

            data = self.read_in_chunks(result_file_path)

            return SdmsResponse(ErrorCode.SUCCESS, data).json
        except FileNotFoundError:
            return SdmsResponse(ErrorCode.FILE_NOT_FOUND).json
        except Exception as e:
            return SdmsResponse(code=ErrorCode.UNKNOWN_ERROR, err_msg=str(e)).json
