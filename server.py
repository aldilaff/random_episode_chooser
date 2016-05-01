# -*- coding: utf-8 -*-
from flask import Flask,  render_template, request
import requests
import api_keys

app = Flask(__name__)
JWT = api_keys.get_JWT()
authorization_header = {'Authorization': 'Bearer {}'.format(JWT)}
# print(authorization_header)
@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route("/show_result", methods=["GET", "POST"])
def show_result():
	if request.method == "POST":
		show_name = request.form["show_name"]
		lookup_show = {'name':show_name}
		r = requests.get('https://api.thetvdb.com/search/series',headers=authorization_header, params=lookup_show)
		if r.status_code==requests.codes.ok:
			print(r)
			result = r.json()['data']
			print(result)
		else:
			print(r.text)
			result = None
	return render_template('show_result.html', show_name=show_name,
	 result=result)





if __name__ == '__main__':
    app.run(debug=True)