"""
OTS 连接器
"""

import ssl
from typing import Optional

import otssql
from metasequoia_connector.node import SshTunnel, OTSInstance

__all__ = ["OTSConnector"]


class OTSConnector:
    def __init__(self, ots_instance: OTSInstance, ssh_tunnel_info: Optional[SshTunnel], **params) -> None:
        """OTS 连接的构造方法

        Parameters
        ----------
        ots_instance : OTSInstance
            OTS 实例的对象
        ssh_tunnel_info : Optional[SshTunnel]
            SSH 隧道的对象 TODO 暂未生效
        """
        self.ots_instance = ots_instance  # MySQl 实例的配置
        self.ssh_tunnel_info = ssh_tunnel_info  # SSH 隧道的配置
        self.params = params

        # 初始化 MySQL 连接和 SSH 隧道连接
        self.ots_conn: Optional[otssql.Connection] = None
        self.ssh_tunnel = None

    @staticmethod
    def create_by_rds_instance(ots_instance: OTSInstance, **params) -> "OTSConnector":
        """根据 OTSInstance 构造"""
        return OTSConnector(ots_instance=ots_instance, ssh_tunnel_info=None, **params)

    @staticmethod
    def create_by_rds_name(configuration, name: str, **params) -> "OTSConnector":
        # 读取 MySQL 实例的配置
        ots_instance = configuration.get_ots_instance(name)
        ssh_tunnel_info = None
        return OTSConnector(ots_instance=ots_instance, ssh_tunnel_info=ssh_tunnel_info, **params)

    def __enter__(self):
        """在进入 with as 语句的时候被 with 调用，返回值作为 as 后面的变量"""
        self.ots_conn = otssql.connect(
            end_point=self.ots_instance.end_point,
            access_key_id=self.ots_instance.access_key_id,
            access_key_secret=self.ots_instance.access_key_secret,
            instance_name=self.ots_instance.instance_name,
            ssl_version=ssl.PROTOCOL_TLSv1_2,
            **self.params
        )
        return self.ots_conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.ots_conn is not None:
            self.ots_conn.close()
        if self.ssh_tunnel is not None:
            self.ssh_tunnel.close()
