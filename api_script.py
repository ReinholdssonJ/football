# -*- coding: utf-8 -*-
"""

Football Script for Fantasy Football

Created on Sun Oct 22 13:56:35 2023

@author: jakob
"""

#Sample script from the website documention
#https://www.api-football.com/documentation-v3#section/Sample-Scripts/Python
import http.client
import json

#import numpy as np
#import pandas as pd

api_key = "c9ec6c67bce8b8f11e8c83cfdb868ce9"

player_id=276
season=2022
league=61
endpoint = f"/players?id={player_id}&season={season}&league={league}"
print(endpoint)

conn = http.client.HTTPSConnection("v3.football.api-sports.io")

headers = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': api_key
    }

conn.request("GET", endpoint, headers=headers)

res = conn.getresponse()
data = res.read()

#Prints out the results as a string
print(data.decode("utf-8"))

#Trying to make the results into a dictionary.
result_string = data.decode("utf-8")

test = json.loads(result_string)
response = test['response']
player = response[0]

items_to_remove = ['get','parameters', 'errors', 'results', 'paging']

for item in items_to_remove:
    del test[item]





















