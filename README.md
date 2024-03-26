# Análisis sobre los Hechos de Tránsito en Guatemala
Los datos con los que se realiza el siguiente análisis son obtenidos del portal del Instituto Nacional de Estadística (INE) de Guatemala. Pueden ser descargados [aquí](https://www.ine.gob.gt/bases-de-datos/accidentes-de-transito/).

## Objetivos generales
- Comprender exhaustivamente los patrones y factores de riesgo asociados con los hechos de tránsito, utilizando herramientas de minería de datos para identificar relaciones significativas entre las variables involucradas.
- Desarrollar medidas preventivas basadas en la evidencia obtenida del análisis de datos, con el fin de reducir la incidencia y gravedad de los accidentes de tráfico y mejorar la seguridad vial en general.
- Promover la conciencia sobre la importancia de la seguridad vial y fomentar la acción para implementar medidas efectivas de prevención de accidentes.

## Objetivos específicos
- Identificar períodos y áreas de mayor riesgo de accidentes de tráfico mediante el análisis de la distribución temporal y geográfica de los incidentes, con el fin de orientar la asignación de recursos para la prevención.
- Evaluar la influencia de las características del piloto, como el sexo, la edad y el estado del piloto, en la ocurrencia y gravedad de los accidentes, proporcionando información relevante para campañas de concienciación y programas de educación vial.
- Identificar factores de riesgo específicos asociados con las causas y tipos de vehículos involucrados en los accidentes de tráfico, con el fin de desarrollar estrategias de prevención dirigidas y efectivas.

## Descripción de datos
Descripción de los datos

### Descripción de las variables
- dia_ocu: Día en el que ocurrió el accidente.
  Los valores son números enteros que representan días específicos.
  Es cuantitativa discreta.
- mes_ocu: Mes en el que ocurrió el accidente.
  Los valores son nombres de meses y no tienen un orden específico.
  Es cualitativa nominal.
- dia_sem_ocu: Día de la semana en el que ocurrió el accidente.
  Los valores son nombres de días de la semana y no tienen un orden específico.
  Es cualitativa nominal.
- hora_ocu: Hora, en formato de 24 horas, en la que ocurrió el accidente.
  Los valores son números enteros que representan horas específicas.
  Es cuantitativa discreta.
- depto_ocu: Departamento del país en el que ocurrió el accidente.
  Los valores son nombres de departamentos y no tienen un orden específico.
  Es cualitativa nominal.
- zona_ocu: Zona en la que ocurrió el accidente.
  Los valores son números enteros que representan zonas específicas.
  Es cuantitativa discreta.
- sexo_pil: Sexo del piloto involucrado en el accidente.
  Los valores son "Hombre" o "Mujer", sin un orden específico.
  Es cualitativa nominal.
- edad_pil: Edad del piloto involucrado en el accidente.
  Los valores son números enteros que representan años específicos.
  Es cuantitativa discreta.
- mayor_menor: Indica si el piloto es mayor o menor de edad.
  Los valores son "Mayor" o "Menor", sin un orden específico.
  Es cualitativa nominal.
- estado_pil: Estado del piloto involucrado en el accidente.
  Los valores son categorías como "Ebrio", "Sobrio", “Ignorado”, etc…, sin un orden específico.
  Es cualitativa nominal.
- tipo_vehi: Tipo de vehículo involucrado en el accidente.
  Los valores son categorías como "Automóvil", "Motocicleta", etc…, sin un orden específico.
  Es cualitativa nominal.
- marca_vehi: Marca del vehículo involucrado en el accidente.
  Los valores son nombres de marcas y no tienen un orden específico.
  Es cualitativa nominal.
- causa_acc: Causa del accidente.
  Los valores son categorías como "Colisión", "Volco", “Empotro”, etc…, sin un orden específico.
  Es cualitativa nominal.
- year: Año en el que ocurrió el accidente.
  Los valores son números enteros que representan años específicos.
  Es cuantitativa discreta.

### Operaciones de limpieza
Los datos a utilizar fueron obtenidos en diferentes dataframes, uno para cada año. Esto presenta un gran problema para el análisis de los mismos, ya que dichos datos y sus variables presentan una gran inconsistencia en los diferentes años. Debido a esto se realizó una exhaustiva operación de limpieza, la cual se dividió en 2 fases:
#### Corrección de archivos
- Los archivos a utilizar no seguían un estándar en cuanto al formato, por lo que se decidió convertirlos a un estándar csv para facilitar su uso.
- Se eliminaron archivos que se consideraron innecesarios debido a su alto nivel de inconsistencias, las cuales no podían ser corregidas sin sesgar el resultado del análisis.
- Debido a la inconsistencia de las columnas en los documentos, fue necesario llegar a un acuerdo de cuales variables deberán ser eliminadas y cuales se conservaran debido a su importancia para el análisis.
#### Corrección de variables
- Se aseguró que todas las variables categóricas se encontrarán en minúsculas. Esto se realizó por medio de funciones lambda dentro de python.
- Debido a que muchas variables categóricas poseían inconsistencias debido a acentos, se decidió crear un diccionario para la corrección y reemplazo de dichos caracteres.
- Se corrigieron faltas ortográficas en diferentes variables categóricas para asegurar su consistencia.
- Se corrigieron inconsistencias en variables que presentaban características cuantitativas y cualitativas siguiendo los detalles que provee el diccionario de variables del INE.
- Se corrigieron los valores nulos. Para variables categóricas se decidió realizar una nueva categoría cuando dicho valor no se provee. Para variables numéricas se reemplazará el valor por el estadístico que no represente un sesgo significativo en los resultados.