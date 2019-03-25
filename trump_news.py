from newsapi import NewsApiClient
import json

# Init
newsapi = NewsApiClient(api_key='1d28a210f7b24d87bd0c299d47b53553')

# /v2/top-headlines
#top_headlines = newsapi.get_top_headlines(q='trump',
#                                           sources='bbc-news,the-verge',
#                                           category='business',
#                                           language='en',
#                                           country='us')
all_sources = ['the-new-york-times', 'breitbart-news', 'fox-news', 'the-american-conservative', 'daily-mail', 'the-huffington-post', 'the-washington-post', 'associated-press']


# for i in range(len(all_sources)):
#     articles = newsapi.get_everything(q='trump', sources=all_sources[i],
#                                             from_param='2019-02-25', to='2019-03-25', language='en', page=index)
#     with open('trump_news.json', 'w') as outfile:
#         json.dump(articles, outfile)
trump_articles = []
for index in range(1, 99):
    articles = newsapi.get_everything(q='Trump',  from_param='2019-02-25', to='2019-03-25', page=index)
    trump_articles.append(articles)

#trump_articles = newsapi.get_everything(q='Trump',  from_param='2019-02-25', to='2019-03-25', page=50)

with open('trump_news.json', 'w') as outfile:
    json.dump(trump_articles, outfile)

# /v2/everything
# all_articles = newsapi.get_everything(q='bitcoin',
#                                       sources='bbc-news,the-verge',
#                                       domains='bbc.co.uk,techcrunch.com',
#                                       from_param='2017-12-01',
#                                       to='2017-12-12',
#                                       language='en',
#                                       sort_by='relevancy',
#                                       page=2)

# /v2/sources
#sources = newsapi.get_sources()


# with open('trump_news.json', 'w') as outfile:
#     json.dump(all_articles, outfile)
#
# print(len(all_articles))


