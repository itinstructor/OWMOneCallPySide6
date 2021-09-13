"""
    Name: one_call_class.py
    Author: William A Loring
    Created: 07/04/21
    Purpose: OOP console app
    Get lat and lon from Openweather map current weather
    Use lat and lon for One Call Weather
    Use geopy to reverse lookup to confirm location
"""

from datetime import datetime
from PySide6 import QtGui
from PySide6.QtCore import QRectF, Qt
from PySide6.QtWidgets import QMessageBox
import requests
import weather_utils
# import geocode_owm for reverse geocode
import geocode_geopy
# Request icon from url
import urllib.request


class OneCall:
    def __init__(self, owm):
        """ 
            Add owm reference to access owm from this class
        """
        # Create empty dictionary for weather data
        self.weather_data = {}
        # Create owm object reference for access
        self.owm = owm

#--------------------------------- GET LOCATION -------------------------------------#
    def get_location(self):
        """
            Get weather location and weather information
        """
        try:
            # Get the text in the lineEdit text box
            location = self.owm.lineEdit.text()
            # Get location input from user
            self.__location = location

            # Build the openweathermap api url
            url = weather_utils.URL + self.__location

            # Get the weather information out as a weather object
            response = requests.get(url)
            # print(response.text)

            # If the status_code is 200, successful connection and data
            if(response.status_code == 200):
                # Load json response into __weather dictionary
                weather_data = response.json()
                # For testing
                # print(self.__weather)
                # Let user know the connection was successful
                # print("\n[+] The connection to OpenWeatherMap was successful.")
                # Get latitude and longitude from owm
                self.__latitude = weather_data.get("coord").get("lat")
                self.__longitude = weather_data.get("coord").get("lon")

                # Reverse gecode the address with geopy Nominatim to confirm address
                self.address = geocode_geopy.reverse_geocode(
                    self.__latitude,
                    self.__longitude
                )
            else:
               # If there was a response code other than 200
                title = "Problem"
                message = f"The response status code for OWM weather was: {response.status_code}"
                message += "\nYou may have typed an invalid location."
                message += "\nPlease try again."
                QMessageBox.information(self.owm, title, message)
                # Select the input box, let the user try again
                self.owm.set_input()
        except:
            # Handle connection exception
            title = "Problem"
            message = "[-] Sorry, there was a problem \nconnecting with OWM for location."
            message += "\nPlease try again."
            QMessageBox.information(self.owm, title, message)
            # Select the input box, let the user try again
            self.owm.set_input()

        # If everything is successful, get weather
        self.owm.get_weather()

#-------------------------- GET ONE CALL WEATHER DATA -------------------------------#
    def get_one_call_weather(self):
        """ Get one call weather data """
        try:
            # Parameters for building the URL
            weather_params = {
                "lat": self.__latitude,
                "lon": self.__longitude,
                "appid": weather_utils.API_KEY,
                "units": "imperial",
                "exclude": "minutely"
            }

            # Make request to API with parameters
            self.response = requests.get(
                weather_utils.ONE_CALL_URL,
                params=weather_params
            )

            # Testing
            # print(self.response.content)
            # Raise exception if anything other than status code 200
            self.response.raise_for_status

        # Recursive call for error to try a new location
        except Exception as e:
            # print(e)
            # print("Oops, try again.")
            # Handle connection exception
            title = "Problem"
            message = "[-] Sorry, there was a problem connecting with OneCall. " + e
            message += "\nPlease try again."
            QMessageBox.information(self.owm, title, message)
            # Select the input box, let the user try again
            self.owm.set_input()

        # Get weather data as python dictionary
        self.weather_data = self.response.json()

#----------------------------- GET CURRENT WEATHER ----------------------------------#
    def get_current_weather(self):
        """
            Get current weather from One Call weather data
        """
        # Create dictionary of current weather data
        weather_dict = self.weather_data.get("current")
        # Get time of data calculation
        self.__data_time = weather_utils.convert_time(weather_dict.get("dt"))
        # Weather description, Clear, Partly Cloudy
        self.__description = weather_dict.get(
            "weather")[0].get("description").title()
        self.__temperature = weather_dict.get("temp")
        self.__feels_like = weather_dict.get("feels_like")
        self.__humidity = weather_dict.get("humidity")
        self.__wind_speed = weather_dict.get("wind_speed")
        self.degrees = weather_dict.get("wind_deg")
        self.__cardinal_direction = weather_utils.degrees_to_cardinal(
            self.degrees)
        # Get pascals and convert to inches of mercury
        self.__pressure = round(weather_dict.get('pressure') / 33.86, 2)
        self.__clouds = weather_dict.get("clouds")
        self.__uvi = weather_dict.get("uvi")
        self.__uvi_string = weather_utils.uvi_to_string(self.__uvi)
        # Get visibility in meters, convert to miles
        self.__visibility = round(
            weather_dict.get("visibility") * 0.00062137, 1)
        # Get sunrise and sunset time
        self.__sunrise_time = weather_utils.convert_time(
            weather_dict.get("sunrise"))
        self.__sunset_time = weather_utils.convert_time(
            weather_dict.get("sunset"))

