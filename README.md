Email Sender
This Python script allows you to send an email with a customized HTML content using Gmail's SMTP server.

Prerequisites
Python 3 installed on your system
Access to the internet to connect to Gmail's SMTP server
Gmail account credentials
Usage
Clone or download the repository containing this script.
Ensure you have an index.html file in the same directory as the script. This HTML file will be used as the body of the email.
Modify the script to customize sender name, recipient email address, subject, and any other details as needed.
Run the script using the command: python email_sender.py.
If prompted, enter your Gmail account credentials.
Script Details
The script uses the smtplib library to establish a connection to Gmail's SMTP server.
It utilizes the EmailMessage class from the email.message module to create an email message.
The string.Template class from the string module is used to read and substitute placeholders in the HTML content.
Make sure to replace 'hanadtestemail@gmail.com' and 'ghsp nget rhdp kuzr' with your actual Gmail account username and password respectively.
The recipient's email address, sender name, subject, and other details can be customized according to your requirements.
Note
Gmail may require you to allow "Less Secure Apps" in your account settings to use SMTP with less secure login methods. Use caution when enabling this option.
For security reasons, avoid hardcoding sensitive information like passwords directly into scripts. Consider using environment variables or other secure methods of handling credentials.
Make sure to comply with Gmail's policies and guidelines when sending emails, especially in large quantities or for commercial purposes.

For Gmail users this link may be useful if errors with gmail occur that stops the user due to gmails new terms of service https://stackoverflow.com/questions/72480454/sending-email-with-python-google-disables-less-secure-apps. 
