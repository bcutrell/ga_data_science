'''
Pandas Work
Pose 1-3 questions you hope to answer from the data you've gathered.

1) Do madden ratings do a good job of 
predicting player performance for that season?

2) Does player performance do a good job of
predicting their madden ratings?

3) Which one does a better job?

-- Have madden ratings used more advanced statistics over time

'''
# IPython Notes
import pandas as pd
from urllib import urlopen
import numpy as np
import pylab as pl  
from patsy import dmatrices
from patsy import dmatrix
from sklearn.linear_model import LinearRegression
from sklearn import linear_model

madden_from_stats_url = 'https://raw.githubusercontent.com/bcutrell/ga_data_science/master/qb_madden_rating_from_stats.csv'
stats_from_madden_url = 'https://raw.githubusercontent.com/bcutrell/ga_data_science/master/qb_stats_from_madden_rating.csv'
page = urlopen(madden_from_stats_url)
df = pd.read_csv(page)
df['DVOA'] = df['DVOA'].replace('%','',regex=True).astype('float')
df['DVAR'] = df['DVAR'].replace(',','',regex=True).astype('float')
df['Rating'] = df['Rating'].astype('float')
df = df[df['Year'] == 2012]

def run_regre(x, y):
  ''' used to smash possible regressions '''
  x = list(x)
  if len(x) > 1:
    r = y + ' ~ ' + " + ".join(x)
  elif len(x) == 0:
    return None
  else:
    r = y + ' ~ ' + x[0]
  y, X = dmatrices(r, data=df, return_type='dataframe')
  model = LinearRegression()
  model = model.fit(X,y)
  return model.score(X,y)

for L in range(0, len(x_attrs)+1):
  for subset in itertools.combinations(x_attrs, L):
    new_regr = run_regre(subset, y_attr)
    print subset, new_regr


x_attrs = ['QBR', 'DVOA', 'DVAR', 'Yards','TD', 'INT']
y_attr = 'Rating'
regr = y_attr + ' ~ ' + " + ".join(x_attrs)

y, X = dmatrices(regr, data=df, return_type='dataframe')

model = LinearRegression()
model = model.fit(X,y)
print model.score(X,y)

model = linear_model.RidgeCV(alphas=[0.1, 1.0, 10.0], store_cv_values=True)
model.fit(X,y)

print model.coef_
print model.alpha_
print model.cv_values_

'''
  Graph data
'''
# f, axarr = pl.subplots(6, sharey=True, subplot_kw={'aspect':'equal'})
# fig, ax = plt.subplots(ncols=3, nrows=2, subplot_kw={'aspect':'equal'})

class GraphIt(object):
  def __init__(self, X, y):
    self.X = X
    self.y = y

  def two_by_three_scatter(self):
    f, axarr = pl.subplots(2, 3, sharey=True)
    r, c = 0, 0
    for x_attr in x_attrs:
      if c == 3:
        r += 1; c = 0

      if c == 0:
        axarr[r,c].set_ylabel(y_attr)

      axarr[r, c].scatter(X[x_attr], y)
      axarr[r, c].set_title(x_attr)
      c += 1

    f.tight_layout()
    pl.show()

idx = 0
for x_attr in x_attrs:
  axarr[idx].scatter(X[x_attr], y)
  axarr[idx].set_title(x_attr)
  idx += 1
pl.scatter(X['QBR'], y, color='black')
pl.scatter(X['TD'], y, color='black')
pl.plot(X['QBR'], model.predict(X), color='blue', linewidth=3)
pl.hist(y.values)

