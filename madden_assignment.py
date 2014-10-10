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

madden_from_stats_url = 'https://raw.githubusercontent.com/bcutrell/ga_data_science/master/qb_madden_rating_from_stats.csv'
stats_from_madden_url = 'https://raw.githubusercontent.com/bcutrell/ga_data_science/master/qb_stats_from_madden_rating.csv'
page = urlopen(madden_from_stats_url)
# page = urlopen(stats_from_madden_url)
df = pd.read_csv(page)

x_attrs = ['QBR', 'DVAR', 'Yards','TD', 'DVOA', 'INT']
y_attr = 'Rating'

df.head() # show missing data

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
results = []
for x_attr in x_attrs:
  attr = {}
  # result = scipy.stats.spearmanr(df['Rating'], df[x_attr])
  # result = scipy.stats.pearsonr(df[x_attr], df['Rating'])
  attr['attr'] = x_attr
  attr['rho'] = result[0]
  attr['pval'] = result[1]
  results.append(attr)
pd.DataFrame(results)
'''

'''




'''
Do madden ratings do a good job of 
predicting player performance for that season?
'''



'''
Do madden ratings do a good job of 
predicting player performance for that season?
'''


