# -*- coding: utf-8 -*-


from flask import Flask,  render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route("/result", methods=["GET", "POST"])
def result():
	if request.method == "POST":
		show_name = request.form["show_name"]
	return render_template('result.html', show_name=show_name)

if __name__ == '__main__':
    app.run(debug=True)