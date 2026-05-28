# Smart Home AI System - main file
from data import get_sensor_data

data = get_sensor_data()

print("SMART HOME SYSTEM")
print("------------------")

print("Temperature:", data["temperature"])
print("Humidity:", data["humidity"])
print("Energy:", data["energy"])

if data["temperature"] > 30:
    print("WARNING: High temperature!")
if data["energy"] > 500:
    print("WARNING: High energy usage!")
