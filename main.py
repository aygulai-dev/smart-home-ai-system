# Smart Home AI System - main file
from data import get_sensor_data
import time

def analyze(data):
    score = 0

    if data["temperature"] > 30:
        score += 1
    if data["energy"] > 500:
        score += 1
    if data["humidity"] < 30:
        score += 1

    return score

while True:
    data = get_sensor_data()
    risk = analyze(data)

    print("\n" + "="*35)
    print("SMART HOME AI SYSTEM (LIVE)")
    print("="*35)

    print(f"Temperature: {data['temperature']}°C")
    print(f"Humidity: {data['humidity']}%")
    print(f"Energy: {data['energy']}W")

    if risk == 0:
        print("🟢 Status: NORMAL")
    elif risk == 1:
        print("🟡 Status: WARNING")
    else:
        print("🔴 Status: CRITICAL")

    print("="*35)

    time.sleep(2)
