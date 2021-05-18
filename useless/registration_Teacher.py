import sys
import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox


class Registration_Teacher(QMainWindow):
    def __init__(self, parent=None):
        self.polz = sqlite3.connect("data/project.db")
        self.cur = self.polz.cursor()
        super().__init__()
        uic.loadUi('data/design_regist_Teacher.ui', self)
        self.initUI()

    def initUI(self):
        self.btn_registration.clicked.connect(self.registra)
        self.btn_go_back.clicked.connect(self.back)

    def registra(self):
        self.surname = self.edit_surname.text()
        self.name = self.edit_name.text()
        self.second_name = self.edit_second_name.text()
        self.school = self.edit_school.text()
        self.login = self.edit_login.text()
        self.password = self.edit_password.text()
        My_sql_query = """SELECT Login from Teachers where Login = ?"""
        dat = self.cur.execute(My_sql_query, (self.login,))
        print(dat)
        record = len(self.cur.fetchall())
        if (self.surname != '') and (self.name != '') and (self.login != '') and (self.password != '') and \
                (self.school != '') and (self.second_name != ''):
            if (record == 0) and (self.edit_password.text()):
                self.cur.execute("""INSERT INTO Teachers VALUES(?, ?, ?, ?, ?, ?)""",
                                 (self.surname, self.name, self.second_name, self.school, self.login, self.password))
                self.polz.commit()
            elif record != 0:
                reply = QMessageBox.about(self, 'Error',
                                          "Такой логин уже существует, придумайте новый.")

            elif (self.vvod_password.text() != self.repit_password.text()):
                reply = QMessageBox.about(self, 'Error',
                                          "Пароли не совпадают.")
        else:
            reply = QMessageBox.about(self, 'Error',
                                      "Заполните пустые строки.")

    def back(self):
        pass
