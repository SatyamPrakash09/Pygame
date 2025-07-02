# 🌍 ISS Tracker with Turtle Graphics

This Python project tracks the **International Space Station (ISS)** in real-time on a world map using **Turtle Graphics**, fetching data via the [wheretheiss.at API](https://wheretheiss.at/), and logs location data to a CSV file.

## 🛠️ Features

- Realtime tracking of ISS coordinates.
- Displays movement on a world map using the Turtle graphics module.
- Logs latitude, longitude, velocity, and timestamp to a CSV file.
- Custom ISS icon and background image for better visualization.

## 📦 Requirements

Make sure you have the following Python libraries installed:

```bash
pip install requests
```

You also need:

- `iss.gif` – A small icon/image for ISS.
- `world.png` – A map of the world (720x360) to be used as the background.

## 📁 Project Files

- `main.py` – Main Python script (your code).
- `world.png` – Background world map image.
- `iss.gif` – Shape/icon used to represent the ISS.
- `iss_data.csv` – CSV file where the ISS data is logged.
- `README.md` – This file.

## 🧑‍💻 How to Run

1. Clone or download the repository.

2. Make sure `world.png` and `iss.gif` are in the same directory as `main.py`.

3. Run the Python script:

```bash
python main.py
```

The turtle window will open and begin tracking the ISS in real time.

## 📝 Data Format (CSV Output)

Each line in `iss_data.csv` will look like this:

```
Timestamp, Latitude, Longitude, Velocity (kmph)
02-July-2025, 03:15:42 PM IST, -33.123, 144.567, 27600.8
```

## 🌐 API Used

- **URL**: `https://api.wheretheiss.at/v1/satellites/25544`
- Provides current location and velocity of the ISS.

## 🖼️ Example

![screenshot](screenshot.png) *(Add your own screenshot for better visualization)*

## 🚨 Error Handling

- If API fails, it will wait 10 seconds before retrying.

## 🕒 Update Frequency

- Fetches and plots ISS data every **3 seconds**.

---

## 👤 Author

**Satyam Prakash**  
📧 Email: [satyamprakash996@gmail.com](satyamprakashhp09@gmail.com)  
💼 GitHub: [SatyamPrakash09](https://github.com/SatyamPrakash09)

---

**Made with 🛰️ and 💻**
