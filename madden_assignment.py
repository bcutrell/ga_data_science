from IPython.core.display import Image
Image(url='http://investorplace.com/wp-content/uploads/2013/02/tom-brady-headshot.jpg', width=100 , height=100)

#setup env
import pandas as pd
from urllib import urlopen
import numpy as np
import pylab as pl  
from patsy import dmatrices
from patsy import dmatrix
from sklearn.linear_model import LinearRegression
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
from sklearn.metrics import make_scorer
from sklearn.cross_validation import KFold

'''
How correlated is on field performance with
Madden Ratings?
'''
madden_from_stats_url = 'https://raw.githubusercontent.com/bcutrell/ga_data_science/master/qb_madden_rating_from_stats.csv'
page = urlopen(madden_from_stats_url)
df = pd.read_csv(page)
df['Year'] = df['Year'].astype('datetime64')
full_df = df.dropna()

x_attrs = ['QBR', 'DVAR', 'Yards','TD', 'DVOA', 'INT']
y_attr = 'Rating'

df.head() # show missing data
full_df.head() # no missing data

df[x_attrs].hist(figsize=(10,10))


from pandas.tools.plotting import scatter_matrix
scatter_matrix(df[x_attrs], alpha=0.2, figsize=(10, 10), diagonal='kde')

df[df['Name'] == 'T.Brady'].plot(x='Year', y='Rating')

regr = y_attr + ' ~ ' + " + ".join(x_attrs)
y, X = dmatrices(regr, data=df, return_type='dataframe')

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

import scipy
def corr(df, method="spearman"):
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


'''
Do Madden Ratings do a good job of 
predicting player performance for that season?
'''
stats_from_madden_url = 'https://raw.githubusercontent.com/bcutrell/ga_data_science/master/qb_stats_from_madden_rating.csv'
page = urlopen(stats_from_madden_url)
df = pd.read_csv(page)

# hacky way to fix qbr data
df['QBR'][df['Year'] == df['Year'][200]] = np.nan
df['QBR'][df['Year'] == df['Year'][1]] = np.nan

full_df = df.dropna()
df.head() # show missing data
full_df.head() # no missing data

y_attrs = ['QBR', 'DVAR', 'Yards','TD', 'DVOA', 'INT']
y_attr = 'Rating'

tbrady = df[df['Name'] == 'T.Brady'].set_index('Year')
pmanning = df[df['Name'] == 'P.Manning'].set_index('Year')
broberger = df[df['Name'] == 'B.Roethlisberger'].set_index('Year')
dbress = df[df['Name'] == 'D.Brees'].set_index('Year')

tbrady[x_attrs].pct_change()[:-1].plot(figsize=(10,10))
pmanning[x_attrs].pct_change()[:-1].plot(figsize=(10,10))
broberger[x_attrs].pct_change()[:-1].plot(figsize=(10,10))
dbress[x_attrs].pct_change()[:-1].plot(figsize=(10,10))

attrs = ['QBR', 'DVAR', 'Yards','TD', 'DVOA', 'INT']

# four player comparison
fig, axes = plt.subplots(nrows=4, ncols=2, figsize=(16,16))
tbrady[attrs].pct_change()[:-1].plot(ax=axes[0,0], kind='bar'); axes[0,0].set_title('Brady')
tbrady['Rating'].plot(ax=axes[0,1], linewidth=6); axes[0,1].set_title('Brady')
axes[0,0].get_xaxis().set_ticks([])
axes[0,1].get_xaxis().set_ticks([])

pmanning[attrs].pct_change()[:-1].plot(ax=axes[1,0], kind='bar'); axes[1,0].set_title('Manning')
pmanning['Rating'].plot(ax=axes[1,1], linewidth=6); axes[1,1].set_title('Manning')
axes[1,0].get_xaxis().set_ticks([])
axes[1,1].get_xaxis().set_ticks([])

broberger[attrs].pct_change()[:-1].plot(ax=axes[2,0], kind='bar'); axes[2,0].set_title('Roethlisberger')
broberger['Rating'].plot(ax=axes[2,1], linewidth=6); axes[2,1].set_title('Roethlisberger')
axes[2,0].get_xaxis().set_ticks([])
axes[2,1].get_xaxis().set_ticks([])

dbress[attrs].pct_change()[:-1].plot(ax=axes[3,0], kind='bar'); axes[3,0].set_title('Brees')
dbress['Rating'].plot(ax=axes[3,1], linewidth=6); axes[3,1].set_title('Brees')
axes[3,0].get_xaxis().set_ticks([])

# individual player vs rating
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(12,12))
tbrady[attrs].pct_change()[:-1].plot(ax=axes[0], kind='bar'); axes[0].set_title('Brady')
tbrady['Rating'].plot(ax=axes[1], linewidth=6)
axes[0].get_xaxis().set_ticks([])

fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(12,12))
pmanning[attrs].pct_change()[:-1].plot(ax=axes[0], kind='bar'); axes[0].set_title('Manning')
pmanning['Rating'].plot(ax=axes[1], linewidth=6)
axes[0].get_xaxis().set_ticks([])

corr(df)
corr(full_df)

corr(df, 'pearson')
corr(full_df, 'pearson')


