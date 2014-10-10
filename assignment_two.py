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

# set up env
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
df = pd.read_csv(page)

# cleanup
df['DVOA'] = df['DVOA'].replace('%','',regex=True).astype('float')
df['DVAR'] = df['DVAR'].replace(',','',regex=True).astype('float')
df['Rating'] = df['Rating'].astype('float')
df['Year'] = df['Year'].astype('datetime64')
df['QBR'][df['Year'] == 2008] = np.nan
df['QBR'][df['Year'] == 2014] = np.nan

# gen regressions
x_attrs = ['QBR', 'DVAR', 'Yards','TD', 'DVOA', 'INT']
y_attr = 'Rating'
regr = y_attr + ' ~ ' + " + ".join(x_attrs)
y, X = dmatrices(regr, data=df, return_type='dataframe')

# correlation nums
df.corr() # correlation matrix

model = LinearRegression()
model = model.fit(X,y)
print model.score(X,y)

scoring = make_scorer(mean_squared_error, greater_is_better=False)
cv = KFold(X.shape[0], 10)
model = linear_model.RidgeCV(alphas=[0.1, 1.0, 10.0], cv=cv, scoring=scoring)
model.fit(X,y)

print model.coef_
print model.alpha_
print model.cv_values_

'''
  Graph data
'''
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

      temp_y, temp_X = dmatrices(('Rating ~ ' + x_attr), data=df, return_type='dataframe')
      model = LinearRegression()
      model = model.fit(temp_X,temp_y)
      axarr[r,c].plot(temp_X[x_attr], model.predict(temp_X), color='red', linewidth=2)
      axarr[r, c].set_title(x_attr)
      axarr[r, c].set_xticks(())
      c += 1

    f.savefig('foo.png', bbox_inches='tight')
    f.tight_layout()
    pl.show()

  def two_by_three_histogram(self):
    pl.hist(y.values)
    pl.hist(X['QBR'].values)


pl.scatter(X['QBR'], y, c=X['Year'])
pl.legend()

pl.scatter(X['QBR'], y, label=['2010','2011'], c=X['Year'])
pl.legend()

pl.scatter(X['QBR'], y, c=X['Year'])

pl.scatter(X['TD'], y, color='black')
pl.plot(X['QBR'], model.predict(X), color='blue', linewidth=3)

# Ranking Histogram
pl.hist(y.values)

pl.hist(X['QBR'].values)


# pandas graphing
df[x_attrs].hist()
df[x_attrs].hist(figsize=(10,10))

from pandas.tools.plotting import scatter_matrix

scatter_matrix(df[x_attrs], alpha=0.2, figsize=(10, 10), diagonal='kde')

from pandas.tools.plotting import andrews_curves
andrews_curves(df[x_attrs], 'Name')

df[x_attrs].plot(subplots=True, figsize=(6, 6));

df[df['Name'] == 'T.Brady'].plot(subplots=True, x='Year')

df[df['Name'] == 'T.Brady'].plot(subplots=True, x='Year', y='Rating')

df_scaled[df_scaled['Name'] == 'T.Brady'].plot()

# scale data

df.fillna(0, inplace=True) # remove nan

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
df_scaled = pd.DataFrame(scaler.fit_transform(df[x_attrs]), columns=x_attrs)

df_scaled['Name'] = df['Name']
df_scaled.index = df['Year']

df_scaled[df_scaled['Name'] == 'T.Brady'].plot()
df_scaled[df_scaled['Name'] == 'T.Brady'].plot(y=["DVAR","TD","INT"])

df[df['Name'] == 'T.Brady'].set_index('Year')[x_attrs].pct_change().plot()
df[df['Name'] == 'T.Brady'].set_index('Year')[x_attrs].pct_change().dropna().plot(figsize=(10,10))
df[df['Name'] == 'P.Manning'].set_index('Year')[x_attrs].pct_change().dropna().plot(figsize=(10,10))

df[df['Name'] == 'P.Manning'].set_index('Year')[x_attrs][:-1] # all but last year

