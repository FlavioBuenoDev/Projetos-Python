# Enviando E-mails SMTP com Python

import os
from dotenv import load_dotenv #type:ignore
import pathlib
from string import Template
from email.mime.multipart import  MIMEMultipart
from email.mime.text import MIMEText
import smtplib

load_dotenv()

# Caminho arquivo HTML
CAMINHO_HTML = pathlib.Path(__file__).parent / 'aula303.html'


# Dados do remetente
remetente = os.getenv('FROM_EMAIL', '')
destinatario = remetente

# cConfigura SMTP
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = os.getenv('FROM_EMAIL', '')
smtp_password = os.getenv('EMAIL_PASSW', '')

# Mensagem de texto
with open(CAMINHO_HTML, 'r', encoding='utf8') as arquivo:
    texto_arquivo = arquivo.read()
    template = Template(texto_arquivo)
    texto_email = template.substitute(nome='Flavio')

# Transformar nossa mensagem em MIMEMultipart
mime_multipart = MIMEMultipart()
mime_multipart['from'] = remetente
mime_multipart['to'] = destinatario
mime_multipart['subject'] = 'Este é o assunto do e-mail'

corpo_email = MIMEText(texto_email, 'html', 'utf-8')
mime_multipart.attach(corpo_email)

with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo()
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.send_message(mime_multipart)
    print("Emails enviado com suscesso")