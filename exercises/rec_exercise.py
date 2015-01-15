import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import manhattan_distances
from sklearn.metrics.pairwise import euclidean_distances

'curl -O https://s3.amazonaws.com/demo-datasets/beer_reviews.tar.gz'

df = pd.read_csv('/Users/bcutrell/beer_reviews.tar.gz', compression='gzip', low_memory=False)
df.head()

	df_test = df[df['beer_name'].isin(['Pale Ale'])]
	top_250_beer_names = pd.value_counts(df['beer_name'].values.ravel())[0:250].keys().tolist()
	top_250_df = df[df['beer_name'].isin(top_250_beer_names)]
	pt = pd.pivot_table(top_250_df, values='review_overall', index=['beer_name'], columns=['review_profilename'], aggfunc=np.mean)
	pt = pt.fillna(0)

pt_matrix = pt.as_matrix()

cs_pt = cosine_similarity(pt)
df_from_pt = pd.DataFrame(cs_pt, columns=columns)

df_from_pt = pd.DataFrame(cs_pt, columns=columns, index=columns)

df_from_pt[['Tröegs Mad Elf', '90 Minute IPA']].diff()

Test your function. Find the 10 beers most similar to "120 Minute IPA"

d = df_from_pt["120 Minute IPA"].sort()



pd.DataFrame(df_from_pt["120 Minute IPA"]).sort('120 Minute IPA', ascending=False)
def sim_to(beers, sort_by):
	return pd.DataFrame(df_from_pt[beers]).sort(sort_by, ascending=False)

sim_to(["Coors Light", "Bud Light", "Amstel Light"])
# Cool, let's try again with the 10 beers most similar to ["Coors Light", "Bud Light", "Amstel Light"]





columns = pt.index.tolist()



# [x for x in b if x not in a]
# pt = pd.pivot_table(top_250_df, values='review_overall', index=['beer_name', 'review_profilename'], aggfunc=np.mean)
# pt = pd.pivot_table(df, values='review_overall', index=['beer_name', 'review_profilename'], columns=['beer_name'], aggfunc=np.mean)
# pt = pd.pivot_table(df, values='beer_name', index=['review_profilename'], columns=['review_overall'], aggfunc=np.mean)
# pt = pd.pivot_table(df, index=['beer_name', 'review_profilename'], columns=['review_overall'], aggfunc=np.mean)
# df_test.sort('review_profilename')
# pd.value_counts(df['beer_name'].values.ravel())
'''Aggregate the data in a pivot table using the pivot_table method. 
Display the mean review_overall for each beer_name aggregating 
the review_overall values by review_profilename. 
Use the mean (numpy) as aggregator.'''