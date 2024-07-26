"""
Kafka 连接器：基于 kafka-python
"""

from typing import Optional

import sshtunnel
from kafka import KafkaConsumer, KafkaProducer
from kafka.admin import KafkaAdminClient

from metasequoia_connector.node import KafkaServer

__all__ = ["ConnKafkaAdminClient", "ConnKafkaConsumer", "ConnKafkaProducer"]


class ConnKafkaAdminClient:
    """根据 KafkaServer 对象创建 kafka-python 的 KafkaAdminClient 对象"""

    def __init__(self, kafka_server: KafkaServer):
        self.kafka_server = kafka_server  # MySQl 实例的配置

        # 初始化 MySQL 连接和 SSH 隧道连接
        self.kafka_admin_client = None
        self.ssh_tunnel = None

    def __enter__(self):
        """在进入 with as 语句的时候被 with 调用，返回值作为 as 后面的变量"""
        if self.kafka_server.ssh_tunnel is not None:
            # 启动 SSH 隧道
            self.ssh_tunnel = sshtunnel.SSHTunnelForwarder(
                ssh_address_or_host=self.kafka_server.ssh_tunnel.address,
                ssh_username=self.kafka_server.ssh_tunnel.username,
                ssh_pkey=self.kafka_server.ssh_tunnel.pkey,
                remote_bind_addresses=[(host_port.host, host_port.port)
                                       for host_port in self.kafka_server.get_host_list()]
            )
            self.ssh_tunnel.start()

            # 更新 Kafka 集群连接信息，令 Kafka 集群连接到 SSH 隧道
            addresses = [f"127.0.0.1:{self.ssh_tunnel.local_bind_port}"]
        else:
            addresses = [f"{host_port.host}:{host_port.port}" for host_port in self.kafka_server.get_host_list()]

        # 启动 Kafka 集群连接
        print(addresses)
        self.kafka_admin_client = KafkaAdminClient(bootstrap_servers=addresses)

        return self.kafka_admin_client

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.kafka_admin_client is not None:
            self.kafka_admin_client.close()
        if self.ssh_tunnel is not None:
            self.ssh_tunnel.close()


class ConnKafkaConsumer:
    """根据 KafkaServer 对象创建 kafka-python 的 KafkaConsumer 对象"""

    def __init__(self, kafka_server: KafkaServer, group_id: Optional[str]):
        self.kafka_server = kafka_server  # MySQl 实例的配置
        self.group_id = group_id

        # 初始化 MySQL 连接和 SSH 隧道连接
        self.kafka_consumer = None
        self.ssh_tunnel = None

    def __enter__(self):
        """在进入 with as 语句的时候被 with 调用，返回值作为 as 后面的变量"""
        if self.kafka_server.ssh_tunnel is not None:
            # 启动 SSH 隧道
            self.ssh_tunnel = sshtunnel.SSHTunnelForwarder(
                ssh_address_or_host=self.kafka_server.ssh_tunnel.address,
                ssh_username=self.kafka_server.ssh_tunnel.username,
                ssh_pkey=self.kafka_server.ssh_tunnel.pkey,
                remote_bind_addresses=[(host_port.host, host_port.port)
                                       for host_port in self.kafka_server.get_host_list()]
            )
            self.ssh_tunnel.start()

            # 更新 Kafka 集群连接信息，令 Kafka 集群连接到 SSH 隧道
            addresses = [f"127.0.0.1:{self.ssh_tunnel.local_bind_port}"]
        else:
            addresses = [f"{host_port.host}:{host_port.port}" for host_port in self.kafka_server.get_host_list()]

        # 启动 Kafka 集群连接
        self.kafka_consumer = KafkaConsumer(bootstrap_servers=addresses,
                                            group_id=self.group_id,
                                            auto_offset_reset="latest",
                                            api_version=(0, 11))

        return self.kafka_consumer

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.kafka_consumer is not None:
            self.kafka_consumer.close()
        if self.ssh_tunnel is not None:
            self.ssh_tunnel.close()


class ConnKafkaProducer:
    """根据 KafkaServer 对象创建 kafka-python 的 KafkaProducer 对象"""

    def __init__(self, kafka_server: KafkaServer):
        self.kafka_server = kafka_server  # MySQl 实例的配置

        # 初始化 MySQL 连接和 SSH 隧道连接
        self.kafka_producer = None
        self.ssh_tunnel = None

    def __enter__(self):
        """在进入 with as 语句的时候被 with 调用，返回值作为 as 后面的变量"""
        if self.kafka_server.ssh_tunnel is not None:
            # 启动 SSH 隧道
            self.ssh_tunnel = sshtunnel.SSHTunnelForwarder(
                ssh_address_or_host=self.kafka_server.ssh_tunnel.address,
                ssh_username=self.kafka_server.ssh_tunnel.username,
                ssh_pkey=self.kafka_server.ssh_tunnel.pkey,
                remote_bind_addresses=[(host_port.host, host_port.port)
                                       for host_port in self.kafka_server.get_host_list()]
            )
            self.ssh_tunnel.start()

            # 更新 Kafka 集群连接信息，令 Kafka 集群连接到 SSH 隧道
            addresses = [f"127.0.0.1:{self.ssh_tunnel.local_bind_port}"]
        else:
            addresses = [f"{host_port.host}:{host_port.port}" for host_port in self.kafka_server.get_host_list()]

        # 启动 Kafka 集群连接
        self.kafka_producer = KafkaProducer(bootstrap_servers=addresses,
                                            batch_size=1048576,
                                            linger_ms=50)

        return self.kafka_producer

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.kafka_producer is not None:
            self.kafka_producer.close()
        if self.ssh_tunnel is not None:
            self.ssh_tunnel.close()
