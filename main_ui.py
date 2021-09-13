# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(526, 665)
        self.action_exit = QAction(MainWindow)
        self.action_exit.setObjectName(u"action_exit")
        self.action_about = QAction(MainWindow)
        self.action_about.setObjectName(u"action_about")
        self.action_get_weather = QAction(MainWindow)
        self.action_get_weather.setObjectName(u"action_get_weather")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(15, 5, 241, 31))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label_2.setFont(font)
        self.frame_get_location = QFrame(self.centralwidget)
        self.frame_get_location.setObjectName(u"frame_get_location")
        self.frame_get_location.setGeometry(QRect(20, 50, 486, 80))
        self.frame_get_location.setFrameShape(QFrame.Panel)
        self.frame_get_location.setFrameShadow(QFrame.Plain)
        self.frame_get_location.setLineWidth(1)
        self.label = QLabel(self.frame_get_location)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 15, 91, 20))
        self.lineEdit = QLineEdit(self.frame_get_location)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(100, 15, 236, 22))
        self.lbl_reverse_geocode = QLabel(self.frame_get_location)
        self.lbl_reverse_geocode.setObjectName(u"lbl_reverse_geocode")
        self.lbl_reverse_geocode.setGeometry(QRect(10, 45, 461, 20))
        self.lbl_reverse_geocode.setWordWrap(False)
        self.btn_get_weather = QPushButton(self.frame_get_location)
        self.btn_get_weather.setObjectName(u"btn_get_weather")
        self.btn_get_weather.setGeometry(QRect(385, 15, 75, 24))
        self.frame_weather = QFrame(self.centralwidget)
        self.frame_weather.setObjectName(u"frame_weather")
        self.frame_weather.setGeometry(QRect(20, 155, 211, 426))
        self.frame_weather.setFrameShape(QFrame.Panel)
        self.frame_weather.setFrameShadow(QFrame.Plain)
        self.frame_weather.setLineWidth(1)
        self.gridLayout2 = QGridLayout(self.frame_weather)
        self.gridLayout2.setObjectName(u"gridLayout2")
        self.gridLayout2.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout2.setHorizontalSpacing(10)
        self.gridLayout2.setVerticalSpacing(12)
        self.gridLayout2.setContentsMargins(15, 15, 15, 15)
        self.label_9 = QLabel(self.frame_weather)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout2.addWidget(self.label_9, 5, 0, 1, 1)

        self.label_11 = QLabel(self.frame_weather)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout2.addWidget(self.label_11, 8, 0, 1, 1)

        self.label_10 = QLabel(self.frame_weather)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout2.addWidget(self.label_10, 9, 0, 1, 1)

        self.lbl_sunset = QLabel(self.frame_weather)
        self.lbl_sunset.setObjectName(u"lbl_sunset")
        self.lbl_sunset.setAutoFillBackground(False)
        self.lbl_sunset.setFrameShape(QFrame.Box)
        self.lbl_sunset.setFrameShadow(QFrame.Raised)

        self.gridLayout2.addWidget(self.lbl_sunset, 9, 1, 1, 1)

        self.lbl_temperature = QLabel(self.frame_weather)
        self.lbl_temperature.setObjectName(u"lbl_temperature")
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.lbl_temperature.setFont(font1)
        self.lbl_temperature.setFrameShape(QFrame.NoFrame)

        self.gridLayout2.addWidget(self.lbl_temperature, 0, 1, 1, 1)

        self.label_3 = QLabel(self.frame_weather)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout2.addWidget(self.label_3, 1, 0, 1, 1)

        self.lbl_pressure = QLabel(self.frame_weather)
        self.lbl_pressure.setObjectName(u"lbl_pressure")
        self.lbl_pressure.setAutoFillBackground(False)
        self.lbl_pressure.setFrameShape(QFrame.Box)
        self.lbl_pressure.setFrameShadow(QFrame.Raised)

        self.gridLayout2.addWidget(self.lbl_pressure, 3, 1, 1, 1)

        self.lbl_cloud_cover = QLabel(self.frame_weather)
        self.lbl_cloud_cover.setObjectName(u"lbl_cloud_cover")
        self.lbl_cloud_cover.setAutoFillBackground(False)
        self.lbl_cloud_cover.setFrameShape(QFrame.Box)
        self.lbl_cloud_cover.setFrameShadow(QFrame.Raised)

        self.gridLayout2.addWidget(self.lbl_cloud_cover, 5, 1, 1, 1)

        self.lbl_sunrise = QLabel(self.frame_weather)
        self.lbl_sunrise.setObjectName(u"lbl_sunrise")
        self.lbl_sunrise.setAutoFillBackground(False)
        self.lbl_sunrise.setFrameShape(QFrame.Box)
        self.lbl_sunrise.setFrameShadow(QFrame.Raised)

        self.gridLayout2.addWidget(self.lbl_sunrise, 8, 1, 1, 1)

        self.label_8 = QLabel(self.frame_weather)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout2.addWidget(self.label_8, 11, 0, 1, 1)

        self.lbl_longitude = QLabel(self.frame_weather)
        self.lbl_longitude.setObjectName(u"lbl_longitude")
        self.lbl_longitude.setAutoFillBackground(False)
        self.lbl_longitude.setFrameShape(QFrame.Box)
        self.lbl_longitude.setFrameShadow(QFrame.Raised)

        self.gridLayout2.addWidget(self.lbl_longitude, 11, 1, 1, 1)

        self.lbl_latitude = QLabel(self.frame_weather)
        self.lbl_latitude.setObjectName(u"lbl_latitude")
        self.lbl_latitude.setAutoFillBackground(False)
        self.lbl_latitude.setFrameShape(QFrame.Box)
        self.lbl_latitude.setFrameShadow(QFrame.Raised)

        self.gridLayout2.addWidget(self.lbl_latitude, 10, 1, 1, 1)

        self.label_4 = QLabel(self.frame_weather)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout2.addWidget(self.label_4, 2, 0, 1, 1)

        self.lbl_wind = QLabel(self.frame_weather)
        self.lbl_wind.setObjectName(u"lbl_wind")
        self.lbl_wind.setAutoFillBackground(False)
        self.lbl_wind.setFrameShape(QFrame.Box)
        self.lbl_wind.setFrameShadow(QFrame.Raised)

        self.gridLayout2.addWidget(self.lbl_wind, 4, 1, 1, 1)

        self.lbl_humidity = QLabel(self.frame_weather)
        self.lbl_humidity.setObjectName(u"lbl_humidity")
        self.lbl_humidity.setAutoFillBackground(False)
        self.lbl_humidity.setFrameShape(QFrame.Box)
        self.lbl_humidity.setFrameShadow(QFrame.Raised)

        self.gridLayout2.addWidget(self.lbl_humidity, 2, 1, 1, 1)

        self.label_5 = QLabel(self.frame_weather)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout2.addWidget(self.label_5, 3, 0, 1, 1)

        self.lbl_feels_like = QLabel(self.frame_weather)
        self.lbl_feels_like.setObjectName(u"lbl_feels_like")
        self.lbl_feels_like.setAutoFillBackground(False)
        self.lbl_feels_like.setStyleSheet(u"")
        self.lbl_feels_like.setFrameShape(QFrame.Box)
        self.lbl_feels_like.setFrameShadow(QFrame.Raised)

        self.gridLayout2.addWidget(self.lbl_feels_like, 1, 1, 1, 1)

        self.label_7 = QLabel(self.frame_weather)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout2.addWidget(self.label_7, 10, 0, 1, 1)

        self.label_6 = QLabel(self.frame_weather)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout2.addWidget(self.label_6, 4, 0, 1, 1)

        self.lbl_uv_index = QLabel(self.frame_weather)
        self.lbl_uv_index.setObjectName(u"lbl_uv_index")
        self.lbl_uv_index.setAutoFillBackground(False)
        self.lbl_uv_index.setFrameShape(QFrame.Box)
        self.lbl_uv_index.setFrameShadow(QFrame.Raised)

        self.gridLayout2.addWidget(self.lbl_uv_index, 6, 1, 1, 1)

        self.label_19 = QLabel(self.frame_weather)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout2.addWidget(self.label_19, 6, 0, 1, 1)

        self.label_20 = QLabel(self.frame_weather)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout2.addWidget(self.label_20, 7, 0, 1, 1)

        self.lbl_visibility = QLabel(self.frame_weather)
        self.lbl_visibility.setObjectName(u"lbl_visibility")
        self.lbl_visibility.setAutoFillBackground(False)
        self.lbl_visibility.setFrameShape(QFrame.Box)
        self.lbl_visibility.setFrameShadow(QFrame.Raised)

        self.gridLayout2.addWidget(self.lbl_visibility, 7, 1, 1, 1)

        self.gridLayout2.setColumnMinimumWidth(1, 100)
        self.frame_aqi = QFrame(self.centralwidget)
        self.frame_aqi.setObjectName(u"frame_aqi")
        self.frame_aqi.setGeometry(QRect(240, 320, 266, 261))
        self.frame_aqi.setFrameShape(QFrame.Panel)
        self.frame_aqi.setFrameShadow(QFrame.Plain)
        self.frame_aqi.setLineWidth(1)
        self.gridLayout = QGridLayout(self.frame_aqi)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(12)
        self.gridLayout.setContentsMargins(15, 15, 15, 15)
        self.label_12 = QLabel(self.frame_aqi)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_12, 0, 0, 1, 1)

        self.lbl_aqi = QLabel(self.frame_aqi)
        self.lbl_aqi.setObjectName(u"lbl_aqi")
        self.lbl_aqi.setAutoFillBackground(False)
        self.lbl_aqi.setStyleSheet(u"")
        self.lbl_aqi.setFrameShape(QFrame.Box)
        self.lbl_aqi.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.lbl_aqi, 0, 1, 1, 1)

        self.label_13 = QLabel(self.frame_aqi)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_13, 1, 0, 1, 1)

        self.lbl_ozone = QLabel(self.frame_aqi)
        self.lbl_ozone.setObjectName(u"lbl_ozone")
        self.lbl_ozone.setAutoFillBackground(False)
        self.lbl_ozone.setStyleSheet(u"")
        self.lbl_ozone.setFrameShape(QFrame.Box)
        self.lbl_ozone.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.lbl_ozone, 1, 1, 1, 1)

        self.label_15 = QLabel(self.frame_aqi)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_15, 2, 0, 1, 1)

        self.lbl_pm25 = QLabel(self.frame_aqi)
        self.lbl_pm25.setObjectName(u"lbl_pm25")
        self.lbl_pm25.setAutoFillBackground(False)
        self.lbl_pm25.setStyleSheet(u"")
        self.lbl_pm25.setFrameShape(QFrame.Box)
        self.lbl_pm25.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.lbl_pm25, 2, 1, 1, 1)

        self.label_18 = QLabel(self.frame_aqi)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_18, 3, 0, 1, 1)

        self.lbl_pm10 = QLabel(self.frame_aqi)
        self.lbl_pm10.setObjectName(u"lbl_pm10")
        self.lbl_pm10.setAutoFillBackground(False)
        self.lbl_pm10.setStyleSheet(u"")
        self.lbl_pm10.setFrameShape(QFrame.Box)
        self.lbl_pm10.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.lbl_pm10, 3, 1, 1, 1)

        self.label_14 = QLabel(self.frame_aqi)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_14, 4, 0, 1, 1)

        self.lbl_carbon_monoxide = QLabel(self.frame_aqi)
        self.lbl_carbon_monoxide.setObjectName(u"lbl_carbon_monoxide")
        self.lbl_carbon_monoxide.setAutoFillBackground(False)
        self.lbl_carbon_monoxide.setStyleSheet(u"")
        self.lbl_carbon_monoxide.setFrameShape(QFrame.Box)
        self.lbl_carbon_monoxide.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.lbl_carbon_monoxide, 4, 1, 1, 1)

        self.label_16 = QLabel(self.frame_aqi)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_16, 5, 0, 1, 1)

        self.lbl_sulphur_dioxide = QLabel(self.frame_aqi)
        self.lbl_sulphur_dioxide.setObjectName(u"lbl_sulphur_dioxide")
        self.lbl_sulphur_dioxide.setAutoFillBackground(False)
        self.lbl_sulphur_dioxide.setStyleSheet(u"")
        self.lbl_sulphur_dioxide.setFrameShape(QFrame.Box)
        self.lbl_sulphur_dioxide.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.lbl_sulphur_dioxide, 5, 1, 1, 1)

        self.label_17 = QLabel(self.frame_aqi)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_17, 6, 0, 1, 1)

        self.lbl_nitrogen_dioxide = QLabel(self.frame_aqi)
        self.lbl_nitrogen_dioxide.setObjectName(u"lbl_nitrogen_dioxide")
        self.lbl_nitrogen_dioxide.setAutoFillBackground(False)
        self.lbl_nitrogen_dioxide.setStyleSheet(u"")
        self.lbl_nitrogen_dioxide.setFrameShape(QFrame.Box)
        self.lbl_nitrogen_dioxide.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.lbl_nitrogen_dioxide, 6, 1, 1, 1)

        self.gridLayout.setColumnMinimumWidth(1, 80)
        self.lbl_description = QLabel(self.centralwidget)
        self.lbl_description.setObjectName(u"lbl_description")
        self.lbl_description.setGeometry(QRect(250, 170, 231, 16))
        font2 = QFont()
        font2.setPointSize(11)
        self.lbl_description.setFont(font2)
        self.lbl_description.setAlignment(Qt.AlignCenter)
        self.lbl_weather_icon = QLabel(self.centralwidget)
        self.lbl_weather_icon.setObjectName(u"lbl_weather_icon")
        self.lbl_weather_icon.setGeometry(QRect(405, 215, 50, 50))
        self.lbl_weather_icon.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.progress_bar = QProgressBar(self.centralwidget)
        self.progress_bar.setObjectName(u"progress_bar")
        self.progress_bar.setGeometry(QRect(15, 665, 118, 16))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progress_bar.sizePolicy().hasHeightForWidth())
        self.progress_bar.setSizePolicy(sizePolicy)
        self.progress_bar.setValue(0)
        self.lbl_wind_arrow = QLabel(self.centralwidget)
        self.lbl_wind_arrow.setObjectName(u"lbl_wind_arrow")
        self.lbl_wind_arrow.setGeometry(QRect(275, 200, 80, 80))
        self.lbl_wind_arrow.setFrameShape(QFrame.NoFrame)
        self.btn_exit = QPushButton(self.centralwidget)
        self.btn_exit.setObjectName(u"btn_exit")
        self.btn_exit.setGeometry(QRect(430, 10, 75, 24))
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 605, 318, 26))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 0, 10, 0)
        self.btn_12_hour_forecast = QPushButton(self.layoutWidget)
        self.btn_12_hour_forecast.setObjectName(u"btn_12_hour_forecast")

        self.horizontalLayout.addWidget(self.btn_12_hour_forecast)

        self.btn_7_day_forecast = QPushButton(self.layoutWidget)
        self.btn_7_day_forecast.setObjectName(u"btn_7_day_forecast")

        self.horizontalLayout.addWidget(self.btn_7_day_forecast)

        self.btn_48_hour_forecast = QPushButton(self.layoutWidget)
        self.btn_48_hour_forecast.setObjectName(u"btn_48_hour_forecast")

        self.horizontalLayout.addWidget(self.btn_48_hour_forecast)

        MainWindow.setCentralWidget(self.centralwidget)
        self.status_bar = QStatusBar(MainWindow)
        self.status_bar.setObjectName(u"status_bar")
        MainWindow.setStatusBar(self.status_bar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Weather App", None))
        self.action_exit.setText(QCoreApplication.translate("MainWindow", u"E&xit", None))
        self.action_about.setText(QCoreApplication.translate("MainWindow", u"&About", None))
        self.action_get_weather.setText(QCoreApplication.translate("MainWindow", u"&Get Weather", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Bill's Weather App", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Enter Location:", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"Scottsbluff, NE, US", None))
        self.lbl_reverse_geocode.setText("")
        self.btn_get_weather.setText(QCoreApplication.translate("MainWindow", u"Get Weather", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Cloud Cover:", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Sunrise:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Sunset:", None))
        self.lbl_sunset.setText("")
        self.lbl_temperature.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Feels Like:", None))
        self.lbl_pressure.setText("")
        self.lbl_cloud_cover.setText("")
        self.lbl_sunrise.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Longitude:", None))
        self.lbl_longitude.setText("")
        self.lbl_latitude.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Humidity:", None))
        self.lbl_wind.setText("")
        self.lbl_humidity.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Pressure:", None))
        self.lbl_feels_like.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Latitude:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Wind:", None))
        self.lbl_uv_index.setText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"UV Index:", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Visibility:", None))
        self.lbl_visibility.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Air Quality Index (AQI):", None))
        self.lbl_aqi.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Ground Level Ozone (O\u2083):", None))
        self.lbl_ozone.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Fine Particulates (PM25):", None))
        self.lbl_pm25.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Coarse Particulates (PM10):", None))
        self.lbl_pm10.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Carbon Monoxide (CO):", None))
        self.lbl_carbon_monoxide.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Sulphur Dioxide (SO\u2082):", None))
        self.lbl_sulphur_dioxide.setText("")
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Nitrogen Dioxide (NO\u2082):", None))
        self.lbl_nitrogen_dioxide.setText("")
        self.lbl_description.setText("")
        self.lbl_weather_icon.setText("")
        self.lbl_wind_arrow.setText("")
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.btn_12_hour_forecast.setText(QCoreApplication.translate("MainWindow", u"12 Hour Forecast", None))
        self.btn_7_day_forecast.setText(QCoreApplication.translate("MainWindow", u"7 Day Forecast", None))
        self.btn_48_hour_forecast.setText(QCoreApplication.translate("MainWindow", u"48 Hour Forecast", None))
    # retranslateUi

