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
  for player_str in results:
    try: 
      position, rating, name = \
      parse_player_str(player_str)

      nfl_player = NFLPlayer(name, position, rating, year)
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
  for year in range(2009, 2014):
    url = "http://www.footballoutsiders.com/stats/qb%s" % str(year)
    page = urllib.urlopen(url)
    soup = BeautifulSoup(page.read())
    tables = soup.findChildren('table')
    my_table = tables[0]
    rows = my_table.findChildren(['th', 'tr'])
    for row in rows[1:]:
      cells = row.findChildren('td')
      player_name = cells[0].text
      player = filter(lambda p: p.name == player_name and p.year == str(year)[2:], all_player_stats)
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

  pd.DataFrame(csv).to_csv(pos.lower() + '_stats_and_madden_ratings.csv')
  

# VARIABLES
madden_years = ["09", "10", "11", "12", "13", "25", "15"]
kim_url = "https://www.kimonolabs.com/api/9dtcwnt8?apikey=2c5543a652a646b03103e96704c3c5a9"
kimpath = "&kimpath1=madden-nfl-%s-key-players.html"
full_url = 'http://maddenratings.weebly.com/madden-nfl-%s-key-players.html'
roster = []

'''
Seed Data

  First: Create NFLPlayer objects based on
  yearly Madden Ratings
  Second: Seed NFLPlayer objects with season stats and FO stats
'''
# Kimono Labs 
# get_madden_ratings(madden_years, (kim_url + kimpath))

# Beautiful Soup
# get_madden_ratings(madden_years, full_url, version="BeautifulSoup")

# Write to file
# position = 'QB'
# generate_csv_for_all(position, roster)

'''
Pandas Work
Pose 1-3 questions you hope to answer from the data you've gathered.
'''

df = pd.read_csv('qb_stats_and_madden_ratings.csv')
code.interact(local=locals())