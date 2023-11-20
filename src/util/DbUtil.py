import pymysql


# 帮助类
class DbUtil:
    connect: object
    cursor: object

    # def __init__(self, student, username, password):
    #     self.connect = pymysql.Connect(host='localhost', port = 3306, database='studentxj',
    #                                    user=username, passwd=password, charset='utf8')
    #     self.cursor = self.connect.cursor()

    # 测试
    def __init__(self):
        self.connect = pymysql.Connect(host='localhost', port=3306, database='studentxj',
                                       user='root', passwd='assassin030527', charset='utf8')
        self.cursor = self.connect.cursor()

    def close(self):
        self.connect.close()
        self.cursor.close()

    def execute(self, sql: str, val: tuple = None):
        self.cursor.execute(sql, val)
        self.connect.commit()

    def executeList(self, sql: str):
        self.cursor.execute(sql, None)
        return self.cursor.fetchall()
