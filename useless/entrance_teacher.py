import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from forms.apposition import APp


class Entrance_Teacher(QMainWindow):
    def __init__(self, parent=None):
        self.polz = sqlite3.connect("data/project.db")
        self.cur = self.polz.cursor()
        super().__init__()
        uic.loadUi('data/design_ent_check.ui', self)
        self.initUI()

    def initUI(self):
        self.btn_enter.clicked.connect(self.check)

    def check(self):
        My_sql_query = """SELECT Login from Students where Login = ?"""
        self.login = str(self.cur.execute(My_sql_query, (self.edit_login.text(),)))
        self.cur.fetchall()
        My_sql_query = """SELECT Password from Students where Password = ?"""
        self.passw = str(self.cur.execute(My_sql_query, (self.edit_password.text(),)))
        self.cur.fetchall()
        print(self.login, self.passw)
        if self.edit_password.text() == '' or self.edit_login.text() == '':
            reply = QMessageBox.about(self, 'Error',
                                      "Заполните пустые строки.")
        elif self.login == '' or self.login is None:
            reply = QMessageBox.about(self, 'Error',
                                      "Такого логина не существует")
        elif self.login == self.edit_login.text() and self.passw == self.edit_password.text():
            app = APp()
            app.show()
