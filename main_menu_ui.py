# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'photo_detection.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(950, 600)
        self.centralwidget = QtWidgets.QWidget(Dialog)
        self.centralwidget.setObjectName("centralwidget")
        self.FaceRecognition = QtWidgets.QWidget(self.centralwidget)
        self.FaceRecognition.setGeometry(QtCore.QRect(0, 0,950, 700))
        self.FaceRecognition.setStyleSheet("background-color: rgb(84, 84, 84);")
        self.FaceRecognition.setObjectName("FaceRecognition")
        self.pushButton = QtWidgets.QPushButton(self.FaceRecognition)
        self.pushButton.setGeometry(QtCore.QRect(610, 210, 281, 31))
        self.pushButton.setStyleSheet("background-color:goldenrod;\n"
                                      "font: 14pt \"MS Shell Dlg 2\";\n")
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.FaceRecognition)
        self.pushButton_2.setGeometry(QtCore.QRect(610, 260, 281, 31))
        self.pushButton_2.setStyleSheet("background-color:goldenrod;\n"
                                        "font: 14pt \"MS Shell Dlg 2\";\n")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setChecked(True)
        self.pushButton_3 = QtWidgets.QPushButton(self.FaceRecognition)
        self.pushButton_3.setGeometry(QtCore.QRect(610, 310, 281, 31))
        self.pushButton_3.setStyleSheet("background-color:goldenrod;\n"
                                        "font: 14pt \"MS Shell Dlg 2\";\n")
        self.pushButton_3.setObjectName("pushButton_3")
        self.photoMainMenu = QtWidgets.QLabel(self.centralwidget)
        self.photoMainMenu.setGeometry(QtCore.QRect(80, 40, 471, 471))
        self.photoMainMenu.setPixmap(QtGui.QPixmap("photo_main_menu.jpg"))
        self.photoMainMenu.setStyleSheet("border-radius: 20px;\n"
                                         "font: 20pt \"MS Shell Dlg 2\";\n")


        self._retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def _retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Face Recognition"))
        self.pushButton.setText(_translate("Dialog", "Face Detection - Cam"))
        self.pushButton_2.setText(_translate("Dialog", "Face Detection - Photo"))
        self.pushButton_3.setText(_translate("Dialog", "Face Recognition"))
