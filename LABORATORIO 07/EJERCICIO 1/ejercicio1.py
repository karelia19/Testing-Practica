from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Iniciar navegador Edge
driver = webdriver.Edge()

# Ir a Google
driver.get("https://www.google.com")
driver.save_screenshot("01_google_home.png")

# Aceptar cookies si aparecen
try:
    consent = driver.find_element(By.XPATH, '//button[contains(text(),"Aceptar todo")]')
    consent.click()
    driver.save_screenshot("02_google_consent_accepted.png")
except:
    pass

# Buscar "Selenium IDE"
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium IDE")
search_box.send_keys(Keys.RETURN)
time.sleep(3)
driver.save_screenshot("03_search_results.png")

# Esperar un poco para cargar bien resultados
time.sleep(2)
driver.save_screenshot("04_post_captcha_results.png")

# Cerrar navegador
driver.quit()
