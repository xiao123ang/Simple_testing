# utils/request_handler.py
import requests
import websockets
import asyncio

def send_request(method, url, **kwargs):
    """Send HTTP requests."""
    response = requests.request(method, url, **kwargs)
    return response

async def send_websocket_message(uri, message):
    """Send a message over WebSocket."""
    async with websockets.connect(uri) as websocket:
        await websocket.send(message)
        response = await websocket.recv()
        return response

def send_websocket_message_sync(uri, message):
    """Synchronous wrapper for sending WebSocket messages."""
    return asyncio.run(send_websocket_message(uri, message))