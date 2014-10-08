'''
Pandas Work
Pose 1-3 questions you hope to answer from the data you've gathered.

1) Do madden ratings do a good job of 
predicting player performance for that season?

2) Does player performance do a good job of
predicting their madden ratings?

3) Which one does a better job?

'''
def run_data():
  # IPython Notes
  qb_stats_from_rating = 'qb_stats_from_rating.csv'
  rating_from_qb_stats = 'rating_from_qb_stats.csv'
  df = pd.read_csv(rating_from_qb_stats)

  rating_df['DVOA'] = rating_df['DVOA'].replace('%','',regex=True).astype('float')
  rating_df['DVAR'] = rating_df['DVAR'].replace(',','',regex=True).astype('float')

  import pandas as pd
  import numpy as np
  import pylab as pl
  from patsy import dmatrices
  from sklearn.linear_model import LinearRegression
  from sklearn import linear_model

  regr = 'Rating ~ QBR + DVOA + DVAR'

  y, X = dmatrices(regr, data=df, return_type='dataframe')
  pl.scatter(X['QBR'], y, color='black')
  pl.plot(X['Rating'], model.predict(X), color='blue', linewidth=3)

  model = LinearRegression()
  model = model.fit(X,y)
  model.score(X,y)

  model = linear_model.RidgeCV(alphas=[0.1, 1.0, 10.0], store_cv_values=True)
  model.fit(X,y)

  print model.coef_
  print model.alpha_
  print model.cv_values_
