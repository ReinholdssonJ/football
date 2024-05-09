# -*- coding: utf-8 -*-
"""

Football Script for Fantasy Football

Created on Sun Oct 22 13:56:35 2023

@author: jakob
"""

#Sample script from the website documention
#https://www.api-football.com/documentation-v3#section/Sample-Scripts/Python

# Load libraries
exec(open('libraries.py').read())

# Load custom function
exec(open('functions.py').read())

# Get some data in 
json_data = get_data(player_id=276, season=2022, league=61)

# Convert json string into a dictionary
dic = json.loads(json_data)

# The data is all in the 'response' key
response = dict(dic['response'][0])

player = response['player']

player.keys()

statistics = response['statistics'][0]

statistics.keys()






