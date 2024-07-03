import requests
from bs4 import BeautifulSoup
url = 'https://www.youtube.com/'
response = requests.get(url)
status = response.status_code
print(status)  #200 significa que a busca deu certo