#--------------------- DISPLAY WEATHER ON FORM -------------------#
    def display_weather(self):
        """
            Get information from owm_class, display on form
        """
        # Display reverse geocode address to confirm that we have the right location
        self.owm.lbl_reverse_geocode.setText(f'{self.address}')

        # Display weather information on form
        self.owm.lbl_temperature.setText(f'{self.__temperature}°F 🌡')
        self.owm.lbl_description.setText(f"{self.__description}")
        self.owm.lbl_feels_like.setText(f"{self.__feels_like}°F")
        self.owm.lbl_humidity.setText(f"{self.__humidity}%")
        self.owm.lbl_pressure.setText(f"{self.__pressure} inHg")
        self.owm.lbl_wind.setText(
            f"{self.__wind_speed} mph {self.__cardinal_direction}")
        self.owm.lbl_cloud_cover.setText(f"{self.__clouds}%")
        self.owm.lbl_uv_index.setText(f"{self.__uvi} {self.__uvi_string}")
        self.owm.lbl_visibility.setText(f"{self.__visibility} miles")
        self.owm.lbl_sunrise.setText(f"{self.__sunrise_time}")
        self.owm.lbl_sunset.setText(f"{self.__sunset_time}")
        self.owm.lbl_latitude.setText(f"{self.__latitude}")
        self.owm.lbl_longitude.setText(f"{self.__longitude}")

        # Get and display OpenWeatherMap Icon on form
        self.owm.lbl_weather_icon.setPixmap(QtGui.QPixmap(
            self.weather_icon_image))

        # Display Air Quality Index
        self.owm.lbl_aqi.setText(
            f"{self.__aqi} {self.__aqi_string}")
        self.owm.lbl_ozone.setText(f"{self.__ozone} µg/m³")
        self.owm.lbl_pm25.setText(f"{self.__pm25} µg/m³")
        self.owm.lbl_pm10.setText(f"{self.__pm10} µg/m³")
        self.owm.lbl_carbon_monoxide.setText(
            f"{self.__carbon_monoxide} µg/m³")
        self.owm.lbl_sulphur_dioxide.setText(
            f"{self.__sulphur_dioxide} µg/m³")
        self.owm.lbl_nitrogen_dioxide.setText(
            f"{self.__nitrogen_dioxide} µg/m³")

#----------------------------- 48-HOUR FORECAST -------------------------------------#
    def get_forty_eight_hour(self):
        """
            Get 48-hour forecast from One Call Weather data
        """
        # Slice 48 hours out of weather_data
        weather_slice = self.weather_data["hourly"][:]

        print()
        print("="*70)
        print(
            f"48 Hour Weather Forecast for {datetime.datetime.now():%m/%d/%Y}")
        print(f"{self.address}")
        print("="*70)

        counter = 0
        # Iterate through the hourly weather data
        for hourly_data in weather_slice:
            counter += 1
            # Only display every even data slice
            if counter % 2:
                temp = hourly_data["temp"]
                description = hourly_data["weather"][0]["main"]
                time = weather_utils.convert_hourly_time(hourly_data["dt"])
                print(f"{time:>8}: {temp:>5.1f} °F  {description}")

#------------------------------- 7-DAY FORECAST -------------------------------------#
    def get_seven_day(self):
        """
            Get 7 day forecast from One Call Weather data
        """
        # Slice the daily list out of weather_data
        weather_slice = self.weather_data["daily"][:]

        print(f"                 7 Day Forecast")
        print(f"{self.address}")
        print("="*70)
        # print(f"Weather Forecast for {datetime.datetime.now():%m/%d/%Y}")
        print(f"Date           Max       Min     Wind Spd  ")
        # Iterate through the temps
        for daily_data in weather_slice:
            temp_max = daily_data["temp"]["max"]
            temp_min = daily_data["temp"]["min"]
            wind_speed = daily_data["wind_speed"]
            description = daily_data["weather"][0]["description"].title()
            time = weather_utils.convert_day_time(daily_data["dt"])
            print(
                f"{time:>9} {temp_max:7.1f} °F | {temp_min:4.1f} °F | {wind_speed:4.1f} mph | {description}")

#-------------------------- GET WEATHER ICON FROM URL ----------------------------#
    def get_weather_icon(self):
        """
            Get OWM weather icon from url in weather dictionary
        """
        # Get url for weather icon
        icon_id = self.weather_data.get(
            "current").get("weather")[0].get("icon")
        # print(icon_id)
        weather_icon_url = f'http://openweathermap.org/img/wn/{icon_id}.png'

        # Get the data from the weather icon url
        data = urllib.request.urlopen(weather_icon_url).read()

        # Create a QT Image object
        self.weather_icon_image = QtGui.QImage()

        # Load the url data into the image object
        self.weather_icon_image.loadFromData(data)

