from twilio.rest import Client
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


servico = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=servico)

driver.get("https://tensurafan.github.io/")

dados = driver.find_elements(By.CLASS_NAME, "button")
dados = dados[3:-4]
volumes = []
for item in dados:
    volumes.append(item.text)

lista_de_volumes = "\n".join(volumes)


account_sid = ""  # Twilio
token = ""  # Twilio

remetente = ""  # Quem envia
destino = ""  # Quem recebe

client = Client(account_sid, token)

message = client.messages.create(
    to=destino,
    from_=remetente,
    body=f"{lista_de_volumes}"
)

print(message.sid)
