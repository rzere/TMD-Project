from newsapi import NewsApiClient
import pickle
import pandas as pd
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
                                              page=index)
        final_list.extend(list(all_articles['articles']))
    with open('my_news_list.pkl', 'wb') as f:
        pickle.dump(final_list, f)

# /v2/sources
# sources = newsapi.get_sources()
#
# print(top_headlines)
df = pd.DataFrame(final_list)
print (df.columns)
