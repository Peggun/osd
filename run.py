from src.app.website import create_app

import socket

hostname = socket.gethostname()
ip_addr = socket.gethostbyname(hostname)

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, host=ip_addr)