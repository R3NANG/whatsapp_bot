from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import pyautogui

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(30)
#contador = input('Digite de qual contato deseja começar: ')

nome_contato = 'Teste'
mensagem = 'Oi, to testando'

#Encontrando o botao de nova conversa
nova_conversa = driver.find_element_by_xpath('//span[@data-icon="chat"]')
nova_conversa.click()
time.sleep(2)

#Encontrando o campo de pesquisa do nome do contato
campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
campo_pesquisa.click()
campo_pesquisa.send_keys(nome_contato)
time.sleep(2)
pyautogui.press('down', presses=3)
time.sleep(1)
pyautogui.press('enter')

#Encontrando o campo para enviar a mensagem
campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
campo_mensagem[2].click()
time.sleep(1)
campo_mensagem[2].send_keys(mensagem)
campo_mensagem[2].send_keys(Keys.ENTER)
#print('Contato: ' + contador)