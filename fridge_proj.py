from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QIcon

def main_screen():
    app = QApplication([])
    main_win = QMainWindow()
    main_win.setWindowTitle("Fridgerator")
    main_win.setGeometry(650, 300, 700, 700)
    main_win.setWindowIcon(QIcon("icoon.png"))

    add_btn = QPushButton(main_win)
    add_btn.setText("Add a product!")
    add_btn.move(50, 150)

    remove_btn = QPushButton(main_win)
    remove_btn.setText("Remove")
    remove_btn.move(50,450)

    ice_btn = QPushButton(main_win)
    ice_btn.setText("Put some ice")
    ice_btn.move(500, 150)

    amount_btn = QPushButton(main_win)
    amount_btn.setText("Set an amount")
    amount_btn.move(500, 450)

    main_win.show()
    app.exec_()

class Product():
    def __init__(self, amount, type):
        self.amount = amount
        self.type = type


main_screen()
