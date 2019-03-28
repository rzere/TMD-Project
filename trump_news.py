from newsapi import NewsApiClient
import pickle
import pandas as pd
import numpy as np
import re
import nltk
from gensim.models import Word2Vec
import itertools
# Init
newsapi = NewsApiClient(api_key='9f1e0b11257f4b14b0e18428c40a3e97')

# /v2/top-headlines
# for index in range(1, 11):
#     print (index)
#     top_headlines = newsapi.get_top_headlines(q='Trump', sources='google-news', page_size=100, page=index)
#     print(top_headlines)

# /v2/everything
try:
    with open('my_news_list.pkl', 'rb') as f:
        final_list=pickle.load(f)
except:
    final_list = list()
    for index in range(1, 11):
        all_articles = newsapi.get_everything(q='Trump',
                                              from_param='2019-02-29',
                                              language='en',
                                              sort_by='relevancy',
                                              page_size=100,
                                              page=index)
        final_list.extend(list(all_articles['articles']))
    with open('my_news_list.pkl', 'wb') as f:
        pickle.dump(final_list, f)

# /v2/sources
# sources = newsapi.get_sources()
#
# print(top_headlines)
df = pd.DataFrame(final_list)
df = df.replace(to_replace='None', value=np.nan).dropna()
df.sort_values(by=['publishedAt'])
final_list = list()

# Cleaning the text
raw_content = list(df['description'])
for content in raw_content:
    processed_article = content.lower()
    processed_article = re.sub('[^a-zA-Z]', ' ', processed_article)
    processed_article = re.sub(r'\s+', ' ', processed_article)
    all_sentences = nltk.sent_tokenize(processed_article)
    all_words = [nltk.word_tokenize(sent) for sent in all_sentences]
    from nltk.corpus import stopwords
    for i in range(len(all_words)):
        all_words[i] = [w for w in all_words[i] if w not in stopwords.words('english')]
    final_list.extend(all_words)

# word_list = list(itertools.chain.from_iterable(final_list))
word2vec = Word2Vec(final_list, min_count=1)
vocabulary = word2vec.wv.vocab
sim_words = word2vec.wv.most_similar('mueller')
print(sim_words)