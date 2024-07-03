import requests
from bs4 import BeautifulSoup
url = 'https://www.cebraspe.org.br/'

resposta = requests.get(url)
conteudo = resposta.content  # Pega todo o conteúdo do site
soup = BeautifulSoup(conteudo, 'html.parser')
# soup.title copia o comando com a tag
# soup.title.get_text()) copia só o texto do title
# soup.body copia todo o corpo do site
print(resposta.status_code)

tables = soup.find_all('table', {'cellpadding':'3'})
# We are targeting the table with cellpadding attribute with the value of 3
# We can select using id, class or HTML tag , for more information check the beautifulsoup doc
table = tables[0] # the result is a list, we are taking out data from it
for td in table.find('tr').find_all('td'):
    print(td.text)