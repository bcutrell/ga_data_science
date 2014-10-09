import csv
import pandas as pd
import numpy as np
from patsy import dmatrices
# from sklearn.linear_model import LinearRegression
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
from sklearn.metrics import make_scorer
from sklearn.cross_validation import KFold
import itertools

class SmashBro(object):
  '''
  Headers should have no spaces or characters
  first column of dataframe must be the y variable
  the remaining should be the x variables
  '''
  def __init__(self, df):
    self.df = df
    self.scoring = make_scorer(mean_squared_error, greater_is_better=False)
    

  def run_regre(self, x, y):
    x = list(x)
    if len(x) > 1:
      r = y + ' ~ ' + " + ".join(x)
    elif len(x) == 0:
      return None
    else:
      r = y + ' ~ ' + x[0]

    y_set, X_set = dmatrices(r, data=self.df, return_type='dataframe')
    cv = KFold(X_set.shape[0], 10)
    model = linear_model.RidgeCV(alphas=[0.1, 1.0, 10.0], cv=cv, scoring=self.scoring)
    model.fit(X_set, y_set)
    return model.score(X_set,y_set)
    ## using CV to breakout train / test
    # then test on test set
    # train on ~ 2/3
    # test on ~ 1/3

  def smash(self):
    smash_scores = []
    # x_attrs = self.df.columns[1:]
    # y_attr = self.df.columns[0]
    x_attrs = ['QBR', 'DVOA', 'DVAR', 'Yards','TD', 'INT']
    y_attr = 'Rating'

    for index in range(0, len(x_attrs)+1):
      for subset in itertools.combinations(x_attrs, index):
        new_score = self.run_regre(subset, y_attr)
        smash_scores.append({subset: new_score})
        print subset, new_score

    self.write_to_csv(smash_scores)

  def write_to_csv(self, scores):
    w = csv.writer(open("smash_output.csv", "w"))
    for s in scores:
      for key, val in s.items():
        w.writerow([key, val])

import argparse

parser = argparse.ArgumentParser()
# argparse.FileType('r')
parser.add_argument('file')#, type=pd.read_csv(args.file))
args = parser.parse_args()

try:
  dataframe = pd.read_csv(args.file)
except:
  "Incorrect file path"

# try:
smash_bro = SmashBro(dataframe)
smash_bro.smash()
# except e:
#   print "Smash Error"
#   print e



