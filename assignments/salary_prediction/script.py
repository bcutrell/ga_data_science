import code # code.interact(local=locals())
import pandas as pd
# import statsmodels.api as sm
from sklearn import cross_validation

df = pd.read_csv('/Users/bcutrell/python/ga_data_science/assignments/salary_prediction/train1k.csv')

'''
split into city + state
'''
def location_splitter(text, case='')
  if case == 'City'
    x.split(',')[0]
  elif case == 'Country'
    x.split(',')[-1]
  elif case == 'State'
    


df['City'] = df['LocationRaw'].apply(lambda x: x.split(',')[0])
df['Country'] = df['LocationRaw'].apply(lambda x: x.split(',')[-1])
code.interact(local=locals())

X = sm.tools.tools.categorical(df['Category'].values, drop=True)
y = df['SalaryNormalized'].values

df1 = pd.get_dummies(df['Category'])
df1['Salary'] = df['SalaryNormalized']

attrs = sm.tools.tools.categorical(df.columns.values, drop=True)

train_set, test_set = cross_validation.train_test_split(df, test_size=0.3, random_state=0)

mod = sm.formula.ols("SalaryNormalized ~ LocationNormalized", data=df)
res = mod.fit()
print res.summary()

from patsy import dmatrices

y, X = dmatrices('sl ~ sx + yr + rk', data=data, return_type='dataframe')
import pylab as pl

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model = model.fit(X,y)
model.score(X,y)

from sklearn.metrics import mean_squared_error
from sklearn.metrics import make_scorer
from sklearn.cross_validation import KFold

scoring = make_scorer(mean_squared_error, greater_is_better=False)
cv = KFold(X.shape[0], 10)
model = linear_model.RidgeCV(alphas=[0.1, 1.0, 10.0], cv=cv, scoring=scoring)
model.fit(X,y)

train_set.dtype = df.columnsl

from pandas.tools.plotting import scatter_matrix
scatter_matrix(df1, alpha=0.2, figsize=(10, 10), diagonal='kde');

'Id',
'Title',
'FullDescription',
'LocationRaw',
'LocationNormalized',
'ContractType',
'ContractTime',
'Company',
'Category',
'SalaryRaw',
'SalaryNormalized',
'SourceName'

# import numpy as np
# from sklearn.feature_extraction import DictVectorizer as DV
# nphitters=np.loadtxt('Hitters.csv',delimiter=',', skiprows=1)
# vec = DV( sparse = False )
# catL=vec.fit_transform(nphitters[:,3:4])

