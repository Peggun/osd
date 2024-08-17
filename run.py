from src.app.website import create_app
import socket
import os
import sentry_sdk
import threading
from sentry_sdk.integrations.flask import FlaskIntegration

hostname = socket.gethostname()
ip_addr = socket.gethostbyname(hostname)

app, db = create_app()

def before_send(event, hint):
    if 'exc_info' in hint:
        exc_type, exc_value, _ = hint['exc_info']
        if isinstance(exc_value, OSError) and exc_value.winerror == 10038:
            return None
        return event

print(os.environ.get('SENTRY_IO_DSN'))
sentry_sdk.init(
    dsn=os.environ.get('SENTRY_IO_DSN'),
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for tracing.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
    before_send=before_send,
    integrations=[FlaskIntegration()]
)

if __name__ == '__main__':
    try:
        server_thread=threading.Thread(target=app.run(debug=True, host=ip_addr))
        server_thread.start()
        server_thread.join()
    except KeyboardInterrupt:
        print("Shutting server down...")
    finally:
        pass
