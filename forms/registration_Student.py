import sys
import hashlib
import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QDesktopWidget


class Registration_Student(QMainWindow):
    def __init__(self, parent=None):
        self.polz = sqlite3.connect("db/clever_placing.db")
        self.cur = self.polz.cursor()
        super().__init__()
        uic.loadUi('data/design_regist_Student.ui', self)
        self.initUI()

    def initUI(self):
        self.center()
        self.btn_registration.clicked.connect(self.registra)
        self.btn_go_back.clicked.connect(self.back)

    def registra(self):
        self.surname = self.edit_surname.text()
        self.name = self.edit_name.text()
        self.second_name = self.edit_second_name.text()
        self.school = self.edit_school.text()
        self.class_number = self.edit_class_number.text()
        self.class_char = self.edit_class_char.text()
        self.login = self.edit_login.text()
        self.password = self.edit_password.text()
        My_sql_query = """SELECT Login from Students where Login = ?"""
        dat = self.cur.execute(My_sql_query, (self.login,))
        record = len(self.cur.fetchall())
        if (self.surname != '') and (self.name != '') and (self.login != '') and (self.password != '') and \
                (self.school != '') and (self.second_name != ''):
            if (record == 0) and (self.edit_password.text()):
                self.cur.execute(
                    """INSERT INTO Students (surname, name, second_name, school, class_number, class_char, login, 
                    password, main_admin, admin) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                    (self.surname, self.name, self.second_name, self.school, self.class_number,
                     self.class_char, self.login, self.password, 0, 0))
                self.polz.commit()
                self.close()
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

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
