from selenium import webdriver
import time, pyautogui
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from PySimpleGUI import PySimpleGUI as sg

# Layout
sg.theme('Reddit')
layout = [
    [sg.Text('Contador (Se está iniciando a automação agora, digite 1):'), sg.Input(key='contador', size=(5,1))],
    [sg.Text('Sufixo:'), sg.Input(key='sufixo_contato', size=(25,1))],
    [sg.Text('Mensagem:')],
    [sg.Multiline(key='mensagem', size=(55, 5))],
    [sg.Text('Saída:')],
    [sg.Output(size=(55, 5))],
    [sg.Button('Iniciar')]
]

# Janela
janela = sg.Window('Bot WhatsApp', layout)

# Abrindo o WhatsApp
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')

# Ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Iniciar':
        contador = int(valores['contador'])
        sufixo_contato = valores['sufixo_contato']
        mensagem = valores['mensagem']

        # O contador serve para caso voce pare o programa durante a execucao, voce pode voltar de onde parou

        while True:
            # Encontrando o botao de nova conversa
            nova_conversa = driver.find_element_by_xpath('//span[@data-icon="chat"]')
            nova_conversa.click()
            time.sleep(1)

            # Encontrando o campo de pesquisa do nome do contato
            campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
            campo_pesquisa.click()
            campo_pesquisa.send_keys(sufixo_contato)
            time.sleep(2)
            for varrer_contatos in range(contador):
                pyautogui.press('down')
            time.sleep(1)
            pyautogui.press('enter')

            # Modifique aqui o nome do ultimo contato para definir o ponto de parada do programa
            teste_final = driver.find_elements_by_xpath('//span[@title="Zfinal Teste"]')

            # Se o nome encontrado for igual ao definido no programa, o xpath retorna uma lista com 2 elementos.
            # Se for diferente, retorna uma lista com apenas 1 elemento.
            if len(teste_final) == 2:
                print('Ponto de parada :D')
                break

            # Encontrando o campo para enviar a mensagem
            campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
            campo_mensagem[2].click()
            time.sleep(1)
            campo_mensagem[2].send_keys(mensagem)
            campo_mensagem[2].send_keys(Keys.ENTER)
            print('Contato: ' + str(contador))
            time.sleep(1)
            contador += 1