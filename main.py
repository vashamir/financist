from ui2 import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
import sys


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self, my_balance)


if __name__ == '__main__':
    my_balance = 1520
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
