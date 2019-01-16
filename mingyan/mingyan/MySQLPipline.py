#!/usr/bin/python
# -*- encoding:utf-8 -*-
import logging
import pymysql.cursors


class MySQLPipeline(object):
    def __init__(self):
        self.connect = pymysql.connect(
            host="127.0.0.1",# 数据库地址
            port=3306,
            db="scrapyMysql",
            user='yusuzi',
            passwd='yusuzi',
            charset='utf8',
            use_unicode=True
        )
        self.cursor = self.connect.cursor()
        

    def process_item(self, item, spider):
        self.cursor.execute(
            """insert into mingyan(tag,cont) value (%s,%s)""",
            (item['tag'],
            item['cont']))
        # 提交sql 语句
        self.connect.commit()
        return item # 必须实现返回