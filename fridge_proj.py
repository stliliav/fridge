from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt, QTime
from PyQt5.QtWidgets import QLineEdit, QApplication, QMainWindow, QPushButton, QMessageBox, QLabel
from PyQt5.QtGui import QIcon, QFont

def main_scr():
    app = QApplication([])
    global main_win
    main_win = QMainWindow()

    def click_to_add(self):
        added = QMessageBox(main_win)
        added.setText("What do you want to add?     \n\n\n\n")
        global line
        line = QLineEdit(added)
        line.move(65,45)
        save = QPushButton(added)
        save.setText("Save")
        save.setGeometry(QtCore.QRect(15, 135, 100, 30))
        save.clicked.connect(save_product)
        added.exec_()

    def label(self):
        inside = QLabel(main_win)
        inside.setText("Inside:")
        inside.setGeometry((QtCore.QRect(300, 150, 120, 35)))
        inside.setFont(QFont('Times', 18))
        inside.show()

    def save_product(self):
        food = line.text()
        food_in = QLabel(main_win)
        food_in.setText(food)
        products = QLabel(main_win)
        food_in.setGeometry((QtCore.QRect(300, 200, 120, 35)))
        food_in.setFont(QFont('Times', 12))
        food_in.show()

    def need_the_time(self):
        time = QTime.currentTime()
        show_time = QMessageBox(main_win)
        show_time.setText("This is the time now: " + time.toString())
        show_time.setGeometry(QtCore.QRect(275, 50, 120, 35))
        show_time.exec_()
        
    main_win.setWindowTitle("Fridgerator")
    main_win.setGeometry(650, 300, 700, 700)
    main_win.setWindowIcon(QIcon("icoon.png"))

    #add radio buttons to have an ability to remove objects
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
    ice_btn.clicked.connect(is_clicked)
            
    amount_btn = QPushButton(main_win)
    amount_btn.setGeometry(QtCore.QRect(500, 450, 120, 35))
    amount_btn.setText("Set the amount")
    amount_btn.clicked.connect(is_clicked)

    time_btn = QPushButton(main_win)
    time_btn.setGeometry(QtCore.QRect(275, 75, 120, 35))
    time_btn.setText("Check time")
    time_btn.clicked.connect(need_the_time)

    main_win.show()
    app.exec_()

def is_clicked(self):
    print("it works")

#def need_the_time(self):
    #show_time = QPushButton(main_win)
    #show_time.setGeometry(QtCore.QRect(275, 50, 120, 35))
    #show_time.setText("This is the time now: " + time.toString())
    #print("This is the time now: " + time.toString())
    

class Product():
    def __init__(self, amount, type):
        self.amount = amount
        self.type = type

main_scr()
