import sys
import os
from termcolor import colored

def main_menu():
    logo = colored(r'''

███████  █████  ███    ███  █████  ███████ ██          ██████  ██████  ███    ███ 
██      ██   ██ ████  ████ ██   ██ ██      ██         ██      ██    ██ ████  ████ 
███████ ███████ ██ ████ ██ ███████ █████   ██         ██      ██    ██ ██ ████ ██ 
     ██ ██   ██ ██  ██  ██ ██   ██ ██      ██         ██      ██    ██ ██  ██  ██ 
███████ ██   ██ ██      ██ ██   ██ ███████ ███████ ██  ██████  ██████  ██      ██ 
                                                                               
    ''', 'cyan')
    print(logo.center(80))
    print(colored("Choose an encryption technique:", "yellow").center(80))
    print("1. Caesar Cipher".center(80))
    print("2. Columnar Transposition".center(80))
    print("3. Row Transposition".center(80))
    print("4. Monoalphabetic Substitution".center(80))
    print("6. Rail Fence Transposition".center(80))
    print("6. Vigenere Cipher".center(80))
    print("7. Exit".center(80))
    choice = input(colored("\n Enter your choice (1/2/3/4/5/6/7): ", "green"))
    return choice


def run_script(script_name):
    os.system(f"python3 {script_name}.py")

if __name__ == "__main__":
    while True:
        choice = main_menu()
        
        if choice == '1':
            run_script("ceaser")
        elif choice == '2':
            run_script("c-transposition")
        elif choice == '3':
            run_script("r-transposition")    
        elif choice == '4':
            run_script("monoalphabetic")
        elif choice == '5':
            run_script("railfence")
        elif choice == '6':
            run_script("vigenere")
        elif choice == '7':
            print(colored("Goodbye!", "red"))
            break
        else:
            print(colored("Invalid choice. Please select a valid option (1-7).", 'red'))
