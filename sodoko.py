import math
import random
from sympy import cot
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *
import sympy
from functools import partial

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()


        loader = QUiLoader()
        self.ui = loader.load("sodoko.ui" , None)

        self.game = [[None for i in range(9)] for i in range(9)]
        

        for i in range(9):
            for j in range(9):
                tb = QLineEdit()
                tb.setStyleSheet("font-size :18px")
                tb.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
                self.game[i][j] = tb
                self.ui.gla.addWidget(tb , i, j) 

        self.ui.show()
        self.ui.pbt_1.clicked.connect(self.new_game)
        self.ui.btn_check.clicked.connect(self.check)
   
    def check(self):
      
        for col in range(9):
            for i in range (9):
                for j in range(9):
                    if self.game[i][col].text() == self.game[j][col].text() and i != j and self.game[i][col].text() != "" :
                        self.game[i][col].setStyleSheet("font-size :18px;color :white ;background-color:pink")

        
        for row in range(9):
            for i in range (9):
                for j in range(9):
                    if self.game[row][i].text() == self.game[row][j].text() and i != j and self.game[row][i].text() != "" :
                        self.game[row][j].setStyleSheet("font-size :18px;color :white ;background-color:pink")
    def new_game(self):
        for i in range(9):
            for j in range(9):
                self.game[i][j].setText("")
        r = random.randint(1, 6)
        file_path = f"data/s{r}.txt"
        f = open(file_path, "r")
        big_text = f.read()
        rows = big_text.split("\n")

        for i in range (9):
            numbers= rows[i].split(" ")
            for j in range (9):
                if numbers[j] != "0":
                    self.game[i][j].setStyleSheet("font-size :18px; color:green ; alignment:center")
                    self.game[i][j].setText(numbers[j])
                else: 
                    self.game[i][j].setStyleSheet("font-size :18px; color:blue ; alignment:center")
app = QApplication([])
window = Calculator()



app.exec()        