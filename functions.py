# -*- coding: utf-8 -*-
"""
Created on Thu May  9 22:03:16 2024

@author: jakob

Script to access the API
"""

def get_data(player_id, 
              season, 
              league,
              api_key = MyKey):
    """
    Pull data from football website with an API
    
    Parameters: 
        - player_id (int): Specifies which player to get data for
        - season (int): Specifies which season (year) to get data for
        - league (int): specifies which league to get data from, ex Champions League
        - api_key (str): Key which authenticates you for the website
        
    Returns:
        A json file with the data
        
    Ex: 
        data = get_data(player_id=276, season=2022, league=61)
    
    """
    
    # Setup connection
    conn = http.client.HTTPSConnection("v3.football.api-sports.io")
    
    headers = {
        'x-rapidapi-host': "v3.football.api-sports.io",
        'x-rapidapi-key': api_key
        }
    
    # The endpoint is the string which says what data to request from the server
    endpoint = "/players?id={}&season={}&league={}".format(player_id,
                                                           season,
                                                           league)
    
    conn.request("GET", endpoint, headers=headers)

    res = conn.getresponse()
    
    return(res.read())

