#!/usr/bin/python3

#Name: Abdullah Tahir
#Date: 13/11/2022

import os
import time
import subprocess

from termcolor import cprint
from tqdm import tqdm

green = "\u001b[32m"
white = "\u001b[37m"
red = "\u001b[31m"
user= os.environ['USER']#Takes the username from the environment variable

def find():
    from subprocess import Popen, PIPE
    file= input("\nPlease enter the file name to create a shortcut: ")#Takes the input from the user of the file they want to create a shortcut for
    fil= Popen(['find', '/', '-type', 'f', '-name', file], stdout=PIPE,stderr=PIPE)#It searches if the file exists and Popen makes a new process that runs the given command
    output = fil.communicate()[0]#It allows to interact with the output and 0 takes the first value
    output = output.decode('utf-8')#It decodes the output
    for i in tqdm(range(10)):
        time.sleep(.2)
    if output != '':#If the output isnt empty
        print(f'{green}\nFound: {white}{output}')#It prints if the file is found
        os.symlink(output.rstrip(), f'/home/{user}/{file}')#It creats the shortcut
        print(f'{green}Successful{white}')
        print(f'{green}\nShortcut created for:{white}')
        os.system(f'readlink /home/{user}/{file}')
    else:
        print(f'{red}\nFile {green}{file} {red}Not Found{white}')#If the file isnt found it prints File not found

def rem():
    file= input("\nPlease enter the shortcut/link to remove: ")
    print(f'\nAre you sure you want to delete {green}{file}{white}? Type {green}Y/y{white} if so.')#It prints if the user is sure they want to delete the shortcut
    choice= input()
    if choice == 'y' or choice == 'Y':#If the user types y or Y it unlinks the shortcut meaning removing it
        for i in tqdm(range(10)):
            time.sleep(.2)
        os.system(f'unlink /home/{user}/{file}')#It removes the shortcut
        print(f'{green}\nShortcut/Link removed{white}')#Prints that the shortcut has been removed
    else:
        main()

def report():
    for i in tqdm(range(10)):
        time.sleep(.2)
    dire= subprocess.check_output('pwd')
    dire= dire.decode('utf-8')
    print (f'\nYour current directory is: {green}{dire}{white}')#It prints the current working directory
    symlink= subprocess.check_output(f'ls -la /home/{user} | grep ^l |' + '''awk '{print $9 "\t" $10 "\t" $11}' ''', shell=True)#It finds the location of all the shortcuts that currently exists
    symlink= symlink.decode('utf-8')
    count= subprocess.check_output(f'ls -la /home/{user} | grep ^l | wc -l', shell=True)#It finds all the shortcuts that exists and we use this to find the total amount of shortcuts that exists
    count= count.decode('utf-8')
    print(f'{green}Symbolic Link            Target Path{white}')
    print(symlink)#It prints all teh shortcut that exists with the location of what file they have been linked with
    print(f'\nNumber of Shortcuts/Links: {green}{count}{white}')#Prints the total amount of shortcuts that are present
    return dire


def main():
    option=0
    while option != 'q' or 'Q' or 'quit':
        time.sleep(5)
        os.system('clear')
        option=input('''     
   _____ _                _             _                         _             
  / ____| |              | |           | |                       | |            
 | (___ | |__   ___  _ __| |_ ___ _   _| |_    ___ _ __ ___  __ _| |_ ___  _ __ 
  \___ \| '_ \ / _ \| '__| __/ __| | | | __|  / __| '__/ _ \/ _` | __/ _ \| '__|
  ____) | | | | (_) | |  | || (__| |_| | |_  | (__| | |  __/ (_| | || (_) | |   
 |_____/|_| |_|\___/|_|   \__\___|\__,_|\__|  \___|_|  \___|\__,_|\__\___/|_|   
                                                                                

Enter Selection:

    1 - Create a shortcut in your home directory.
    2 - Remove a shortcut from your home directory.
    3 - Run shortcut report.

Please enter your option or type quit(q/Q) to quit the program.''')
        if option == '1':
            find()
        elif option == '2':
            rem()
        elif option == '3':
            report()
        elif option == 'q' or option =='Q' or option =='quit':
            cprint ('\nQuiting program: Returning to shell.', 'red', attrs=['blink'])
            time.sleep(5)
            os.system('clear')
            exit()
        else:
            print ('\nInvalid option. Try again')
main()