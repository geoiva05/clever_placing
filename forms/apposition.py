import sys
import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QDesktopWidget


class clever_placing(QMainWindow):
    def __init__(self, user, autorised, main_admin, admin):
        super().__init__()
        self.polz = sqlite3.connect("data/clever_placing.db")
        self.cur = self.polz.cursor()
        self.user = user
        self.autorised = autorised
        self.main_admin = main_admin
        self.adminn = admin
        if main_admin[0][0] == 1:
            uic.loadUi('data/main_admin.ui', self)
        elif admin[0][0] == 1:
            uic.loadUi('data/admin.ui', self)
        else:
            uic.loadUi('data/sth.ui', self)
        self.initUI()

    def initUI(self):
        self.center()
        if self.adminn[0][0] == 1 or self.main_admin[0][0] == 1:
            self.students.clicked.connect(self.edit_students)
            self.books.clicked.connect(self.edit_books)
            self.lessons.clicked.connect(self.edit_lessons)
            self.search_student.clicked.connect(self.search_students)
            self.view_lessons.clicked.connect(self.time_table)
            self.search_book.clicked.connect(self.search_books)
            if self.main_admin[0][0] == 1:
                self.admin.clicked.connect(self.give_admin)

    def edit_students(self):
        self.center()
        uic.loadUi('data/editing_student.ui', self)
        self.back.clicked.connect(self.returning)

    def edit_books(self):
        self.center()
        uic.loadUi('data/editing_book.ui', self)
        self.back.clicked.connect(self.returning)

    def edit_lessons(self):
        pass

    def search_students(self):
        pass

    def time_table(self):
        pass

    def give_admin(self):
        pass

    def search_books(self):
        pass

    def returning(self):
        if self.main_admin[0][0] == 1:
            uic.loadUi('data/main_admin.ui', self)
        elif self.adminn[0][0] == 1:
            uic.loadUi('data/admin.ui', self)
        else:
            uic.loadUi('data/sth.ui', self)
        self.initUI()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
