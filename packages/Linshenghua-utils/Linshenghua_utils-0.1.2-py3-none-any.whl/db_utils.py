# pymysql数据库操作
import pymysql
import os

# 加载环境变量

# 获取环境变量
os.loadenv('dotenv', verbose=True)
env = os.getenv('ENV', 'prod')

# 使用类创建一个数据库操作
class DBUtils:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conn = None
        self.cursor = None

    def connect(self):
        try:
            self.conn = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            self.cursor = self.conn.cursor()
        except pymysql.MySQLError as e:
            print("数据库连接失败:", e)

    def disconnect(self):
        if self.cursor:
            self.cursor.close()

        if self.conn:
            self.conn.close()

    def select_all(self, query):
        self.connect()
        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            self.disconnect()
            return result
        except pymysql.MySQLError as e:
            print("数据库查询失败:", e)

    def select_one(self, query):
        self.connect()
        try:
            self.cursor.execute(query)
            result = self.cursor.fetchone()
            self.disconnect()
            return result
        except pymysql.MySQLError as e:
            print("数据库操作失败:", e)
