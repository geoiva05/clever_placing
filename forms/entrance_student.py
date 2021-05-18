import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QDesktopWidget


class Entrance_Student(QMainWindow):
    def __init__(self, parent=None):
        self.polz = sqlite3.connect("db/clever_placing.db")
        self.cur = self.polz.cursor()
        super().__init__()
        uic.loadUi('data/design_ent_check.ui', self)
        self.initUI()
        self.autorised = False

    def initUI(self):
        self.center()
        self.btn_enter.clicked.connect(self.check)

    def check(self):
        My_sql_query = f"""SELECT Login from Students where Login = "{str(self.edit_login.text())}" """
        self.login = self.cur.execute(My_sql_query).fetchall()
        My_sql_query = f"""SELECT Password from Students where Password = "{self.edit_password.text()}" """
        self.passw = self.cur.execute(My_sql_query).fetchall()
        if self.edit_password.text() == '' or self.edit_login.text() == '':
            reply = QMessageBox.about(self, 'Error',
                                      "Заполните пустые строки.")
        elif self.login == '' or self.login is None:
            reply = QMessageBox.about(self, 'Error',
                                      "Такого логина не существует")
        elif self.login[0][0] == self.edit_login.text() and self.passw[0][0] == self.edit_password.text():
            self.autorised = True
            self.user = self.login
            self.close()

    def enter(self):
        return self.user, self.autorised()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