#------------------------------- AIR QUALITY INDEX -------------------------------------#
    def get_air_quality(self):
        """ 
            Get Air Quality Index from OpenWeatherMap with API call
            How do I calculate the AQI from pollutant concentration data? 
            The AQI is the highest value calculated for each pollutant as follows:
            Identify the highest concentration among all of the monitors
            within each reporting area and truncate as follows:
              Ozone (ppm) – truncate to 3 decimal places
              PM2.5 (μg/m3) – truncate to 1 decimal place
              PM10 (μg/m3) – truncate to integer
              CO (ppm) truncate to 1 decimal place
              SO2 (ppb) – truncate to integer
              NO2 (ppb) – truncate to integer 
        """
        params = {
            "lat": self.__latitude,
            "lon": self.__longitude
        }
        # Build request with url and parameters
        url = weather_utils.OWM_AQI_ENDPOINT

        try:
            response = requests.get(url, params)
            # print(response.text)

            # If the status_code is 200, successful connection and data
            if(response.status_code == 200):
                # Load json response into dictionary
                data = response.json()
                # Air Quality Index from OWM
                self.__aqi = data.get("list")[0].get("main").get("aqi")

                # Ground level ozone, convert ug/m3 to ppm truncate to 3 decimal places
                # Get and truncate the ug/m3 data
                self.__ozone = round(data.get("list")[0].get(
                    "components").get("o3"), 3)

                # Fine particulates truncate to 1 decimal place
                self.__pm25 = round(data.get("list")[0].get(
                    "components").get("pm2_5"), 1)

                # Coarse particulates truncate to nearest integer
                self.__pm10 = round(data.get("list")[0].get(
                    "components").get("pm10"))

                # Carbon Monoxide round to 1 decimal place
                carbon_monoxide = data.get(
                    "list")[0].get("components").get("co")
                self.__carbon_monoxide = round(carbon_monoxide, 1)

                # Sulphur Dioxide round to nearest integer
                sulphur_dioxide = data.get(
                    "list")[0].get("components").get("so2")
                self.__sulphur_dioxide = round(sulphur_dioxide)

                # Nitrogen Dioxide round to nearest integer
                nitrogen_dioxide = data.get(
                    "list")[0].get("components").get("no2")
                self.__nitrogen_dioxide = round(nitrogen_dioxide)

                # Convert AQI to text
                if self.__aqi == 1:
                    self.__aqi_string = "Good"
                elif self.__aqi == 2:
                    self.__aqi_string = "Fair"
                elif self.__aqi == 3:
                    self.__aqi_string = "Moderate"
                elif self.__aqi == 4:
                    self.__aqi_string = "Poor"
                elif self.__aqi == 5:
                    self.__aqi_string = "Very Poor"
            else:
                title = "Problem"
                message = f"The response status code for OWM AQI was: {response.status_code}"
                message += "\nPlease try again."
                QMessageBox.information(self.owm, title, message)
        except:
            title = "Problem"
            message = "[-] Sorry, there was a problem connecting with OWM AQI."
            message += "\nPlease try again."
            QMessageBox.information(self.owm, title, message)

#--------------------- DRAW WEATHER ARROW -------------------#
    def draw_weather_arrow(self):
        # Get the size of the label, create pixmap the same size
        pixmap = QtGui.QPixmap(self.owm.lbl_wind_arrow.size())
        # Clear the pixmap
        pixmap.fill(Qt.transparent)
        # Create a QPainter object to draw on the pixmap
        painter = QtGui.QPainter(pixmap)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)

        # Create a pen color, width, type of line
        pen = QtGui.QPen(Qt.blue, 2, Qt.SolidLine)
        painter.setPen(pen)
        painter.drawEllipse(15, 15, 50, 50)

        # Change brush and pen color
        painter.setBrush(Qt.red)
        painter.setPen(Qt.NoPen)

        # Create rectangle to draw pie shape in
        rect = QRectF(10, 10, 60, 60)
        
        # Set the start angle + 80 degrees as drawPie starts at 90 degrees
        # multiply by 16, the drawing angle increments in 1/16 of a degree
        # Convert from clockwise to counterclockwise
        startAngle = ((-self.degrees + 80)% 360) * 16
        spanAngle = 20 * 16
        # Draw weather direction
        painter.drawPie(rect, startAngle, spanAngle)
        # End drawing, paint to pixmap
        painter.end()
        # Set pixmap to label
        self.owm.lbl_wind_arrow.setPixmap(pixmap)

#--------------------- ABOUT MESSAGE BOX -------------------#
    def about_program(self):
        title = "OpenWeatherMap OneCall Weather App"
        message = "Built with: Python 3.9.7 and PySide 6.12."
        message += "\nAuthor: Bill Loring"
        QMessageBox.about(self.owm, title, message)
