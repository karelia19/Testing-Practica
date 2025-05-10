from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep

#Ir a la pagina de la cato https://ucsm.edu.pe/
#Aceptar las cookies
#EN admision - Convenio Cooperacion Interinstitucional
#hacer click en ver mas
#Corroborar que la informacion del modal tenga acceso al texto
#Admision - Convenio Cooperacion Interinstitucional

driver = webdriver.Chrome()
driver.get("https://ucsm.edu.pe/")

try:
    # Aceptar las cookies usando el ID proporcionado
    boton_cookies = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "euCookieAcceptWP"))
    )
    boton_cookies.click()
    print("Cookies aceptadas.")

    # Hacer clic en "Ver más >" usando el texto del enlace
    ver_mas_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Ver más >')]"))
    )
    ver_mas_link.click()
    print("Se hizo clic en 'Ver más >'.")

    modal_content = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='modal-content']//*[contains(text(), 'Admision - Convenio Cooperacion Interinstitucional')]"))
    ) # Este es un ejemplo, ¡debes cambiarlo!
    assert "Admision - Convenio Cooperacion Interinstitucional" in modal_content.text
    print("Se verificó el contenido del modal.")


except Exception as e:
    print(f"Ocurrió un error: {e}")

finally:
    sleep(5)
    driver.quit()


