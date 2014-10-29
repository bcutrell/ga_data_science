import code # code.interact(local=locals())
import pandas as pd
import numpy as np
import pylab as pl

from sklearn.linear_model import ( LinearRegression, LogisticRegression)
from sklearn.ensemble.weight_boosting import AdaBoostClassifier
from sklearn.ensemble.forest import (RandomForestClassifier,
                                        ExtraTreesClassifier)
# from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn import svm

'''
1. Wife's age (numerical) 
2. Wife's education (categorical) 1=low, 2, 3, 4=high 
3. Husband's education (categorical) 1=low, 2, 3, 4=high 
4. Number of children ever born (numerical) 
5. Wife's religion (binary) 0=Non-Islam, 1=Islam 
6. Wife's now working? (binary) 0=Yes, 1=No 
7. Husband's occupation (categorical) 1, 2, 3, 4 
8. Standard-of-living index (categorical) 1=low, 2, 3, 4=high 
9. Media exposure (binary) 0=Good, 1=Not good 
10. Contraceptive method used (class attribute) 1=No-use, 2=Long-term, 3=Short-term
'''

names = ["one",
"two",
"three",
"four",
"five",
"six",
"seven",
"eight",
"nine",
"ten"]

file_path = '/Users/bcutrell/python/ga_data_science/contraceptive_method_choice.csv'
df = pd.read_csv(file_path, names=names)

y, X = df[names[-1]], df[names[:-1]]

# what about using a linear regression here?
# bad idea. why?

models = [LogisticRegression,
          RandomForestClassifier,
          AdaBoostClassifier,
          ExtraTreesClassifier,
          DecisionTreeClassifier,
          KNeighborsClassifier,
          MultinomialNB,
          svm.SVC]

# from sklearn import cross_validation
from sklearn.cross_validation import cross_val_score

for model in models:
  clf = model()
  clf.fit(X.as_matrix(), np.ravel(y.as_matrix()))
  print model.__name__
  print '***************'
  results = cross_val_score(clf, X.as_matrix(), np.ravel(y.as_matrix()))
  print np.mean(results)
  print ''
