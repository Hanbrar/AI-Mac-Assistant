
from newsapi import NewsApiClient

# Initialize the NewsApiClient with your API key
def news():
    newsapi = NewsApiClient(api_key='')

    # Get the top headlines from the specified city
    top_headlines = newsapi.get_top_headlines(country='us')
    # Print the titles of the top headlines
    i = 0
    article1=''
    for article in top_headlines['articles']:
        if i > 9:
            break
        i = i + 1
        article1=article1+article['title']
        
    return article1

