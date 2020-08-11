
#@author: Daniel Villada
# Web Scraping : Automatizacion de login facebook

#██████╗ ██╗  ██╗██████╗ ██╗      ██████╗ ██╗████████╗ █████╗  █████╗
#╚════██╗╚██╗██╔╝██╔══██╗██║     ██╔═══██╗██║╚══██╔══╝██╔══██╗██╔══██╗
# █████╔╝ ╚███╔╝ ██████╔╝██║     ██║   ██║██║   ██║   ╚██████║╚█████╔╝
# ╚═══██╗ ██╔██╗ ██╔═══╝ ██║     ██║   ██║██║   ██║    ╚═══██║██╔══██╗
#██████╔╝██╔╝ ██╗██║     ███████╗╚██████╔╝██║   ██║    █████╔╝╚█████╔╝
#╚═════╝ ╚═╝  ╚═╝╚═╝     ╚══════╝ ╚═════╝ ╚═╝   ╚═╝    ╚════╝  ╚════╝ 

import unittest
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

driver_navegator = webdriver.Chrome("webScraping/chromedriver.exe")
driver_navegator.get("https://www.facebook.com/") #Aqui va la url

email = driver_navegator.find_element_by_id("email") #find_element_by_name or find_element_by_id 
email.send_keys("tikadaj208@mail2paste.com") # email or username
time.sleep(2)
password = driver_navegator.find_element_by_name("pass") #find_element_by_name or find_element_by_id 
password.send_keys("Prueba2020") #password
password.send_keys(Keys.ENTER) #Tecla de Accion
time.sleep(2) # Tiempo de espera
