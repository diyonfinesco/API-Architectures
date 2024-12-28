import paho.mqtt.client as mqtt

BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "iweather/temperature"

def on_message(client, userdata, message):
    print(f"Received message: {message.payload.decode()} on topic {message.topic}")

def subscribe():
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.on_message = on_message
    client.connect(BROKER, PORT, 10)

    client.subscribe(TOPIC)
    print(f"Subscribed to topic: {TOPIC}")

    client.loop_forever()

if __name__ == "__main__":
    subscribe()
