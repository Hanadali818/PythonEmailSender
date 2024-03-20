import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Hanad Ali'
email['to'] = 'RecipientEmail@gmail.com'
email['subject'] = 'You won 1,000,000 dollars'

email.set_content(html.substitute({'name': 'tintin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('Sender@gmail.com', 'SenderPassword')
    smtp.send_message(email)
    print('Sent message')
