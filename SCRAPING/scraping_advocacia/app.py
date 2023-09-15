from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

numero_oab = 133864

driver = webdriver.Chrome()
driver.get('https://pje-consulta-publica.tjmg.jus.br/')
sleep(30)
# digitar numero AOB
campo_oab = driver.find_element(
    By.XPATH, '//*[@id="fPP:Decoration:numeroOAB"]')
campo_oab.send_keys(numero_oab)

# selecionar estado
dropdown_estados = driver.find_element(
    By.XPATH, '//*[@id="fPP:Decoration:estadoComboOAB"]')
opcoes_estados = Select(dropdown_estados)
opcoes_estados.select_by_visible_text("SP")

# clicar em pesquisar
botao_pesquisar = driver.find_element(By.XPATH, "fPP:searchProcessos")
botao_pesquisar.click()
sleep(5)
