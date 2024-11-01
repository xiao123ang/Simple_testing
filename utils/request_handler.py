# utils/request_handler.py
import requests

def send_request(method, url, **kwargs):
    response = requests.request(method, url, **kwargs)
    return response