from flask import Flask, render_template

app = Flask(__name__)

@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/left_sidebar")
def left_sidebar():
    return render_template("left-sidebar.html")

@app.route("/no_sidebar")
def no_sidebar():
    return render_template("no-sidebar.html")

@app.route("/right_sidebar")
def right_sidebar():
    return render_template("right-sidebar.html")

if __name__ == '__main__':
    app.run()

