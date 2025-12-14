# Evaluación Final – IP Python

Autor: Aaron Carvajal Serrano  
Curso: IP_IAPython_1

## Descripción
Proyecto de evaluación final que incluye:
- Procesamiento de datos con Python
- Aplicación Django
- Ejercicio de Machine Learning
- Interfaz frontend
- Simulación Scrum

## Tecnologías utilizadas

- **Python 3**
- **Django**
- **scikit-learn**
- **pandas**
- **HTML / CSS / JavaScript**
- **Jupyter Notebook**
- **Git & GitHub**
- **SQLite**

---

## Estructura del proyecto

evaluacion-final-ip-python/
├── README.md
├── requirements.txt
├── procesador.py
├── usuarios.txt
├── usuarios_limpios.csv
├── scrum.md
├── notebooks/
│ └── ml_clasificacion_iris.ipynb
├── django_project/
│ ├── manage.py
│ ├── config/
│ └── notas/
└── frontend/
└── html/
├── index.html
├── css/
│ └── styles.css
└── js/
└── script.js


---

## Ejercicio 1 – GitHub + Markdown

- Repositorio creado en GitHub con estructura clara
- Uso de commits significativos
- Documentación del proyecto mediante este README.md

---

## Ejercicio 2 – Procesador de datos con Python

Archivo principal: `procesador.py`

### Funcionalidad
- Lee un archivo `usuarios.txt`
- Extrae nombre, email y edad usando **Regex**
- Valida correctamente los emails
- Genera un archivo `usuarios_limpios.csv`

### Ejecución
```bash
python procesador.py

Ejercicio 3 – Mini aplicación Django (Notas)

Aplicación Django que permite gestionar notas.

Modelo

Nota

título

contenido

fecha

Características

Base de datos SQLite

Uso de models, views, urls y templates

Visualización de notas desde interfaz web

Creación de notas desde el panel de administración

Ejecución
cd django_project
python manage.py migrate
python manage.py runserver


Acceso:

Aplicación: http://127.0.0.1:8000/

Admin: http://127.0.0.1:8000/admin/

Ejercicio 4 – Machine Learning

Notebook: notebooks/ml_clasificacion_iris.ipynb

Descripción

Uso del dataset Iris

Entrenamiento de un modelo de clasificación con scikit-learn

División de datos en entrenamiento y test

Predicción y evaluación del modelo

Explicación del proceso en celdas Markdown

Ejecución
jupyter notebook


Abrir el notebook y ejecutar todas las celdas.

Ejercicio 5 – Frontend

Interfaz desarrollada con HTML, CSS y JavaScript.

Funcionalidad

Formulario de registro de usuario

Validaciones en JavaScript

Estilos básicos con CSS

Ejecución

Abrir directamente en el navegador:

frontend/html/index.html

Ejercicio 6 – Scrum

Archivo: scrum.md

Incluye:

Product Backlog

Sprint con objetivo y tareas

Retrospectiva (qué fue bien y qué mejorar)

Instalación de dependencias

Se recomienda usar un entorno virtual:

python -m venv venv
source venv/bin/activate   # Mac / Linux
pip install -r requirements.txt

Conclusión

Este proyecto integra los conocimientos adquiridos durante el curso IP Python,
aplicando buenas prácticas de desarrollo, organización de código y documentación,
cumpliendo todos los requisitos de la evaluación final.