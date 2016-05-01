import requests
import json
import os

thetvdb_key=os.environ.get('TVDB_KEY')

def get_JWT():
	data ={'apikey':thetvdb_key}
	r = requests.post('https://api.thetvdb.com/login',json=data)
	return r.json()['token']
	#need to add checks that the request is successful

