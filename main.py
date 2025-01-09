import time
import board
import adafruit_dht
import RPi.GPIO as GPIO
import requests

# Configure DHT Sensor
DHT_SENSOR = adafruit_dht.DHT11(board.D4)

# Configure LDR
LDR_PIN = 18  # Replace with your GPIO pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(LDR_PIN, GPIO.IN)

# ThingSpeak Configuration
THINGSPEAK_API_KEY = 'YOUR_API_KEY'  # Replace with your ThingSpeak API key
THINGSPEAK_URL = 'https://api.thingspeak.com/update'

def read_dht_sensor():
    """Reads temperature and humidity from the DHT sensor."""
    try:
        temperature = DHT_SENSOR.temperature
        humidity = DHT_SENSOR.humidity
        if temperature is not None and humidity is not None:
            return temperature, humidity
        else:
            print("Invalid DHT sensor data.")
            return None, None
    except Exception as e:
        print(f"Error reading DHT sensor: {e}")
        return None, None

def read_ldr():
    """Reads the light sensor value (LDR)."""
    return GPIO.input(LDR_PIN)

def upload_to_thingspeak(temp, hum, light):
    """Uploads temperature, humidity, and light data to ThingSpeak."""
    data = {
        'api_key': THINGSPEAK_API_KEY,
        'field1': temp,
        'field2': hum,
        'field3': light
    }
    try:
        response = requests.post(THINGSPEAK_URL, data=data)
        if response.status_code == 200:
            print(f"Data uploaded: Temp={temp}, Humidity={hum}, Light={light}")
        else:
            print(f"Failed to upload data: HTTP {response.status_code}")
    except Exception as e:
        print(f"Error uploading data to ThingSpeak: {e}")

try:
    while True:
        temperature, humidity = read_dht_sensor()  # Updated to use the function
        light = read_ldr()

        if temperature is not None and humidity is not None:
            print(f"Temp: {temperature:.1f}C, Humidity: {humidity:.1f}%, Light: {light}")
            upload_to_thingspeak(temperature, humidity, light)
        else:
            print("Skipping upload due to invalid sensor data.")

        time.sleep(15)  # Upload interval

except KeyboardInterrupt:
    print("Program terminated by user.")
finally:
    GPIO.cleanup()
