from PyQt5.QtWidgets import QWidget, QVBoxLayout, QApplication, QPushButton, QScrollArea, \
    QHBoxLayout, QLabel, QInputDialog, QMessageBox
from PyQt5 import QtCore
import sys


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.my_balance = my_balance
        self.count = 0
        self.inform = -1
        self.setGeometry(450, 200, 400, 400)

        self.topLayout = QHBoxLayout()
        self.topLayout.setGeometry(QtCore.QRect(5, 5, 390, 50))
        self.mainLayout = QVBoxLayout()

        self.btn = QPushButton(self)
        self.btn.move(5, 5)
        self.btn.setText("Доход")
        self.btn.clicked.connect(self.btn_plus_money)

        self.btn_2 = QPushButton(self)
        self.btn_2.move(5, 5)
        self.btn_2.setText("Расход")
        self.btn_2.clicked.connect(self.btn_minus_money)

        self.balance = QLabel(f'Ваш Баланс: {str(self.my_balance)}', self)

        self.itemsLayout = QVBoxLayout()

        self.scrollWidget = QWidget()
        self.scrollWidget.setLayout(self.itemsLayout)

        self.scrollArea = QScrollArea()
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.scrollWidget)

        self.topLayout.addWidget(self.btn)
        self.topLayout.addWidget(self.btn_2)
        self.topLayout.addWidget(self.balance)
        self.mainLayout.addLayout(self.topLayout)
        self.mainLayout.addWidget(self.scrollArea)

        self.setLayout(self.mainLayout)

    def btn_on_click(self):
        btn = QPushButton(self)
        btn.setText(str(self.count))
        self.count += 1
        self.itemsLayout.addWidget(btn)

    def btn_plus_money(self):
        corrective = QHBoxLayout()
        self.btn_added_in_plus = QPushButton(self)
        self.btn_added_in_plus.setText('Информация')
        self.showDialogForPlus()
        corrective.addWidget(self.profit)
        corrective.addWidget(self.btn_added_in_plus)
        self.itemsLayout.addLayout(corrective)

    def showDialogForPlus(self):
        cash, ok = QInputDialog.getText(self, 'Доход', 'Сколько получили?')

        if ok:
            self.profit = QLabel(f'+{str(cash)}', self)
            self.my_balance += int(cash)
            self.balance.setText(f'Ваш баланс: {str(self.my_balance)}')

    def btn_minus_money(self):
        corrective = QHBoxLayout()
        self.btn_added_in_minus = QPushButton(self)
        self.btn_added_in_minus.setText('Информация')
        self.showDialogForMinus()
        self.showDialogForInformation()
        self.btn_added_in_minus.clicked.connect(self.btn_for_information)
        corrective.addWidget(self.outgo)
        corrective.addWidget(self.btn_added_in_minus)
        self.itemsLayout.addLayout(corrective)

    def showDialogForMinus(self):
        cash, ok = QInputDialog.getText(self, 'Расход', 'Сколько потратили?')

        if ok:
            self.outgo = QLabel(f'-{str(cash)}', self)
            self.my_balance -= int(cash)
            self.balance.setText(f'Ваш баланс: {str(self.my_balance)}')

    def showDialogForInformation(self):
        information, ok = QInputDialog.getText(self, 'Информация', 'Описание')

        if ok:
            self.inform = information

    def btn_for_information(self, information):
        QMessageBox.information(self, 'Message', f'{information}')


if __name__ == '__main__':
    my_balance = 0
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
