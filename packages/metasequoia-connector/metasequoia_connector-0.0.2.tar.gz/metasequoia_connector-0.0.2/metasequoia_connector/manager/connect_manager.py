import json
import os
from typing import Dict, Any, List, Optional

from metasequoia_connector.connector import MysqlConnector, DSMetaConnector
from metasequoia_connector.node import KafkaServer, DSMetaInstance, SshTunnel, MysqlInstance, HiveInstance, OTSInstance

__all__ = ["ConnectManager", "MODE"]

MODE = "dev"

# 配置文件的默认环境变量名称
DEFAULT_METASEQUOIA_CONNECTOR_CONFIG_NAME = "METASEQUOIA_CONNECTOR_CONFIG"


# TODO 将配置输出到文件：https://www.cnblogs.com/wengzx/p/18019494


class ConnectManager:
    ENCODING = "UTF-8"  # 编码格式

    def __init__(self, config_path: str):
        # 从配置文件中读取配置信息
        with open(config_path, "r", encoding=self.ENCODING) as file:
            self._configuration = json.load(file)

    @classmethod
    def from_environment(cls, environ_name: Optional[str] = None):
        """从环境变量中读取配置文件路径，并加载配置文件

        Parameters
        ----------
        environ_name : Optional[str], default = None
            环境变量名称，如果为空则使用默认名称
        """
        if environ_name is None:
            environ_name = DEFAULT_METASEQUOIA_CONNECTOR_CONFIG_NAME
        config_path = os.environ.get(environ_name)
        return ConnectManager(config_path)  # 实现配置信息的单例

    # ---------- 读取 MySQL 相关配置 ----------

    def get_mysql_list(self) -> List[str]:
        """获取 MySQL 列表"""
        return list(self._configuration.get("MySQL", {}).keys())

    def get_mysql_info(self, name: str, mode: str = MODE) -> Dict[str, Any]:
        """获取 MySQL 信息"""
        return self._confirm_params("MySQL", self._get_section("MySQL", name, mode), ["host", "port", "user"])

    def get_mysql_instance(self, name: str) -> MysqlInstance:
        """获取 MysqlInstance 对象"""
        mysql_info = self.get_mysql_info(name)
        ssh_tunnel = self.get_ssh_tunnel(mysql_info["use_ssh"]) if mysql_info.get("use_ssh") else None
        return MysqlInstance(host=mysql_info["host"],
                             port=mysql_info["port"],
                             user=mysql_info["user"],
                             passwd=mysql_info["passwd"],
                             ssh_tunnel=ssh_tunnel)

    def get_mysql_name(self, name: str) -> str:
        """获取 MySQL 的名称"""
        return self._configuration["MySQL"][name].get("_name", "")

    def get_mysql_type(self, name: str) -> str:
        """获取 MySQL 的类型"""
        return self._configuration["MySQL"][name].get("_type", "")

    def get_mysql_type_list(self):
        """获取 MySQL 的所有类型"""
        return {self.get_mysql_type(mysql_name) for mysql_name in self.get_mysql_list()}

    def connect_mysql_by_name(self, name: str, schema_name: Optional[str] = None):
        """根据实例名称，创建 MySQL 连接器"""
        mysql_instance = self.get_mysql_instance(name)
        return MysqlConnector.create_by_instance(mysql_instance=mysql_instance, schema=schema_name)

    # ---------- 读取 SSH 相关配置 ----------

    def get_ssh(self, name: str, mode: str = MODE) -> Dict[str, Any]:
        """获取 SSH 信息"""
        return self._confirm_params("SSH", self._get_section("SSH", name, mode), ["host", "port"])

    def get_ssh_tunnel(self, name: str) -> SshTunnel:
        """获取 SshTunnel 对象"""
        ssh_info = self.get_ssh(name)
        return SshTunnel(host=ssh_info["host"],
                         port=ssh_info["port"],
                         username=ssh_info["username"],
                         pkey=ssh_info["pkey"])

    def get_ssh_list(self):
        """获取 SSH 列表"""
        return list(self._configuration["SSH"].keys())

    # ---------- 读取 Kafka 相关配置 ----------

    def get_kafka_list(self) -> List[str]:
        """获取 Kafka 列表"""
        return list(self._configuration.get("Kafka", {}).keys())

    def get_kafka_info(self, name: str, mode: str = MODE) -> Dict[str, Any]:
        return self._confirm_params("Kafka", self._get_section("Kafka", name, mode), ["bootstrap_servers"])

    def get_kafka_server(self, name: str) -> KafkaServer:
        """获取 Kafka Servers 对象"""
        kafka_info = self.get_kafka_info(name)
        ssh_tunnel = self.get_ssh_tunnel(kafka_info["use_ssh"]) if kafka_info.get("use_ssh") else None
        return KafkaServer(bootstrap_servers=kafka_info["bootstrap_servers"],
                           ssh_tunnel=ssh_tunnel)

    # ---------- 读取 Hive 相关配置 ----------

    def get_hive_list(self) -> List[str]:
        """获取 Hive 列表"""
        return list(self._configuration.get("Hive", {}).keys())

    def get_hive_info(self, name: str, mode: str = MODE) -> Dict[str, Any]:
        return self._confirm_params("Hive", self._get_section("Hive", name, mode), ["hosts", "port"])

    def get_hive_instance(self, name: str) -> HiveInstance:
        """获取 Hive 列表"""
        hive_info = self.get_hive_info(name)
        ssh_tunnel = self.get_ssh_tunnel(hive_info["use_ssh"]) if hive_info.get("use_ssh") else None
        return HiveInstance(hosts=hive_info["hosts"], port=hive_info["port"],
                            ssh_tunnel=ssh_tunnel)

    # ---------- 读取 DolphinScheduler 相关配置 ----------

    def get_dolphin_meta_list(self) -> List[str]:
        """获取海豚调度元数据清单"""
        return list(self._configuration["DolphinMeta"])

    def get_dolphin_meta_info(self, name: str, mode: str = MODE) -> Dict[str, Any]:
        """获取海豚调度元数据信息"""
        return self._get_section("DolphinMeta", name, mode)

    def get_dolphin_meta_instance(self, name: str) -> DSMetaInstance:
        """获取海豚调度元数据的 DolphinMetaInstance 对象"""
        dolphin_meta_info = self.get_dolphin_meta_info(name)
        ssh_tunnel = self.get_ssh_tunnel(dolphin_meta_info["use_ssh"]) if dolphin_meta_info.get("use_ssh") else None
        return DSMetaInstance(
            host=dolphin_meta_info["host"],
            port=dolphin_meta_info["port"],
            user=dolphin_meta_info["user"],
            passwd=dolphin_meta_info["passwd"],
            db=dolphin_meta_info["db"],
            ssh_tunnel=ssh_tunnel
        )

    def connect_dolphin_by_name(self, name: str):
        """根据海豚元数据名称，创建海豚元数据连接器"""
        dolphin_meta_instance = self.get_dolphin_meta_instance(name)
        return DSMetaConnector(dolphin_scheduler_meta_info=dolphin_meta_instance)

    # ---------- 读取 OTS 相关配置 ----------

    def get_ots_list(self) -> List[str]:
        """获取 OTS 元数据清单"""
        return list(self._configuration["OTS"])

    def get_ots_info(self, name: str, mode: str = MODE) -> Dict[str, Any]:
        """获取 OTS 元数据信息"""
        return self._get_section("OTS", name, mode)

    def get_ots_instance(self, name: str) -> OTSInstance:
        """获取 OTS 元数据的 OTSInstance 对象"""
        ots_info = self.get_ots_info(name)
        return OTSInstance(
            end_point=ots_info["end_point"],
            access_key_id=ots_info["access_key_id"],
            access_key_secret=ots_info["access_key_secret"],
            instance_name=ots_info["instance_name"]
        )

    # ---------- 其他工具方法 ----------

    def _get_section(self, section: str, name: str, mode: str) -> Dict[str, Any]:
        """获取每种类型的配置信息数据"""
        if section not in self._configuration or name not in self._configuration[section]:
            return {}
        config = self._configuration[section][name].get("mode:common", {}).copy()  # 先加载通用配置
        config.update(self._configuration[section][name].get(f"mode:{mode}", {}))  # 然后再加对应模式的配置
        return config

    @staticmethod
    def _confirm_params(section: str, config: Dict[str, Any], params: List[str]) -> Dict[str, Any]:
        """检查参数是否满足"""
        for param in params:
            assert param in config, f"param {param} not in {section} config"
        return config

    @classmethod
    def make_templates(cls, path: str):
        """在指定路径下生成模板配置文件"""
        if os.path.exists(path):
            raise ValueError(f"配置文件已存在({path}),创建模板文件失败!")
        with open(path, "w", encoding=cls.ENCODING) as file:
            file.write(json.dumps(
                {"MySQL": {"localhost": {"host": "localhost", "port": 3306, "user": "root", "passwd": "123456"}},
                 "SSH": {"demo": {"host": "...", "port": "...", "username": "...", "pkey": "..."}}}))
            print("配置文件模板生成完成")
