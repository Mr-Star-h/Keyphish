#-*-coding: utf-8 -*-
escribir= open('usuario.txt', 'w')
print('''Debe poner el nombre entre comillas ejemplo:
"Anonimo" \n''')
y=input('Ingrese el nombre de la víctima: ')
r=('''var insertotexto=""+ 
"{} <br>";
document.write(insertotexto);'''.format(y))
escribir.write(r)