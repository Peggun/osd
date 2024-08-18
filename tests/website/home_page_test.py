import requests
import socket

hostname = socket.gethostname()
ip_addr = socket.gethostbyname(hostname)

def test_server_connection():
    url = f"http://{ip_addr}:5000"
    response = requests.get(url)
    assert response.status_code == 200

def test_home_page_connection():
    url = f"http://{ip_addr}:5000/home"
    response = requests.get(url)
    assert response.status_code == 200