from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
# O webdriver manager identifica e utiliza a  versão atual do navegador
# Essas 3 linhas são linhas padrões
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
servico = Service(ChromeDriverManager().install())
# Instala o chrome driver correspondente a versão atual
navegador = webdriver.Chrome(service=servico, options=chrome_options)
# navegador.get(link) para acessar o link
navegador.get('https://pages.hashtagtreinamentos.com/inscricao-minicurso-python-automacao-org?origemurl=hashtag_yt_org_minipython_videoselenium')
# navegador.find_element('ID'/'Tag'/'xpath', ID/Tag/xpath)
# Todos os elementos possuem um xpath
# Métodos .click() e .send_keys
navegador.find_element('xpath',
                       '//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/div[1]/div/div[1]/div/input').send_keys('Lira')
navegador.find_element('xpath',
                       '//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/div[1]/div/div[2]/div/input').send_keys('pythonimpressionador@gmail.com')
navegador.find_element('xpath',
                       '//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/button').click()
