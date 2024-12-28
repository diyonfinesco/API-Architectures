import paho.mqtt.client as mqtt
import time

BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "iweather/temperature"

def publish():
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.connect(BROKER, PORT, 10)

    for i in range(30, 35): 
        message = f"Temperature {i}"
        client.publish(TOPIC, message)
        print(f"Published: {message}")
        time.sleep(1) 

    client.disconnect()

if __name__ == "__main__":
    publish()
