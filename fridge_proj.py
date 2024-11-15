from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt, QTime
from PyQt5.QtWidgets import QLineEdit, QApplication, QMainWindow, QPushButton, QMessageBox, QLabel, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QIcon, QFont

def main_scr():
    app = QApplication([])
    global main_win
    main_win = QMainWindow()
    main_win.setStyleSheet("background-color: powderblue;")

    def click_to_add(self):
        added = QMessageBox(main_win)
        added.setText("What do you want to add?     \n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        global line1, line2, line3, line4, line5, line6, line7, line8, line9, line10
        line1 = QLineEdit(added)
        line1.move(5,45)

        line2 = QLineEdit(added)
        line2.move(5,80)

        line3 = QLineEdit(added)
        line3.move(5,115)

        line4 = QLineEdit(added)
        line4.move(5,150)

        line5 = QLineEdit(added)
        line5.move(5,185)

        line6 = QLineEdit(added)
        line6.move(120, 45)

        line7 = QLineEdit(added)
        line7.move(120, 80)

        line8 = QLineEdit(added)
        line8.move(120, 115)

        line9 = QLineEdit(added)
        line9.move(120, 150)

        line10 = QLineEdit(added)
        line10.move(120, 185)

        save = QPushButton(added)
        save.setText("Save")
        save.setGeometry(QtCore.QRect(15, 335, 90, 30))
        save.clicked.connect(save_product)
        added.exec_()

    def make_ice(self):
        cubes = QLabel(main_win)
        cubes.setText("ice cubes")
        cubes.setGeometry((QtCore.QRect(190, 350, 120, 35)))
        cubes.setFont(QFont('Times', 12))
        cubes.show()

    def label(self):
        inside = QLabel(main_win)
        inside.setText("Inside:")
        inside.setGeometry((QtCore.QRect(300, 150, 120, 35)))
        inside.setFont(QFont('Times', 18))
        inside.show()

    def save_product(self):
        food1 = line1.text()
        food_in1 = QLabel(main_win)
        food_in1.setText(food1)
        food_in1.setGeometry((QtCore.QRect(190, 200, 150, 35)))
        food_in1.setFont(QFont('Times', 12))

        food2 = line2.text()
        food_in2 = QLabel(main_win)
        food_in2.setText(food2)
        food_in2.setGeometry((QtCore.QRect(190, 230, 150, 35)))
        food_in2.setFont(QFont('Times', 12))

        food3 = line3.text()
        food_in3 = QLabel(main_win)
        food_in3.setText(food3)
        food_in3.setGeometry((QtCore.QRect(190, 260, 150, 35)))
        food_in3.setFont(QFont('Times', 12))

        food4 = line4.text()
        food_in4 = QLabel(main_win)
        food_in4.setText(food4)
        food_in4.setGeometry((QtCore.QRect(190, 290, 150, 35)))
        food_in4.setFont(QFont('Times', 12))

        food5 = line5.text()
        food_in5 = QLabel(main_win)
        food_in5.setText(food5)
        food_in5.setGeometry((QtCore.QRect(190, 320, 150, 40)))
        food_in5.setFont(QFont('Times', 12))

        food6 = line6.text()
        food_in6 = QLabel(main_win)
        food_in6.setText(food6)
        food_in6.setGeometry((QtCore.QRect(410, 200, 150, 40)))
        food_in6.setFont(QFont('Times', 12))

        food7 = line7.text()
        food_in7 = QLabel(main_win)
        food_in7.setText(food7)
        food_in7.setGeometry((QtCore.QRect(410, 230, 150, 40)))
        food_in7.setFont(QFont('Times', 12))

        food8 = line8.text()
        food_in8 = QLabel(main_win)
        food_in8.setText(food8)
        food_in8.setGeometry((QtCore.QRect(410, 260, 150, 40)))
        food_in8.setFont(QFont('Times', 12))

        food9 = line9.text()
        food_in9 = QLabel(main_win)
        food_in9.setText(food9)
        food_in9.setGeometry((QtCore.QRect(410, 290, 150, 40)))
        food_in9.setFont(QFont('Times', 12))

        food10 = line10.text()
        food_in10 = QLabel(main_win)
        food_in10.setText(food10)
        food_in10.setGeometry((QtCore.QRect(410, 320, 150, 40)))
        food_in10.setFont(QFont('Times', 12))

        layout_line1 = QHBoxLayout()
        layout_line2 = QHBoxLayout()
        layout_line3 = QHBoxLayout()
        layout_line4 = QHBoxLayout()
        layout_line5 = QHBoxLayout()
        layout_line6 = QHBoxLayout()
        layout_line7 = QHBoxLayout()
        layout_line8 = QHBoxLayout()
        layout_line9 = QHBoxLayout()
        layout_line10 = QHBoxLayout()
        layout_line1.addWidget(food_in1)
        layout_line2.addWidget(food_in2)
        layout_line3.addWidget(food_in3)
        layout_line4.addWidget(food_in4)
        layout_line5.addWidget(food_in5)
        layout_line6.addWidget(food_in6)
        layout_line7.addWidget(food_in7)
        layout_line8.addWidget(food_in8)
        layout_line9.addWidget(food_in9)
        layout_line10.addWidget(food_in10)
        food_in1.show()
        food_in2.show()
        food_in3.show()
        food_in4.show()
        food_in5.show()
        food_in6.show()
        food_in7.show()
        food_in8.show()
        food_in9.show()
        food_in10.show()

    def need_the_time(self):
        time = QTime.currentTime()
        show_time = QMessageBox(main_win)
        show_time.setStyleSheet("background-color: mistyrose;")
        show_time.setText("This is the time now: " + time.toString())
        show_time.setGeometry(QtCore.QRect(865, 300, 120, 35))
        show_time.exec_()

    def remove_the_object(self):
        choose1 = QPushButton(main_win)
        choose1.setGeometry((QtCore.QRect(190, 200, 150, 40)))
        choose1.setStyleSheet("border: black;")
        choose1.show()
        
        
    main_win.setWindowTitle("Fridgerator")
    main_win.setGeometry(650, 300, 700, 700)
    main_win.setWindowIcon(QIcon("icoon.png"))

    add_btn = QPushButton(main_win)
    add_btn.setStyleSheet("background-color: lightpink;")
    add_btn.setGeometry(QtCore.QRect(50, 150, 120, 35))
    add_btn.setText("Add a product")
    add_btn.clicked.connect(click_to_add)
    add_btn.clicked.connect(label)
            
    remove_btn = QPushButton(main_win)
    remove_btn.setStyleSheet("background-color: lightpink;")
    remove_btn.setGeometry(QtCore.QRect(50, 450, 120, 35))
    remove_btn.setText("Remove a product")
    remove_btn.clicked.connect(remove_the_object)

    ice_btn = QPushButton(main_win)
    ice_btn.setStyleSheet("background-color: lightpink;")
    ice_btn.setGeometry(QtCore.QRect(500, 150, 120, 35))
    ice_btn.setText("Put some ice")
    ice_btn.clicked.connect(make_ice)

    time_btn = QPushButton(main_win)
    time_btn.setStyleSheet("background-color: lightpink;")
    time_btn.setGeometry(QtCore.QRect(500, 450, 120, 35))
    time_btn.setText("Check time")
    time_btn.clicked.connect(need_the_time)

    main_win.show()
    app.exec_()

def is_clicked(self):
    print("it works")

main_scr()

       
