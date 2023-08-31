import asyncio
import websockets

async def send_message():
    uri = "ws://localhost:6666"
    async with websockets.connect(uri) as websocket:
        text = input("Enter message: ")
        await websocket.send(f"send:{text}")
        response = await websocket.recv()
        print(response)

async def receive_messages():
    uri = "ws://localhost:6666"
    async with websockets.connect(uri) as websocket:
        await websocket.send("receive")
        messages = await websocket.recv()
        print("\nReceived Messages:")
        print(messages)

if __name__ == '__main__':
    while True:
        choice = input("Choose an action (send/receive/exit): ").lower()

        if choice == "receive":
            asyncio.get_event_loop().run_until_complete(receive_messages())
        elif choice == "send":
            asyncio.get_event_loop().run_until_complete(send_message())
        elif choice == "exit":
            break
        else:
            print("Invalid choice. Please try again.")
