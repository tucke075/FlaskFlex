from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", Title = 'Home Page')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 80)