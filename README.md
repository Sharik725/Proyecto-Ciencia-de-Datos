_Proyecto Ciencia de Datos_

Presentado por:
-Briggite Arevalo
-Sharik Garnica
-Maykol Millán 

**Predicción de Default en Tarjetas de Crédito como Soporte a la Toma de Decisiones Financieras**

**_INTRODUCCION_**
El riesgo de crédito es uno de los principales desafíos que enfrentan las entidades financieras, especialmente en productos de alta rotación como las tarjetas de crédito. Anticipar qué clientes podrían incumplir sus obligaciones de pago permite reducir pérdidas económicas, optimizar políticas de aprobación y diseñar estrategias preventivas. El uso de las tarjetas de crédito, ha incrementando el riesgo de que un cliente deje de pagar su tarjeta, no solo es un número rojo o una alerta para el banco o la entidad financiera, es un dinero menos para prestar a otros bancos y no tener con que ofrecer un mejor servicio, mientras que para el cliente o deudor es dañar su historial crediticio, lo que le costara a un futuro conseguir un préstamo o alguna adquisición financiera.


En este contexto, la ciencia de datos actua como un mecanismo preventivo, utilizando el análisis exploratorio para identificar patrones y relaciones causales claves. Preguntas como si la edad, el nivel de endeudamiento, o el historial de pagos previos son factores determinantes a antes de que sea tarde, el objetivo es entender la relación entre las variables para saber qué realmente lleva a un impago. Al usar arboles de decisión o regresión logística o redes neuronales, se construirá un modelo predictivo robusto, el cual utilizará los 30.000 registros de clientes para predecir de forma efectiva la probabilidad de default en tarjetas de crédito.

_**OBJETIVO GENERAL**_

Analizar el dataset “Default of Credit Card Clients” mediante técnicas de análisis, procesamiento y modelado predictivo para estimar la probabilidad de incumplimiento de pago y evaluar el rendimiento de distintos modelos de clasificación.

_**OBJETIVOS ESPECIFICOS**_

1.Realizar limpieza, transformación y preprocesamiento del dataset.

2.Desarrollar un análisis exploratorio para identificar patrones y comportamientos relevantes.

3.Implementar modelos de clasificación para predecir el default de clientes.

4.Evaluar los modelos empleando métricas relevantes. 

5.Identificar los factores que más influyen en la probabilidad de incumplimiento.

_**JUSTIFICACION**_

El análisis predictivo del comportamiento crediticio se ha convertido en una herramienta fundamental para las entidades financieras, ya que permite reducir el riesgo de cartera mediante la identificación temprana de clientes con alta probabilidad de incumplimiento. Este tipo de modelos contribuye a optimizar las estrategias de otorgamiento y retención, así como a diseñar políticas preventivas basadas en evidencia. Para fines académicos y de investigación, el dataset utilizado resulta especialmente valioso por su tamaño, diversidad de variables y cercanía con escenarios reales del sector financiero. Su estudio facilita el desarrollo de competencias en análisis de datos, visualización, preprocesamiento y aplicación de técnicas de machine learning orientadas a la resolución de problemas reales en la evaluación del riesgo crediticio.

_**MARCO TEORICO**_

  **Riesgo de Crédito**

El riesgo de crédito se define como la probabilidad de que un cliente no cumpla con las obligaciones financieras adquiridas, generando pérdidas para la entidad que otorgó el crédito. En el sector bancario, este riesgo se evalúa mediante modelos cuantitativos que permiten anticipar situaciones de morosidad y tomar decisiones informadas sobre la aprobación, seguimiento o recuperación del crédito. La correcta gestión de este riesgo es crucial para mantener la estabilidad financiera de las instituciones y garantizar procesos de otorgamiento más eficientes.

**Default o Incumplimiento de Pago**

El término default hace referencia al incumplimiento del pago mínimo o total de una obligación crediticia en el tiempo acordado. En el dataset utilizado, el default representa un evento binario donde 1 indica incumplimiento y 0 indica cumplimiento. Este concepto es especialmente relevante porque permite modelar el comportamiento del cliente desde una perspectiva predictiva, generando información útil para clasificar perfiles de riesgo.

**Análisis de Datos**

El análisis de datos comprende un conjunto de técnicas que permiten transformar información bruta en conocimiento útil. En estudios financieros, este proceso incluye limpieza, exploración, visualización y transformación de los datos, con el objetivo de comprender patrones, relaciones y tendencias que influyen en el comportamiento del cliente. El análisis exploratorio (EDA) es una etapa esencial que permite detectar anomalías, outliers y correlaciones que pueden impactar en el rendimiento de los modelos predictivos.

**Machine Learning Aplicado al Riesgo Crediticio**

El machine learning es un conjunto de métodos que permiten construir modelos capaces de aprender patrones a partir de datos históricos. En el contexto del riesgo crediticio, estos modelos se emplean para predecir la probabilidad de que un cliente incurra en default, permitiendo automatizar decisiones y crear sistemas de alerta temprana.

_Modelos más utilizados_

**Regresión Logística:** modelo estadístico base para problemas de clasificación binaria, ampliamente usado en riesgo crediticio por su interpretabilidad.

**Árboles de Decisión:** permiten segmentar los datos mediante reglas simples, facilitando el entendimiento del comportamiento del cliente.

**Random Forest:** conjunto de múltiples árboles que mejora la precisión y evita el sobreajuste.

Estos algoritmos permiten generar estimaciones más precisas, comparar escenarios y evaluar el impacto de diferentes variables en la probabilidad de incumplimiento.

**Métricas de Evaluación**

Para medir el desempeño de los modelos clasificadores se utilizan métricas como:

**Accuracy:** proporción total de predicciones correctas.

**Precision:** porcentaje de predicciones positivas que realmente son casos de default.

**Recall:** capacidad del modelo para detectar clientes que sí incumplen.

**F1-Score:** equilibrio entre precision y recall.

**Matriz de Confusión:** herramienta que permite visualizar aciertos y errores del modelo de forma estructurada.

La elección de métricas es especialmente importante en este tipo de problemas, ya que suele existir desbalance entre clientes cumplidos y morosos.

**Importancia del Preprocesamiento**

El preprocesamiento es una etapa crítica en proyectos de machine learning. Consiste en estandarizar datos, tratar valores atípicos, transformar variables categóricas y escalar montos financieros. Un adecuado preprocesamiento mejora significativamente el rendimiento final del modelo y garantiza la validez del análisis.

_**METODOLOGIA**_
La metodología utilizada en este estudio se basa en el enfoque de la ciencia de datos, que integra procesos de recolección, exploración, limpieza, modelado y evaluación para desarrollar un sistema predictivo capaz de identificar la probabilidad de incumplimiento de pago en clientes de tarjetas de crédito. El proceso se desarrolló en las siguientes etapas:

1. Obtencion del Dataset
2. Limpieza y preprocesamiento de datos
3. Analisis Exploratorio de datos (EDA)
4. Construcción de Modelos Predictivos
5. Evaluación del Desempeño del Modelo
6. Interpretación y Selección del Modelo Óptimo
7. Documentación y Presentación de Resultados

_**ANALISIS Y RESULTADOS**_
Se visualizara junto con POWERBI el analisis y los resultados obtenidos

_**CONCLUSIONES**_
1. 



