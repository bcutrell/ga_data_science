'''
Data Visualization
Player Statistics vs. Madden NFL Ratings

Player Statistics:
  - DVOA ratings from football outsiders
  - Most relavent per players stats
    * TDs, yards, tackles, etc.
'''

import code # code.interact(local=locals())
import json
import urllib
import re
import nflgame # NFL database information
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

class NFLPlayer(object):
  '''
  Stores all data related to a player instance
  a player instance is their per season data
  '''
  def __init__(self, name, position, rating, year):
    self.name = name
    self.position = position
    self.rating = rating
    self.year = year
    self.dvoa = None
    self.qbr = None
    self.dvar = None
    self.stats = None

def parse_player_str(rating_str):
  position = rating_str[:2]
  rating = re.findall(r'\d+', rating_str)[0]
  name_re = re.search("\d", rating_str)
  name = rating_str[name_re.end() + 1:].strip()
  return [position, rating, name]

def convert_names(roster):
  for p in roster:
    split_name = p.name.split(" ")
    first, last = split_name[0][0] + '.', split_name[1]
    p.name = first + last
  return roster

def store_nfl_player_for(year, results):
  year_map = {"07": 2007, "08": 2008, "09": 2009, 
              "10": 2010, "11": 2011, "12": 2012, 
              "13": 2013, "25": 2014, "15": 2015}

  for player_str in results:
    try: 
      position, rating, name = \
      parse_player_str(player_str)

      nfl_player = NFLPlayer(name, position, rating, year_map[year])
      roster.append(nfl_player)

      print position, rating, name

    except:
      continue


def get_madden_ratings(years, path, version='Kimono'):
  for year in years:
    print ''
    print version
    print "**************************"
    print "Madden %s Ratings" % year
    print "**************************"

    url = path % year
    if version == 'Kimono':
      all_results = json.load(urllib.urlopen(url))['results']['collection1']
      clean_results = [p['player-ratings'] for p in all_results]

    elif version == 'BeautifulSoup':
      page = urllib.urlopen(url)
      soup = BeautifulSoup(page.read())
      all_results = soup.findAll('div',{'style':'display:block;font-size:90%'})
      clean_results = [p.text for p in all_results]

    store_nfl_player_for(year, clean_results) 

def seed_nfl_player_stats(all_nfl_players):
  '''
  TODO: This is messy and SLOW - here is what should fix this
  1. Map players by year
  2. Pass list of player objs
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

def seed_nfl_player_fo_stats(all_player_stats):
  fo_players_list = []
  player_names = []
  for year in range(2007, 2015):
    url = "http://www.footballoutsiders.com/stats/qb%s" % str(year)
    page = urllib.urlopen(url)
    soup = BeautifulSoup(page.read())
    tables = soup.findChildren('table')
    my_table = tables[0]
    rows = my_table.findChildren(['th', 'tr'])
    for row in rows[1:]:
      cells = row.findChildren('td')
      player_name = cells[0].text
      player_names.append(player_name)
      # plus one for stats to predict rating
      # plus zero for rating to predict stats
      player = filter(lambda p: p.name == player_name and p.year == year, all_player_stats)
      if player:
        player = player[0]
        player.dvar = cells[2].text
        player.dvoa = cells[6].text
        player.qbr = cells[9].text
        fo_players_list.append(player)

  return fo_players_list

def generate_csv_for_all(pos, full_player_list):
  '''
  Get the remaining data, FO or NFL
  and put into CSV form
  '''
  roster = filter(lambda p: p.position == pos, full_player_list)
  roster = convert_names(roster)
  roster_with_data = seed_nfl_player_fo_stats(roster)

  # offical NFL stats
  # seed_nfl_player_stats(roster)

  csv = []
  headers = ["Name", "Position", "Rating", "Year", "DVOA", "QBR", "DVAR"]
  csv.append(headers)
  for p in roster_with_data:
    row = [p.name, p.position, p.rating, p.year, p.dvoa, p.qbr, p.dvar]
    csv.append(row)

  # pd.DataFrame(csv).to_csv(pos.lower() + '_stats_and_madden_ratings.csv')
  pd.DataFrame(csv).to_csv(pos.lower() + '_stats_per_rating.csv')
  

# VARIABLES
madden_years = ["07", "08", "09", "10", "11", "12", "13", "25", "15"]
kim_url = "https://www.kimonolabs.com/api/9dtcwnt8?apikey=2c5543a652a646b03103e96704c3c5a9"
kimpath = "&kimpath1=madden-nfl-%s-key-players.html"
full_url = 'http://maddenratings.weebly.com/madden-nfl-%s-key-players.html'
roster = []


import argparse

def main(args):
    cmd = args.command

    if cmd == 'seed_data':
      '''
      Seed Data
        First: Create NFLPlayer objects based on yearly Madden Ratings
        Second: Seed NFLPlayer objects with season stats and FO stats
      '''

      get_madden_ratings(madden_years, full_url, version="BeautifulSoup")
      position = 'QB'
      generate_csv_for_all(position, roster)
    elif cmd == 'pandas_df':
      pass

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('command', choices=['seed_data'])
  args = parser.parse_args()
  main(args)


'''
Pandas Work
Pose 1-3 questions you hope to answer from the data you've gathered.
'''

# df = pd.read_csv('qb_stats_and_madden_ratings.csv')
# code.interact(local=locals())

'''
# IPython Notes
import statsmodels.formula.api as sm
import pandas as pd

data = pd.read_csv("~/python/ga_data_science/qb_stats_and_madden_ratings.csv")
data = data[data['Year'] == 2015]


# Statsmodels
model = sm.ols(formula="Rating ~ QBR", data=data).fit()
from patsy import dmatrices
y, X = dmatrices('Rating ~ QBR', data=data, return_type='dataframe')

import numpy as np
import pylab as pl
pl.scatter(X['QBR'], y, color='black')

## Sklearn
from sklearn.linear_model import LinearRegression
y, X = dmatrices('QBR ~ Rating', data=data, return_type='dataframe')
model = LinearRegression()
model = model.fit(X,y)
model.score(X,y)

pl.scatter(X['yr'], y, color='black')
pl.plot(X['yr'], model.predict(X), color='blue', linewidth=3)
pl.xticks(())
pl.yticks(())

pl.show()
'''