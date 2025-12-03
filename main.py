from flask import Flask, render_template

app = Flask(__name__)

@app.route("/home")
def home():
    return render_template("index.html")

# @app.route("/left_sidebar")
# def left_sidebar():
#     return render_template("left-sidebar.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/studies")
def studies():
    return render_template("studies.html")

@app.route("/career")
def career():
    return render_template("career.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")

@app.route("/blog/day_1")
def day_1():
    return render_template("day_1.html")

@app.route("/blog/day_2")
def day_2():
    return render_template("day_2.html")

@app.route("/blog/greetings")
def greetings():
    return render_template("greetings.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/no_sidebar")
def no_sidebar():
    return render_template("no-sidebar.html")

@app.route("/right_sidebar")
def right_sidebar():
    return render_template("right-sidebar.html")

if __name__ == '__main__':
    app.run()

