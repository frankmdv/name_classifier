# Instructivo

Este archivo de texto te guiará sobre los pasos necesarios para ejecutar el proyecto correctamente.

## Requisitos previos

1. **Instalación de dependencias:**
   Primero, debes descargar e instalar las dependencias requeridas. Para ello, utiliza el siguiente comando en la terminal:

   ```bash
   pip install -r requirements.txt
   ```

2. **Archivo de entrada:**
   El archivo de entrada debe ser un archivo Excel que se encuentra en la carpeta `datasets`.

   - El archivo debe llamarse `nombres.xlsx` por defecto.
   - La hoja de Excel que contiene la información debe ser la primera (hoja inicial).
   - La columna que contiene los nombres a evaluar debe llamarse **'Nombre'**.

3. **Archivo de ejecución:**
   El módulo o archivo de Python que debe ejecutarse es el que tiene el nombre **'main.py'**.

## Salida

Al ejecutar el script, se generará una salida en la consola que mostrará los resultados de la clasificación y la identificación de los nombres similares.  
Además, para mayor comodidad, el resultado también se guardará en un archivo de Excel en la carpeta `results`, con los mismos resultados que se muestran en la consola.
