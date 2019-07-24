import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

"""print ('Enviar email com gmail')

user = input("cuenta de gmail:")
password = getpass.getpass("password: ")"""
user = 'martinezluis201930@gmail.com'
password = '10456795410'
#pasar las cabeceras del email

remitente = 'martinezluis201930@gmail.com'
destinatario = 'labuelvas1@misena.edu.co'
asunto = "Test Prueba"

mensaje = 'correo prueba python'

gmail = smtplib.SMTP('smtp.gmail.com', 587)

gmail.starttls()

gmail.login(user, password)

gmail.set_debuglevel(1)

header = MIMEMultipart()
header['From'] = remitente
header['To'] = destinatario
header['Subject'] = asunto

mensaje = MIMEText(mensaje, 'html')
header.attach(mensaje)

gmail.sendmail(remitente, destinatario, header.as_string())

gmail.quit()