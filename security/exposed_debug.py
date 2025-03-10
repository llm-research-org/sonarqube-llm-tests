from flask import Flask

app = Flask(__name__)

def start_server():
    app.config["DEBUG"] = True  # Debug mode enabled, can potentially expose sensitive information
    app.run(host="0.0.0.0", port=5000)