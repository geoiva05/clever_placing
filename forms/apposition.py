import sys
import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QDesktopWidget


class clever_placing(QMainWindow):
    def __init__(self, user, autorised, main_admin, admin):
        super().__init__()
        self.con = sqlite3.connect("db/clever_placing.db")
        self.cur = self.con.cursor()
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
        self.finish.clicked.connect(self.finish_student)

    def finish_student(self):
        if self.id.text().isdigit():
            id_user = self.id.text()
            My_sql_query = f"""SELECT * from Students where _id_user = "{id_user}" """
            self.student = self.cur.execute(My_sql_query).fetchall()
            if self.student:
                if self.new_surname.text():
                    My_sql_query = f"""Update Students Set surname = "{self.new_surname.text()}"where _id_user = "{id_user}" """
                    self.cur.execute(My_sql_query)
                    self.con.commit()
                if self.new_name.text():
                    My_sql_query = f"""Update Students Set name = "{self.new_name.text()}"where _id_user = "{id_user}" """
                    self.cur.execute(My_sql_query)
                    self.con.commit()

                if self.new_second_name.text():
                    My_sql_query = f"""Update Students Set second_name = "{self.new_second_name.text()}"\
                    where _id_user = "{id_user}" """
                    self.cur.execute(My_sql_query)
                    self.con.commit()
                if self.new_class_number.text():
                    My_sql_query = f"""Update Students Set class_number = "{self.new_class_number.text()}" \
                    where _id_user = "{id_user}" """
                    self.cur.execute(My_sql_query)
                    self.con.commit()
                if self.new_class_char.text():
                    My_sql_query = f"""Update Students Set class_char = "{self.new_class_char.text()}"where _id_user = "{id_user}" """
                    self.cur.execute(My_sql_query)
                    self.con.commit()
                if self.new_school.text():
                    My_sql_query = f"""Update Students Set school = "{self.new_school.text()}"where _id_user = "{id_user}" """
                    self.cur.execute(My_sql_query)
                    self.con.commit()
                reply = QMessageBox.about(self, 'Error',
                                          "Редактирование успешно завершенно")
                self.returning()
            else:
                reply = QMessageBox.about(self, 'Error',
                                          "Введите существующий id")
        else:
            reply = QMessageBox.about(self, 'Error',
                                      "Введите правильный id")

    def edit_books(self):
        self.center()
        uic.loadUi('data/editing_book.ui', self)
        self.back.clicked.connect(self.returning)
        self.finish.clicked.connect(self.finish_book)

    def finish_book(self):
        if self.id.text().isdigit():
            id_book = self.id.text()
            My_sql_query = f"""SELECT * from Students where id_book = "{id_book}" """
            self.student = self.cur.execute(My_sql_query).fetchall()
            if self.student:
                if self.new_name.text():
                    My_sql_query = f"""Update Students Set name = "{self.new_name.text()}"where id_book = "{id_book}" """
                    self.cur.execute(My_sql_query)
                    self.con.commit()
                if self.new_weigh.text():
                    My_sql_query = f"""Update Students Set weigh = "{self.new_weigh.text()}"where id_book = "{id_book}" """
                    self.cur.execute(My_sql_query)
                    self.con.commit()
                if self.new_second_name.text():
                    My_sql_query = f"""Update Students Set author = "{self.new_author.text()}"where id_book = "{id_book}" """
                    self.cur.execute(My_sql_query)
                    self.con.commit()
                if self.new_class_number.text():
                    My_sql_query = f"""Update Students Set class_number = "{self.new_class_number.text()}"\
                    where id_book = "{id_book}" """
                    self.cur.execute(My_sql_query)
                    self.con.commit()
                reply = QMessageBox.about(self, 'Error',
                                          "Редактирование успешно завершенно")
                self.returning()
            else:
                reply = QMessageBox.about(self, 'Error',
                                          "Введите существующий id")
        else:
            reply = QMessageBox.about(self, 'Error',
                                      "Введите правильный id")

    def edit_lessons(self):
        self.center()
        uic.loadUi('data/editing_time_table.ui', self)
        self.back.clicked.connect(self.returning)
        self.finish.clicked.connect(self.finish_lessons)

    def search_students(self):
        self.center()
        uic.loadUi('data/searching_student.ui', self)
        self.back.clicked.connect(self.returning)

    def time_table(self):
        self.center()
        uic.loadUi('data/view_lessons.ui', self)
        self.back.clicked.connect(self.returning)

    def give_admin(self):
        self.center()
        uic.loadUi('data/give_admin.ui', self)
        self.back.clicked.connect(self.returning)

    def search_books(self):
        self.center()
        uic.loadUi('data/searching_book.ui', self)
        self.back.clicked.connect(self.returning)

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
