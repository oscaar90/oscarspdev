"""
Funciones de IA internas para procesamiento de proyectos
Utiliza embeddings ficticios y algoritmos simples (sin proveedores externos)
"""

from typing import List, Dict, Any
import re
from collections import Counter


def generar_embedding_simple(texto: str) -> List[float]:
    """
    Generar embedding simple basado en características del texto
    (simulación básica sin ML real)
    """
    if not texto:
        return [0.0] * 10

    # Características básicas del texto
    palabras = texto.lower().split()
    longitud = len(palabras)
    caracteres = len(texto)
    mayusculas = sum(1 for c in texto if c.isupper())
    numeros = sum(1 for c in texto if c.isdigit())

    # Palabras clave técnicas
    palabras_tech = ['api', 'backend', 'frontend', 'database', 'web', 'app', 'mobile']
    tech_count = sum(1 for p in palabras if p in palabras_tech)

    # Palabras de acción
    palabras_accion = ['crear', 'desarrollar', 'implementar', 'diseñar', 'construir']
    accion_count = sum(1 for p in palabras if p in palabras_accion)

    # Crear vector de características (embedding ficticio)
    embedding = [
        min(longitud / 100, 1.0),  # Normalizar longitud
        min(caracteres / 500, 1.0),  # Normalizar caracteres
        min(mayusculas / 50, 1.0),  # Normalizar mayúsculas
        min(numeros / 20, 1.0),  # Normalizar números
        min(tech_count / 5, 1.0),  # Contenido técnico
        min(accion_count / 3, 1.0),  # Palabras de acción
        len(set(palabras)) / max(longitud, 1),  # Diversidad léxica
        texto.count('!') / max(longitud, 1),  # Signos de exclamación
        texto.count('?') / max(longitud, 1),  # Signos de pregunta
        min(len(re.findall(r'[A-Z][a-z]+', texto)) / 10, 1.0)  # CamelCase
    ]

    return embedding


def calcular_similitud(embedding1: List[float], embedding2: List[float]) -> float:
    """Calcular similitud coseno entre dos embeddings"""
    if len(embedding1) != len(embedding2):
        return 0.0

    # Producto punto
    dot_product = sum(a * b for a, b in zip(embedding1, embedding2))

    # Magnitudes
    mag1 = sum(a ** 2 for a in embedding1) ** 0.5
    mag2 = sum(b ** 2 for b in embedding2) ** 0.5

    if mag1 == 0 or mag2 == 0:
        return 0.0

    return dot_product / (mag1 * mag2)


def clustering_ideas(proyectos: List[Dict[str, Any]]) -> List[List[Dict[str, Any]]]:
    """
    Agrupar proyectos similares usando clustering simple
    Retorna lista de clusters (grupos de proyectos relacionados)
    """
    if not proyectos:
        return []

    # Generar embeddings para cada proyecto
    proyectos_con_embeddings = []
    for proyecto in proyectos:
        texto = f"{proyecto.get('titulo', '')} {proyecto.get('descripcion', '')}"
        embedding = generar_embedding_simple(texto)
        proyectos_con_embeddings.append({
            'proyecto': proyecto,
            'embedding': embedding
        })

    # Clustering simple basado en umbral de similitud
    clusters = []
    procesados = set()

    for i, item in enumerate(proyectos_con_embeddings):
        if i in procesados:
            continue

        cluster = [item['proyecto']]
        procesados.add(i)

        # Buscar proyectos similares
        for j, otro_item in enumerate(proyectos_con_embeddings):
            if j in procesados or i == j:
                continue

            similitud = calcular_similitud(item['embedding'], otro_item['embedding'])

            if similitud > 0.7:  # Umbral de similitud
                cluster.append(otro_item['proyecto'])
                procesados.add(j)

        clusters.append(cluster)

    return clusters


