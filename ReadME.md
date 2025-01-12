# API Overview README

## Introduction
An API (Application Programming Interface) acts as a mediator that allows different software systems to communicate with each other. If you have ever been to a restaurant (if not, it’s time to treat yourself 😁), you have already encountered the perfect analogy for understanding an API. Imagine you are the customer, the kitchen is the service that cooks the food, and the waiter is the API.

### Example:
- **You (Client):** The person placing the order.
- **Waiter (API):** The mediator who takes your order and delivers it to the kitchen.
- **Kitchen (Server):** The service that processes your order and provides the result (food).

You don't walk into the kitchen yourself to prepare your meal. Instead, you rely on the waiter to carry your request to the kitchen and bring back your food. APIs play the same role in software—allowing different systems to communicate without the client directly accessing the internal processes.

---

## 1. REST (Representational State Transfer)
**Analogy:** Ordering from a restaurant menu via a waiter.

- **Best For:** General-purpose APIs, CRUD operations.
- **Key Features:** Stateless operations using standard HTTP methods (GET, POST, PUT, DELETE).

### Example Code:
```python
import requests

def rest_example():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    print(f"GET Response: {response.json()}")

    data = {"userId": 1, "title": "blah", "body": "Woow"}
    response = requests.post("https://jsonplaceholder.typicode.com/posts", json=data)
    print(f"POST Response: {response.json()}")

if __name__ == "__main__":
    print("RESTful example")
    rest_example()
```

---

## 2. GraphQL
**Analogy:** Ordering a custom pizza with exactly the toppings you want.

- **Best For:** Complex data queries where the client specifies exactly what data is needed.
- **Key Features:** Flexible, allows partial or nested data requests.

### Example Code:
```python
import requests

url = "https://countries.trevorblades.com/"

query = """
query {
  country(code: "US") {
    name
    capital
    currency
  }
}
"""

def graphql_example():
    response = requests.post(url, json={"query": query})
    if response.status_code == 200:
        print("GraphQL Response:", response.json())
    else:
        print(f"Query failed with status code {response.status_code}")

if __name__ == "__main__":
    graphql_example()
```

---

## 3. SOAP (Simple Object Access Protocol)
**Analogy:** Filling out formal forms for official processes, such as applying for a passport.

- **Best For:** Secure enterprise applications, complex transactions (e.g., banking or healthcare).
- **Key Features:** Strict structure, XML-based protocol.

### Example Code:
```python
from zeep import Client

def soap_example():
    wsdl = "http://www.dneonline.com/calculator.asmx?WSDL"
    client = Client(wsdl)

    result = client.service.Add(5, 3)
    print(f"SOAP Add result: {result}")

if __name__ == "__main__":
    print("SOAP example")
    soap_example()
```

---

## 4. WebSockets
**Analogy:** A telephone call where both sides can talk to each other in real time without hanging up.

- **Best For:** Real-time communication (e.g., chat apps, live updates).
- **Key Features:** Full-duplex communication between client and server.

### Example Code:
```python
import asyncio
import websockets

async def websocket_example():
    url = "wss://echo.websocket.org"

    async with websockets.connect(url) as websocket:
        message = "Hello World"
        print(f"Sending : {message}")
        await websocket.send(message)

        response = await websocket.recv()
        print(f"Received : {response}")

if __name__ == "__main__":
    print("WebSocket example")
    asyncio.run(websocket_example())
```

---

## 5. MQTT (Message Queuing Telemetry Transport)
**Analogy:** Subscribing to a newspaper where you receive updates when a new issue is published.

- **Best For:** IoT (Internet of Things) applications, lightweight messaging.
- **Key Features:** Publish/subscribe messaging pattern.

### Publisher Example Code:
```python
import paho.mqtt.client as mqtt
import time

BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "iweather/temperature"

def publish():
    client = mqtt.Client()
    client.connect(BROKER, PORT, 10)

    for i in range(30, 35):
        message = f"Temperature {i}"
        client.publish(TOPIC, message)
        print(f"Published: {message}")
        time.sleep(1)

    client.disconnect()

if __name__ == "__main__":
    publish()
```

### Subscriber Example Code:
```python
import paho.mqtt.client as mqtt

BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "iweather/temperature"

def on_message(client, userdata, message):
    print(f"Received message: {message.payload.decode()} on topic {message.topic}")

def subscribe():
    client = mqtt.Client()
    client.on_message = on_message
    client.connect(BROKER, PORT, 10)

    client.subscribe(TOPIC)
    print(f"Subscribed to topic: {TOPIC}")

    client.loop_forever()

if __name__ == "__main__":
    subscribe()
```

---

## Summary
Each API type has its strengths and specific use cases:

- **REST:** Simple, stateless CRUD operations.
- **GraphQL:** Flexible queries for large and complex datasets.
- **SOAP:** Secure, strict transactions suitable for enterprise systems.
- **WebSockets:** Real-time communication for live updates.
- **MQTT:** Lightweight publish/subscribe messaging for IoT applications.

This README provides a foundational understanding and example code to help you start working with different types of APIs.

