# =============================================================================
# PROYECTO FINAL: Análisis del retorno de inversión (ROI) por género cinematográfico
# =============================================================================
# Autor: Nahomi Yamile Velazquez Gasca
# Fecha: 01/Diciembre/2025
# Pregunta de investigación: ¿Qué género cinematográfico ofrece el mayor retorno de inversión (ROI) en el último año (2024)?
# =============================================================================

# -----------------------------------------------------------------------------
# 1. IMPORTACIONES
# -----------------------------------------------------------------------------
import pandas as pd                    # Carga la librería pandas
import matplotlib.pyplot as plt        # Carga librería para crear gráficos
import seaborn as sns                  # Carga librería de visualización 

# Configuración de visualización
plt.style.use('default')               # Usar estilo de gráfico por defecto
sns.set_palette("husl")                # Establecer paleta de colores

print("=== BIBLIOTECAS IMPORTADAS CORRECTAMENTE ===\n")

# -----------------------------------------------------------------------------
# 2. CARGA DE DATOS
# -----------------------------------------------------------------------------

# Crear DataFrame
df = pd.read_csv('peliculas_ratings.csv')

# -----------------------------------------------------------------------------
# 3. EXPLORACIÓN INICIAL
# -----------------------------------------------------------------------------

print("=" * 70)
print("EXPLORACIÓN INICIAL DE DATOS")
print("=" * 70)

# Ver primeras filas
print("\n=== PRIMERAS 5 FILAS ===")
print(df.head())

# Información del dataset
print("\n=== INFORMACIÓN DEL DATASET ===")
print(df.info())

# Estadísticas descriptivas
print("\n=== ESTADÍSTICAS DESCRIPTIVAS ===")
print(df.describe())

# Verificar valores nulos
print("\n=== VALORES NULOS ===")
print(df.isnull().sum())
print()

# INTERPRETACIÓN:   ------- ¡PENDIENTE!

# -----------------------------------------------------------------------------
# 4. LIMPIEZA DE DATOS
# -----------------------------------------------------------------------------
print("=" * 70)
print("LIMPIEZA Y PREPARACIÓN DE DATOS")
print("=" * 70)

# ------------------------------------------------------------------------
# RESUMEN DE LIMPIEZA
# - Corrección de texto (mal codificado)
# - Eliminación de valores faltantes y negativos
# - Eliminación de duplicados
# - Conversión de tipos de datos
# - Eliminar outliers en el retorno de inversión (ROI)
# - Filtrado para el año 2024
# ------------------------------------------------------------------------

# Corrección de texto
df.columns = (df.columns                      # Renombrar enzabezados de columnas mal codificadas
               .str.replace("Ã±", "ñ")        # Uso de replace()
               .str.replace("Ã©", "é")
               .str.replace("Ã³", "ó")
               .str.replace("Ã-­", "í")
)

columnas_mal_codificadas = ["titulo", "genero", "idioma_original"]      # Columnas completas mal codificadas

for columnas in columnas_mal_codificadas:          # Renombrar columnas completas mal codificadas
    df[columnas] = (df[columnas]                   # Uso de replace()
               .str.replace("Ã±", "ñ")        
               .str.replace("Ã©", "é")
               .str.replace("Ã³", "ó")
               .str.replace("Ã-­", "í")
    )


# Verificar y eliminar valores faltantes
valores_faltantes= df.isnull().sum()
print("\nValores faltantes encontrados: ", valores_faltantes)

if valores_faltantes > 0:
    df = df.dropna()
    print("Filas con valores faltantes eliminadas.")


# Verificar y eliminar valores negativos
df = df[df["duracion_minutos"] > 0]
df = df[df["presupuesto_millones"] > 0]
df = df[df["recaudacion_millones"] > 0]


# Verificar y eliminar duplicados
duplicados = df.duplicated().sum()
print("\nDuplicados encontrados: ", duplicados)

if duplicados > 0:
    df = df.drop_duplicates()
    print("Duplicados eliminados.")


# Correción tipo de datos
print("\n=== TIPOS DE DATOS ===")        # Verificar tipos de datos
print(df.dtypes)

df["genero"] = df["genero"].astype("category")

# No se convierte la variable "año" a datetime (202X-XX-XX) 
# El análisis está enfocado por año (202X), por lo que 
# El formato de número entero (int) es adecuado
df["año"] = df["año"].astype(int)


# Eliminar outliers en el retorno de inversión (ROI)
# Uso para evitar que valores extremos distorsionen estadísticas
Q1 = df["roi_porcentaje"].quantile(0.25)       
Q3 = df["roi_porcentaje"].quantile(0.75)
IQR = Q3 - Q1

Limite_inferior = Q1 - 1.5 * IQR            # Limites para definir outliers
Limite_superior = Q3 + 1.5 * IQR

outliers = df[(df["roi_porcentaje"] < Limite_inferior) | (df["roi_porcentaje"] > Limite_superior)]
print("\nOutliers encontrados: ", len(outliers))

if outliers > 0:
    df = df[(df["roi_porcentaje"] >= Limite_inferior) & (df["roi_porcentaje"] <= Limite_superior)]          # Eliminar outliers
    print("Outliers eliminados.")


# Filtración de datos
# Filtrar año 2024 (De acuerdo a pregunta de investigación)
df = df[df["año"] == 2024]              
print("\nPelículas del año 2024:", len(df))


print("\n=== DATOS DESPUÉS DE LIMPIEZA ===")
print(f"Filas: {len(df)}, Columnas: {len(df.columns)}")

print("\n Datos limpios y listos para análisis")
print()


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
