import ISS_Info
import turtle
import time

screen = turtle.Screen()
screen.setup(720,360)
screen.setworldcoordinates(-180,-90,180,90)
screen.bgpic("world.png")
screen.register_shape("iss.gif")

iss = turtle.Turtle()
iss.shape("iss.gif")
iss.penup()

while True:
    location = ISS_Info.iss_current_loc()
    lat = location['iss_position']['latitude']
    lon = location['iss_position']['longitude']
    print("Position: \n latitude: {}, longitude: {}".format(lat,lon))
    iss.goto(float(lon),float(lat))
    iss.pendown()
    time.sleep(5)

##from skyfield.api import load, wgs84, EarthSatellite
import turtle
import time
from datetime import timedelta


# Load TLE data for ISS
stations_url = 'http://celestrak.org/NORAD/elements/stations.txt'
satellites = load.tle_file(stations_url)
by_name = {sat.name: sat for sat in satellites}
iss = by_name['ISS (ZARYA)']

# Setup turtle screen
screen = turtle.Screen()
screen.setup(720, 360)
screen.setworldcoordinates(-180, -90, 180, 90)
screen.bgpic("world.png")
screen.register_shape("iss.gif")

iss_marker = turtle.Turtle()
iss_marker.shape("iss.gif")
iss_marker.penup()

path_marker = turtle.Turtle()
path_marker.color("red")
path_marker.penup()

# Draw predicted path
ts = load.timescale()
now = ts.now()

for minutes_ahead in range(0, 91, 5):  # Next 90 minutes, every 5 minutes
    t = ts.utc(now.utc_datetime() + timedelta(minutes=minutes_ahead))
    geocentric = iss.at(t)
    subpoint = wgs84.subpoint(geocentric)
    lat = subpoint.latitude.degrees
    lon = subpoint.longitude.degrees
    path_marker.goto(lon, lat)
    path_marker.dot(2)  # draw small dot for path

# Show real-time position
while True:
    t = ts.now()
    geocentric = iss.at(t)
    subpoint = wgs84.subpoint(geocentric)
    lat = subpoint.latitude.degrees
    lon = subpoint.longitude.degrees
    print(f"Current ISS position: lat={lat}, lon={lon}")
    iss_marker.goto(lon, lat)
    time.sleep(5)
