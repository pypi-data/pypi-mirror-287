from typing import Optional

from metasequoia_connector.connector import *
from metasequoia_connector.manager import ConnectManager
from metasequoia_connector.node import *
from metasequoia_connector.utils import kafka, dolphin, mysql, hive, sql_format


def from_environment(environ_name: Optional[str] = None) -> ConnectManager:
    """从环境变量中读取配置文件路径，并加载配置文件"""
    return ConnectManager.from_environment(environ_name)


del Optional
