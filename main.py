import requests

api_key = "47b58d96d390496ba812ede756203653"

url = "https://newsapi.org/v2/everything?q=tesla"\
      "&from=2024-10-15&sortBy=publishedAt&apiKey="\
        "47b58d96d390496ba812ede756203653"

request = requests.get(url)
content = request.text

print(content)
