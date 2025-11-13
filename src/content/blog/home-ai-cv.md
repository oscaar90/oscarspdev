---
title: "Tu CV frente a la oferta: IA local para técnicos"
description: "Herramienta para evaluar tu CV contra ofertas usando IA local con Mistral y Ollama. Sin tokens, sin nube, sin filtros de humo."
publishDate: 2025-07-28
category: "ai"
type: "project"
tags: ["cv", "ats", "ollama", "mistral", "automatización", "empleo"]
readingTime: "7 min"
---

Este es uno de los proyectos que más impacto ha tenido en mi entorno: **CVMatcher Local**.

Hace unos días comenté cómo muchos reclutadores están usando IA de forma superficial o directamente inútil. Hoy le doy la vuelta: esto va de usar IA desde el otro lado, sin dependencias externas, para evaluar tu perfil de forma útil y clara.

He creado una herramienta que analiza tu CV frente a una oferta y devuelve un análisis directo y accionable.

## ¿Qué hace?

- Evalúa si pasarías un filtro ATS básico  
- Calcula un porcentaje de encaje con la oferta  
- Resume puntos fuertes y débiles de tu perfil  
- Y lo más práctico: te da 5 consejos concretos y personalizados para mejorar tu CV  

## ¿Cómo lo hace?

Usa IA local con **Mistral** y **Ollama**, ejecutándose 100 % en tu equipo.  
No subes nada, no usas tokens, no dependes de APIs. Solo Python, tu máquina y resultados inmediatos.

---

## Un ejemplo real

Usé mi propio CV contra una oferta de Arquitecto Cloud. Resultado:

- 85 % de encaje  
- Puntos fuertes en automatización, scripting y cloud  
- Debilidades detectadas en seguridad de redes y GCP  
- Consejos concretos para mejorar sin tener que reinventar el CV

---

## ¿Y si le paso una oferta que no es de este perfil?

También lo detecta. Si le pasas una oferta de hostelería, por ejemplo, corta el análisis y lo indica con claridad.

---

## Stack usado

- Python 3.10+  
- `pdfplumber` para leer CVs  
- `requests` para obtener textos  
- Ollama + Mistral para el análisis  
- Sin conexión a OpenAI

---

## Roadmap

- Añadir soporte para URLs directamente  
- Exportar el informe a Markdown o PDF  
- Afinar las recomendaciones para diferentes perfiles

---

##  🔗 Repositorio
<div>
  <a href="https://github.com/oscaar90/cvmatcher-local" target="_blank" rel="noopener" class="btn-primary" style="display: inline-flex; align-items: center; gap: 0.5rem; background: linear-gradient(135deg, #3B82F6 0%, #8B5CF6 100%); color: white; border: none; padding: 0.75rem 1.5rem; border-radius: 0.5rem; font-weight: 600; text-decoration: none; transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1); box-shadow: 0 4px 20px rgba(59, 130, 246, 0.3);">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
      <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
    </svg>
    Ver en GitHub
  </a>


---

## ¿Por qué lo hice?

Porque estoy cansado de probar herramientas sin foco.  
Quería algo que me ayudara en serio a decidir si merece la pena aplicar a una oferta.  
Y de paso, que me indicara qué pulir en mi CV sin tener que pagar a nadie.

---

## ¿Te interesa o te puede servir?

Pruébalo, clónalo o mejóralo. Está bajo licencia MIT.  
Y si te mola, ⭐ en GitHub o compártelo con quien le pueda ir bien.
