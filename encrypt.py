#! /usr/bin/env python3

import os

from cryptography.fernet import Fernet

files = []

key = Fernet.generate_key()

with open('yourdir/thekey.key', 'wb') as thekey:
    thekey.write(key)

type = input('Encrypt folder/dir or file?: ')

if type.lower() == 'file':
    path1 = input('Put the file or dir path here: ')
    if os.path.isfile(path1):
        with open(path1, 'rb') as thefile:
            content = thefile.read()
        content_encryted = Fernet(key).encrypt(content)
        with open(path1, 'wb') as thefile:
            thefile.write(content_encryted)
    else:
        print('Wrong path')
        os.remove('yourdir/thekey.key')


elif type.lower() == 'folder' or type.lower() == 'dir':
    path2 = input('Put the folder/dir path here: ')
    if os.path.isdir(path2):
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
    else:
        print('Wrong path')
        os.remove('yourdir/thekey.key')

else:
    os.remove('yourdir/thekey.key')
    print("We can't handle your situation please try again")
    quit()
