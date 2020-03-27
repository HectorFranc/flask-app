from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello():
    user_ip = request.remote_addr  # Ip del usuario
    return f'Your IP is: {user_ip}'
