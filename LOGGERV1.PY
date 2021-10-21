import random
import time
import glob
import sys
import os.path
import subprocess
import os

print( "=============================================================================================================================")
print("""\

      :::        ::::::::   ::::::::   ::::::::  :::::::::: :::::::::       :::     :::   :::
     :+:       :+:    :+: :+:    :+: :+:    :+: :+:        :+:    :+:      :+:     :+: :+:+:
    +:+       +:+    +:+ +:+        +:+        +:+        +:+    +:+      +:+     +:+   +:+
   +#+       +#+    +:+ :#:        :#:        +#++:++#   +#++:++#:       +#+     +:+   +#+
  +#+       +#+    +#+ +#+   +#+# +#+   +#+# +#+        +#+    +#+       +#+   +#+    +#+
 #+#       #+#    #+# #+#    #+# #+#    #+# #+#        #+#    #+#        #+#+#+#     #+#
########## ########   ########   ########  ########## ###    ###          ###     #######

            """)
print("=============================================================================================================================")
print(" ")

# bk = ??? Need to find a way to go back to previous screen
qt = 'quit'
#am =  Admin Terminal
section_dashline = "============================================================================================================================="
log_out = "\n░ (1) Back to Menu  \n░ (2) Exit"


def logger_prev():
    print("\n", section_dashline)
    print("░ Previous Logs\n")
    os.chdir = ("C:\\Users\\Armand\\Documents\\Python")
    for file in glob.glob("*.txt"):
        print(file)
        print(log_out)
        print("\n (3) Read previous Logs")
        log_menu2 = input("░ :")

        if log_menu2 == '1':
            print(logger_menu)
        if log_menu2 == '2':
            time.sleep(2)
            quit()
        if log_menu2 == '3':
            read_logs = input("░ Previous Logs\n ░ Enter Log:")
            read_file = open(read_logs, "w")

            read_file.close() 


def logger_make():
    print("\n", section_dashline)
    print("\n░ Making Logs\n")
    log_maketextsave = input("░ Text:")
    log_makefilename = input("░ Filename:") + ".txt"
    print(log_out)
    myFile = open(log_makefilename, 'a')
    myFile.write('Time: ' + time.ctime())
    myFile.write('Text: ' + log_maketextsave + '\n')
    myFile.close()


def logger_option():
    print("\n", section_dashline)
    print("\n░ Options")
    print("\n░ (1) Current .txt file directory \n░ (2) Admin Commands \n░ (3) Back to Menu  \n░ (4) Exit")
    log_optionmenu = input("░ :")
    if log_optionmenu == '1':
        save_path = os.chdir
        print("\n", section_dashline)
        print("\n Current file directory:", save_path )
        print(log_out)
        log_optionmenu2 = input("░ :")
        if log_optionmenu2 == '1':
             print(logger_menu)
        if log_optionmenu2 == '2':
             time.sleep(2)
             quit()
    if log_optionmenu == '2':
                print("bk: Allows the users to go back to the previous screen as they were before.")
                print("qt: Quits the entire program now matter where in the program")
                print("he: Places the user back to the Logger menu")
                print("am: Opens admin terminal")
                print(log_out)
                log_optionmenu3 = input("░ :")
                if log_optionmenu3 == '1':
                    print(logger_menu)
                if log_optionmenu3 == '2':
                    time.sleep(2)
                    quit()
    if log_optionmenu == '3':
            print(logger_menu)
    if log_optionmenu == '4':
            time.sleep(2)
            quit()

def logger_menu():
    log_menu=True
    while log_menu:
        print("\n░ Logger Menu Version 1")
        print("\n░ (1) All previous logs \n░ (2) Make a log \n░ (3) Option  \n░ (4) Exit")
        log_menu = input("░ :")
        if log_menu == '1':
            print(logger_prev())
        elif log_menu == '2':
            print(logger_make())
        elif log_menu == '3':
            print(logger_option())
        elif log_menu == '4':
            time.sleep(2)
            quit()
        else:
            print("Unknown Option Selected!")
logger_menu()
