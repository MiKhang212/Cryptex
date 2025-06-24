#! /usr/bin/env python3
from cryptography.fernet import Fernet
import os
import tkinter as tk
from tkinter import filedialog

def choose(cmd):
    if cmd.lower() == 'command':
        print('Command tyoe choosen!')
        return False
    elif cmd.lower() == 'gui':
        print('GUI type choosen!')
        return True
    else:
        print('Default type choosen(GUI)!')
        return True
    

def gui(cmd):
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    root.update()
    root.lift()
    root.focus_force()

    if cmd.lower() == 'folder' or cmd.lower() == 'dir':
        folder = filedialog.askdirectory()
    elif cmd.lower() == 'file':
        folder = filedialog.askopenfilename()

    root.destroy()
    if folder and cmd.lower() == 'file':
        print(f'Selected file: {folder}')

    elif folder and cmd.lower() == 'folder' or folder and cmd.lower() == 'dir':
        print(f'Selected folder/dir: {folder}')

    return folder

def encrypt(path_type):
    files = []

    #path_type = choose()

    type = input('Encrypt folder/dir or file?: ')

    if type.lower() == 'file':
        if path_type == False:
            path1 = input('Put the file or dir path here: ')
        else:
            path1 = gui(type)
        
        try:

            if os.path.isfile(path1) and os.path.getsize(path1) == 0:
                print('The file is empty')
            elif os.path.isfile(path1):
                key = Fernet.generate_key()
                keyname = input("Enter the key's name: ")
                with open(f'yourdir/{keyname}.key', 'wb') as thekey:
                    thekey.write(key)

                with open(path1, 'rb') as thefile:
                    content = thefile.read()
                content_encryted = Fernet(key).encrypt(content)
                with open(path1, 'wb') as thefile:
                    thefile.write(content_encryted)
                print('The file was encrypted!!!')
            else:
                print('Wrong path')
        
        except TypeError:
            print('Wrong path')


    elif type.lower() == 'folder' or type.lower() == 'dir':
        if path_type == False:
            path2 = input('Put the folder/dir path here: ')
        else:
            path2 = gui(type)

        try:

            if os.path.isdir(path2):
                if not os.listdir(path2):
                    print('The folder is empty')
                elif os.listdir(path2):
                    key = Fernet.generate_key()
                    keyname = input("Enter the key's name: ")
                    with open(f'yourdir/{keyname}.key', 'wb') as thekey:
                        thekey.write(key)

                    for file in os.listdir(path2):
                        if file == 'encrypt.py' or file == 'thekey.key' or file == 'decrypt.py':
                            continue
                        
                        file_path = os.path.join(path2, file) 

                        if os.path.isfile(file_path):

                            with open(file_path, 'rb') as thefile:
                                contents = thefile.read()
                            contents_encryted = Fernet(key).encrypt(contents)
                            with open(file_path, 'wb') as thefile:
                                thefile.write(contents_encryted)
                            print('The folder was encrypted!!!')
                else:
                    print('Wrong path')
        except TypeError:
            print('Wrong path')

def decrypt(path_type):
    files = []

    #path_type = choose()

    type = input('Decrypt folder/dir or file?: ')

    if type.lower() == 'file':
        if path_type == False:
            path1 = input('Put the file or dir path here: ')
        else:
            path1 = gui(type)

        try:
            if os.path.isfile(path1) and os.path.getsize == 0:
                print('The file is empty')
            elif os.path.isfile(path1):
                keyname = input("Enter the key's name: ")
                with open(f'yourdir/{keyname}.key', 'rb') as key:
                    secretkey = key.read()
                with open(path1, 'rb') as thefile:
                    content = thefile.read()
                try:
                    content_decryted = Fernet(secretkey).decrypt(content)
                except ValueError:
                    print('Wrong key')
                with open(path1, 'wb') as thefile:
                    thefile.write(content_decryted)
                os.remove(f'yourdir/{keyname}.key')
                print('File decrypted!')
            else:
                print('Wrong path')
        except TypeError:
            print('Wrong path')


    elif type.lower() == 'folder' or type.lower() == 'dir':
        if path_type == False:
            path2 = input('Put the folder/dir path here: ')
        else:
            path2 = gui(type)
        
        try:

            if os.path.isdir(path2):
                if not os.listdir(path2):
                    print('The folder is empty')
                elif os.listdir(path2):
                    keyname = input("Enter the key's name: ")
                    with open(f'yourdir/{keyname}.key', 'rb') as key:
                        secretkey = key.read()

                    for file in os.listdir(path2):
                        if file == 'encrypt.py' or file == 'thekey.key' or file == 'decrypt.py':
                            continue
                        
                        file_path = os.path.join(path2, file) 

                        if os.path.isfile(file_path):

                            with open(file_path, 'rb') as thefile:
                                contents = thefile.read()
                            try:    
                                contents_decryted = Fernet(secretkey).decrypt(contents)
                            except ValueError:
                                print('Wrong key')
                            with open(file_path, 'wb') as thefile:
                                thefile.write(contents_decryted)
                            os.remove(f'yourdir/{keyname}.key')
                            print('Folder decrypted!')
            else:
                print('Wrong path')
        except TypeError:
            print('Wrong path')

    else:
        os.remove('yourdir/thekey.key')
        print("We can't handle your situation please try again")

def main():
    print('Welcome to Crytex!')
    print('Here you can  encrypt and decrypt in any path!!!')
    cmd = input('Choose path by command or gui?: ')
    path_type = choose(cmd)
    

    while True:
        cmd = input('What do you want to do?: ')
        if cmd.lower() == 'encrypt':
            encrypt(path_type)
        elif cmd.lower() == 'decrypt':
            decrypt(path_type)
        elif cmd.lower() == 'exit' or cmd.lower() == 'quit':
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        elif cmd.lower() == 'clear' or cmd.lower() == 'cls':
            os.system('cls' if os.name == 'nt' else 'clear')
        elif cmd.lower() == 'interface':
            cmd = input('Choose path by command or gui?: ')
            path_type = choose(cmd)
        else:
            print('cmd not found!')

if __name__ == '__main__':
    main()
