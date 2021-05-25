import sys, os
import sqlite3
import datetime

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QDesktopWidget


class clever_placing(QMainWindow):
    def __init__(self, user, autorised, main_admin, admin, id_given):
        super().__init__()
        self.con = sqlite3.connect("db/clever_placing.db")
        self.cur = self.con.cursor()
        self.user = user
        self.id_user = id_given[0][0]
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
        self.view_lessons.clicked.connect(self.time_table_)
        if self.adminn[0][0] == 1 or self.main_admin[0][0] == 1:
            self.students.clicked.connect(self.edit_students)
            self.books.clicked.connect(self.edit_books)
            self.lessons.clicked.connect(self.edit_lessons)
            self.search_student.clicked.connect(self.search_students)
            self.search_book.clicked.connect(self.search_books)
            if self.main_admin[0][0] == 1:
                self.admin.clicked.connect(self.give_admin)
        else:
            self.main_button.clicked.connect(self.main_function)

    def main_function(self):
        date_time = datetime.datetime.now()
        exact_hour = date_time.hour
        w = date_time.weekday()
        if exact_hour < 16:
            if w == 0:
                self.wee = 'Понедельник'
            elif w == 1:
                self.wee = 'Вторник'
            elif w == 2:
                self.wee = 'Среда'
            elif w == 3:
                self.wee = 'Четверг'
            elif w == 4:
                self.wee = 'Пятница'
            elif w == 5:
                self.wee = 'Понедельник'
            elif w == 6:
                self.wee = 'Понедельник'
            My_sql_query = f"""SELECT class_number, class_char from Students where _id_user = "{self.id_user}" """
            self.class_user = self.cur.execute(My_sql_query).fetchall()
            My_sql_query = f"""SELECT * from Students where class_number = {self.class_user[0][0]} 
            and class_char = "{self.class_user[0][1]}" """
            self.classmates = self.cur.execute(My_sql_query).fetchall()
            My_sql_query = f"""SELECT id_book from time_table where 
            class_number = {self.class_user[0][0]} and class_char = "{self.class_user[0][1]}" 
            and day = "{self.wee}" """
            self.books = self.cur.execute(My_sql_query).fetchall()
            self.weigh = []
            for el in self.books:
                My_sql_query = f"""SELECT weigh from student_books where id_book = "{el[0]}" """
                self.weigh.append(self.cur.execute(My_sql_query).fetchall()[0][0])
            data = []
            data.append(len(self.classmates))
            data.append(len(self.weigh))
            data.append(self.id_user)
            for el in self.classmates:
                data.append(el[0])
            for el in self.weigh:
                data.append(el)
            with open('in.txt', 'w') as f:
                for el in data:
                    f.write(str(el) + '\n')
            os.system(r'"C:\\Users\Asus\Documents\Python\clever_placing\Olimp proga.exe"')
            with open('out.txt', 'rt') as f:
                self.neighbours = f.readlines()
            uic.loadUi('data/time_table.ui', self)
            self.back.clicked.connect(self.returning)
            self.lab_tt.setText('Ваши соседи на завтра')
            text = ''
            for i in range(len(self.neighbours) // 2):
                if self.neighbours[i] == 'no neighbour\n':
                    neighbour = 'Нет соседа'
                else:
                    q = f"""SELECT name from Students where _id_user = "{self.neighbours[i]}" """
                    name = self.cur.execute(q).fetchall()
                    q = f"""SELECT surname from Students where _id_user = "{self.neighbours[i]}" """
                    surname = self.cur.execute(q).fetchall()
                    q = f"""SELECT second_name from Students where _id_user = "{self.neighbours[i]}" """
                    second_name = self.cur.execute(q).fetchall()
                    neighbour = name[0][0] + ' ' + surname[0][0] + ' ' + second_name[0][0]
                if self.neighbours[i + len(self.weigh)] == 'true\n':
                    take = ' Вы берёте учебник'
                else:
                    take = ' Сосед берёт учебник'
                if neighbour == 'Нет соседа':
                    text += str(i + 1) + ' урок ' + neighbour + '\n'
                else:
                    text += str(i + 1) + ' урок ' + neighbour + take + '\n'
            self.time_table.setText(text)
        elif exact_hour >= 22:
            if w == 0:
                self.wee = 'Вторник'
            elif w == 1:
                self.wee = 'Среда'
            elif w == 2:
                self.wee = 'Четверг'
            elif w == 3:
                self.wee = 'Пятница'
            elif w == 4:
                self.wee = 'Понедельник'
            elif w == 5:
                self.wee = 'Понедельник'
            elif w == 6:
                self.wee = 'Понедельник'
            My_sql_query = f"""SELECT class_number, class_char from Students where _id_user = "{self.id_user}" """
            self.class_user = self.cur.execute(My_sql_query).fetchall()
            My_sql_query = f"""SELECT * from Students where class_number = {self.class_user[0][0]} 
            and class_char = "{self.class_user[0][1]}" """
            self.classmates = self.cur.execute(My_sql_query).fetchall()
            My_sql_query = f"""SELECT id_book from time_table where 
            class_number = {self.class_user[0][0]} and class_char = "{self.class_user[0][1]}" 
            and day = "{self.wee}" """
            self.books = self.cur.execute(My_sql_query).fetchall()
            self.weigh = []
            for el in self.books:
                My_sql_query = f"""SELECT weigh from student_books where id_book = "{el[0]}" """
                self.weigh.append(self.cur.execute(My_sql_query).fetchall()[0][0])
            data = []
            data.append(len(self.classmates))
            data.append(len(self.weigh))
            data.append(self.id_user)
            for el in self.classmates:
                data.append(el[0])
            for el in self.weigh:
                data.append(el)
            with open('in.txt', 'w') as f:
                for el in data:
                    f.write(str(el) + '\n')
            os.system(r'"C:\\Users\Asus\Documents\Python\clever_placing\Olimp proga.exe"')
            with open('out.txt', 'rt') as f:
                self.neighbours = f.readlines()
            uic.loadUi('data/time_table.ui', self)
            self.back.clicked.connect(self.returning)
            self.lab_tt.setText('Ваши соседи на завтра')
            text = ''
            for i in range(len(self.neighbours)):
                if self.neighbours[i] == 'no neighbour\n':
                    neighbour = 'Нет соседа'
                else:
                    name = f"""SELECT name from Students where _id_user = "{self.neighbours[i]}" """
                    surname = f"""SELECT surname from Students where _id_user = "{self.neighbours[i]}" """
                    second_name = f"""SELECT second_name from Students where _id_user = "{self.neighbours[i]}" """
                    neighbour = name + ' ' + surname + ' ' + second_name
                text += str(i + 1) + ' урок ' + neighbour + '\n'
            self.time_table.setText(text)
        else:
            reply = QMessageBox.about(self, 'Error',
                                      "Сейчас ещё нельзя посмотреть ваших соседей по парте")

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
                    My_sql_query = f"""Update Students Set surname = "{self.new_surname.text()}"\
                    where _id_user = "{id_user}" """
                    self.cur.execute(My_sql_query)
                    self.con.commit()
                if self.new_name.text():
                    My_sql_query = f"""Update Students Set name = "{self.new_name.text()}"\
                    where _id_user = "{id_user}" """
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
                    My_sql_query = f"""Update Students Set class_char = "{self.new_class_char.text()}"\
                    where _id_user = "{id_user}" """
                    self.cur.execute(My_sql_query)
                    self.con.commit()
                if self.new_school.text():
                    My_sql_query = f"""Update Students Set school = "{self.new_school.text()}"\
                    where _id_user = "{id_user}" """
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
                    My_sql_query = f"""Update Students Set name = "{self.new_name.text()}" \
                    where id_book = "{id_book}" """
                    self.cur.execute(My_sql_query)
                    self.con.commit()
                if self.new_weigh.text():
                    My_sql_query = f"""Update Students Set weigh = {float(self.new_weigh.text())} \
                    where id_book = "{id_book}" """
                    self.cur.execute(My_sql_query)
                    self.con.commit()
                if self.new_second_name.text():
                    My_sql_query = f"""Update Students Set author = "{self.new_author.text()}" \
                    where id_book = "{id_book}" """
                    self.cur.execute(My_sql_query)
                    self.con.commit()
                if self.new_class_number.text():
                    My_sql_query = f"""Update Students Set class_number = "{self.new_class_number.text()}" \
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

    def finish_lessons(self):
        if self.id.text().isdigit():
            id_lesson = self.id.text()
            My_sql_query = f"""SELECT * from Students where id_lesson = "{id_lesson}" """
            self.student = self.cur.execute(My_sql_query).fetchall()
            if self.student:
                if self.new_number_lesson.text().isdigit():
                    My_sql_query = f"""Update Students Set number_lesson = {int(self.new_number_lesson.text())} \
                    where id_lesson = "{id_lesson}" """
                    self.cur.execute(My_sql_query)
                    self.con.commit()
                if self.new_subject.text():
                    My_sql_query = f"""Update Students Set name_lesson = "{self.new_subject.text()}" \
                    where id_lesson = "{id_lesson}" """
                    self.cur.execute(My_sql_query)
                    self.con.commit()
                if self.new_teacher.text().isdigit():
                    My_sql_query = f"""Update Students Set id_teacher = {int(self.new_teacher.text())} \
                    where id_lesson = "{id_lesson}" """
                    self.cur.execute(My_sql_query)
                    self.con.commit()
                if self.new_class_number.text():
                    My_sql_query = f"""Update Students Set day = "{self.new_class_number.text()}" \
                    where id_lesson = "{id_lesson}" """
                    self.cur.execute(My_sql_query)
                    self.con.commit()
                if self.new_class_char.text():
                    My_sql_query = f"""Update Students Set class_char = "{self.new_class_char.text()}" \
                    where id_lesson = "{id_lesson}" """
                    self.cur.execute(My_sql_query)
                    self.con.commit()
                if self.new_book.text().isdigit():
                    My_sql_query = f"""Update Students Set id_book = {int(self.new_book.text())} \
                    where id_lesson = "{id_lesson}" """
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

    def search_students(self):
        self.center()
        uic.loadUi('data/searching_student.ui', self)
        self.back.clicked.connect(self.returning)
        self.finish.clicked.connect(self.finish_searching_students)

    def finish_searching_students(self):
        uic.loadUi('data/time_table.ui', self)
        self.back.clicked.connect(self.returning)
        text = ''
        if self.id.text():
            My_sql_query = f"""SELECT * from students where _id_user = {self.id.text()} """
            self.student = self.cur.execute(My_sql_query).fetchall()
            print(self.student)
            for el in self.student:
                text += (str(el[0]) + ' ' + str(el[1]) + ' ' + str(el[2]) + ' ' + ' ' + str(el[3]) + ' ' + \
                         str(el[4]) + ' ' + str(el[5]) + str(el[6]) + ' ' + str(el[7]) + ' ')
        if self.name.text():
            My_sql_query = f"""SELECT * from students where name LIKE "{self.name.text()}" """
            self.student = self.cur.execute(My_sql_query).fetchall()
            for el in self.student:
                text += str(el[0]) + ' ' + str(el[1]) + ' ' + str(el[2]) + ' ' + ' ' + str(el[3]) + ' ' + \
                        str(el[4]) + ' ' + str(el[5]) + str(el[6]) + ' ' + str(el[7]) + ' ' + \
                        str(el[8]) + ' ' + str(el[9]) + '\n'
        if self.surname.text():
            My_sql_query = f"""SELECT * from students where surname LIKE "{self.surname.text()}" """
            self.student = self.cur.execute(My_sql_query).fetchall()
            for el in self.student:
                text += str(el[0]) + ' ' + str(el[1]) + ' ' + str(el[2]) + ' ' + ' ' + str(el[3]) + ' ' + \
                        str(el[4]) + ' ' + str(el[5]) + str(el[6]) + ' ' + str(el[7]) + ' ' + \
                        str(el[8]) + ' ' + str(el[9]) + '\n'
        if self.second_name.text():
            My_sql_query = f"""SELECT * from students where second_name LIKE "{self.second_name.text()}" """
            self.student = self.cur.execute(My_sql_query).fetchall()
            for el in self.student:
                text += str(el[0]) + ' ' + str(el[1]) + ' ' + str(el[2]) + ' ' + ' ' + str(el[3]) + ' ' + \
                        str(el[4]) + ' ' + str(el[5]) + str(el[6]) + ' ' + str(el[7]) + ' ' + \
                        str(el[8]) + ' ' + str(el[9]) + '\n'
        if self.class_number.text():
            My_sql_query = f"""SELECT * from students where second_name LIKE {self.class_number.text()} """
            self.student = self.cur.execute(My_sql_query).fetchall()
            for el in self.student:
                text += str(el[0]) + ' ' + str(el[1]) + ' ' + str(el[2]) + ' ' + ' ' + str(el[3]) + ' ' + \
                        str(el[4]) + ' ' + str(el[5]) + str(el[6]) + ' ' + str(el[7]) + ' ' + \
                        str(el[8]) + ' ' + str(el[9]) + '\n'
        if self.class_char.text():
            My_sql_query = f"""SELECT * from students where second_name LIKE "{self.class_char.text()}" """
            self.student = self.cur.execute(My_sql_query).fetchall()
            for el in self.student:
                text += str(el[0]) + ' ' + str(el[1]) + ' ' + str(el[2]) + ' ' + ' ' + str(el[3]) + ' ' + \
                        str(el[4]) + ' ' + str(el[5]) + str(el[6]) + ' ' + str(el[7]) + ' ' + \
                        str(el[8]) + ' ' + str(el[9]) + '\n'
        self.time_table.setText(text)

    def time_table_(self):
        self.center()
        uic.loadUi('data/view_lessons.ui', self)
        self.back.clicked.connect(self.returning)
        self.finish.clicked.connect(self.finish_time_table)

    def finish_time_table(self):
        uic.loadUi('data/time_table.ui', self)
        self.back.clicked.connect(self.returning)
        if self.day.text() and self.class_number.text() and self.class_char.text():
            My_sql_query = f"""SELECT * from time_table where day = "{self.day.text()}" \
            and class_number = {int(self.class_number.text())} and class_char = "{self.class_char.text()}" """
            self.student = self.cur.execute(My_sql_query).fetchall()
            text = ''
            self.lab_tt.setText(
                f"""Расписание на {self.student[0][3]} для{str(self.student[0][5]) + self.student[0][6]}""")
            for el in self.student:
                text += str(el[1]) + ' ' + el[2] + '\n'
            self.time_table.setText(text)

    def give_admin(self):
        self.center()
        uic.loadUi('data/give_admin.ui', self)
        self.back.clicked.connect(self.returning)
        self.finish.clicked.connect(self.finish_admin)

    def finish_admin(self):
        if self.id.text().isdigit():
            id_user = self.id.text()
            My_sql_query = f"""SELECT * from Students where _id_user = "{id_user}" """
            self.student = self.cur.execute(My_sql_query).fetchall()
            if self.student:
                My_sql_query = f"""Update Students Set admin = {1} \
                where _id_user = "{id_user}" """
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

    def search_books(self):
        self.center()
        uic.loadUi('data/searching_book.ui', self)
        self.back.clicked.connect(self.returning)
        self.finish.clicked.connect(self.finish_searching_books)

    def finish_searching_books(self):
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
