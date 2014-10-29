import code # code.interact(local=locals())
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the text data
cats = [ 'alt.atheism',
         'talk.religion.misc',
         'comp.graphics',
         'sci.space']

twenty_train_subset = fetch_20newsgroups(subset='train', categories=cats)
twenty_test_subset = fetch_20newsgroups(subset='test', categories=cats)

# Turn the text documents into vectors of word frequencies
# vectorizer = CountVectorizer(ngram_range=(1,3), stop_words='english')
vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5, stop_words='english')
X_train = vectorizer.fit_transform(twenty_train_subset.data)

from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import cross_val_score
from sklearn.tree import DecisionTreeClassifier

tree_model = DecisionTreeClassifier()

# code.interact(local=locals())
# tree_model.fit(X_train, twenty_train_subset.target)
print cross_val_score(tree_model, X_train.toarray(), twenty_train_subset.target)

rf_model = RandomForestClassifier(n_estimators=10, compute_importances=True)
print cross_val_score(rf_model, X_train.toarray(), twenty_train_subset.target)

#This prints the top 10 most important features
rf_model.fit(X_train.toarray(), twenty_train_subset.target)
print sorted(zip(rf_model.feature_importances_, vectorizer.get_feature_names()), reverse=True)[:10]

'''
from sklearn.pipeline import Pipeline
text_clf = Pipeline([('vect', CountVectorizer()),
('tfidf', TfidfTransformer()),
('clf', MultinomialNB()),
])
'''

