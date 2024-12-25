import smtplib

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'rustambekovaa15@gmail.com'
EMAIL_HOST_PASSWORD = 'qvrtgmgojvabceal'

try:
    server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
    server.starttls() 
    server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
    print("SMTP подключение успешно!")
    server.quit()
except Exception as e:
    print("Ошибка SMTP:", e)
