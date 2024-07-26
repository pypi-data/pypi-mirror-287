"""
MySQL 相关工具类
"""

from typing import Tuple, Dict, Any, List, Optional

import pymysql
import pymysql.cursors

import metasequoia_connector as ms_conn


def show_databases(rds_instance: ms_conn.MysqlInstance):
    """执行：SHOW DATABASES"""
    with ms_conn.MysqlConnector.create_by_instance(mysql_instance=rds_instance) as conn:
        return conn_show_databases(conn)


def show_tables(rds_instance: ms_conn.MysqlInstance, schema: str):
    """执行：SHOW TABLES"""
    with ms_conn.MysqlConnector.create_by_instance(mysql_instance=rds_instance, schema=schema) as conn:
        return conn_show_tables(conn)


def show_create_table(rds_instance: ms_conn.MysqlInstance, schema: str, table: str,
                      ssh_tunnel: Optional[ms_conn.SshTunnel] = None):
    """执行：SHOW CREATE TABLE"""
    with ms_conn.MysqlConnector.create_by_instance(mysql_instance=rds_instance, schema=schema) as conn:
        return conn_show_create_table(conn, table)


def conn_use(conn: pymysql.Connection, schema: str) -> None:
    with conn.cursor() as cursor:
        cursor.execute(f"USE `{schema}`")


def conn_select_all(conn: pymysql.Connection, sql: str) -> Tuple[Tuple[Any, ...], ...]:
    with conn.cursor() as cursor:
        cursor.execute(sql)
        return cursor.fetchall()


def conn_select_all_as_dict(conn: pymysql.Connection, sql: str) -> Tuple[Dict[str, Any], ...]:
    """使用 sql 查询 conn 连接的 MySQL，并将结果作为 dict 的列表返回"""
    with conn.cursor(pymysql.cursors.DictCursor) as cursor:
        cursor.execute(sql)
        return cursor.fetchall()


def conn_select_one_as_dict(conn: pymysql.Connection, sql: str) -> Dict[str, Any]:
    with conn.cursor(pymysql.cursors.DictCursor) as cursor:
        cursor.execute(sql)
        return cursor.fetchone()


def conn_execute_and_commit(conn: pymysql.Connection, sql: str) -> int:
    """执行 SQL 语句，并 commit"""
    with conn.cursor(pymysql.cursors.DictCursor) as cursor:
        result = cursor.execute(sql)
    conn.commit()
    return result


def conn_execute_and_commit_with_args(conn: pymysql.Connection, sql: str, *args) -> int:
    with conn.cursor() as cursor:
        result = cursor.execute(sql, args)
    conn.commit()
    return result


def conn_execute_multi_and_commit(conn: pymysql.Connection, sql_list: List[str]) -> int:
    """在同一个事务中执行多个 SQL 语句，并 commit"""
    with conn.cursor(pymysql.cursors.DictCursor) as cursor:
        for sql in sql_list:
            result = cursor.execute(sql)
        conn.commit()
        return result


def conn_show_databases(conn: pymysql.Connection) -> List[str]:
    """执行 SHOW DATABASES 语句，返回数据库名称的列表"""
    return [row["Database"] for row in conn_select_all_as_dict(conn, "SHOW DATABASES")]


def conn_show_tables(conn: pymysql.Connection) -> List[str]:
    """执行 SHOW TABLES 语句，返回表名的列表"""
    return [row[0] for row in conn_select_all(conn, "SHOW TABLES")]


def conn_show_create_table(conn: pymysql.Connection, table: str) -> Optional[str]:
    """执行 SHOW CREATE TABLE 语句

    无法获取时返回 None，在以下场景下无法获取：
    1. 账号没有权限
    2. 表名不存在

    实现说明：
    1. 为使名称完全为数字的表执行正常，所以在表名外添加了引号
    """
    result = conn_select_all_as_dict(conn, f"SHOW CREATE TABLE `{table}`")[0]
    if "Create Table" in result:
        return result["Create Table"]
    else:  # 当表名不存在或没有权限时，没有 Create Table 列，只有 Error 列
        return None
