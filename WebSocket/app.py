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