# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'seven_day_forecast.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_dialog_7_day_forecast(object):
    def setupUi(self, dialog_7_day_forecast):
        if not dialog_7_day_forecast.objectName():
            dialog_7_day_forecast.setObjectName(u"dialog_7_day_forecast")
        dialog_7_day_forecast.setWindowModality(Qt.NonModal)
        dialog_7_day_forecast.resize(639, 322)
        dialog_7_day_forecast.setModal(True)
        self.buttonBox = QDialogButtonBox(dialog_7_day_forecast)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(270, 275, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok)
        self.listWidget = QListWidget(dialog_7_day_forecast)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(25, 80, 586, 181))
        font = QFont()
        font.setPointSize(9)
        self.listWidget.setFont(font)
        self.label = QLabel(dialog_7_day_forecast)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(25, 15, 346, 21))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setText(u"7-Day Forecast")
        self.lbl_location = QLabel(dialog_7_day_forecast)
        self.lbl_location.setObjectName(u"lbl_location")
        self.lbl_location.setGeometry(QRect(25, 40, 581, 26))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(False)
        self.lbl_location.setFont(font2)
        self.lbl_location.setText(u"7-Day Forecast")

        self.retranslateUi(dialog_7_day_forecast)
        self.buttonBox.accepted.connect(dialog_7_day_forecast.accept)
        self.buttonBox.rejected.connect(dialog_7_day_forecast.reject)

        QMetaObject.connectSlotsByName(dialog_7_day_forecast)
    # setupUi

    def retranslateUi(self, dialog_7_day_forecast):
        dialog_7_day_forecast.setWindowTitle(QCoreApplication.translate("dialog_7_day_forecast", u"12 Hour Forecast", None))
    # retranslateUi

