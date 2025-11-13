---
title: "PassForge: tu propio generador de contraseñas seguro y local"
description: "Crea contraseñas fuertes desde tu equipo, sin depender de webs externas. Interfaz clara, modo oscuro y 100 % control desde tu máquina."
publishDate: 2025-07-29
category: "tools"
type: "project"
tags: ["python", "flask", "seguridad", "contraseñas", "offline", "open-source"]
readingTime: "7 min"
---

## ⚙️ ¿Qué es PassForge?

PassForge es una herramienta local para generar contraseñas seguras desde la web o la terminal.  
Está pensada para quienes quieren dejar de depender de webs externas para una tarea tan crítica como esta, sin complicaciones ni postureo.

---

## 🚀 Características principales

✅ Generación 100 % local (sin conexión a Internet)  
✅ Modo web y CLI (en preparación)  
✅ Personalización completa:
- Longitud  
- Mayúsculas / minúsculas  
- Números y símbolos  

✅ Error si no marcas opciones (para no generar nada al azar)  
✅ Copiado al portapapeles sin alertas intrusivas  
✅ Interfaz limpia, modo oscuro, sin dependencias externas  
✅ Código abierto y extensible (MIT)

---

## 🧠 ¿Por qué lo hice?

Cada día necesitaba generar una contraseña para algo puntual: Wi-Fi, cuentas temporales, correos…  
Siempre acababa entrando en webs que no controlo, con scripts que no veo, y llenas de publicidad o rastreos.

Así que monté **PassForge**:

- Rápido  
- A medida  
- Control total sobre lo que hace  
- Compartible y útil para otros

---

## 🖼️ Interfaz



<script>
function toggleImageSize(img) {
  if (img.style.maxWidth === '400px' || !img.style.maxWidth) {
    // Ampliar imagen
    img.style.maxWidth = '100%';
    img.style.transform = 'scale(1.05)';
    img.style.boxShadow = '0 8px 25px rgba(59, 130, 246, 0.4)';
  } else {
    // Volver al tamaño original
    img.style.maxWidth = '400px';
    img.style.transform = 'scale(1)';
    img.style.boxShadow = '0 4px 12px rgba(0,0,0,0.3)';
  }
}
</script>

### Características de la interfaz:

- ❌ Muestra error si no seleccionas opciones
<div class="interface-preview">
  <img 
    src="https://github.com/oscaar90/PassForge/blob/main/docs/error_no_charset.png?raw=true?auto=compress&cs=tinysrgb&w=600" 
    alt="Interfaz de PassForge mostrando generación de contraseñas" 
    class="preview-image" 
    onclick="toggleImageSize(this)"
    style="cursor: pointer; max-width: 400px; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.3); transition: all 0.3s ease;"
  />
  <p style="font-size: 0.9em; color: #94A3B8; text-align: center; margin-top: 8px;">
    📸 Haz clic en la imagen para ampliar
  </p>
</div>

- ✅ Al copiar, hay feedback sin notificaciones pesadas

<div class="interface-preview">
  <img 
    src="https://github.com/oscaar90/PassForge/blob/main/docs/copied_feedback.png?raw=true?raw=true?auto=compress&cs=tinysrgb&w=600" 
    alt="Interfaz de PassForge mostrando generación de contraseñas" 
    class="preview-image" 
    onclick="toggleImageSize(this)"
    style="cursor: pointer; max-width: 400px; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.3); transition: all 0.3s ease;"
  />
  <p style="font-size: 0.9em; color: #94A3B8; text-align: center; margin-top: 8px;">
    📸 Haz clic en la imagen para ampliar
  </p>
</div>

---

## 🧱 Stack

| Componente     | Descripción                                  |
|----------------|----------------------------------------------|
| 🐍 Python      | Backend + generación segura                  |
| 🌐 Flask       | Servidor web local                           |
| 🎨 HTML/CSS    | Interfaz modo oscuro, responsive             |
| 🧠 JS vanilla  | Interacción web, copiado al portapapeles     |
| 🔐 `secrets`   | Generación criptográficamente fuerte         |
| 📋 pyperclip   | Copiado en CLI (en la futura versión)        |

---

## 🗂️ Estructura del proyecto

```bash
PassForge
├── app/
│   ├── __init__.py
│   ├── routes.py
│   └── generator.py
├── static/
│   ├── css/style.css
│   └── js/main.js
├── templates/
│   └── index.html
├── run.py
├── requirements.txt
└── README.md
```
---

##  🔗 Repositorio
<div>
  <a href="https://github.com/oscaar90/PassForge" target="_blank" rel="noopener" class="btn-primary" style="display: inline-flex; align-items: center; gap: 0.5rem; background: linear-gradient(135deg, #3B82F6 0%, #8B5CF6 100%); color: white; border: none; padding: 0.75rem 1.5rem; border-radius: 0.5rem; font-weight: 600; text-decoration: none; transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1); box-shadow: 0 4px 20px rgba(59, 130, 246, 0.3);">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
      <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
    </svg>
    Ver en GitHub
  </a>
  




## 📌 **Próximos pasos**
- CLI completa con pyperclip` y `argparse`
- Modo diceware para contraseñas fáciles de recordar
- App instalable (modo launcher de escritorio)
- Paquete `.deb` para distros Linux

💬 ¿Lo quieres usar o extender? Está bajo licencia MIT. Haz lo que quieras con él.  
Y si te mola la idea, ⭐ dale una estrella en GitHub o compártelo con quien le venga bien.
</div>
---