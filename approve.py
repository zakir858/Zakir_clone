zakiir_cloneCorrectUsername = 'XXX'
key = 'XNXX'
while key == 'XNXX':
    username = input('\033[0;97m[•]\033[1;96m•➤ \033[1;92mENTER PASSWORD \033[1;91m: \x1b[1;92m')
    if username == CorrectUsername:
            print('\033[1;30m───────────────────────────────────────────\n\033[0;97m[X]\033[1;32m LOGIN SUCCESSFULLY') 
            time.sleep(1)           
            key = 'false'
import os,time
os.system('clear')