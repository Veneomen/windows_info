import sys
import os
import classes
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Info about your computer")
        self.setGeometry(700, 300, 500, 500)
        self.setStyleSheet("background-color: black")
        self.UI()
    def UI(self):
        self.MainLayout=QVBoxLayout()
        self.button=QPushButton("Info", self)
        self.button.setStyleSheet("color: green;")
        self.button.clicked.connect(self.clicked1)
        self.button2=QPushButton("System", self)
        self.button2.setStyleSheet("color: green;")
        self.button2.clicked.connect(self.clicked2)
        self.button3=QPushButton("Memory", self)
        self.button3.setStyleSheet("color: green")
        self.button3.clicked.connect(self.clicked3)
        self.button4=QPushButton("Path", self)
        self.button4.setStyleSheet("color: green;")
        self.button4.clicked.connect(self.clicked4)
        self.label=QLabel("")
        self.label.setStyleSheet("color: green;")
        self.MainLayout.addWidget(self.label)
        self.MainLayout.addWidget(self.button)
        self.MainLayout.addWidget(self.button2)
        self.MainLayout.addWidget(self.button3)
        self.MainLayout.addWidget(self.button4)
        self.setLayout(self.MainLayout)
    def clicked1(self):
        self.label.setText(classes.text1)
    def clicked2(self):
        self.label.setText(classes.text2)
    def clicked3(self):
        self.label.setText(classes.text3)
    def clicked4(self):
        self.label.setText(classes.text4)

def main():
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())

#begin
if __name__=="__main__":
    main()