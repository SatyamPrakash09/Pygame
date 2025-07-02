import turtle
import time
import requests
from datetime import datetime , timezone, timedelta
import os
import csv

filename = "iss_data.csv"
if not os.path.exists(filename):
    with open (filename, "w", newline="") as fin:
        writer = csv.writer(fin)
        writer.writerow(["Timestamp", "Latitude", "Longitude", "Velocity (kmph)"])

screen = turtle.Screen()
screen.setup(720, 360)
screen.setworldcoordinates(-180, -90, 180, 90)
screen.bgpic("world.png")
screen.register_shape("iss.gif")

iss = turtle.Turtle()
iss.shape("iss.gif")
iss.penup()

while True:
    try:
        response = requests.get("https://api.wheretheiss.at/v1/satellites/25544")
        data = response.json()
        lat = data["latitude"]
        lon = data["longitude"]
        velocity = data["velocity"]
        ts = data["timestamp"]
        ist = timezone(timedelta(hours=5, minutes=30))
        dt = datetime.fromtimestamp(ts, tz = ist)
        formated = dt.strftime("%d-%B-%Y, %I:%M:%S %p IST")
        
        print(f"ISS Current Info: \n latitude: {lat}, longitude: {lon}, \n velocity: {velocity}kmph, timestamp:{formated}")
        #entering data in csv file
        with open(filename, "a", newline="") as fin:
            writer = csv.writer(fin)
            writer.writerow([formated, lat, lon, velocity])
            
        iss.goto(lon, lat)
        iss.pendown()
    except requests.exceptions.RequestException as e:
        print("API error:", e)
        time.sleep(10)
        continue
    print("\n")
    time.sleep(3)


