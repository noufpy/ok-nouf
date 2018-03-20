import spacy

import numpy as np
from numpy import dot
from numpy.linalg import norm

nlp = spacy.load('en_core_web_lg')

document = unicode(open("corpus/Nicoo.txt").read().decode('utf8'))
document = nlp(document)

sentences = list(document.sents)

print sentences




























# class predictors(TransformerMixin):
#     def transform(self, X, **transform_params):
#         return [clean_text(text) for text in X]
#     def fit(self, X, y=None, **fit_params):
#         return self
#     def get_params(self, deep=True):
#         return {}
#
# # Basic utility function to clean the text
# def clean_text(text):
#     return text.strip().lower()
#
# #Create spacy tokenizer that parses a sentence and generates tokens
# #these can also be replaced by word vectors
# def spacy_tokenizer(sentence):
#     tokens = parser(sentence)
#     tokens = [tok.lemma_.lower().strip() if tok.lemma_ != '-PRON-' else tok.lower_ for tok in tokens]
#     tokens = [tok for tok in tokens if (tok not in stopwords and tok not in punctuations)]
#     return tokens
#
#
# vectorizer = CountVectorizer(tokenizer = spacy_tokenizer, ngram_range=(1,1))
# classifier = LinearSVC()
#
# # Create the  pipeline to clean, tokenize, vectorize, and classify
# pipe = Pipeline([('cleaner', predictors()),
#                  ('vectorizer', vectorizer),
#                  ('classifier', classifier)])
#
# # Load sample data
# train = [('I love this sandwich.', 'pos'),
#          ('this is an amazing place!', 'pos'),
#          ('I feel very good about these beers.', 'pos'),
#          ('this is my best work.', 'pos'),
#          ("what an awesome view", 'pos'),
#          ('I do not like this restaurant', 'neg'),
#          ('I am tired of this stuff.', 'neg'),
#          ("I can't deal with this", 'neg'),
#          ('he is my sworn enemy!', 'neg'),
#          ('my boss is horrible.', 'neg')]
# test =   [('the beer was good.', 'pos'),
#          ('I do not enjoy my job', 'neg'),
#          ("I ain't feelin dandy today.", 'neg'),
#          ("I feel amazing!", 'pos'),
#          ('Gary is a good friend of mine.', 'pos'),
#          ("I can't believe I'm doing this.", 'neg')]
#
# # Create model and measure accuracy
# pipe.fit([x[0] for x in train], [x[1] for x in train])
# pred_data = pipe.predict([x[0] for x in test])
# for (sample, pred) in zip(test, pred_data):
#     print sample, pred
# print "Accuracy:", accuracy_score([x[1] for x in test], pred_data)






# for word in list(document.sents)[0]:
#     print word, word.tag_
