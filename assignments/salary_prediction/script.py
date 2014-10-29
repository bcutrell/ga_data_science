import code # code.interact(local=locals())
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import ExtraTreesRegressor
from scipy import sparse
from scipy.sparse import hstack, coo_matrix
from sklearn.preprocessing import LabelEncoder
from sklearn import cross_validation
from sklearn.ensemble import RandomForestClassifier
import pickle

model_path = '/Users/bcutrell/Desktop/comp/model.pickle'
benchmark_model = pickle.load(open(model_path))
df = pd.read_csv('/Users/bcutrell/python/ga_data_science/assignments/salary_prediction/train50k.csv')

# Features
text_features = ['Title', 'FullDescription','LocationRaw']
categorical_features = ["Category", "ContractType"]

# Remove NaNs
clean_df = df[text_features + categorical_features + ['SalaryNormalized']].dropna()

# Text Vectorizer
vectorizer = TfidfVectorizer(max_features=240000, norm='l2', smooth_idf=True, sublinear_tf=False, use_idf=True)
X_text = np.array([vectorizer.fit_transform(clean_df[f]) for f in text_features])

# Categorical Vectorizer
le = LabelEncoder()
X_cat = np.array([le.fit_transform(clean_df[c].as_matrix()) for c in categorical_features])

# Merge together
X_text = hstack((X_text))
X_train = hstack((X_text, X_cat.T))

# Declare ExtraTreeRegressor
classifier = ExtraTreesRegressor(n_estimators=10,
                                verbose=2,
                                n_jobs=2,
                                oob_score=False,
                                min_samples_split=2,
                                random_state=3465343)


full_r = cross_validation.cross_val_score(classifier, X_train.toarray(), np.log(clean_df['SalaryNormalized'].values), cv=3, verbose=1)
print np.mean(full_r)

