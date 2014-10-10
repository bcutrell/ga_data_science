# Smash script


import code # code.interact(local=locals())
from sklearn.datasets import load_iris
iris = load_iris()

from sklearn import neighbors

X, y = iris.data, iris.target
code.interact(local=locals())

# classify as whichever one it is closest to
knn = neighbors.KNeighborsClassifier(n_neighbors=1)
knn.fit(X, y)

# What kind of iris has 3cm x 5cm sepal and 4cm x 2cm petal?
print iris.target_names[knn.predict([[3, 5, 4, 2]])]

'''
Cross Validation
'''
from sklearn import cross_validation
X_train, X_test, y_train, y_test = cross_validation.train_test_split(iris.data, iris.target, test_size=0.4, random_state=0)

knn = neighbors.KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
predicted = knn.predict(X_test)

from sklearn import metrics
print metrics.classification_report(y_test, predicted)
print metrics.confusion_matrix(y_test, predicted)
print metrics.f1_score(y_test, predicted)

from sklearn.cross_validation import cross_val_score

scores = cross_val_score(knn, iris.data, iris.target, cv=5)


df = pd.read_csv('/Users/bcutrell/Desktop/clinton_data.csv')

def get_xy(x, y):
  r = y + ' ~ ' + " + ".join(x)
  return dmatrices(r, data=df, return_type='dataframe')

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

for L in range(0, len(x)+1):
  for subset in itertools.combinations(x, L):
    new_regr = run_regre(x, y)
    print subset, new_regr

model = linear_model.RidgeCV(alphas=[0.1, 1.0, 10.0], store_cv_values=True)
model.fit(x_test, y_test)
s1 = model.score(X,y)
print model.score(X,y)
model.fit(x_train, y_train)

headers = ['CountyName',
 'PercentvotingforClintonin1992',
 'MedianAge',
 'MeanSavings',
 'PerCapitaIncome',
 'PercentinPoverty',
 'PercentVeterans',
 'PercentFemale',
 'PopulationDensity',
 'PercentinNursingHomes',
 'CrimeIndex']
y_attr = 'PercentvotingforClintonin1992'
x_attrs = ['MedianAge',
'PerCapitaIncome',
'PercentFemale',
'PopulationDensity']
df_1 = pd.DataFrame(df.row.str.split(',',1).tolist(), columns = ['County','CountyName'])
scoring = make_scorer(mean_squared_error, greater_is_better=False)
cv = KFold(X.shape[0], 10)
model = linear_model.RidgeCV(alphas=[0.1, 1.0, 10.0], cv=cv, scoring=scoring)
model.fit(x,y)

print model.coef_
print model.alpha_
print model.score(X,y)

def rename_columns(name, c):
  if not c == 'Name' or c == 'Year':
    return name + '_' + c.lower()
  else:
    return c.lower()
tbrady.rename(columns=lambda x: rename_columns('brady', x), inplace=True)
pmanning.rename(columns=lambda x: rename_columns('manning', x), inplace=True)


fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10,10))
tbrady[x_attrs].pct_change().plot(ax=axes[0]).set_title('Brady')
pmanning[x_attrs].pct_change().plot(ax=axes[1]).set_title('Manning')
