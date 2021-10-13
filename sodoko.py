import math
import random
from sympy import cot
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *
import sympy
from functools import partial

class Sudoku(QMainWindow):
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
                tb.setAlignment(Qt.AlignCenter)
                self.game[i][j] = tb
                self.game[i][j].textChanged.connect(self.Check)
                self.ui.gla.addWidget(tb , i, j) 

        self.ui.show()
        self.ui.pbt_1.clicked.connect(self.New_game)
        self.ui.btn_check.clicked.connect(self.Check)
        self.ui.rB_dark.clicked.connect(self.Dark)
        self.ui.pB_reset.clicked.connect(self.Reset)

    def Check(self):
      
        for col in range(9):
            for i in range (9):
                for j in range(9):
                    if self.game[i][col].text() == self.game[j][col].text() and i != j and self.game[i][col].text() != "" :
                        self.game[i][col].setStyleSheet("font-size :18px;color :white ;background-color:pink ; text-align:center")

        
        for row in range(9):
            for i in range (9):
                for j in range(9):
                    if self.game[row][i].text() == self.game[row][j].text() and i != j and self.game[row][i].text() != "" :
                        self.game[row][j].setStyleSheet("font-size :18px;color :white ;background-color:pink ; text-align:center")
    
    def New_game(self):
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
                    self.game[i][j].setStyleSheet("font-size :18px; color:green ")
                    self.game[i][j].setText(numbers[j])
                    self.game[i][j].setReadOnly(True)
                else: 
                    self.game[i][j].setStyleSheet("font-size :18px; color:blue ; alignment:center")
                    self.game[i][j].setReadOnly(False)
        msgbox = QMessageBox()
        msgbox.setText(" ")

    def Reset(self):
        for i in range(9):
            for j in range(9):
                self.game[i][j].setText('')
    
    def Dark(self):
        if self.ui.rB_dark.isChecked(): 
            self.ui.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        else:
            self.ui.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 255, 0, 255), stop:1 rgba(255, 255, 255, 255));")


app = QApplication([])
window = Sudoku()



app.exec()        