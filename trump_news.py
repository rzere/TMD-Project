from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='1d28a210f7b24d87bd0c299d47b53553')

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q='bitcoin',
#                                           sources='bbc-news,the-verge',
#                                           category='business',
#                                           language='en',
#                                           country='us')
trump_articles = newsapi.get_everything(q='trump', from_param='2019-02-25',
                                        to='2019-03-25')
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
sources = newsapi.get_sources()

print(trump_articles)
