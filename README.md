# 🌦️ Desktop Weather Application

A modern desktop weather application built with **Python**, **PyQt5**, and the **OpenWeatherMap API**, featuring real-time weather data, emoji-based weather visuals, error handling, and a clean responsive GUI.

![Weather App Preview](./images/london-weather.png)

---

## 📋 Project Overview

This project is a GUI-based desktop weather application developed using **PyQt5**.

The application allows users to search for any city worldwide and instantly retrieve:

* current temperature
* weather conditions
* dynamic weather emojis
* real-time API data

The project demonstrates practical implementation of:

* API integration
* GUI development
* object-oriented programming
* exception handling
* event-driven programming
* custom UI styling using Qt stylesheets

---

## ✨ Key Features

* Real-time weather data retrieval
* Clean and responsive desktop GUI
* Dynamic weather emojis based on conditions
* OpenWeatherMap API integration
* Detailed HTTP error handling
* User-friendly interface
* Styled widgets using Qt CSS
* Temperature conversion from Kelvin to Celsius
* Multi-condition weather support

---

## 🔍 Key Functionalities

* Search weather by city name
* Display:

  * temperature
  * weather description
  * weather condition emoji
* Handle API and network errors gracefully
* Dynamic UI updates without restarting the application
* Event-driven interaction using button click signals

---

## 📁 Repository Structure

```bash
weather-app/
│
├── images/
│   └── london-weather.png
│   └── sylhet-weather.png
│
├── Weather_API_App.py                        # Main application source code
│
│
└── README.md
```

---

## 🛠️ Technologies Used

| Technology                      | Purpose                   |
| ------------------------------- | ------------------------- |
| **Python**                      | Core programming language |
| **PyQt5**                       | GUI framework             |
| **Requests**                    | API communication         |
| **OpenWeatherMap API**          | Real-time weather data    |
| **Qt Stylesheets (QSS)**        | UI styling                |
| **Object-Oriented Programming** | Application structure     |

---

## 🔄 How It Was Built

### 1. GUI Development with PyQt5

The graphical user interface was built using PyQt5 widgets including:

* `QLabel`
* `QLineEdit`
* `QPushButton`
* `QVBoxLayout`

The layout was designed vertically for simplicity and readability.

```python id="gzc85v"
vbox = QVBoxLayout()
vbox.addWidget(self.city_label)
vbox.addWidget(self.city_input)
vbox.addWidget(self.get_weather_btn)
```

---

### 2. API Integration

The application connects to the OpenWeatherMap API using the `requests` library.

A dynamic API URL is generated using the city entered by the user.

```python id="50l0vk"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
```

The returned JSON data is parsed to extract:

* temperature
* weather ID
* weather description

---

### 3. Weather Display System

Weather conditions are displayed using:

* temperature text
* weather descriptions
* condition-specific emojis

Example mappings:

| Weather Condition | Emoji |
| ----------------- | ----- |
| Thunderstorm      | ⛈️    |
| Rain              | 🌧️   |
| Snow              | ❄️    |
| Clear Sky         | ☀️    |
| Clouds            | 🌤️   |

The emoji system improves readability and user experience.

---

### 4. Error Handling

Robust exception handling was implemented to manage:

* invalid city names
* API authentication issues
* connection failures
* timeout errors
* server-side API errors

Example:

```python id="x4r2nt"
except requests.exceptions.ConnectionError:
    self.display_error("Connection Error:\nCheck your Internet connection.")
```

This ensures the application remains stable and user-friendly under unexpected conditions.

---

## 🎨 User Interface Design

The application uses custom Qt stylesheets for modern UI styling.

Styled elements include:

* large typography
* centered alignment
* custom button styling
* emoji rendering support
* responsive spacing

Example styling:

```python id="x3gnt0"
QPushButton#get_weather_btn{
    font-size: 30px;
    font-weight: bold;
}
```

---

## 📸 Screenshots

### 🌍 London Weather

**7 May 2026 — 22:15 (London Time)**

![London Weather](./images/london-weather.png)

---

### 🌴 Sylhet Weather

**7 May 2026 — 22:15 (London Time)**

![Sylhet Weather](./images/sylhet-weather.png)

---

## 🧠 Concepts Demonstrated

This project demonstrates understanding of:

* GUI development with PyQt5
* REST API integration
* JSON data parsing
* exception handling
* object-oriented programming
* event-driven programming
* desktop application architecture
* UI styling with Qt CSS

---

## 🚧 Challenges & Solutions

| Challenge                           | Solution                                                            |
| ----------------------------------- | ------------------------------------------------------------------- |
| Managing multiple HTTP errors       | Implemented detailed exception handling using `requests.exceptions` |
| Mapping weather conditions visually | Created emoji mapping system using weather IDs                      |
| Styling PyQt widgets consistently   | Used object names with Qt stylesheets                               |
| Preventing application crashes      | Added robust request validation and error handling                  |

---

## 📚 Learning Outcomes

Through this project I strengthened my understanding of:

* Python GUI development
* API consumption and integration
* handling asynchronous user interactions
* error management in real-world applications
* object-oriented application design
* desktop application styling and UX principles

---

## ▶️ How to Run

### 1. Install dependencies

```bash id="f9zzij"
pip install PyQt5 requests
```

### 2. Run the application

```bash id="3bsg1l"
python main.py
```

---

## 📂 API Source

**API:** OpenWeatherMap API
**Website:** [https://openweathermap.org/api](https://openweathermap.org/api)

---

## 👨‍💻 Author

**Mohius Sunnah Chowdhury**
Python Desktop Weather Application Project
