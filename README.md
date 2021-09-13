# OpenWeatherMap OneCall Python PySide6 GUI Program
OpenWeatherMap OneCall Python GUI Program with PySide6
### Overview
- Python PySide6 GUI program using requests, OpenWeatherMap API, OpenWeatherMap Air Pollution API, and Nominatim from geopy.
- Includes current and forecast weather and AQI (Air Quality Index).
- The ui was built (and a lot of time was saved) using QT Designer.
- Air Quality Index is a separate API call from OpenWeatherMap Air Pollution API.
- The lat and long retrieved from OpenWeatherMap is reverse geocoded into the name of the location using Nominatim from geopy.
    * The reverse geocoding from geopy confirms that we have the weather for the right city.
- JSON sample response files used to build the program are in the json_response_files folder.
- A batch file is included for nuitka building to a Windows exe (nuitka_gui.bat)
    * Install nuitka: pip install nuitka
### Acknowledgement
I used the following book to get started with PySide6:
Create GUI Applications with Python & Qt6 
The hands-on guide to making apps with Python
by Martin Fitzpatrick
### API Key
- To run the program, go to www.openweathermap.org. Get a free API key.
- Go to weather_utils.py. Put in your OpenWeatherMap API key.
### Changes
- 09/12/2021: Initial commit
### License
<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.
Copyright (c) 2021 William A Loring
