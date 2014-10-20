# Scrapper
# The data was scrapped from the following two sites and mathced with actual nfl statistics
from IPython.core.display import HTML
HTML("<iframe src=http://maddenratings.weebly.com/madden-nfl-15-key-players.html width=800 height=350></iframe>")
HTML("<iframe src=http://www.footballoutsiders.com/stats/qb2012 width=800 height=350></iframe>")

from IPython.core.display import Image

Image(url='http://bigcommentary.com/wp-content/uploads/2014/01/brady-manning-260x148.jpg', width=100 , height=100)
Image(url='http://www.sportsgrindent.com/blog/wp-content/uploads/2010/06/matthew-stafford-21.jpg', width=100 , height=100)

#setup env
%matplotlib inline
import pandas as pd
from pandas.tools.plotting import scatter_matrix
from urllib import urlopen
import scipy
import numpy as np
import pylab as pl
from patsy import dmatrices
from sklearn.linear_model import LinearRegression
from sklearn import linear_model
plt_styles_url = "https://raw.githubusercontent.com/CamDavidsonPilon/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers/master/styles/bmh_matplotlibrc.json"
r = urlopen(plt_styles_url)
plt_styles = json.load(r)
pl.rcParams.update(plt_styles)

'''
The Madden Curse:
  What is the relationship between a players on field performance
  and their rating in Madden?

*The current data only examines QBs but the scrapper can be easily modified

1) Do madden ratings do a good job of predicting performance?

2) Can we predict madden ratings based on performance?
'''

# How does performance impact madden rating?
madden_from_stats_url = 'https://raw.githubusercontent.com/bcutrell/ga_data_science/master/qb_madden_rating_from_stats.csv'
page = urlopen(madden_from_stats_url)
df = pd.read_csv(page)

# hacky data cleanup
df['QBR'][df['Year'] == df['Year'][200]] = np.nan
df['QBR'][df['Year'] == df['Year'][1]] = np.nan
pd.to_datetime(df['Year'], coerce=True)
df['Year'] =  pd.DatetimeIndex(df['Year']).year

full_df = df.dropna()

x_attrs = ['QBR', 'DVAR', 'Yards','TD', 'DVOA', 'INT']
y_attr = 'Rating'

df.head() # show missing data
full_df.head() # no missing data

df[df['Name'] == 'T.Brady'].plot(x='Year', y='Rating')

df[x_attrs].hist(figsize=(10,10))

scatter_matrix(df[x_attrs], alpha=0.2, figsize=(10, 10), diagonal='kde')

corr_matix(df)

corr(df)
corr(full_df)

corr(df, 'pearson')
corr(full_df, 'pearson')

regr = y_attr + ' ~ ' + " + ".join(x_attrs)
y, X = dmatrices(regr, data=df, return_type='dataframe')
two_by_three_scatter() # who the hell is that lower dot? 
# Matthew Stafford

mstafford = df[df['Name'] == 'M.Stafford'].set_index('Year')

tbrady = df[df['Name'] == 'T.Brady'].set_index('Year')
pmanning = df[df['Name'] == 'P.Manning'].set_index('Year')
broberger = df[df['Name'] == 'B.Roethlisberger'].set_index('Year')
dbrees = df[df['Name'] == 'D.Brees'].set_index('Year')

players_graph(tbrady, pmanning, broberger, dbrees)
player_graph(tbrady)
player_graph(pmanning)
player_graph(broberger)

# Do madden ratings do a good job of predicting performace?
stats_from_madden_url = 'https://raw.githubusercontent.com/bcutrell/ga_data_science/master/qb_stats_from_madden_rating.csv'
page = urlopen(stats_from_madden_url)
df = pd.read_csv(page)
df['QBR'][df['Year'] == df['Year'][200]] = np.nan
df['QBR'][df['Year'] == df['Year'][1]] = np.nan

full_df = df.dropna()
df.head() # show missing data
full_df.head() # no missing data

corr_matix(df)

corr(df)
corr(full_df)

corr(df, 'pearson')
corr(full_df, 'pearson')

tbrady = df[df['Name'] == 'T.Brady'].set_index('Year')
pmanning = df[df['Name'] == 'P.Manning'].set_index('Year')
broberger = df[df['Name'] == 'B.Roethlisberger'].set_index('Year')
dbrees = df[df['Name'] == 'D.Brees'].set_index('Year')

players_graph(tbrady, pmanning, broberger, dbrees)

player_graph(tbrady)
player_graph(pmanning)
player_graph(broberger)

def corr(df, method="spearman"):
  '''
    Pearson vs. Spearman
    
    Spearman: a distribution free rank statistic used to 
    determine the strength of association between two variables. It is not a measure of the
    linear relationship

    Pearson: ranks the relationship between varaibles assuming a normal distribution

    *Missing Tau, which is generally the most preferred method...
  '''
  results = []
  for x_attr in x_attrs:
    attr = {}
    if method=="spearman":
      result = scipy.stats.spearmanr(df['Rating'], df[x_attr])
    elif method=="pearson":
      result = scipy.stats.pearsonr(df[x_attr], df['Rating'])
    else:
      return "No method for " + method

    attr['attr'] = x_attr
    attr['corr'] = result[0]
    attr['pval'] = result[1]
    results.append(attr)

  return pd.DataFrame(results)

def corr_matix(df):
  corr_df = df.corr()
  plt.pcolor(corr_df)
  plt.yticks(np.arange(0.5, len(corr_df), 1), corr_df.index)
  plt.xticks(np.arange(0.5, len(corr_df), 1), corr_df.columns)
  plt.show()

def player_graph(player):
  fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(12,12))
  player[x_attrs].pct_change()[:-1].plot(ax=axes[0], kind='bar'); axes[0].set_title(player['Name'][0])
  player['Rating'].plot(ax=axes[1], linewidth=6)
  axes[0].get_xaxis().set_ticks([])

def players_graph(*players):
  x_idx = 0
  fig, axes = plt.subplots(nrows=4, ncols=2, figsize=(16,16))
  for player in players:
    player[x_attrs].pct_change()[:-1].plot(ax=axes[x_idx,0], kind='bar'); axes[x_idx,0].set_title(player['Name'][0])
    player['Rating'].plot(ax=axes[x_idx,1], linewidth=6); axes[x_idx,1].set_title(player['Name'][0])
    axes[x_idx,0].get_xaxis().set_ticks([])
    if not x_idx == 3:
      axes[x_idx,1].get_xaxis().set_ticks([])
    x_idx += 1

def two_by_three_scatter():
  f, axarr = pl.subplots(2, 3, sharey=True, figsize=(10,10))
  r, c = 0, 0
  for x_attr in x_attrs:
    if c == 3:
      r += 1; c = 0

    if c == 0:
      axarr[r,c].set_ylabel(y_attr)

    axarr[r, c].scatter(X[x_attr], y)

    temp_y, temp_X = dmatrices(('Rating ~ ' + x_attr), data=df, return_type='dataframe')
    model = LinearRegression()
    model = model.fit(temp_X,temp_y)
    axarr[r,c].plot(temp_X[x_attr], model.predict(temp_X), color='red', linewidth=2)
    axarr[r, c].set_title(x_attr)
    axarr[r, c].set_xticks(())
    c += 1
