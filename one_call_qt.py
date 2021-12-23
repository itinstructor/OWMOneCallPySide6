"""
    Name: owm_gui.py
    Author: William A Loring
    Created: 08-05-2021
    Purpose: OpenWeatherMap GUI with PySide6
    stick with pyside6 for nuitka
    Command line to rebuild ui to py
    pyside6-uic main_window.ui –o main_ui.py
    pyside6-uic twelve_hour_forecast.ui –o twelve_hour_ui.py
    pyside6-uic seven_day_forecast.ui –o seven_day_ui.py
    pyside6-uic forty_eight_hour_forecast.ui –o forty_eight_hour_ui.py
"""

# import datetime
import sys
from PySide6 import QtGui
from PySide6 import QtCore
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QDialog, QMainWindow, QMenu
# Import gui py file created by QT Designer
from main_ui import Ui_MainWindow
from twelve_hour_ui import Ui_dialog_12_hour_forecast
from seven_day_ui import Ui_dialog_7_day_forecast
from forty_eight_hour_ui import Ui_dialog_48_hour_forecast

# Import controller class
from one_call_class import OneCall
import weather_utils
# Qt dark palette
import dark_palette


#------------------- TWELVE HOUR FORECAST DIALOG CLASS ---------------#
class twelve_hour_forecast_dialog(QDialog):
    """
        Create class to display the QT Designer created dialog box
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        # Create an instance of the dialog UI
        self.twelve_ui = Ui_dialog_12_hour_forecast()

        # Run the .setupUi() method to show the GUI
        self.twelve_ui.setupUi(self)

        # Create a reference to the listWidget and label
        self.lbl_12_label = self.twelve_ui.lbl_location
        self.twelve_hour_list = self.twelve_ui.listWidget

        # Set the font for the listWidgets
        self.list_font = QtGui.QFont()
        self.list_font.setPointSize(11)
        self.list_font.setFamily("Consolas, Courier New, monospace")
        self.twelve_hour_list.setFont(self.list_font)
        # Set alternating row color property
        self.twelve_hour_list.setAlternatingRowColors(True)

    def display_info(self):
        """ Create the 12 hour forecast dialog """
        # Show the dialog with exec()
        # Blocks all other windows until this is closed
        self.exec()

    def accept(self):
        """ Overide accept event """
        # Close QDialog
        self.close()


#------------------- TWELVE HOUR FORECAST DIALOG CLASS ---------------#
class seven_day_forecast_dialog(QDialog):
    """
        Create class to display the QT Designer created dialog box
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        # Create an instance of the dialog UI
        self.seven_ui = Ui_dialog_7_day_forecast()

        # Run the .setupUi() method to show the GUI
        self.seven_ui.setupUi(self)

        # Create a reference to the listWidget and label for forecasts
        self.lbl_7_location = self.seven_ui.lbl_location
        self.seven_day_list = self.seven_ui.listWidget

        # Set the font for the listWidgets
        self.list_font = QtGui.QFont()
        self.list_font.setPointSize(11)
        self.list_font.setFamily("Consolas, Courier New, monospace")
        self.seven_day_list.setFont(self.list_font)
        # Set alternating row color property
        self.seven_day_list.setAlternatingRowColors(True)

    def display_info(self):
        """ Create the 7 day forecast dialog """
        # Show the dialog with exec()
        # Blocks all other windows until this is closed
        self.exec()

    def accept(self):
        """ Overide accept event """
        # Close QDialog
        self.close()


