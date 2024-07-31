#!/usr/bin/env python
# coding=utf-8
import os
import pymysql
from dotenv import load_dotenv, find_dotenv
from abc import ABCMeta, abstractmethod
from typing import Union, List, Dict, Tuple, Any
from sshtunnel import SSHTunnelForwarder

class DBUtils(metaclass=ABCMeta):
    def __init__(self, database, is_ssh=False, curson_type=True):
        # 加载环境变量
        load_dotenv(find_dotenv(), override=True)
        # 初始化数据库连接
        self.host = os.getenv("DB_HOST", "localhost")
        self.port = int(os.getenv("DB_PORT", 3306))
        self.user = os.getenv("DB_USER", "root")
        self.password = os.getenv("DB_PASSWORD", "123456")
        self.ssh_host = os.getenv("SSH_HOST", None)
        self.ssh_port = int(os.getenv("SSH_PORT", 22))
        self.ssh_user = os.getenv("SSH_USER", None)
        self.ssh_password = os.getenv("SSH_PASSWORD", None)
        self.database = database
        self.is_ssh = is_ssh
        self.cursor_type = curson_type

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def execute(self, sql) -> None:
        pass

    @abstractmethod
    def select_one(self) -> Union[None, Dict[str, Any], Tuple[Any]]:
        pass

    @abstractmethod
    def select_all(self) -> Union[None, List[Dict[str, Any]], Tuple[Tuple[Any]]]:
        pass

    @abstractmethod
    def close(self):
        pass


class MysqlUtils(DBUtils):
    def __init__(self, database, is_ssh=False, curson_type=True):
        super().__init__(database, is_ssh, curson_type)

    def connect(self) -> None:
        if self.is_ssh:
            server = SSHTunnelForwarder(
                # 指定ssh登录的跳转机的address
                ssh_address_or_host=(self.ssh_host, int(self.ssh_port)),
                ssh_username=self.ssh_user,
                ssh_password=self.ssh_password,
                # 设置数据库服务地址及端口
                remote_bind_address=(self.host, int(self.port)))
            server.start()
            self.conn = pymysql.connect(
                database=self.database,
                user=self.user,
                password=self.password,
                host='127.0.0.1',
                port=server.local_bind_port,
                cursorclass=pymysql.cursors.DictCursor if self.cursor_type else pymysql.cursors.Cursor
        )
        else:
            self.conn = pymysql.connect(
                host=self.host, port=self.port, user=self.user, password=self.password, database=self.database,
                cursorclass=pymysql.cursors.DictCursor if self.cursor_type else pymysql.cursors.Cursor
        )

    def execute(self, sql) -> None:
        self.cursor = self.conn.cursor()
        self.cursor.execute(sql)

    def select_one(self) -> Union[None, Dict[str, Any], Tuple[Any]]:
        return self.cursor.fetchone()

    def select_all(self) ->  Union[None, List[Dict[str, Any]], Tuple[Tuple[Any]]]:
        return self.cursor.fetchall()

    def close(self) -> None:
        self.conn.close()

def get_db_data(conn: DBUtils, sql: str, is_one: bool = False) -> Union[None, Dict[str, Any], Tuple[Any]]:
    conn.connect()
    conn.execute(sql)
    conn.close()
    if is_one:
        return conn.select_one()
    else:
        return conn.select_all()

if __name__ == '__main__':
    a = MysqlUtils("base")
    # a.connect()
    # a.execute("select name from user")
    # print(a.select_one())
    # a.close()
    # print(a.select_all())

    print(get_db_data(a, "select name from user"))
