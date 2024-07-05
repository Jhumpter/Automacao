from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configurações do Chrome
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# Inicialização do WebDriver
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico, options=chrome_options)

# Navegar para o WhatsApp Web
navegador.get('https://web.whatsapp.com/')
# Definir a espera explícita
wait = WebDriverWait(navegador, 60)

# Esperar até que o elemento do QR Code esteja presente
elemento = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/header/div/div/div/div/span/div/div[1]/div[1]/div/div/span')))

# Esperar até que o contato esteja visível e clicável
contato = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="pane-side"]/div[2]/div/div/div[1]/div/div/div/div[2]')))
contato.click()

# Esperar até que o campo de mensagem esteja presente
campo_mensagem = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')))
campo_mensagem.send_keys('Funciona')

# Esperar até que o botão de enviar esteja clicável
botao_enviar = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span')))
botao_enviar.click()
