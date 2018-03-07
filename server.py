from flask import Flask, render_template, redirect, request
app = Flask(__name__)
red = 255
green = 255
blue = 255
@app.route("/")
def index():
    return render_template("index.html", red=red, green=green, blue=blue)
@app.route("/colors", methods=["POST"])
def colors():
    global red
    global green
    global blue
    red = request.form["red"]
    green = request.form["green"]
    blue = request.form["blue"]
    return redirect("/")
app.run(debug=True)