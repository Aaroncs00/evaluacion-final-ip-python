# Evaluación Final – IP Python

**Autor:** Aaron Carvajal Serrano  
**Curso:** IP_IAPython_1  

---

## Descripción general

Este repositorio contiene la **evaluación final del curso IP Python**, donde se aplican de forma práctica los conocimientos adquiridos a lo largo del curso, incluyendo:

- Procesamiento de datos con Python y expresiones regulares
- Desarrollo de una mini aplicación backend con Django
- Creación de un modelo de Machine Learning con scikit-learn
- Desarrollo de una interfaz frontend con HTML, CSS y JavaScript
- Simulación de trabajo con metodología Scrum
- Uso de GitHub y documentación en Markdown

El proyecto está organizado por ejercicios, facilitando su comprensión, ejecución y evaluación.

---

## Tecnologías utilizadas

- **Python 3**
- **Django**
- **scikit-learn**
- **pandas**
- **Jupyter Notebook**
- **HTML / CSS / JavaScript**
- **SQLite**
- **Git y GitHub**

---

## Ejercicio 1 – GitHub y Markdown

- Creación de un repositorio profesional en GitHub
- Uso de commits significativos
- Documentación del proyecto mediante este archivo `README.md`
- Estructura clara y organizada de carpetas

---

## Ejercicio 2 – Procesador de datos con Python

Archivo principal: **`procesador.py`**

### Funcionalidad
- Lee un archivo de texto `usuarios.txt`
- Extrae **nombre, email y edad** utilizando expresiones regulares (Regex)
- Valida correctamente los correos electrónicos
- Genera un archivo `usuarios_limpios.csv` con los datos procesados
- Uso de funciones, listas, diccionarios y manejo de errores (`try/except`)

### Ejecución
Desde la raíz del proyecto:

python procesador.py

Ejercicio 3 – Mini aplicación Django (Notas)

Aplicación web desarrollada con Django para la gestión de notas.

Modelo

Nota

título

contenido

fecha

Características

Base de datos SQLite

Uso de models.py, views.py, urls.py y templates HTML

Visualización de las notas en una interfaz web

Creación y gestión de notas desde el panel de administración de Django

Ejecución

cd django_project
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

Acceso:

Aplicación: http://127.0.0.1:8000/

Administración: http://127.0.0.1:8000/admin/

Ejercicio 4 – Machine Learning

Notebook: notebooks/ml_clasificacion_iris.ipynb

Descripción

Uso del dataset clásico Iris

División de datos en entrenamiento y test

Entrenamiento de un modelo de clasificación con scikit-learn

Predicción y evaluación del modelo (accuracy y classification report)

Explicación del proceso y resultados en celdas Markdown

Ejecución
jupyter notebook
Abrir el notebook y ejecutar todas las celdas en orden.

Ejercicio 5 – Frontend

Interfaz desarrollada con HTML, CSS y JavaScript.

Funcionalidad

Formulario de registro de usuario

Validación de campos obligatorios

Validación de edad mínima

Mensajes de error y éxito mediante JavaScript

Estilos básicos con CSS

Ejecución

Abrir directamente en el navegador:
frontend/html/index.html

Ejercicio 6 – Scrum

Archivo: scrum.md

Incluye:

Product Backlog (lista de tareas del proyecto)

Definición de un Sprint con objetivo y tareas

Retrospectiva (qué fue bien y qué se puede mejorar)

Instalación de dependencias

Se recomienda el uso de un entorno virtual:
python -m venv venv
source venv/bin/activate   # Mac / Linux
pip install -r requirements.txt

Conclusión

Este proyecto integra los distintos conceptos vistos durante el curso IP Python,
aplicando buenas prácticas de desarrollo, organización del código y documentación.
El resultado es un proyecto completo y funcional que cumple con todos los requisitos
de la evaluación final.
