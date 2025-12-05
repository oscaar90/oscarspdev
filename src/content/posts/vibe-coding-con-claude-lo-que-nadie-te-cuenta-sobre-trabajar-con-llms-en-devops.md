---
title: "Vibe Coding con Claude: Lo que nadie te cuenta sobre trabajar con LLMs
  en DevOps"
published: 2025-12-05
draft: false
tags:
  - devops
  - claude-ai
  - python
  - vibe-coding
  - platform-engineering ci-cd
  - llm
---
Llevo varios meses trabajando intensivamente con Claude en el desarrollo de TENVY y en mi trabajo como Platform Engineer. No voy a venderte humo sobre "el futuro del desarrollo" ni a decirte que la IA no te va a quitar el trabajo. La verdad es que no lo sé. Lo que sí sé es que las cosas están cambiando, rápido, y me he encontrado aprendiendo tecnologías y conceptos que jamás pensé que tocaría.

## ¿Qué coño es "vibe coding"?

Olvídate de la definición marketiniana. En la práctica vibe coding es esto: describes lo que quieres hacer, el LLM te genera código, tú lo revisas, lo entiendes, lo ajustas, y lo iteras. No es magia. No es copiapega. Es un ciclo de colaboración donde TÚ sigues siendo el que entiende el sistema, la arquitectura, y los trade-offs.

Ejemplo de mi día a día:
```bash
# Antes (enfoque tradicional):
# 1. Googlear "kubernetes cronjob with secrets"
# 2. Leer 3 artículos de StackOverflow
# 3. Adaptar el código a mi caso
# 4. Debuggear durante 40 minutos porque olvidé un indentado en el YAML
# Tiempo total: ~2 horas

# Ahora (con Claude):
# 1. "Claude, necesito un CronJob de K8s que ejecute este script cada 6 horas,
#     monte estos secrets, y tenga retry policy con backoff exponencial"
# 2. Revisar el YAML generado
# 3. Ajustar según mis políticas de cluster
# Tiempo total: ~20 minutos
```

**La diferencia no es que Claude haga tu trabajo. Es que elimina la fricción entre pensar y ejecutar.**

## Lo que he aprendido (y nadie me dijo)

### 1. No todas las herramientas LLM son iguales

He probado Cursor, GitHub Copilot, y Claude CLI directamente. Para debugging complejo y problemas de arquitectura, Claude CLI me ha dado resultados significativamente mejores. ¿Por qué? Contexto. Cuando le das el contexto completo de tu problema (logs, configuraciones, código relacionado), la calidad de las respuestas es otro nivel.

**Copilot**: Genial para autocompletar funciones simples.  
**Cursor**: Bueno para refactors y edición inline.  
**Claude CLI**: Superior para arquitectura, debugging complejo, y cuando necesitas entender el "por qué".

### 2. La calidad del prompt = calidad del código

Esto suena obvio, pero no lo es. Aprendí por las malas que "haz una API en Flask" te da código de tutorial. En cambio:
```
"Necesito una API REST en Flask que:
- Maneje autenticación OAuth con Google
- Procese PDFs en memoria (sin guardarlos en disco por GDPR)
- Use SQLAlchemy con PostgreSQL
- Tenga rate limiting por IP
- Devuelva errores en formato JSON con códigos HTTP apropiados
- Incluya logging estructurado"
```

Te da código production-ready (o casi).

### 3. El debugging ha cambiado radicalmente

Antes: Leer stacktraces, googlear el error, probar soluciones random hasta que algo funciona.

Ahora: Le paso el stacktrace completo a Claude con contexto del código. En el 80% de los casos, identifica el problema exacto y me da la solución. Pero aquí está el truco: **tengo que entender la solución para verificar que tiene sentido en mi arquitectura.**

No es copiar código ciegamente. Es tener un pair programmer experto disponible 24/7.

### 4. La curva de aprendizaje se ha invertido

