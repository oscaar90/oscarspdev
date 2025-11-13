---
title: "Idea Tracker: tu cabeza está llena, no tu escritorio"
description: "Sistema local para gestionar ideas sin perder el norte. Estado, resumen y foco. Nada de ruido, solo ejecución."
publishDate: 2025-07-18
category: "tools"
type: "project"
tags: ["flask", "python", "productividad", "sqlite", "local", "opensource"]
readingTime: "6 min"
---

## ¿Por qué nació esto?

Tenía mil ideas apuntadas en mil sitios. Notas en el móvil, en Obsidian, en correos enviados a mí mismo. Resultado: caos.  
Empecé a olvidarme de lo importante, a duplicar cosas o a pasar semanas sin saber en qué estaba trabajando.

**Idea Tracker** nace para eso. No para organizar el universo, sino para tener un panel claro con 3 cosas:  
- Qué ideas tengo  
- En qué estado están  
- Qué me falta para cerrarlas

Ni más, ni menos.

## Qué hace exactamente

- Cada idea se define con un título, un estado (`pendiente`, `en progreso`, `cerrado`) y un resumen corto.  
- Puedes escribir un README por cada una, por si quieres documentar a fondo.  
- Tiene una **interfaz oscura**, sencilla y accesible desde cualquier navegador en tu red local.  
- Sin cuentas, sin nube, sin historias.

No te va a salvar la vida, pero te quita el bloqueo de no saber por dónde seguir.

## Cómo lo hice

El stack es el de batalla:

- `Python`  
- `Flask`  
- `SQLite`  
- `Bootstrap` para el estilo

Todo en un único script, sin dependencias raras ni magia detrás.  
Lo levantas con `python app.py` y ya estás dentro.


## ¿Por qué local?

Porque no necesito otra web con login, tokens, suscripciones ni publicidad para escribir "aprender pytest".

Esto vive en mi equipo. Si mañana lo borro, no he vendido nada a nadie.  
Y si quiero que otro lo use, le paso el `.zip`, lo abre y a correr.

## ¿Qué vendrá después?

Estoy trabajando en la **versión 2** con:

- Instalador interactivo (Windows/Linux)
- Servicio en segundo plano que se levante solo al arrancar
- Acceso desde el móvil en LAN
- Rediseño más pulido

Todo seguirá siendo **local y sin nube**. Como debe ser.

---
🔗 Repositorio
<div>
  <a href="https://github.com/oscaar90/idea-tracker" target="_blank" rel="noopener" class="btn-primary" style="display: inline-flex; align-items: center; gap: 0.5rem; background: linear-gradient(135deg, #3B82F6 0%, #8B5CF6 100%); color: white; border: none; padding: 0.75rem 1.5rem; border-radius: 0.5rem; font-weight: 600; text-decoration: none; transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1); box-shadow: 0 4px 20px rgba(59, 130, 246, 0.3);">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
      <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
    </svg>
    Ver en GitHub
  </a>

¿Tú también tienes ideas sueltas por todos lados?  
Pues ya sabes. Clónalo, arráncalo y empieza a cerrar cosas de una vez.
</div>

