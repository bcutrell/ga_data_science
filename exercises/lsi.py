import pandas as pd 
import numpy as np

import nltk
from nltk.corpus import stopwords



'''
The way we're going to attack this is to build out the TDM matrix with the documents as rows and terms as columns
and then we'll call the transpose operator to flip it to the representation we need for LSI.

We need the following:
    1.  Dictionary of word --> index to define vectors (index for each term)
    2.  Dictionary of word --> total count to get the global (IDF)
    3.  Dictionary of word --> document count for each document to get the local (TF) weighting
'''

# Implement a function that returns the 3 dictionaries that we need above
def find_frequencies(docs):
		eng_stopwords = stopwords.words('english')
    term_indices = {} ## This is #1 above
    currentIndex = 0 ## This is the counter to make sure we correctly populate the term indices in order
    corpus_bag = {} ## This is #2 above
    doc_bags = [] ## This is the collection for #3 above
    for i, doc in iteritems(docs):
        doc_bag = {} ## This is the dictionary of term frequencies for the doc we're currently examining, doc_bags stores a collection of these
        ## TODO: Tokenize each document with nltk
        # nltk.tokenize
        text = nltk.word_tokenize(doc)
        clean_text = [w for w in text if w.lower() not in eng_stopwords]
        ## TODO: For each token in the current document:
        	for w in clean_text:
        		## Optionally ignore stopword and continue
            ## If the word is new (not in term_indices): 
        		if w not in term_indices:
        			term_indices[w] = currentIndex
        			currentIndex += 1
                ## add it to term_indices and give it the index value currentIndex, increment currentIndex
                ## add it to the corpus_bag with count 1
                ## add it to the current doc_bag with count 1
            ## If the word is not new:
                ## increment the corpus_bag counter
                ## If the word is already in the doc_bag, increment that counter, else set it to 1
        doc_bags.append(doc_bag)
    return term_indices, corpus_bag, doc_bags

