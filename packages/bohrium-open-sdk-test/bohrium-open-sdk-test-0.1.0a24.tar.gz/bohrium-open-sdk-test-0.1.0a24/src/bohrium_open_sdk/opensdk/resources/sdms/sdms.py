import os
from .response import SdmsResponse
from bohrium_open_sdk.opensdk._resource import SyncAPIResource


class Sdms(SyncAPIResource):
    def __init__(self, client):
        base_path = os.getenv("SDMS_BASE_PATH")
        if base_path:
            self.base_path = base_path
        else:
            self.base_path = "/tmp/sdms"
            # 警告！
            print(
                "\033[93m[Warning] SDMS_BASE_PATH is not set, use default path: /tmp/sdms\033[0m"
            )
        # if storage_type == "oss":
        #     return SdmsOss(*args, **kwargs)
        # else:
        from .local import SdmsLocal  # type: ignore

        self.client = SdmsLocal(client, self.base_path)

    def _ensure_base_path(self):
        """确保基础路径存在"""
        if not os.path.exists(self.base_path):
            try:
                os.makedirs(self.base_path)
                print(f"Created base directory: {self.base_path}")
            except Exception as e:
                print(f"Error creating base directory: {e}")
                raise

    def _check_file_suffix(self, filename, allowed_suffixes):
        """
        检查文件后缀是否在允许的列表中（不区分大小写）

        参数:
        filename: 文件名
        allowed_suffixes: 允许的后缀列表

        返回:
        如果后缀有效返回True，否则返回False
        """
        file_suffix = os.path.splitext(filename)[1][1:].lower()
        return file_suffix.lower() in [suffix.lower() for suffix in allowed_suffixes]

    def _get_meta_file_path(self, owner_id, char_data_name):
        """获取元数据文件路径

        Args:
            owner_id (_type_): 归属用户id
            char_data_name (_type_): 表征数据名

        Returns:
            _type_: str
        """
        # json名要替换调原始数据的后缀
        json_file_name = os.path.splitext(char_data_name)[0] + ".json"
        return f"{self.base_path}/meta/{owner_id}/{json_file_name}"

    def read_in_chunks(self, file_path, chunk_size=1024 * 1024):
        """
        Lazy function (generator) to read a file piece by piece.
        """
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            return "".join(iter(lambda: f.read(chunk_size), ""))

    def add_characterization_buffer(
        self,
        uploader_id: int,
        owner_id: int,
        machine_model: str,
        sample_id: str,
        char_data_name: str,
        char_type: str,
        allowed_suffixes=["xlsx", "pdf", "csv", "xls"],
        description="",
        buffer="",
    ) -> SdmsResponse:
        """
        添加表征缓冲区

        参数说明:
        uploader_id: 上传用户id
        owner_id: 归属用户id
        machine_model: 机器型号
        sample_id: 样本id
        char_data_name: 表征数据名
        char_type: 表征类型
        allowed_suffixes: 表征文件名支持后缀列表
        description: 描述
        buffer: 缓冲区

        owner_id + char_data_name 作为唯一标识

        返回: SdmsResponse code 为0成功，否则失败
        """
        self._ensure_base_path()
        return self.client.add_characterization_buffer(
            uploader_id,
            owner_id,
            machine_model,
            sample_id,
            char_data_name,
            char_type,
            allowed_suffixes,
            description,
            buffer,
        )

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
        """
        添加表征文件

        参数说明:
        uploader_id: 上传用户id
        owner_id: 归属用户id
        machine_model: 机器型号
        sample_id: 样本id
        char_data_name: 表征数据名
        char_type: 表征类型
        allowed_suffixes: 表征文件名支持后缀列表
        description: 描述
        temp_file_path: 临时文件路径

        owner_id + char_data_name 作为唯一标识

        返回: SdmsResponse code 为0成功，否则失败
        """

        self._ensure_base_path()
        return self.client.add_characterization_file(
            uploader_id,
            owner_id,
            machine_model,
            sample_id,
            char_data_name,
            char_type,
            allowed_suffixes,
            description,
            temp_file_path,
        )

    def delete_characterization_file(self, owner_id, char_data_name) -> SdmsResponse:
        """
        删除表征文件

        参数说明:
        owner_id: 归属用户id
        char_data_name: 表征数据名

        返回: SdmsResponse
        code 为0成功，否则失败
        """
        self._ensure_base_path()
        return self.client.delete_characterization_file(owner_id, char_data_name)

    def query_characterization_files(self, owner_id, key_name) -> SdmsResponse:
        """
        根据关键词查询表征文件列表

        参数说明:
        owner_id: 归属用户id
        key_name: 关键词, 匹配文件名称

        返回: SdmsResponse code 为0成功，否则失败
        """
        self._ensure_base_path()
        return self.client.query_characterization_files(owner_id, key_name)

    def get_characterization_file(self, owner_id, char_data_name) -> SdmsResponse:
        """
        获取表征文件内容

        参数说明:
        owner_id: 归属用户id
        char_data_name: 表征数据名

        返回: SdmsResponse code 为0成功，否则失败
        """
        self._ensure_base_path()
        return self.client.get_characterization_file(owner_id, char_data_name)
