from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from random import choice
from time import sleep
tamanhos = ['//*[@id="i9"]/div[3]/div', '//*[@id="i12"]/div[3]/div', '//*[@id="i15"]/div[3]/div',
            '//*[@id="i18"]/div[3]/div', '//*[@id="i21"]/div[3]/div']
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico, options=chrome_options)
navegador.get(
    'https://docs.google.com/forms/d/e/1FAIpQLSfmSWAVs8KgZ2M-CnJb_duGe2zv7iea_nhqNj-RYPOhsHellA/viewform?usp=sf_link')
for c in range(0, 5):
    nome = navegador.find_element(By.XPATH,
                                  '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    nome.send_keys('João')
    tamanho = navegador.find_element(By.XPATH, choice(tamanhos))
    tamanho.click()
    navegador.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span').click()
    sleep(2)
    navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()
