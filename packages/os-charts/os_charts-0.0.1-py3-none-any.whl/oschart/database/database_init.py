#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/4/28 6:17 PM
# @Author  : zy
# @Site    :
# @File    : database_init.py
# @Software: PyCharm
"""
文件功能:

"""
from dataclasses import dataclass


@dataclass()
class DbChartMsql:
    """
    mysql 信息
    """

    host: str = None
    user: str = None
    password: str = None
    db: str = None
    port: int = 4000
    charset: str = "utf8mb4"


@dataclass()
class DbChartEs:
    """
    es 信息
    """

    host: str = None
    user: str = None
    password: str = None
    port: int = 9000


def set_db_chart_config(db_const: dict):
    """
    设置 数据源配置
    """
    if not db_const:
        raise Exception(f"db_const not null")
    db_mysql = db_const.get("db_mysql", {})
    db_es = db_const.get("db_es", {})

    DbChartMsql.host = db_mysql.get("host")
    DbChartMsql.user = db_mysql.get("user")
    DbChartMsql.password = db_mysql.get("password")
    DbChartMsql.db = db_mysql.get("db")
    DbChartMsql.port = db_mysql.get("port") or DbChartMsql.port

    DbChartEs.host = db_es.get("host")
    DbChartEs.user = db_es.get("user")
    DbChartEs.password = db_es.get("password")
    DbChartEs.port = db_es.get("port") or DbChartEs.port
