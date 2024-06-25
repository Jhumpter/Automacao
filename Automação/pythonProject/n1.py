from selenium import webdriver
# Faz a automação em si
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
# O webdriver manager identifica e utiliza a  versão atual do navegador
# Essas 3 linhas são linhas padrões
servico = Service(ChromeDriverManager().install())
# Instala o chrome driver correspondente a versão atual
navegador = webdriver.Chrome(service=servico)
