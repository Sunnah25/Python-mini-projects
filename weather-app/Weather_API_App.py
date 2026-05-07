import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt


class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter City name:", self)
        self.city_input = QLineEdit(self)
        self.get_weather_btn = QPushButton("Get Weather", self)
        self.temp_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.desc_label = QLabel(self)
        self.initUI()



    
    def initUI(self):
        self.setWindowTitle("Weather App")
        self.setGeometry(700, 250, 400, 500)


        #layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_btn)
        vbox.addWidget(self.temp_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.desc_label)


        self.setLayout(vbox)

        #alingment
        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temp_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.desc_label.setAlignment(Qt.AlignCenter)



        #css
        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_btn.setObjectName("get_weather_btn")
        self.temp_label.setObjectName("temp_label")
        self.emoji_label.setObjectName("emoji_label")
        self.desc_label.setObjectName("desc_label")






        self.setStyleSheet("""
                            QLabel#city_label{
                                font-size:40px;
                                font-style:italic;
                           }

                           QLineEdit#city_input{
                                font-size: 40px;
                           }

                           QPushButton#get_weather_btn{
                                font-size: 30px;
                                font-weight: bold;
                           }

                           QLabel#temp_label{
                                font-size: 75px;
                           }
                           
                           QLabel#emoji_label{
                                font-size: 100px;
                                font-family: Segoe UI emoji;
                           }

                           QLabel#desc_label{
                                font-size: 50px;
                           }
                           """)







        self.get_weather_btn.clicked.connect(self.get_weather)



    def get_weather(self):
        api_key = "6f1178ca73e2fa257c3cacbf15aff33e"

        city = self.city_input.text()


        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"


        try:
            response = requests.get(url)
            response.raise_for_status()  #this method will raise an exception if there any HTTP error

            data = response.json()

            if data["cod"] == 200:
                self.display_weather(data)

        
        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400:
                    self.display_error("Bad Request:\nPlease check your input")
                case 401:
                    self.display_error("Unauthorised:\nInvalid API key")
                case 403:
                    self.display_error("Forbidden:\nAccess is denied")
                case 404:
                    self.display_error("Not found:\nCity not found")
                case 500:
                    self.display_error("Internel server error:\nPlease try again later")
                case 502:
                    self.display_error("Bad Gateway:\nInvalid response from the server")
                case 503:
                    self.display_error("Service Unavailable:\nServer is down")
                case 504:
                    self.display_error("Gateway Timeout:\nNo response from the server")
                case _:
                    self.display_error(f"HTTP error occured:\n{http_error}")



        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error:\nCheck your Internet connection.")
        except requests.exceptions.Timeout:
            self.display_error("Timout Error:\nThe request timeout")
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many redirects:\nChech the URL")
        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request error:\n{req_error}")





    def display_error(self, message):
        self.temp_label.setStyleSheet("font-size: 30px;")
        self.temp_label.setText(message)

        self.emoji_label.clear()
        self.desc_label.clear()


    def display_weather(self, data):
        self.temp_label.setStyleSheet("font-size: 75px;")
        temperature_k = data["main"]["temp"]
        temperature_C = temperature_k - 273.15
        weather_id = data["weather"][0]["id"]
        weather_desc = data["weather"][0]["description"]





        
        self.temp_label.setText(f"{temperature_C:.0f}°C")
        self.emoji_label.setText(self.get_weather_emoji(weather_id))
        self.desc_label.setText(f"{weather_desc}")
        




    @staticmethod
    def get_weather_emoji(weather_id):
        if 200 <= weather_id <= 232:
            return "⛈️"
        elif 300 <= weather_id <= 321:
            return "☁️"
        elif 500 <= weather_id <= 531:
            return "🌧️"
        elif 600 <= weather_id <= 622:
            return "❄️"
        elif 701 <= weather_id <= 741:
            return "🌫️"
        elif weather_id == 762:
            return "🌋"
        elif weather_id == 771:
            return "💨"
        elif weather_id == 781:
            return "🌪️"
        elif weather_id == 800:
            return "☀️"
        elif 801 <= weather_id <= 804:
            return "🌤️"
        else:
            return ""





if __name__=="__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())