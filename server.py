# -*- coding: utf-8 -*-
from flask import Flask,  render_template, request
import requests
import api_keys
import random
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)
JWT = api_keys.get_JWT()
authorization_header = {'Authorization': 'Bearer {}'.format(JWT)}
# print(authorization_header)
@app.route('/')
def index():
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

@app.route('/result/<show_id>', methods=["GET", "POST"])
def result(show_id):
	show_name = request.args.get('show_name')
	r = requests.get('https://api.thetvdb.com/series/'+show_id+'/episodes', headers=authorization_header)
	if r.status_code==requests.codes.ok:
		data = r.json()['data']
		print(len(data))
		while r.json()['links']['next'] is not None:
			print('in loop')
			params = {'page':r.json()['links']['next']}
			r = requests.get('https://api.thetvdb.com/series/'+show_id+'/episodes', headers=authorization_header, params=params)
			data += r.json()['data']
			print(len(data))
		random_episode = data[random.randrange(len(data))]
	else:
		print(r.text)
		data = None
	return render_template('result.html', show_name=show_name, random_episode=random_episode)





if __name__ == '__main__':
    app.run(debug=True)