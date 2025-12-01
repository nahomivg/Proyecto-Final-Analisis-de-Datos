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
# Exploración del dataset para entender la estructura y tipo de datos. 
# Esto ayuda a planear la limpieza y verificar si hay errores.

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


# INTERPRETACIÓN: 
# El dataset contiene 200 películas con información general, financiera y calificaciones. 
# Algunas columnas tienen valores faltantes (presupuesto_millones y votos).
# Se presentan valores faltantes y valores negativos.
# Es necesaria una limpieza antes del análisis. 
# Las películas presentan una duración, presupuestos y recaudaciones muy variables.
# Se presentan calificaciones de crítica y audiencia relativamente consistentes. 
# En general, los datos son adecuados para analizar tendencias por retorno de inversión (ROI)
# Es conveniente considerar outliers y sesgo de filas eliminadas al interpretar resultados


# -----------------------------------------------------------------------------
# 4. LIMPIEZA DE DATOS
# -----------------------------------------------------------------------------
print("=" * 70)
print("LIMPIEZA Y PREPARACIÓN DE DATOS")
print("=" * 70)

# ------------------------------------------------------------------------
# RESUMEN DE LIMPIEZA
# Tiene el objetivo de asegurar un análisis confiable de los datos
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
print("\n========== ANÁLISIS DESCRIPTIVO ==========")
print("\n--- ANALISIS DE PELÍCULAS DEL AÑO 2024 --- ")

# ----- Conteo de películas por género -----
# Con el objetivo de conocer la representatividad del número de películas por género
conteos_genero = df["genero"].value_counts()
print("\nNúmero de películas por género:")
for genero, cantidad in conteos_genero.items():
    print(f"- {genero}: {cantidad}")


# ----- Media de calificación de critica -----
# Con el objetivo de comparar la percepción de críticos y espectadores
media_calif_critica = df.groupby("genero")["calificacion_critica"].mean().sort_values(ascending=False)
print("\nMedia de calificación de critica por género:")        # Ordenados de mayor a menor
for genero, cantidad in media_calif_critica.items():
    print(f"- {genero}: {round(cantidad, 2)}")                   # Uso de round() para redondear


# ----- Media de calificación de audiencia -----
# Con el objetivo de comparar la percepción de críticos y espectadores
media_calif_audiencia = df.groupby("genero")["calificacion_audiencia"].mean().sort_values(ascending=False)
print("\nMedia de calificación de audiencia por género:")      # Ordenados de mayor a menor
for genero, cantidad in media_calif_audiencia.items():
    print(f"- {genero}: {round(cantidad, 2)}")                   # Uso de round() para redondear


# ----- Promedio de ROI por género -----
# Con el objetivo de identificar los géneros más rentables basados en el ROI(%)
roi_por_genero = df.groupby("genero")["roi_porcentaje"].mean().sort_values(ascending=False)
print("\nROI promedio por género:")                            # Ordenados de mayor a menor
for genero, cantidad in roi_por_genero.items():
    print(f"- {genero}: {round(cantidad, 2)}")                   # Uso de round() para redondear


# ----- Ganancia promedio por género -----
# Con el objetivo de identificar los géneros más rentables en valores netos
ganancia_por_genero = df.groupby("genero")["ganancia_millones"].mean().sort_values(ascending=False)
print("\nGanancia promedio por género:")                       # Ordenados de mayor a menor
for genero, cantidad in ganancia_por_genero.items():
    print(f"- {genero}: {round(cantidad, 2)}")                   # Uso de round() para redondear


# ----- Correlación -----
# Para descubrir relaciones clave entre las variables de interés
correlacion = df[["presupuesto_millones", "recaudacion_millones", "roi_porcentaje"]].corr().round(2)
print("\nCorrelación:")
print(correlacion)
("\n")


# INTERPRETACIÓN:
# De acuerdo al análisis de datos, en el año 2024 se hallaron los siguientes resultados:

# --- Número de películas por género ---
# Los géneros más producidos fueron Animación y Ciencia Ficción (6 cintas en cada categoría)
# El género menos producido fue Acción (1 cinta)
# Esto indica que en 2024 hubo una tendencia hacia géneros con un tono más familiar/científico

