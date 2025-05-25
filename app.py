from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    print("Trying to render index.html from:", os.listdir("templates"))
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
