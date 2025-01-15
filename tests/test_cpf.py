from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configuração do driver
driver = webdriver.Chrome()
url = "https://www.4devs.com.br/gerador_de_cpf"
driver.get(url)

# Configurar opções
driver.find_element(By.ID, "pontuacao_nao").click()
time.sleep(10)
state_dropdown = driver.find_element(By.ID, "cpf_estado")
state_dropdown.send_keys("AM")
time.sleep(5)

# Gerar CPF até encontrar o desejado
while True:
    driver.find_element(By.ID, "bt_gerar_cpf").click()
    time.sleep(5)
    generated_cpf = driver.find_element(By.ID, "texto_cpf").text
    if generated_cpf.startswith("7"):
        print(f"CPF encontrado: {generated_cpf}")
        break

driver.quit()
