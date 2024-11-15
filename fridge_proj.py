from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt, QTime
from PyQt5.QtWidgets import QLineEdit, QApplication, QMainWindow, QPushButton, QMessageBox, QLabel, QHBoxLayout
from PyQt5.QtGui import QIcon, QFont

def main_scr():
    app = QApplication([])
    global main_win
    main_win = QMainWindow()

    def click_to_add(self):
        added = QMessageBox(main_win)
        added.setText("What do you want to add?     \n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        global line1, line2, line3, line4, line5
        line1 = QLineEdit(added)
        line1.move(65,45)

        line2 = QLineEdit(added)
        line2.move(65,80)

        line3 = QLineEdit(added)
        line3.move(65,115)

        line4 = QLineEdit(added)
        line4.move(65,150)

        line5 = QLineEdit(added)
        line5.move(65,185)

        save = QPushButton(added)
        save.setText("Save")
        save.setGeometry(QtCore.QRect(15, 335, 90, 30))
        save.clicked.connect(save_product)
        added.exec_()

    def make_ice(self):
        cubes = QLabel(main_win)
        cubes.setText("ice cubes")
        cubes.setGeometry((QtCore.QRect(300, 350, 120, 35)))
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
        food_in1.setGeometry((QtCore.QRect(300, 200, 120, 35)))
        food_in1.setFont(QFont('Times', 12))

        food2 = line2.text()
        food_in2 = QLabel(main_win)
        food_in2.setText(food2)
        food_in2.setGeometry((QtCore.QRect(300, 230, 120, 35)))
        food_in2.setFont(QFont('Times', 12))

        food3 = line3.text()
        food_in3 = QLabel(main_win)
        food_in3.setText(food3)
        food_in3.setGeometry((QtCore.QRect(300, 260, 120, 35)))
        food_in3.setFont(QFont('Times', 12))

        food4 = line4.text()
        food_in4 = QLabel(main_win)
        food_in4.setText(food4)
        food_in4.setGeometry((QtCore.QRect(300, 290, 120, 35)))
        food_in4.setFont(QFont('Times', 12))

        food5 = line5.text()
        food_in5 = QLabel(main_win)
        food_in5.setText(food5)
        food_in5.setGeometry((QtCore.QRect(300, 320, 120, 35)))
        food_in5.setFont(QFont('Times', 12))

        layout_line1 = QHBoxLayout()
        layout_line2 = QHBoxLayout()
        layout_line3 = QHBoxLayout()
        layout_line4 = QHBoxLayout()
        layout_line5 = QHBoxLayout()
        layout_line1.addWidget(food_in1)
        layout_line2.addWidget(food_in2)
        layout_line3.addWidget(food_in3)
        layout_line4.addWidget(food_in4)
        layout_line5.addWidget(food_in5)
        food_in1.show()
        food_in2.show()
        food_in3.show()
        food_in4.show()
        food_in5.show()

    def need_the_time(self):
        time = QTime.currentTime()
        show_time = QMessageBox(main_win)
        show_time.setText("This is the time now: " + time.toString())
        show_time.setGeometry(QtCore.QRect(860, 800, 120, 35))
        show_time.exec_()
        
    main_win.setWindowTitle("Fridgerator")
    main_win.setGeometry(650, 300, 700, 700)
    main_win.setWindowIcon(QIcon("icoon.png"))

    add_btn = QPushButton(main_win)
    add_btn.setGeometry(QtCore.QRect(50, 150, 120, 35))
    add_btn.setText("Add a product")
    add_btn.clicked.connect(click_to_add)
    add_btn.clicked.connect(label)
            
    remove_btn = QPushButton(main_win)
    remove_btn.setGeometry(QtCore.QRect(50, 450, 120, 35))
    remove_btn.setText("Remove a product")
    remove_btn.clicked.connect(is_clicked)

    ice_btn = QPushButton(main_win)
    ice_btn.setGeometry(QtCore.QRect(500, 150, 120, 35))
    ice_btn.setText("Put some ice")
    ice_btn.clicked.connect(make_ice)
            
    edit_btn = QPushButton(main_win)
    edit_btn.setGeometry(QtCore.QRect(500, 450, 120, 35))
    edit_btn.setText("Edit")
    edit_btn.clicked.connect(is_clicked)

    time_btn = QPushButton(main_win)
    time_btn.setGeometry(QtCore.QRect(270, 75, 120, 35))
    time_btn.setText("Check time")
    time_btn.clicked.connect(need_the_time)

    main_win.show()
    app.exec_()

def is_clicked(self):
    print("it works")
    
class Product():
    def __init__(self, amount, type):
        self.amount = amount
        self.type = type

main_scr()
