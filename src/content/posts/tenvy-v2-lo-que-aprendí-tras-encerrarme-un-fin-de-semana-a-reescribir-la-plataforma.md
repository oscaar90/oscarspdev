---
title: "TENVY v2: Lo que aprendí tras encerrarme un fin de semana a reescribir
  la plataforma"
published: 2025-12-02
draft: false
tags:
  - Empleabilidad
  - Búsqueda de Empleo
  - ATS
  - Tenvy
  - Optimización de CV
  - Build in Public
  - Desarrollo
  - IA
---
Martes, 02 de Diciembre. Acabo de publicar en LinkedIn el lanzamiento de la nueva versión de Tenvy. Pero LinkedIn es para el titular; aquí quiero contar la historia completa.

Hace tres meses lancé [este proyecto ( tenvy )](https://tenvy.es) con un eslogan que, para mí, es una ley: "Buscar trabajo NO debería costar dinero".

La acogida de la versión 1 (v1) fue numéricamente buena para un proyecto que acaba de nacer:

* 264 usuarios registrados.
* 570 currículums analizados.

Pero los números son vanidad si la experiencia de usuario falla. Y falló.

## El valor de la imperfección (y de escuchar)

Como emprendedor, a veces te obsesionas con el *roadmap*, con las *features* futuras o con el diseño perfecto. Pero la realidad te golpea cuando abres el correo. Recibí mensajes de 15 usuarios. No eran mensajes de felicitación, eran reportes de errores:

> *"Oye, el login no va".*
> *"El análisis se queda colgado a la mitad".*
> *"Los caracteres del ATS salen raros y no se entiende nada".*

En ese momento tienes dos opciones:

1. Poner excusas ("es que es una beta", "es que tu navegador...").
2. Aceptar que el usuario manda.

Elegí la segunda. Como he leído recientemente en la historia de otros emprendedores, lanzar algo imperfecto no es malo, siempre y cuando estés dispuesto a escuchar el *feedback* y pivotar rápido .

## Crónica de un fin de semana de código

Decidí que la "v1.5" no era suficiente. Necesitaba una v2.

Me encerré este fin de semana. Café, música y Visual Studio Code. He tocado prácticamente todo el *core* de la plataforma. No solo he puesto parches; he reescrito la lógica que estaba fallando.

### ¿Qué trae la v2 bajo el capó?

1. Estabilidad total en el Login: He simplificado el proceso de autenticación. Entrar en Tenvy ahora es inmediato.
2. Análisis de CV robusto: Ya no se "cuelga". He optimizado la forma en que procesamos el archivo para que, incluso si tu PDF es pesado o tiene un formato extraño, el sistema responda.
3. El problema de la "Sobrecualificación": Este es el cambio más importante.
   Analizando los datos de esos 570 CVs, detecté un patrón alarmante. Mucha gente no es rechazada por falta de experiencia, sino por exceso. Los sistemas ATS (y los reclutadores humanos) a veces descartan perfiles "caros" o "demasiado senior" antes de siquiera hablar con ellos.

   La v2 de Tenvy ahora detecta explícitamente si tu perfil corre riesgo de ser descartado por estar sobrecualificado para la oferta y te sugiere cómo adaptarlo. Ya no basta con tener experiencia; hay que mostrar la experiencia *exacta* que pide la oferta.

## La marca soy yo, la comunidad sois vosotros

Tenvy no es una multinacional. Detrás de cada línea de código y de cada respuesta de soporte estoy yo, Óscar.

No tengo inversores presionando para monetizar tus datos. No tengo un equipo de marketing maquillando la realidad. Mi objetivo es simple: usar mis conocimientos en tecnología y ciberseguridad para nivelar el campo de juego en la búsqueda de empleo.

No puedo hacer la entrevista por ti, ni puedo arreglar un mercado laboral que a veces parece roto. Pero puedo darte las herramientas para que tu CV pase el primer filtro.

## ¿Qué sigue?

Seguir escuchando. Esos 15 usuarios que se quejaron han aportado más valor a Tenvy que cualquier plan de negocio teórico que yo pudiera haber escrito en una servilleta.

La v2 ya está online. Es más rápida, más visual y, sobre todo, más honesta.

Si estás buscando trabajo, te invito a probarla. Y si encuentras un fallo, por favor, escríbeme. Me volveré a encerrar otro fin de semana si hace falta.

Porque buscar trabajo no debería costar dinero.
