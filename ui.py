# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QApplication, QPushButton, QScrollArea


class Ui_MainWindow(QWidget()):
    def setupUi(self):
        self.setWindowIcon(QIcon('bank.svg'))
        super().__init__()
        self.count = 0
        self.setGeometry(300, 300, 300, 300)

        self.mainLayout = QVBoxLayout()

        self.btn = QPushButton(self)
        self.btn.move(20, 40)
        self.btn.setText("Добавить")
        self.btn.clicked.connect(self.btn_on_click)

        self.itemsLayout = QVBoxLayout()

        self.scrollWidget = QWidget()
        self.scrollWidget.setLayout(self.itemsLayout)

        self.scrollArea = QScrollArea()
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.scrollWidget)

        self.mainLayout.addWidget(self.btn)
        self.mainLayout.addWidget(self.scrollArea)

        self.setLayout(self.mainLayout)

    def btn_on_click(self):
        btn = QPushButton(self)
        btn.setText(str(self.count))
        self.count += 1
        self.itemsLayout.addWidget(btn)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Financian", "Financian"))
        self.btn.setText(_translate("MainWindow", "Добавить"))