#------------------- TWELVE HOUR FORECAST DIALOG CLASS ---------------#
class forty_eight_hour_forecast_dialog(QDialog):
    """
        Create class to display the QT Designer created dialog box
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        # Create an instance of the dialog UI
        self.forty_eight_ui = Ui_dialog_48_hour_forecast()

        # Run the .setupUi() method to show the GUI
        self.forty_eight_ui.setupUi(self)

        # Create a reference to the listWidgets for forecasts
        self.forty_eight_list = self.forty_eight_ui.listWidget
        self.lbl_48_location = self.forty_eight_ui.lbl_location

        # Set the font for the listWidgets
        self.list_font = QtGui.QFont()
        self.list_font.setPointSize(11)
        self.list_font.setFamily("Consolas, Courier New, monospace")
        self.forty_eight_list.setFont(self.list_font)
        # Set alternating row color property
        self.forty_eight_list.setAlternatingRowColors(True)

    def display_info(self):
        """ Create the 7 day forecast dialog """
        # Show the dialog with exec()
        # Blocks all other windows until this is closed
        self.exec()

    def accept(self):
        """ Overide accept event """
        # Close QDialog
        self.close()


#----------------------- MAIN PROGRAM WINDOW ---------------------#
class OWM(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(OWM, self).__init__()

        """ Initialize PySide6 QT GUI"""
        # Create the GUI
        self.setupUi(self)
        # Remove title bar
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setFixedSize(self.size())
        # Create weather object with a reference to current class
        self.weather_class = OneCall(self)

        # Create an instance of the dialog boxes gui
        self.twelve_hour_dialog = twelve_hour_forecast_dialog()
        self.seven_day_dialog = seven_day_forecast_dialog()
        self.forty_eight_hour_dialog = forty_eight_hour_forecast_dialog()

        # Connect the clicked event/signal to the set_weather event handler/slot
        self.btn_get_weather.clicked.connect(self.weather_class.get_location)

        # Exit the program
        self.btn_exit.clicked.connect(self.close)
        self.btn_exit.setShortcut("Esc")
        self.action_exit.triggered.connect(self.close)

        self.action_about.triggered.connect(self.weather_class.about_program)
        self.action_get_weather.triggered.connect(
            self.weather_class.get_location)

        # Add widgets to status bar
        self.status_bar.setSizeGripEnabled(False)
        self.status_bar.addPermanentWidget(self.progress_bar)
        # Set statusbar tips
        self.btn_get_weather.setStatusTip("Get current weather (Press Enter)")
        self.btn_exit.setStatusTip("Exit (Press Esc)")
        self.lineEdit.setStatusTip(
            "Enter Town, State, Country (Scottsbluff, NE, US)")

        self.btn_12_hour_forecast.clicked.connect(self.show_12_hour_forecast)
        self.btn_12_hour_forecast.setEnabled(False)

        self.btn_7_day_forecast.clicked.connect(self.show_7_day_forecast)
        self.btn_7_day_forecast.setEnabled(False)
        self.btn_48_hour_forecast.clicked.connect(self.show_48_hour_forecast)
        self.btn_48_hour_forecast.setEnabled(False)

        # Select the input box
        # Wait for the user to click Get Weather or press Return
        self.set_input()

#--------------------- SELECT INPUT -------------------#
    def set_input(self):
        """ Set focus and select lineEdit, wait for user input"""
        self.lineEdit.setFocus()
        self.lineEdit.selectAll()
        self.progress_bar.setValue(0)

#--------------------- GET WEATHER -------------------#
    def get_weather(self):
        """ Get and display weather on form """
        self.progress_bar.setValue(33)
        self.weather_class.get_one_call_weather()
        self.weather_class.get_current_weather()
        self.weather_class.get_air_quality()
        self.weather_class.draw_weather_arrow()
        self.weather_class.get_weather_icon()
        self.progress_bar.setValue(66)
        self.weather_class.display_weather()
        # # Set focus and select lineEdit for next user entry
        self.lineEdit.setFocus()
        self.lineEdit.selectAll()
        self.progress_bar.setValue(100)
        self.btn_12_hour_forecast.setDisabled(False)
        self.btn_7_day_forecast.setDisabled(False)
        self.btn_48_hour_forecast.setDisabled(False)

#-------- OVERRIDE MOUSE EVENTS TO MOVE PROGRAM WINDOW -------------#
    def mousePressEvent(self, event):
        """ Override the mousePressEvent """
        # Store the current position of the mouse in previous position
        self.previous_pos = event.globalPosition()

    def mouseMoveEvent(self, event):
        """ Override the mouseMoveEvent """
        # Subtract the previous position from the current position
        delta = event.globalPosition() - self.previous_pos
        # Add the delta calculation to the current position
        self.move(self.x() + delta.x(), self.y()+delta.y())
        # Store the current position
        self.previous_pos = event.globalPosition()
        # self._drag_active = True

#-------- OVERRIDE KEYPRESS EVENTS TO CAPTURE KEYSTROKES -------------#
    # Overide the keyPressEvent
    def keyPressEvent(self, event):
        # Get location for weather
        if event.key() == QtCore.Qt.Key_Enter or QtCore.Qt.Key_Return:
            self.weather_class.get_location()

#----------------------- TWELVE HOUR FORECAST DIALOG CLASS ----------#
    def show_12_hour_forecast(self):
        """
            Get 12-hour forecast from One Call Weather data
        """
        self.twelve_hour_dialog.lbl_12_label.setText(f"{self.weather_class.address}")
        
        # Clear weather_list
        self.twelve_hour_dialog.twelve_hour_list.clear()
        # Slice 12 hours out of weather_data
        weather_slice = self.weather_class.weather_data["hourly"][:12]
        # print(
        #     f"12 Hour Weather Forecast for {datetime.datetime.now():%m/%d/%Y}")
        # print(f"{self.__address}")
        self.twelve_hour_dialog.twelve_hour_list.addItem(
            f"  Time      Temp    Humidity  Wind Spd")
        count = 0

        # Iterate through the temps
        for hourly_data in weather_slice:
            temperature = hourly_data["temp"]
            description_main = hourly_data["weather"][0]["main"]
            description = hourly_data["weather"][0]["description"]
            humidity = hourly_data["humidity"]
            wind_speed = hourly_data["wind_speed"]
            time = weather_utils.convert_hourly_time(hourly_data["dt"])
            display = f"{time:>8}: {temperature:>5.1f} °F   {humidity:4.1f} %   {wind_speed:4.1f} mph   {description_main} ({description})"
            self.twelve_hour_dialog.twelve_hour_list.addItem(
                display)
            count += 1

        # Call QDialog display_info method
        self.twelve_hour_dialog.display_info()

#----------------------- SEVEN DAY FORECAST DIALOG CLASS ----------#
    def show_7_day_forecast(self):
        """
            Get 7 day forecast from One Call Weather data
        """
        self.seven_day_dialog.lbl_7_location.setText(f"{self.weather_class.address}")
        
        # Clear weather_list
        self.seven_day_dialog.seven_day_list.clear()
        # Slice the daily list out of weather_data
        weather_slice = self.weather_class.weather_data["daily"][:]
        
        self.seven_day_dialog.seven_day_list.addItem(
            f"Date           Max       Min     Wind Spd  ")
        count = 0
        # Iterate through the forecast
        for daily_data in weather_slice:
            temp_max = daily_data["temp"]["max"]
            temp_min = daily_data["temp"]["min"]
            wind_speed = daily_data["wind_speed"]
            description_main = daily_data["weather"][0]["main"]
            description = daily_data["weather"][0]["description"]
            time = weather_utils.convert_day_time(daily_data["dt"])
            display = f"{time:>9} {temp_max:7.1f} °F   {temp_min:4.1f} °F   {wind_speed:4.1f} mph    {description_main} ({description})"
            self.seven_day_dialog.seven_day_list.addItem(
                display)
            count += 1

        # Call QDialog display_info method
        self.seven_day_dialog.display_info()

#----------------------- FORTY EIGHT HOUR FORECAST DIALOG CLASS ----------#
    def show_48_hour_forecast(self):
        """
            Get 48 hour forecast from One Call Weather data
        """
        self.forty_eight_hour_dialog.lbl_48_location.setText(f"{self.weather_class.address}")
        # Clear weather_list
        self.forty_eight_hour_dialog.forty_eight_list.clear()
        # Slice the daily list out of weather_data
        weather_slice = self.weather_class.weather_data["hourly"][:]

        count = 0
        # Iterate through the forecast
        for hourly_data in weather_slice:
            # Only display every even data slice
            if count % 2:
                temp = hourly_data["temp"]
                description_main = hourly_data["weather"][0]["main"]
                description = hourly_data["weather"][0]["main"]
                time = weather_utils.convert_hourly_time(hourly_data["dt"])
                display = f"{time:>8}   {temp:>5.1f} °F   {description_main} ({description})"
                self.forty_eight_hour_dialog.forty_eight_list.addItem(display)
            count += 1

        # Call QDialog display_info method
        self.forty_eight_hour_dialog.display_info()

#--------------------- SETUP CONTEXT MENU -------------------#
    def contextMenuEvent(self, event):
        """ 
            Override the contextMenuEvent
            Setup a context or right click menu
        """
        # Creating a menu object with the central widget as parent
        menu = QMenu(self)
        # Populating the menu with actions defined in init
        menu.addAction(self.action_about)
        menu.addAction(self.action_get_weather)
        menu.addAction(self.action_exit)
        # Launching the menu
        menu.exec(event.globalPos())


#--------------------- START APPLICATION -------------------#
def main():
    # Create application object
    owm = QApplication(sys.argv)
    # Set a QT style
    owm.setStyle('Fusion')
    # Set colors to darkPalette, from external py file
    owm.setPalette(dark_palette.darkPalette)
    # Create program object
    window = OWM()
    # Make program visible
    window.show()
    # Execute the program, setup clean exit of program
    sys.exit(owm.exec())


main()
