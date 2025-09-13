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
        self.buttonn = QPushButton("Activation Windows", self)
        self.buttonn.clicked.connect(self.clicked2)
        self.label=QLabel("")
        self.MainLayout.addWidget(self.label)
        self.MainLayout.addWidget(self.button)
        self.MainLayout.addWidget(self.buttonn)
        self.setLayout(self.MainLayout)
    def clicked1(self):
        self.label.setText(classes.text)
    def clicked2(self):
        sel
    def clickedd(self):
        self.label.setText(classes.text1, classes.text2, classes.text3)

def main():
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()