Tradicionalmente: Aprendes la teoría → Practicas → Construyes.

Con LLMs: Construyes → Entiendes qué está pasando → Profundizas en la teoría cuando necesitas optimizar.

He implementado patrones de diseño que antes me habría costado semanas entender, y luego los he estudiado a fondo porque ya los tenía funcionando en producción. Es... diferente. No sé si mejor o peor, pero definitivamente más rápido para iterar.

## Casos de uso en DevOps

### Infraestructura como Código
```python
# Ejemplo: Migrar configuración manual de Nginx a código
# Le pasé mi nginx.conf actual y pedí:
# "Convierte esto a configuración de Ansible, hazlo idempotente,
#  y añade validación de sintaxis antes de aplicar cambios"

# Resultado: Playbook completo con validación, rollback, y testing
# Tiempo ahorrado: ~4 horas
```

### CI/CD Pipelines

He montado mi primer sistema CI/CD con GitHub Actions literalmente aprendiendo sobre la marcha con Claude. Antes me daba pereza meterme en YAML de pipelines porque la curva de aprendizaje era empinada. Con Claude:

1. "Necesito un pipeline que haga testing, build de Docker, y deploy a mi VPS"
2. Me genera el `.github/workflows/deploy.yml`
3. Ajusto según mi infra específica
4. Funciona al segundo intento (el primero fallé yo, no Claude)

### Gestión de Secrets y Seguridad

Hace poco metí la pata y comiteé secrets a un repo público. Claude me ayudó a:
- Revocar los secrets comprometidos
- Implementar git-secrets para prevenir futuros incidentes
- Configurar pre-commit hooks
- Documentar el proceso para el equipo

Todo en una sesión de 2 horas. Antes, esto habría sido un día completo de investigación + implementación.

## Lo que NO ha cambiado (y no va a cambiar)

- **Tienes que entender lo que hace el código.** Si no, estás generando deuda técnica.
- **Tienes que conocer tu arquitectura.** Claude no sabe cómo está montado tu K8s cluster.
- **Tienes que tomar decisiones.** Claude te da opciones, tú decides cuál encaja mejor.
- **Tienes que debuggear cuando falla.** Y va a fallar, porque las herramientas no son perfectas.

## El cambio

No es que ahora "cualquiera pueda programar". Es que los que ya sabemos programar podemos:
- Iterar 5-10x más rápido
- Explorar tecnologías nuevas sin meses de curva de aprendizaje
- Enfocarnos en arquitectura y decisiones, no en sintaxis
- Mantener múltiples proyectos que antes serían imposibles

En mi caso: mantengo TENVY (una plataforma completa con Flask, PostgreSQL, Docker, CI/CD) mientras trabajo full-time en ALDI España y estudio un máster en IA. Antes, uno de esos tres habría sido insostenible.

## Conclusión: Adaptarse o quedarse atrás

No sé si la IA va a quitar trabajos. Lo que sí sé es que los desarrolladores/DevOps que sepan trabajar con LLMs van a ser mucho más productivos que los que no. Y en un mercado competitivo, esa diferencia importa.

Mi consejo: 
1. **Experimenta.** Prueba Claude, ChatGPT, Cursor, lo que sea.
2. **Documenta tu aprendizaje.** Yo he aprendido una burrada y me arrepiento de no haber documentado más desde el principio.
3. **Mantén el pensamiento crítico.** El código generado por IA no es perfecto. Revísalo, entiéndelo, mejóralo.
4. **No tengas miedo a parecer "junior".** He preguntado cosas básicas a Claude que me daba vergüenza googlear. Resultado: he aprendido más en 6 meses que en años de copiar código de StackOverflow.

El cambio está aquí. Nos guste o no. Yo he decidido adaptarme. ¿Y tú?

---

*Este post está basado en mi experiencia desarrollando TENVY y trabajando como Platform Engineer. Si tienes preguntas o quieres discutir sobre el tema, escríbeme en LinkedIn.*
```
