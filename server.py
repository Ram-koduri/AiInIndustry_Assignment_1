import asyncio
import websockets

messages = []

async def send_message(websocket, path):
    async for message in websocket:
        data = message.split(":")
        action = data[0]

        if action == "receive":
            await websocket.send("\n".join(messages))
        elif action == "send":
            text = data[1]
            messages.append(text)
            await websocket.send("Message sent successfully!")

start_server = websockets.serve(send_message, "localhost", 6666)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
