# Proyecto-Final-Analisis-de-Datos
Proyecto final de curso: "Fundamentos de Python para Análisis de Datos".  
Trabajo de análisis completo y presentación de resultados

#==================================================================
#PROYECTO FINAL: Análisis del retorno de inversión (ROI) por género cinematográfico
#==================================================================
#Autor: Nahomi Yamile Velazquez Gasca
#Fecha: 01/Diciembre/2025
#===================================================================

**1. Pregunta de investigación**
¿Cuál género cinematográfico ofrece el mayor retorno de inversión (ROI) en el último año (2024)?

**2. Descripción de los datos**
El dataset contiene información de 200 películas de los últimos años (2018-2024), incluyendo:
- id_pelicula: Número en lista
- titulo: Identificador único de la película
- genero: Género cinematográfico
- año: Año de estreno
- duracion_minutos: Duración en minutos
- presupuesto_millones: Presupuesto en millones de dólares
- recaudacion_millones: Recaudación en millones de dólares
- calificacion_critica: Puntuación de críticos
- calificacion_audiencia: Puntuación del público
- votos: Número de votos
- idioma_original: Idioma original
- ganancia_millones: Ganancia neta en millones de dólares
- roi_porcentaje: Retorno de inversión (ROI) en porcentaje

**3. Limpieza de datos**
- Se hizo corrección de texto mal codificado
- Se eliminaron filas con valores faltantes y duplicados en columnas críticas  
- Se filtraron valores negativos o cero en columnas numéricas relevantes
- Se eliminaron filas con valores duplicados  
- Se convirtieron los tipos de datos de las columnas para un manejo más eficiente.
- Se eliminaron outliers en el retorno de inversión (ROI)
- Se filtraron los datos para el año 2024


**4. Análisis descriptivo**
*Número de películas por género:*
  - Los géneros más producidos fueron Animación y Ciencia Ficción 
  - El menos producido fue Acción 

*Media de calificación por género:*
  - Por la crítica: Acción y Drama mejor valoradas  
  - Por la audiencia: Acción y Comedia mejor valoradas  

*ROI promedio por género:*
  - Más rentable: Ciencia Ficción, seguido por Drama y Animación  
  - Menos rentable: Terror y Comedia  

*Ganancia promedio por género:*
  - Más ingresos: Acción y Ciencia Ficción  
  - Menos ingresos: Romance y Comedia  

*Correlación:*
  - Presupuesto vs ROI: negativa fuerte (-0.77)  
  - Recaudación vs ROI: positiva pero débil (0.22)  
  - Presupuesto vs Recaudación: Casi nula (0.04)


**5. Visualizaciones**
*Cantidad de películas por género (2024)*
  grafico1_peliculas_genero.png

*ROI promedio por género (2024)*
  grafico2_roi_genero.png

*Correlación entre presupuesto, recaudación y ROI*
  grafico3_correlacion.png

*Distribución de ROI por género (boxplot)*
  grafico4_boxplot_roi.png


**6. Interpretación y conclusiones**
a. Los géneros con mayor ROI promedio fueron Ciencia Ficción, seguido por Drama y Animación.
   Evidencia: Gráfico de barras de ROI promedio por género (VISUALIZACIÓN 2)
              y boxplot de ROI (VISUALIZACIÓN 4).

b. La audiencia valora más Acción y Comedia, mientras que los críticos prefieren Acción y Drama.
   Evidencia: Media de calificación de audiencia y crítica por género (impresiones en consola).

c. Existe una correlación negativa fuerte entre presupuesto y ROI, indicando que películas 
   con presupuestos altos no siempre generan un alto retorno monetario.
   Evidencia: Heatmap de correlación entre presupuesto, recaudación y ROI (VISUALIZACIÓN 3).

       
RESPUESTA A LA PREGUNTA DE INVESTIGACIÓN:
#--------------------------------------------
Según los datos de 2024, el género de Ciencia Ficción ofreció el mayor retorno de inversión promedio,
seguido por Drama y Animación. Esto indica que, en promedio, estas películas generan más ROI por
cada unidad invertida.


LIMITACIONES:
#-------------
- Sesgo debido a la limpieza de datos (Eliminación de filas).
- Tamaño de muestra reducido (21 películas en 2024), lo que puede afectar la representatividad.
- Datos concentrados únicamente en un año; no se incluyen tendencias históricas.


PRÓXIMOS PASOS:
#---------------
- Analizar datos de varios años para ver tendencias en ROI por género.
- Incluir métricas adicionales como presencia en streaming (plataformas digitales).
- Explorar relación entre ROI y otras variables (por ejemplo duración, idioma, país de producción).


CONCLUSIÓN GENERAL:
#-------------------
El género de Ciencia Ficción se destaca como el más rentable en términos de ROI en 2024.
Aunque los ingresos absolutos son mayores en Acción, el retorno relativo es menor. 
Esto sugiere que películas con menor presupuesto pero buena aceptación pueden ser más eficientes financieramente.


**7. Archivos incluidos**
- 'Proyecto_final.py' – Código completo  
- 'peliculas_ratings.csv' – Dataset usado  
- 'grafico1_peliculas_genero.png' 
- 'grafico2_roi_genero.png'
- 'grafico3_correlacion.png'
- 'grafico4_boxplot_roi.png'
