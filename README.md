# 🌦️ Weather Notifier

A simple Python-based desktop notification system that fetches real-time weather data for your city and displays a friendly notification with temperature and conditions.

---

## 📌 Features

- 🌤️ Fetches current weather data using [WeatherAPI](https://www.weatherapi.com/)
- 🔔 Sends desktop notifications with temperature and condition
- 😊 Includes friendly, mood-based messages based on the weather
- 🕒 Supports scheduled daily notifications (using `schedule`)

---

## 🛠️ Technologies Used

- Python
- `requests` – for API calls  
- `plyer` – for desktop notifications  
- `schedule` – to automate periodic weather checks (optional)

---

## 🚀 How to Run

### 🔧 Step 1: Clone the repository

```bash
git clone https://github.com/AaryanPuri/weather-notifier.git
cd weather-notifier
```

### 📦 Step 2: Install dependencies

```bash
pip install -r requirements.txt
```

This installs:
- `requests`
- `plyer`
- `schedule` (optional if you're automating)

### ▶️ Step 3: Run the script

```bash
python main.py
```

### 🏙️ Step 4: Enter your city name

Example:

```text
Enter the city name: Pune
```

You’ll get a desktop notification like:

```
Weather Update for Pune
Temperature: 29°C
Condition: Partly cloudy
🌤️ Looks like a normal day.
```

---

## 👨‍💻 Author

- **Aaryan Puri**
- GitHub: [@AaryanPuri](https://github.com/AaryanPuri)

---

## 📜 License

This project is open-source and free to use for learning and personal projects.
