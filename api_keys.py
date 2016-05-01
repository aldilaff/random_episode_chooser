import requests
import json
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

thetvdb_key=os.getenv('TVDB_KEY')

def get_JWT():
	data ={'apikey':thetvdb_key}
	r = requests.post('https://api.thetvdb.com/login',json=data)
	return r.json()['token']
	#need to add checks that the request is successful