# --- Media de calificación de crítica ---
# Acción y Drama tienen las mejores críticas (7.5 y 7.1)
# Terror y Animación tienen las criticas más bajas (4.65 y 6.43)
# Se sugiere que los críticos valoran más géneros de narrativa seria o más estructurada, 
# teniendo menos preferencia con géneros relacionados únicamente al entretenimiento

# --- Media de calificación de audiencia ---
# Acción y Comedia destacan con las calificaciones más altas (9.2 y 9.1)
# Drama y Terror se valoran por debajo (5.95 y 6.9)
# La audiencia valora más el entretenimiento ligero y emocionante

# --- ROI promedio por género ---
# Ciencia Ficción, Drama y Animación lideran el ROI
# Terror y Comedia tienen los valores más bajos
# Esto indica que ciertos géneros generan mayor retorno económico relativo a su presupuesto

# --- Ganancia promedio por género ---
# Acción y Ciencia Ficción tienen las mayores ganancias totales (623.3 y 492.48 millones)
# Romance y Comedia tienen las ganancias más bajas
# Los géneros más populares o con mayor producción tienden a generar mayores ingresos absolutos

# --- Correlación --- 
# Hay una correlación negativa fuerte entre presupuesto y ROI (-0.77),
# por lo que películas con presupuestos más altos no necesariamente tienen mejor retorno porcentual.
# La correlación entre recaudación y ROI es positiva pero débil (0.22),
# por lo que más ingresos no garantizan un ROI alto.
# Presupuesto y recaudación no se correlacionan (0.04),
# por lo que gastar más no asegura más ganancias.


# -----------------------------------------------------------------------------
# 6. VISUALIZACIONES
# -----------------------------------------------------------------------------
print("\n=== CREANDO VISUALIZACIONES ===")

# ----- Gráfico de barras: Películas por género -----
# Para identificar la frecuencia de los géneros en producción
print("VISUALIZACIÓN 1: Total de películas por año")
sns.barplot(x=conteos_genero.index, y=conteos_genero.values)   # Gráfico con Seaborn
plt.title("Cantidad de películas por género en 2024")          # Titulo
plt.xlabel("Género")                                           # Eje X
plt.ylabel("Cantidad de películas")                            # Eje Y
plt.xticks(rotation=45)                                        # Rotar etiquetas
plt.tight_layout()                                             # Ajustar automáticamente elementos del gráfico
plt.savefig("grafico1_peliculas_genero.png")                   # Guardar imagen
plt.close()                                                    # Cerrar figura actual
print("Grafico guardado\n")


# ----- Gráfico de barras: ROI promedio por género -----
# Para identificar qué géneros generan mayor ROI relativo a su presupuesto
print("VISUALIZACIÓN 2: ROI promedio por género")
plt.figure(figsize=(8,5))
sns.barplot(x=roi_por_genero.index, y=roi_por_genero.values)
plt.title("ROI promedio por género (2024)")
plt.xlabel("Género")
plt.ylabel("ROI(%)")
plt.xticks(rotation=45) 
plt.tight_layout() 
plt.savefig("grafico2_roi_genero.png")
plt.close()
print("Grafico guardado\n")


# ----- Heatmap de correlación: Correlación entre presupuesto, recaudación y ROI -----
# Para identificar patrones de correlación, como la relación negativa entre presupuesto y ROI
print("VISUALIZACIÓN 3: Correlación entre presupuesto, recaudación y ROI")
plt.figure(figsize=(8, 5))
correlacion = df[["presupuesto_millones", "recaudacion_millones", "roi_porcentaje"]].corr()
sns.heatmap(correlacion, annot=True, cmap="coolwarm", center=0)
plt.title("Correlación entre presupuesto, recaudación y ROI (2024)")
plt.xticks(rotation=45) 
plt.tight_layout() 
plt.savefig("grafico3_correlacion.png")
plt.close()
print("Grafico guardado\n")


