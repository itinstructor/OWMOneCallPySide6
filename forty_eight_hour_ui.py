# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'forty_eight_hour_forecast.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_dialog_48_hour_forecast(object):
    def setupUi(self, dialog_48_hour_forecast):
        if not dialog_48_hour_forecast.objectName():
            dialog_48_hour_forecast.setObjectName(u"dialog_48_hour_forecast")
        dialog_48_hour_forecast.setWindowModality(Qt.NonModal)
        dialog_48_hour_forecast.resize(645, 578)
        dialog_48_hour_forecast.setModal(True)
        self.buttonBox = QDialogButtonBox(dialog_48_hour_forecast)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(280, 535, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok)
        self.listWidget = QListWidget(dialog_48_hour_forecast)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(25, 80, 596, 446))
        font = QFont()
        font.setPointSize(9)
        self.listWidget.setFont(font)
        self.label = QLabel(dialog_48_hour_forecast)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(25, 15, 346, 21))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setText(u"48-Hour Forecast")
        self.lbl_location = QLabel(dialog_48_hour_forecast)
        self.lbl_location.setObjectName(u"lbl_location")
        self.lbl_location.setGeometry(QRect(25, 40, 591, 26))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(False)
        self.lbl_location.setFont(font2)
        self.lbl_location.setText(u"48-Hour Forecast")

        self.retranslateUi(dialog_48_hour_forecast)
        self.buttonBox.accepted.connect(dialog_48_hour_forecast.accept)
        self.buttonBox.rejected.connect(dialog_48_hour_forecast.reject)

        QMetaObject.connectSlotsByName(dialog_48_hour_forecast)
    # setupUi

    def retranslateUi(self, dialog_48_hour_forecast):
        dialog_48_hour_forecast.setWindowTitle(QCoreApplication.translate("dialog_48_hour_forecast", u"12 Hour Forecast", None))
    # retranslateUi

