import pymysql
import tkinter as tk
import sys


class Student:
    def __init__(self, student, username, password):
        self.connect = pymysql.Connect(host='localhost', port = 3306, database=studentxj, user=username, passwd=password)

    def __del__(self):
        self.connect.close()