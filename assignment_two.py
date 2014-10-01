'''
Data Visualization
Player Statistics vs. Madden NFL Ratings
'''
import code # code.interact(local=locals())
import json
import urllib
import re
import nflgame # NFL database information
import pandas as pd
import matplotlib.pyplot as plt

class NFLPlayer(object):
  '''
  Stores all data related to a player instance
  a player instance is there per season data
  '''
  def __init__(self, name, position, rating, year):
    self.name = name
    self.position = position
    self.rating = rating
    self.year = year
    self.stats = None

def parse_player_str(rating_str):
  position = rating_str[:2]
  rating = re.findall(r'\d+', rating_str)[0]
  name_re = re.search("\d", rating_str)
  name = rating_str[name_re.end() + 1:].strip()
  return [position, rating, name]

def store_nfl_player_for(year, results, version):
  for player in results[:5]:
    if version == 'Kimono':
      player_str = player['player-ratings']
    elif version == 'BeautifulSoup':
      player_str = player.text

    position, rating, name = \
    parse_player_str(player_str)

    nfl_player = NFLPlayer(name, position, rating, year)
    roster.append(nfl_player)

    print position, rating, name

def get_madden_ratings(years, path, version='Kimono'):
  for year in years:
    print "**************************"
    print "Madden %s Ratings" % year
    print "**************************"

    url = path % year
    if version == 'Kimono':
      query_results = json.load(urllib.urlopen(url))['results']['collection1']

    elif version == 'BeautifulSoup':

      page = urllib.urlopen(url)
      soup = BeautifulSoup(page.read())
      query_results = soup.findAll('div',{'style':'display:block;font-size:90%'})

    # needs refactor, this should not know about the version
    store_nfl_player_for(year, query_results, version) 

def seed_nfl_player_stats(all_nfl_players):
  '''
  TODO: This is messy and SLOW - here is what should fix this
  1. Map players by year
  2. Pass array of list names
  3. Match objects => update stats
  '''

  for nfl_player in all_nfl_players[:1]:
      nflgame_player = nflgame.find(nfl_player.name)

      if len(nflgame_player) == 1:
        for year in range(2009, 2014): # data starts in 2009
          try:
            all_player_stats = nflgame_player[0].stats(year)
            nfl_player.stats = all_player_stats.stats
          except:
            pass

# VARIABLES
madden_years = ["09", "10", "11", "12", "13", "25", "15"]
kim_url = "https://www.kimonolabs.com/api/9dtcwnt8?apikey=2c5543a652a646b03103e96704c3c5a9"
kimpath = "&kimpath1=madden-nfl-%s-key-players.html"
full_url = 'http://maddenratings.weebly.com/madden-nfl-%s-key-players.html'
roster = []

'''
Create NFLPlayer objects based on
yearly Madden Ratings
'''
##############################################
############### Kimono Labs ##################
##############################################
print '****   KIMONO   ****'
get_madden_ratings(madden_years, (kim_url + kimpath))

##############################################
############## Beautiful Soup ################
##############################################
print '****   BeautifulSoup   ****'
from bs4 import BeautifulSoup
get_madden_ratings(madden_years, full_url, version="BeautifulSoup")

'''
Seed NFLPlayer objects with season stats
'''
seed_nfl_player_stats(roster)

'''
Pandas Work
'''
import pandas as pd







