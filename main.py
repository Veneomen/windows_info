import sys
import os
import classes
from PyQt5.QtWidgets import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Info about your computer")
        self.setGeometry(700, 300, 500, 500)
        self.UI()
    def UI(self):
        self.MainLayout=QVBoxLayout()
        self.button=QPushButton("Info", self)
        self.button.clicked.connect(self.clicked1)
        self.button2=QPushButton("System", self)
        self.button2.clicked.connect(self.clicked2)
        self.button3=QPushButton("Memory", self)
        self.button3.clicked.connect(self.clicked3)
        self.button4=QPushButton("Path", self)
        self.button4.clicked.connect(self.clicked4)
        self.buttonn = QPushButton("Activation Windows", self)
        self.buttonn.clicked.connect(self.clickedd)
        self.label=QLabel("")
        self.MainLayout.addWidget(self.label)
        self.MainLayout.addWidget(self.button)
        self.MainLayout.addWidget(self.button2)
        self.MainLayout.addWidget(self.button3)
        self.MainLayout.addWidget(self.button4)
        self.MainLayout.addWidget(self.buttonn)
        self.setLayout(self.MainLayout)
    def clicked1(self):
        self.label.setText(classes.text1)
    def clicked2(self):
        self.label.setText(classes.text2)
    def clicked3(self):
        self.label.setText(classes.text3)
    def clicked4(self):
        self.label.setText(classes.text4)
    def clickedd(self):
        self.label.setText(classes.text1, classes.text2, classes.text3)

def main():
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()