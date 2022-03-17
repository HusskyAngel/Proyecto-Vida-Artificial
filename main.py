import MainWindow
import sys
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from MainWindow import *

if __name__=="__main__":
    app=QApplication(sys.argv)
    aw = Ui_MainWindow()
    w=QMainWindow()
    aw.setupUi(w)
    w.show()
    sys.exit(app.exec())
