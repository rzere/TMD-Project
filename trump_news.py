from newsapi import NewsApiClient
import json

# Init
nap = NewsApiClient(api_key='1d28a210f7b24d87bd0c299d47b53553')

# for index in range(1, 50):
#     trump_articles = nap.get_everything(q='Trump',  from_param='2019-02-25', to='2019-03-25', page=index)
#     with open('trump_news.json', 'a') as outfile:
#         json.dump(trump_articles['articles'], outfile)


with open('trump_news.json') as json_file:
    data = json.load(json_file)
    print(data)
