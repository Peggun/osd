from src.app.website import create_app
import socket
import os
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
from logger.logger import Logger, LogLevels

Logger.log(f"Script started", LogLevels.DEBUG)

hostname = socket.gethostname()
ip_addr = socket.gethostbyname(hostname)

app, db = create_app()  # Now just returns the app, not db

def before_send(event, hint):
    if "exc_info" in hint:
        exc_type, exc_value, _ = hint["exc_info"]
        if isinstance(exc_value, OSError) and exc_value.winerror == 10038:
            return None
        if isinstance(exc_value, KeyboardInterrupt):
            return None
        return event

# Initializes SentryIO for Github.
sentry_sdk.init(
    dsn=os.environ.get("SENTRY_IO_DSN"),
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
    before_send=before_send,
    integrations=[FlaskIntegration()],
)

if __name__ == "__main__":
    try:
        Logger.log(f"Server starting... (Host: {ip_addr})", LogLevels.DEBUG)
        app.run(debug=True, host=ip_addr)  # Run the server.
    except KeyboardInterrupt:
        Logger.log("Shutting server down...", LogLevels.INFO)
    finally:
        Logger.log("Server has been shut down.", LogLevels.INFO)