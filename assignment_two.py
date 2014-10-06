'''
Pandas Work
Pose 1-3 questions you hope to answer from the data you've gathered.

1) 
'''
def run_data():
  # IPython Notes
  qb_stats_from_rating = 'qb_stats_from_rating.csv'
  rating_from_qb_stats = 'rating_from_qb_stats.csv'
  df = pd.read_csv(rating_per_qb_stats)

  # code.interact(local=locals())
  import statsmodels.formula.api as sm
  import pandas as pd

  data = pd.read_csv("python/ga_data_science/qb_stats_from_rating.csv")
  data = data[data['Year'] == 2014]

  # Statsmodels
  model = sm.ols(formula="QBR ~ Rating", data=data).fit()
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

  y, X = dmatrices('sl ~ sx + yr + rk', data=data, return_type='dataframe')
  model = LinearRegression()
  model = model.fit(X,y)
  model.score(X,y)

  from sklearn import linear_model

  model = linear_model.Ridge(alpha = .5)
  model.fit(X,y)

  print model.coef_

  from sklearn import linear_model

  model = linear_model.RidgeCV(alphas=[0.1, 1.0, 10.0])
  model.fit(X,y)

  print model.coef_
  print model.alpha_

