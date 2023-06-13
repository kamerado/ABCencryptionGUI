#!/usr/bin/env python3
import PySimpleGUI as sg
import os

alphabet1 = 'abcdefghijklmnopqrstuvwxyz'
alphabet2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet3 = '1234567890-=`~!@#$%^&*()_+[]\\;\',./{}|:"<>?'
my_file = ''
encrypt = ''
de = ''

def is_valid(filepath):
    if os.path.exists(filepath) == True:
        return True
    sg.popup_error('Filepath does not exist')
    return False

def encrypts(a, b, n):
    global encrypt
    encrypted_file = open(n, 'w')
    for i in a:
        if i == ' ':
            encrypt += ' '
        else:
            if i in alphabet1:
                position = alphabet1.find(i)
                new_position = (position + int(b)) % 26
                encrypt += (alphabet1[new_position])
            if i in alphabet2:
                position = alphabet2.find(i)
                new_position = (position + int(b)) % 26
                encrypt += (alphabet2[new_position])
            if i in alphabet3:
                position = alphabet3.find(i)
                new_position = (position + int(b)) % 42
                encrypt += (alphabet3[new_position])
    print('New encrypted file', n, 'has been created\n\n')
    encrypted_file.write(encrypt)
    encrypted_file.close()
    return 0

def decrypt(c, d, n):
    global de
    decrypt_file = open(n, 'w')
    for i in c:
        if i == ' ':
            de += ' '
        else:
            if i in alphabet1:
                position = alphabet1.find(i)
                new_position = (position - int(d)) % 26
                de += (alphabet1[new_position])
            if i in alphabet2:
                position = alphabet2.find(i)
                new_position = (position - int(d)) % 26
                de += (alphabet2[new_position])
            if i in alphabet3:
                position = alphabet3.find(i)
                new_position = (position - int(d)) % 42
                de += (alphabet3[new_position])
    print('New decrypted file', n, 'has been created\n\n')
    decrypt_file.write(de)
    decrypt_file.close()
    return 0

def main_screen():
    layout1 = [
        [sg.Button('Encrypt', key = '-ENCRYPT-', expand_x=True)],
        [sg.Button('Decrypt', key = '-DECRYPT-', expand_x=True)],
        [sg.Button('Exit', key = '-EXIT-', expand_x=True)]
    ]
    return sg.Window('Main Screen', layout1)

def encryption():
    layout2 = [
        [sg.Text('Input File', expand_x=True), sg.Input(key="-IN-"), sg.FileBrowse()],
        [sg.Text('Output File', expand_x=True), sg.Input(key='-OUT-'), sg.FolderBrowse()],
        [sg.Text('Create Key'), sg.InputText(key='-KEY-')],
        [sg.Button('Back', key = '-BACK-'), sg.Button('Encrypt', key = '-START-')]
    ]
    return sg.Window('Encrypt', layout2)

def decryption():
    layout3 = [
        [sg.Text('Input File', expand_x=True), sg.Input(key='-IN-'), sg.FileBrowse()],
        [sg.Text('Output File', expand_x=True), sg.Input(key='-OUT-'), sg.FolderBrowse()],
        [sg.Text('Decrypt Key'), sg.InputText(key='-KEY-')],
        [sg.Button('Back', key='-BACK-'), sg.Button('Decrypt', key='-START-')]
    ]
    return sg.Window('Decrypt', layout3)

window = main_screen()

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == '-ENCRYPT-':
        window.close()
        window = encryption()
        while True:
            event, values = window.read()
            if event == '-BACK-':
                window.close()
                window = main_screen()
                break
            if event == '-START-':
                if is_valid(values['-IN-']):
                    try:
                        a = values['-IN-']
                        n = values['-OUT-']
                        b = values['-KEY-']
                        my_file = open(a, 'r')
                        content = my_file.readlines()
                        content = str(content)
                        content = content[2:-2]
                        encrypts(content, b, n)
                        print('done')
                        window.close()
                        window = main_screen()
                    except Exception as err:
                        sg.popup_error('Invalid entree')
                        window.close()
                        window = main_screen()
            break
    if event == '-DECRYPT-':
        window.close()
        window = decryption()
        while True:
            event, values = window.read()
            if event == '-BACK-':
                window.close()
                window = main_screen()
                break
            if event == '-START-':
                if is_valid(values['-IN-']):
                    try:
                        print(values)
                        c = values['-IN-']
                        n = values['-OUT-']
                        d = values['-KEY-']
                        my_file = open(c, 'r')
                        content = my_file.readlines()
                        content = str(content)
                        content = content[2:-2]
                        decrypt(content, d, n)
                        window.close()
                        window = main_screen()
                    except Exception as err:
                        sg.popup_error('Invalid entree')
                        window.close()
                        window = main_screen()
            break
    if event == '-EXIT-':
        window.close()

window.close()
