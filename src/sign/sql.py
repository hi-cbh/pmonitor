# urs/bin/python
# encoding:utf-8
import pymysql.cursors
import os
import configparser as cparser

host = "127.0.0.1"
port = "3306"
user="root"
password="123456"
db="monitor"





class DB:

    def __init__(self):
        try:
            # Connect to the database
            self.connection = pymysql.connect(host=host,
                                              port=int(port),
                                              user=user,
                                              password=password,
                                              db=db,
                                              charset='utf8mb4',
                                              cursorclass=pymysql.cursors.DictCursor)
        except pymysql.err.OperationalError as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))

    # clear table data
    def clear(self, table_name):
        real_sql = "delete from " + table_name + ";"
        with self.connection.cursor() as cursor:
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            cursor.execute(real_sql)
        self.connection.commit()

    # insert sql statement
    def insert(self, table_name, table_data):
        for key in table_data:
            table_data[key] = "'"+str(table_data[key])+"'"
        key   = ','.join(table_data.keys())
        value = ','.join(table_data.values())
        real_sql = "INSERT INTO " + table_name + " (" + key + ") VALUES (" + value + ")"
        print(real_sql)

        with self.connection.cursor() as cursor:
            cursor.execute(real_sql)

        self.connection.commit()

    # 修改
    def update(self, table_name, table_data):
        key   = "='%d',".join(table_data.keys())
        key = key + "='%d'"
        # print(tuple(table_data.values()))
        real_sql = "UPDATE " + table_name + " SET " + key %tuple(table_data.values())
        print(real_sql)

        with self.connection.cursor() as cursor:
            cursor.execute(real_sql)

        self.connection.commit()



    # close database
    def close(self):
        self.connection.close()

    # init data
    def init_data(self, datas):
        for table, data in datas.items():
            self.clear(table)
            for d in data:
                self.insert(table, d)
        self.close()

    def show_data(self,table_name):
        sql = "SELECT * FROM %s" %table_name
        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            results = cursor.fetchall()

        # print(results)
        return results

if __name__ == '__main__':
    datas={"testcaseonbtnlogin":2,'testcaselogin': 2, 'testcasesendnoattach': 3}
    db = DB()
    db.update("test_data",datas)
    db.close()
