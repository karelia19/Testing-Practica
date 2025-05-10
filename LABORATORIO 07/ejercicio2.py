from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Configurar el navegador
driver = webdriver.Chrome()
driver.maximize_window()

try:
    # 1. Abrir Google
    driver.get("https://www.google.com")
    time.sleep(2)
    driver.save_screenshot("01_google_home.png")

    # 2. Buscar "Selenium IDE"
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Selenium IDE")
    search_box.send_keys(Keys.ENTER)
    time.sleep(3)
    driver.save_screenshot("02_resultados_busqueda.png")

    # 3. Verificar que el primer resultado contenga el sitio oficial
    primer_resultado = driver.find_element(By.XPATH, "(//h3)[1]")
    texto_resultado = primer_resultado.text

    # Validación interna (lanza excepción si no es correcto)
    assert "Selenium IDE" in texto_resultado or "selenium.dev" in texto_resultado.lower()

    # 4. Hacer clic en el primer resultado
    primer_resultado.find_element(By.XPATH, "./ancestor::a").click()
    time.sleep(3)
    driver.save_screenshot("03_pagina_oficial.png")

finally:
    driver.quit()

