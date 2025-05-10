from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys

#Herrramienta que permite hacer testing
driver = webdriver.Chrome()

#indicamos en que URL vamos a empezar
driver.get("http://youtube.com")


#buscamos un elemento
cuadro_busqueda = driver.find_element(By.NAME, "search_query")

#Ingresamos un elemento a buscar
cuadro_busqueda.send_keys("Bad Bunny")
driver.save_screenshot("Prueba_de_busqueda.jpg")

#Presionamos enter
cuadro_busqueda.send_keys(Keys.ENTER)
sleep(3)
driver.save_screenshot("Prueba_de_resultado.jpg")

sleep(10)
