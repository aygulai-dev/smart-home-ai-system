# Simulated Smart Home Sensor Data
import random

def get_sensor_data():
    return {
        "temperature": random.randint(18, 40),
        "humidity": random.randint(30, 80),
        "energy": random.randint(100, 600)
    }
