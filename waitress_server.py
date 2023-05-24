from flask import Flask
from app import app
from waitress import serve

if __name__ == '__main__':
    serve(app, host='192.168.0.134', port=8000)
