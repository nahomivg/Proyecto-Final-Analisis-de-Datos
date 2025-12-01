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

import warnings                        # Silenciar advertencias en consola
warnings.simplefilter(action='ignore', category=FutureWarning)

print("\n=== BIBLIOTECAS IMPORTADAS CORRECTAMENTE ===\n")

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
print(df.describe(), "\n")


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
# - Eliminación de valores faltantes
# - Eliminación de valores negativos o inválidos
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
valores_faltantes= df.isnull().sum()                            # Conteo de valores faltantes
valores_faltantes = valores_faltantes[valores_faltantes > 0]    # Filtrar columnas con valores faltantes
print("\nValores faltantes encontrados:")

for columna, valores in valores_faltantes.items():            
    print(f"{columna}: {valores}")

if len(valores_faltantes) > 0:                           # Eliminar valores faltantes
    df = df.dropna()
    print("Filas con valores faltantes eliminadas.")
else:
    print("No se encontraron valores faltantes.")  


# Verificar y eliminar valores negativos o inválidos
columnas_numericas = df.select_dtypes(include=["int", "float"]).columns     # Seleccionar columnas numéricas

valores_invalidos = {}                                  
for columna in columnas_numericas:              
    total_invalidos = (df[columna] <= 0).sum()          # Conteo de valores negativos o inválidos(0)
    if total_invalidos > 0:
        valores_invalidos[columna] = total_invalidos

print("\nValores inválidos encontrados:")
for columna, count in valores_invalidos.items():
    print(f"{columna}: {count}")

if len(valores_invalidos) > 0:                              # Eliminar filas con algún valor inválido
    df = df[(df[columnas_numericas] > 0).all(axis=1)]
    print("Filas con valores inválidos eliminadas.")
else:
    print("No se encontraron valores inválidos.")


# Verificar y eliminar duplicados
duplicados = df.duplicated().sum()
print("\nDuplicados encontrados: ", duplicados)

if duplicados > 0:
    df = df.drop_duplicates()
    print("Duplicados eliminados.")
else:
    print("No se encontraron duplicados.")  


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

if len(outliers) > 0:
    df = df[(df["roi_porcentaje"] >= Limite_inferior) & (df["roi_porcentaje"] <= Limite_superior)]          # Eliminar outliers
    print("Outliers eliminados.")


# Filtración de datos
# Filtrar año 2024 (De acuerdo a pregunta de investigación)
df = df[df["año"] == 2024]              
print("\nPelículas del año 2024:", len(df))

print("\n=== DATOS DESPUÉS DE LIMPIEZA ===")
print(f"Filas: {len(df)}, Columnas: {len(df.columns)}")

print("\n¡Datos limpios y listos para análisis!")
print()


# -----------------------------------------------------------------------------
# 5. ANÁLISIS DESCRIPTIVO
# -----------------------------------------------------------------------------
print("\n========= ANÁLISIS DESCRIPTIVO =========")
print("\n--- ANALISIS DE PELÍCULAS DEL AÑO 2024 --- ")

# ----- Conteo de películas por género -----
conteos_genero = df["genero"].value_counts()
print("\nNúmero de películas por género:")
for genero, cantidad in conteos_genero.items():
    print(f"- {genero}: {cantidad}")


# ----- Media de calificación de critica -----
media_calif_critica = df.groupby("genero")["calificacion_critica"].mean().sort_values(ascending=False)
print("\nMedia de calificación de critica por género:")        # Ordenados de mayor a menor
for genero, cantidad in media_calif_critica.items():
    print(f"- {genero}: {round(cantidad, 2)}")                   # Uso de round() para redondear


# ----- Media de calificación de audiencia -----
media_calif_audiencia = df.groupby("genero")["calificacion_audiencia"].mean().sort_values(ascending=False)
print("\nMedia de calificación de audiencia por género:")      # Ordenados de mayor a menor
for genero, cantidad in media_calif_audiencia.items():
    print(f"- {genero}: {round(cantidad, 2)}")                   # Uso de round() para redondear


# ----- Promedio de ROI por género -----
roi_por_genero = df.groupby("genero")["roi_porcentaje"].mean().sort_values(ascending=False)
print("\nROI promedio por género:")                            # Ordenados de mayor a menor
for genero, cantidad in roi_por_genero.items():
    print(f"- {genero}: {round(cantidad, 2)}")                   # Uso de round() para redondear


# ----- Ganancia promedio por género -----
ganancia_por_genero = df.groupby("genero")["ganancia_millones"].mean().sort_values(ascending=False)
print("\nGanancia promedio por género:")                       # Ordenados de mayor a menor
for genero, cantidad in ganancia_por_genero.items():
    print(f"- {genero}: {round(cantidad, 2)}")                   # Uso de round() para redondear


# ----- Correlación -----
correlacion = df[["presupuesto_millones", "recaudacion_millones", "roi_porcentaje"]].corr().round(2)
print("\nCorrelación:")
print(correlacion)


# INTERPRETACIÓN: [Escribe aquí qué significan tus estadísticas]


# -----------------------------------------------------------------------------
# 6. VISUALIZACIONES
# -----------------------------------------------------------------------------
print("\n=== CREANDO VISUALIZACIONES ===")

# ----- Histograma: Total de películas por año -----
print("VISUALIZACIÓN 1: Total de películas por año")
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x="año", bins=20, kde=True)
plt.title("Número de películas por año")
plt.xlabel("Año")
plt.ylabel("Cantidad de películas")
plt.tight_layout() 
plt.savefig("grafico1_peliculas_año.png")
plt.close()
print("Grafico guardado\n")


# ----- Gráfico de barras: Películas por género -----
print("VISUALIZACIÓN 2: Total de películas por año")
sns.barplot(x=conteos_genero.index, y=conteos_genero.values)
plt.title("Cantidad de películas por género en 2024")
plt.xlabel("Género")
plt.ylabel("Cantidad de películas")
plt.tight_layout() 
plt.savefig("grafico2_peliculas_genero.png")
plt.close()
print("Grafico guardado\n")


# ----- Gráfico de barras: ROI promedio por género -----
print("VISUALIZACIÓN 3: ROI promedio por género")
plt.figure(figsize=(8,5))
sns.barplot(x=roi_por_genero.index, y=roi_por_genero.values)
plt.title("ROI promedio por género (2024)")
plt.xlabel("Género")
plt.ylabel("ROI(%)")
plt.tight_layout() 
plt.savefig("grafico3_roi_genero.png")
plt.close()
print("Grafico guardado\n")


# ----- Heatmap de correlación: Correlación entre presupuesto, recaudación y ROI -----
print("VISUALIZACIÓN 4: Correlación entre presupuesto, recaudación y ROI")
plt.figure(figsize=(8, 5))
correlacion = df[["presupuesto_millones", "recaudacion_millones", "roi_porcentaje"]].corr()
sns.heatmap(correlacion, annot=True, cmap="coolwarm", center=0)
plt.title("Correlación entre presupuesto, recaudación y ROI (2024)")
plt.tight_layout() 
plt.savefig("grafico4_correlacion.png")
plt.close()
print("Grafico guardado\n")


# ----- Boxplot: ROI -----
print("VISUALIZACIÓN 5: Botplot de ROI")
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="genero", y="roi_porcentaje")
plt.title("Distribución de ROI por género (2024)")
plt.xlabel("Género")
plt.ylabel("ROI(%)")
plt.tight_layout() 
plt.savefig("grafico5_boxplot_roi.png")
plt.close()
print("Grafico guardado\n")

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
