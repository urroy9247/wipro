from flask import Flask

app=Flask(__name__)

def home():
    return "Hello, Flask in Docker!"

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)