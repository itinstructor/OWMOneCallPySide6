# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'twelve_hour_forecast.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_dialog_12_hour_forecast(object):
    def setupUi(self, dialog_12_hour_forecast):
        if not dialog_12_hour_forecast.objectName():
            dialog_12_hour_forecast.setObjectName(u"dialog_12_hour_forecast")
        dialog_12_hour_forecast.setWindowModality(Qt.NonModal)
        dialog_12_hour_forecast.resize(628, 378)
        dialog_12_hour_forecast.setModal(True)
        self.buttonBox = QDialogButtonBox(dialog_12_hour_forecast)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(265, 335, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok)
        self.listWidget = QListWidget(dialog_12_hour_forecast)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(25, 80, 581, 246))
        font = QFont()
        font.setPointSize(9)
        self.listWidget.setFont(font)
        self.label = QLabel(dialog_12_hour_forecast)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(25, 20, 346, 16))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setText(u"12-Hour Forecast")
        self.lbl_location = QLabel(dialog_12_hour_forecast)
        self.lbl_location.setObjectName(u"lbl_location")
        self.lbl_location.setGeometry(QRect(25, 45, 576, 21))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(False)
        self.lbl_location.setFont(font2)
        self.lbl_location.setText(u"12-Hour Forecast")

        self.retranslateUi(dialog_12_hour_forecast)
        self.buttonBox.accepted.connect(dialog_12_hour_forecast.accept)
        self.buttonBox.rejected.connect(dialog_12_hour_forecast.reject)

        QMetaObject.connectSlotsByName(dialog_12_hour_forecast)
    # setupUi

    def retranslateUi(self, dialog_12_hour_forecast):
        dialog_12_hour_forecast.setWindowTitle(QCoreApplication.translate("dialog_12_hour_forecast", u"12 Hour Forecast", None))
    # retranslateUi

