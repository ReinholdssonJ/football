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





