def generar_resumen(texto: str, max_palabras: int = 50) -> str:
    """
    Generar resumen simple de un texto
    Extrae las primeras frases hasta alcanzar el límite de palabras
    """
    if not texto:
        return ""

    palabras = texto.split()
    if len(palabras) <= max_palabras:
        return texto

    # Encontrar punto más cercano al límite
    resumen_palabras = palabras[:max_palabras]
    resumen = ' '.join(resumen_palabras)

    # Intentar terminar en una frase completa
    ultimo_punto = resumen.rfind('.')
    if ultimo_punto > len(resumen) * 0.5:  # Si el punto está en la segunda mitad
        resumen = resumen[:ultimo_punto + 1]
    else:
        resumen += '...'

    return resumen


def extraer_palabras_clave(texto: str, top_n: int = 5) -> List[str]:
    """Extraer palabras clave más frecuentes del texto"""
    if not texto:
        return []

    # Palabras a ignorar
    stopwords = {
        'el', 'la', 'los', 'las', 'un', 'una', 'unos', 'unas',
        'de', 'del', 'y', 'o', 'en', 'a', 'por', 'para', 'con',
        'que', 'es', 'se', 'al', 'lo', 'como', 'más', 'pero',
        'sus', 'le', 'ya', 'son', 'este', 'esta', 'estos', 'estas'
    }

    # Limpiar y tokenizar
    palabras = re.findall(r'\b\w+\b', texto.lower())
    palabras_filtradas = [p for p in palabras if p not in stopwords and len(p) > 3]

    # Contar frecuencias
    contador = Counter(palabras_filtradas)

    # Retornar las más frecuentes
    return [palabra for palabra, _ in contador.most_common(top_n)]


def generar_roadmap(titulo: str, descripcion: str = "") -> List[Dict[str, Any]]:
    """
    Generar roadmap básico en formato checklist basado en el proyecto
    Usa heurísticas simples para determinar pasos
    """
    checklist = []

    # Analizar título y descripción para determinar tipo de proyecto
    texto_completo = f"{titulo} {descripcion}".lower()

    # Pasos comunes para cualquier proyecto
    checklist.append({
        "texto": "Definir requisitos y objetivos del proyecto",
        "completado": False
    })

    # Heurísticas basadas en palabras clave
    if any(word in texto_completo for word in ['web', 'website', 'sitio', 'página']):
        checklist.extend([
            {"texto": "Diseñar wireframes y mockups", "completado": False},
            {"texto": "Desarrollar frontend", "completado": False},
            {"texto": "Desarrollar backend", "completado": False},
            {"texto": "Integrar frontend con backend", "completado": False},
        ])

    elif any(word in texto_completo for word in ['api', 'backend', 'servidor']):
        checklist.extend([
            {"texto": "Diseñar arquitectura de la API", "completado": False},
            {"texto": "Implementar endpoints principales", "completado": False},
            {"texto": "Configurar base de datos", "completado": False},
            {"texto": "Implementar autenticación", "completado": False},
        ])

    elif any(word in texto_completo for word in ['app', 'aplicación', 'mobile']):
        checklist.extend([
            {"texto": "Diseñar UI/UX de la aplicación", "completado": False},
            {"texto": "Implementar pantallas principales", "completado": False},
            {"texto": "Configurar navegación", "completado": False},
            {"texto": "Integrar con servicios backend", "completado": False},
        ])

    elif any(word in texto_completo for word in ['análisis', 'investigación', 'estudio']):
        checklist.extend([
            {"texto": "Recolectar datos necesarios", "completado": False},
            {"texto": "Analizar y procesar información", "completado": False},
            {"texto": "Generar visualizaciones", "completado": False},
            {"texto": "Documentar hallazgos", "completado": False},
        ])

    else:
        # Pasos genéricos si no se detecta tipo específico
        checklist.extend([
            {"texto": "Investigar y planificar solución", "completado": False},
            {"texto": "Implementar funcionalidad principal", "completado": False},
            {"texto": "Realizar pruebas", "completado": False},
        ])

    # Pasos finales comunes
    checklist.extend([
        {"texto": "Realizar pruebas completas", "completado": False},
        {"texto": "Documentar el proyecto", "completado": False},
        {"texto": "Desplegar/Entregar proyecto", "completado": False},
    ])

    return checklist
