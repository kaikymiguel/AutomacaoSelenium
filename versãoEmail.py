from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import win32com.client as win32
from time import sleep
from data import email


def coletando_volumes():
    """
    Coleta informações de volumes a partir de um site específico.

    Essa função utiliza o Selenium para abrir uma página web(SlimeReader), esperar 10 segundos
    para garantir que a página seja carregada, extrair elementos com uma classe
    específica ("button"), coletar informações de texto desses elementos(volumes) e,
    finalmente, fecha o navegador Chrome.

    Returns:
    volumes (list): Uma lista contendo todos os volumes lançado até o momento.
    """
    chrome_options = Options()
    # Faz o nevagador ficar oculto ao rodar o código
    chrome_options.add_argument('--headless')
    servico = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=servico, options=chrome_options)

    driver.get("https://tensurafan.github.io/")
    sleep(10)
    dados = driver.find_elements(By.CLASS_NAME, "button")
    dados = dados[3:-4]
    volumes = []
    for item in dados:
        volumes.append(item.text)
    driver.quit()
    return volumes


def enviando_volumes():
    """
    Envia informações de volumes por e-mail utilizando o Microsoft Outlook.

    Esta função utiliza a biblioteca win32com para interagir com o Microsoft Outlook.
    Ela coleta a lista de volumes (global) e cria um e-mail no Outlook contendo essas informações.

    Returns:
    None
    """
    global volumes
    outlook = win32.Dispatch('outlook.application')
    lista_de_volumes = "\n".join(volumes)
    mail = outlook.CreateItem(0)
    mail.To = email  # Email Fictício
    mail.Subject = 'Verificar lançamentos'
    mail.Body = f'{lista_de_volumes}'

    mail.Send()
    print("Email enviado")


volumes = coletando_volumes()
enviando_volumes()
