---
title: "La Evolución del Prompting: ¿JSON o Texto Plano? Desmitificando la
  Comunicación con LLMs"
published: 2025-11-25
draft: false
description: Un experimento comparativo sobre la eficacia de los formatos en
  LLMs y las reglas de oro para obtener mejores resultados.
tags:
  - Prompt Engineering
  - LLM
  - Experimentos
---
¿Alguna vez te has sentido como si necesitaras aprender un lenguaje de programación secreto solo para obtener una respuesta decente de una Inteligencia Artificial? En el vertiginoso mundo de los Grandes Modelos de Lenguaje (LLM), existe la creencia persistente de que cuanto más complejo y técnico sea tu "prompt" (la instrucción que le das a la IA), mejor será el resultado. Durante mucho tiempo, se nos ha dicho que estructurar nuestros pedidos como si fueran código es el Santo Grial.

Sin embargo, la tecnología avanza a pasos agigantados y lo que era cierto hace seis meses, hoy podría ser obsoleto. Recientemente, me embarqué en un experimento para desentrañar este misterio que ronda a la comunidad del *prompting*: ¿Es el formato estructurado (JSON) realmente superior al texto natural para obtener resultados de calidad?

Lo que descubrí en mi laboratorio de pruebas no solo me sorprendió, sino que simplifica enormemente la forma en que todos —desde desarrolladores hasta creadores de contenido— deberíamos interactuar con estas herramientas. Spoiler alert: la "magia" no está en los paréntesis ni en las llaves.



### El Experimento: El Duelo de Formatos



Para poner a prueba la teoría, diseñé una serie de pruebas comparativas utilizando los modelos más avanzados del mercado actual. El objetivo era simple: pedir exactamente lo mismo de dos maneras radicalmente distintas y analizar la calidad, precisión y utilidad de la respuesta.

Por un lado, utilicé prompts en formato JSON. El JSON (*JavaScript Object Notation*) es un formato de texto estándar para representar datos estructurados. Se ve muy "técnico" y ordenado. Por otro lado, utilicé prompts en texto plano, hablando con la IA como si fuera un colega humano.

Para que visualices la diferencia, aquí tienes un ejemplo simplificado de lo que comparé:

* El Prompt en JSON:

  > `{"tarea": "resumir", "documento": "[texto del artículo]", "longitud_max": "50 palabras", "tono": "profesional"}`
* El Prompt en Texto Plano:

  > "Por favor, resume el siguiente artículo en un máximo de 50 palabras usando un tono profesional: \[texto del artículo]"

El Hallazgo:
Contra todo pronóstico inicial, los resultados fueron prácticamente indistinguibles.

Esto nos dice algo fascinante sobre la evolución de los LLM: su capacidad de comprensión semántica ha madurado hasta tal punto que son capaces de interpretar nuestra intención con una precisión asombrosa, independientemente de si usamos una estructura de código rígida o una frase natural. La IA ya no necesita que le "hables en robot" para entenderte; necesita que le hables con claridad.



## Las 3 'Reglas de Oro' del Prompting Moderno



Si el formato (JSON vs. Texto) ya no es el factor decisivo, ¿qué es lo que realmente importa? A través de mis pruebas, identifiqué que el éxito no depende de *cómo* empaquetes la información, sino de la calidad de la instrucción misma.

A pesar de la convergencia en los formatos, he aislado tres Reglas de Oro universales. Si aplicas estos tres principios, mejorarás drásticamente tus resultados, sin importar si usas ChatGPT, Claude o Llama.



### 1. Define Explícitamente el "QUÉ"



El error más común es asumir que la IA lee tu mente. Un LLM es una máquina de predicción, y si dejas espacio a la ambigüedad, intentará adivinar (y a menudo fallará).

* La clave: Sé directo sobre el objetivo final. No digas "mira este texto"; di "analiza este texto y extrae los 3 argumentos principales". Cuanto más específico sea el verbo de acción, mejor será la ejecución.



### 2. Especifica Claramente el "CÓMO"



Aquí es donde muchos fallan. Una vez que la IA sabe qué hacer, necesita saber bajo qué parámetros hacerlo. Si no defines el formato, el tono y la estructura, recibirás una respuesta genérica.

* La clave: Dale restricciones.

  * *¿Formato?* "Entrégalo en una tabla de dos columnas" o "En una lista con viñetas".
  * *¿Tono?* "Usa un tono sarcástico pero educativo" o "Sé formal y conciso".
  * *¿Estructura?* "Empieza con una conclusión y luego desglosa los puntos".



### 3. Exige la Totalidad del Contenido ("Todo, y sin atajos")



Los LLM, por diseño, a veces tienden a la "pereza" computacional para ahorrar recursos, dándote resúmenes o fragmentos de código con comentarios como `// ... resto del código aquí`.

* La clave: Instruye explícitamente al modelo para que genere TODO el contenido necesario.

  * *Ejemplo:* "Escribe el código completo, sin omitir ninguna función ni usar marcadores de posición".
  * *Ejemplo:* "Desarrolla la respuesta completa paso a paso, sin dejar cabos sueltos ni resumir secciones críticas".
    Esta simple instrucción obliga al modelo a realizar un esfuerzo computacional mayor para cumplir con la solicitud íntegra.



### Conclusión: Claridad sobre Complejidad



La era de tener que ser un "susurrador de código" para obtener buenos resultados de una IA está llegando a su fin. Mi experimento demuestra que la barrera de entrada técnica se está desmoronando: un prompt en texto plano bien redactado es tan poderoso como una estructura JSON compleja.

Lo que permanece constante, y se vuelve aún más valioso, es nuestra capacidad de comunicación. Las Reglas de Oro (Qué, Cómo y Totalidad) son tu mejor herramienta. No te obsesiones con los paréntesis; obsesiónate con la claridad de tu intención.

La próxima vez que te sientes frente a un prompt, te invito a probar estas reglas. Olvida la sintaxis compleja y concéntrate en ser el mejor jefe posible para tu asistente digital: claro, específico y exigente.

¿Quieres que analice un caso de uso específico en mi próximo experimento? Déjame un comentario o contáctame en redes sociales. ¡La evolución de la IA la escribimos entre todos!
