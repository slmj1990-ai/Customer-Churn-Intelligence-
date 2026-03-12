**Predicción de la pérdida de clientes y estrategia de retención**

**Resumen del proyecto**



La pérdida de clientes es uno de los problemas más críticos para las empresas de suscripción y comercio electrónico. Retener a los clientes existentes es significativamente más económico que adquirir nuevos, lo que convierte la predicción de la pérdida de clientes en una aplicación clave de la ciencia de datos.



Este proyecto desarrolla un sistema de aprendizaje automático para predecir el riesgo de pérdida de clientes y propone estrategias de retención basadas en datos, basadas en predicciones de modelos.





**La solución final incluye:**



Predicción de la pérdida de clientes mediante múltiples modelos de aprendizaje automático



Comparación y evaluación de modelos



Explicabilidad mediante SHAP



Segmentación del riesgo de clientes



Estrategias de retención orientadas al negocio





**Objetivo empresarial**



El objetivo de este proyecto es:



Predecir qué clientes tienen mayor probabilidad de pérdida



Identificar los factores clave de pérdida



Segmentar a los clientes según el riesgo de pérdida



Proponer estrategias de retención específicas





**Características del conjunto de datos**



El conjunto de datos contiene variables de comportamiento y transaccionales como:



* Actividad del cliente
* 
* Frecuencia de inicio de sesión
* 
* Duración promedio de la sesión
* 
* Páginas por sesión
* 
* Métricas de interacción
* 
* Índice de interacción en redes sociales
* 
* Tasa de apertura de correo electrónico
* 
* Índice de interacción
* 
* Comportamiento de compra
* 
* Compras totales
* 
* Valor promedio del pedido
* 
* Valor de la vida útil
* 
* Indicadores de fricción del cliente
* 
* Índice de abandono del carrito
* 
* Índice de devoluciones
* 
* Llamadas de servicio al cliente
* 
* Señales de inactividad del cliente
* 
* Días transcurridos desde la última compra
* 
* Índice de inactividad
* 
* Características demográficas
* 
* Edad
* 
* Género
* 
* País



**Aprendizaje automático Modelos**



Se probaron y compararon varios modelos:



Precisión del modelo: ROC-AUC

Regresión logística: 0,82 0,88

Bosque aleatorio: 0,90 0,94

Gradient Boosting: 0,91 0,95

XGBoost: 0,92 0,96



El modelo con mejor rendimiento fue Random Forest y Gradient Boosting/XGBoost.





**Evaluación del modelo**



El modelo se evaluó mediante:



Precisión



ROC-AUC



Matriz de confusión



Curva ROC



Ejemplos de información:



Alta tasa de recuperación para clientes que abandonan el servicio



Fuerte separación entre grupos de clientes que abandonan el servicio y los que no



ROC-AUC superior a 0,90





**Explicabilidad del modelo (SHAP)**



Para comprender por qué los clientes abandonan el servicio, se utilizó el análisis SHAP.





Los principales factores que impulsan la pérdida de clientes incluyen:



* Puntuación de inactividad



* Tasa de abandono del carrito



* Puntuación de interacción



* Días transcurridos desde la última compra



* Dependencia del descuento



Esta información ayuda a la empresa a diseñar estrategias de retención específicas.





**Segmentación del riesgo del cliente**



Utilizando la probabilidad de pérdida prevista, los clientes se segmentaron en tres grupos:



Segmento de riesgo Probabilidad de pérdida

Riesgo bajo < 30 %

Riesgo medio 30-60 %

Riesgo alto > 60 %



Esta segmentación permite a la empresa priorizar las intervenciones.





**Estrategia de retención**



Basada en la segmentación de riesgo:



Estrategia recomendada por segmento

Riesgo bajo: programas de fidelización

Riesgo medio: ofertas personalizadas

Riesgo alto: campañas de retención urgentes



Ejemplos de acciones:



**Riesgo alto:**



Ofertas de descuento



Campañas de reactivación



Atención al cliente proactiva



**Riesgo medio:**



Recomendaciones personalizadas de productos



Promociones dirigidas



**Riesgo bajo:**



Recompensas de fidelización



Programas VIP



Visualizaciones





El proyecto incluye varias visualizaciones analíticas:



* Curva ROC
* 
* Matriz de confusión
* 
* Importancia de las características
* 
* Gráfico de resumen SHAP
* 
* Distribución de probabilidad de abandono
* 
* Distribución de segmentos de riesgo
* 
* Pila tecnológica





Bibliotecas de Python utilizadas:



* pandas



* numpy



* scikit-learn



* xgboost



* lightgbm



* seaborn



* matplotlib



* shap







**Técnicas clave de ciencia de datos**



El proyecto demuestra varias habilidades importantes:



Característica Ingeniería



Comparación de modelos



Modelado de clasificación



IA explicable



Segmentación de clientes



Traducción empresarial de los resultados de ML



Cómo ejecutar el proyecto







**Clonar el repositorio:**



git clone https://github.com/slmj1990-ai/Customer-Churn-Intelligence-.git



Instalar dependencias:



pip install -r requirements.txt



Ejecutar los notebooks en orden:



01\_eda.ipynb

02\_feature\_engineering.ipynb

03\_modeling.ipynb

Mejoras futuras



**Posibles pasos a seguir:**



Ajuste de hiperparámetros



Implementación del modelo (API)



Predicción de abandono en tiempo real



Desarrollo de paneles (Power BI/Tableau)



Campañas de retención automatizadas





**Autor: Sara Leticia Marín Jáuregui** 



Proyecto de ciencia de datos



Predicción de abandono de clientes y estrategia de retención



Desarrollado como un proyecto de portafolio para demostrar un flujo de trabajo integral de aprendizaje automático.