# ----- Boxplot: ROI -----
# Para observar la variabilidad del ROI dentro de cada género, mostrando medianas, cuartiles y 
# posibles valores atípicos
print("VISUALIZACIÓN 4: Botplot de ROI")
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="genero", y="roi_porcentaje")
plt.title("Distribución de ROI por género (2024)")
plt.xlabel("Género")
plt.ylabel("ROI(%)")
plt.xticks(rotation=45) 
plt.tight_layout() 
plt.savefig("grafico4_boxplot_roi.png")
plt.close()
print("Grafico guardado\n")


# -----------------------------------------------------------------------------
# 7. INTERPRETACIÓN Y CONCLUSIONES
# -----------------------------------------------------------------------------
print("\n========= HALLAZGOS PRINCIPALES =========")

# Uso de comillas triple ("""") para imprimir en pantalla.
print("""                            
1. Los géneros con mayor ROI promedio fueron Ciencia Ficción, seguido por Drama y Animación.
   Evidencia: Gráfico de barras de ROI promedio por género (VISUALIZACIÓN 2)
              y boxplot de ROI (VISUALIZACIÓN 4).

2. La audiencia valora más Acción y Comedia, mientras que los críticos prefieren Acción y Drama.
   Evidencia: Media de calificación de audiencia y crítica por género (impresiones en consola).

3. Existe una correlación negativa fuerte entre presupuesto y ROI, indicando que películas 
   con presupuestos altos no siempre generan un alto retorno monetario.
   Evidencia: Heatmap de correlación entre presupuesto, recaudación y ROI (VISUALIZACIÓN 3).

       
RESPUESTA A LA PREGUNTA DE INVESTIGACIÓN:
--------------------------------------------
Según los datos de 2024, el género de Ciencia Ficción ofreció el mayor retorno de inversión promedio,
seguido por Drama y Animación. Esto indica que, en promedio, estas películas generan más ROI por
cada unidad invertida.


LIMITACIONES:
-------------
- Sesgo debido a la limpieza de datos (Eliminación de filas).
- Tamaño de muestra reducido (21 películas en 2024), lo que puede afectar la representatividad.
- Datos concentrados únicamente en un año; no se incluyen tendencias históricas.


PRÓXIMOS PASOS:
---------------
- Analizar datos de varios años para ver tendencias en ROI por género.
- Incluir métricas adicionales como presencia en streaming (plataformas digitales).
- Explorar relación entre ROI y otras variables (por ejemplo duración, idioma, país de producción).


CONCLUSIÓN GENERAL:
-------------------
El género de Ciencia Ficción se destaca como el más rentable en términos de ROI en 2024.
Aunque los ingresos absolutos son mayores en Acción, el retorno relativo es menor. 
Esto sugiere que películas con menor presupuesto pero buena aceptación pueden ser más eficientes financieramente.
""")

# ------------------------------------------------------------------------

print("\nANÁLISIS COMPLETADO CORRECTAMENTE\n")

# =============================================================================
# FIN DEL PROYECTO
# =============================================================================


# CHECKLIST DE ENTREGA
# ====================

# Antes de entregar tu proyecto, verifica que hayas completado:
# CÓDIGO:
# [✓] Todas las importaciones necesarias
# [✓] Carga de datos correctamente
# [✓] Exploración inicial (head, info, describe)
# [✓] Limpieza de datos documentada
# [✓] Al menos 3 análisis descriptivos diferentes
# [✓] Al menos 3 visualizaciones con títulos y etiquetas
# [✓] Código comentado explicando cada paso
# [✓] Interpretación en comentarios

# ARCHIVOS:
# [✓] proyecto_final.py (este archivo completo)
# [✓] datos.csv (tu dataset)
# [✓] grafico1.png
# [✓] grafico2.png
# [✓] grafico3.png
# [✓] README.md con documentación del proyecto

# DOCUMENTACIÓN:
# [✓] Pregunta de investigación clara
# [✓] Descripción de los datos usados
# [✓] Explicación de la limpieza realizada
# [✓] Interpretación de cada análisis
# [✓] Conclusiones basadas en evidencia
# [✓] Limitaciones identificadas