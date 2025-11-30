# =============================================================================
# PROYECTO FINAL: Análisis del retorno de inversión (ROI) por género cinematográfico
# =============================================================================
# Autor: Nahomi Yamile Velazquez Gasca
# Fecha: 01/Diciembre/2025
# Pregunta de investigación: ¿Qué género cinematográfico ofrece el mayor retorno de inversión (ROI) en los últimos 5 años?
# =============================================================================

# -----------------------------------------------------------------------------
# 1. IMPORTACIONES
# -----------------------------------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración de visualización
plt.style.use('default')
sns.set_palette("husl")

# -----------------------------------------------------------------------------
# 2. CARGA DE DATOS
# -----------------------------------------------------------------------------
# TODO: Carga tu dataset aquí
# df = pd.read_csv('ruta/a/tu/archivo.csv')

# EJEMPLO:
# df = pd.read_csv('ventas_2024.csv')

# -----------------------------------------------------------------------------
# 3. EXPLORACIÓN INICIAL
# -----------------------------------------------------------------------------
# TODO: Explora tu dataset

# Ver primeras filas
# print("\n=== PRIMERAS FILAS ===")
# print(df.head())

# Información del dataset
# print("\n=== INFORMACIÓN DEL DATASET ===")
# print(df.info())

# Estadísticas descriptivas
# print("\n=== ESTADÍSTICAS DESCRIPTIVAS ===")
# print(df.describe())

# Valores nulos
# print("\n=== VALORES NULOS ===")
# print(df.isnull().sum())

# -----------------------------------------------------------------------------
# 4. LIMPIEZA DE DATOS
# -----------------------------------------------------------------------------
# TODO: Limpia tu dataset según necesites

# Eliminar duplicados
# df = df.drop_duplicates()

# Manejar valores nulos (elige la estrategia apropiada)
# df = df.dropna()  # Eliminar filas con nulos
# df = df.fillna(valor)  # Rellenar con un valor
# df['columna'] = df['columna'].fillna(df['columna'].mean())  # Rellenar con media

# Convertir tipos de datos
# df['fecha'] = pd.to_datetime(df['fecha'])
# df['categoria'] = df['categoria'].astype('category')

# Crear nuevas columnas si es necesario
# df['nueva_columna'] = df['col1'] + df['col2']

# Filtrar datos si es necesario
# df = df[df['columna'] > valor]

print("\n=== DATOS DESPUÉS DE LIMPIEZA ===")
# print(f"Filas: {len(df)}, Columnas: {len(df.columns)}")

# -----------------------------------------------------------------------------
# 5. ANÁLISIS DESCRIPTIVO
# -----------------------------------------------------------------------------
# TODO: Calcula estadísticas relevantes para tu pregunta

print("\n=== ANÁLISIS DESCRIPTIVO ===")

# Ejemplo 1: Medidas de tendencia central
# media = df['columna_numerica'].mean()
# mediana = df['columna_numerica'].median()
# print(f"Media: {media:.2f}")
# print(f"Mediana: {mediana:.2f}")

# Ejemplo 2: Agrupaciones
# resumen = df.groupby('categoria')['valor'].agg(['sum', 'mean', 'count'])
# print(resumen)

# Ejemplo 3: Frecuencias
# conteos = df['columna_categorica'].value_counts()
# print(conteos)

# Ejemplo 4: Correlaciones (si aplica)
# correlacion = df[['col1', 'col2', 'col3']].corr()
# print(correlacion)

# INTERPRETACIÓN: [Escribe aquí qué significan tus estadísticas]

# -----------------------------------------------------------------------------
# 6. VISUALIZACIONES
# -----------------------------------------------------------------------------
# TODO: Crea al menos 3 visualizaciones diferentes

print("\n=== CREANDO VISUALIZACIONES ===")

# VISUALIZACIÓN 1: [Describe qué muestra]
# plt.figure(figsize=(10, 6))
# # Tu código de visualización aquí
# plt.title('Título Descriptivo')
# plt.xlabel('Etiqueta X')
# plt.ylabel('Etiqueta Y')
# plt.tight_layout()
# plt.savefig('grafico1.png', dpi=300, bbox_inches='tight')
# plt.show()

# VISUALIZACIÓN 2: [Describe qué muestra]
# plt.figure(figsize=(10, 6))
# # Tu código de visualización aquí
# plt.title('Título Descriptivo')
# plt.xlabel('Etiqueta X')
# plt.ylabel('Etiqueta Y')
# plt.tight_layout()
# plt.savefig('grafico2.png', dpi=300, bbox_inches='tight')
# plt.show()

# VISUALIZACIÓN 3: [Describe qué muestra]
# plt.figure(figsize=(10, 6))
# # Tu código de visualización aquí
# plt.title('Título Descriptivo')
# plt.xlabel('Etiqueta X')
# plt.ylabel('Etiqueta Y')
# plt.tight_layout()
# plt.savefig('grafico3.png', dpi=300, bbox_inches='tight')
# plt.show()

# -----------------------------------------------------------------------------
# 7. INTERPRETACIÓN Y CONCLUSIONES
# -----------------------------------------------------------------------------
"""
HALLAZGOS PRINCIPALES:
----------------------
1. [Primer hallazgo basado en tu análisis]
   Evidencia: [Qué estadística o gráfico lo respalda]

2. [Segundo hallazgo]
   Evidencia: [Qué estadística o gráfico lo respalda]

3. [Tercer hallazgo]
   Evidencia: [Qué estadística o gráfico lo respalda]

RESPUESTA A LA PREGUNTA DE INVESTIGACIÓN:
------------------------------------------
[Responde claramente a tu pregunta inicial basándote en tu análisis]

LIMITACIONES:
-------------
- [Limitación 1: ej. tamaño de muestra pequeño]
- [Limitación 2: ej. falta de datos de cierto periodo]
- [Limitación 3: ej. posible sesgo en la recolección]

PRÓXIMOS PASOS:
---------------
- [Qué análisis adicionales podrías hacer]
- [Qué datos adicionales serían útiles]
- [Qué preguntas surgen de este análisis]

CONCLUSIÓN GENERAL:
-------------------
[Resume en 2-3 oraciones el insight principal de tu proyecto]
"""

# =============================================================================
# FIN DEL PROYECTO
# =============================================================================
