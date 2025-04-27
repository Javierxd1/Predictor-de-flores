# Iris Predictor API

Este proyecto es una API simple construida con FastAPI que permite predecir la especie de una flor del dataset Iris a partir de cuatro características: longitud y ancho del sépalo, longitud y ancho del pétalo.

## Características

- API RESTful utilizando FastAPI.
- Endpoint que recibe datos del dataset Iris y devuelve una predicción sobre la especie de la flor.
- Implementación de CORS (Cross-Origin Resource Sharing) para permitir el acceso desde cualquier origen.

## Instalación y configuración

Para comenzar, sigue estos pasos:

### 1. Crear un entorno virtual

Primero, crea un entorno virtual para tu proyecto:

```bash
python -m venv nombreEntorno
```
### 2. Activa el entorno virtual

```bash
source nombreEntorno/bin/activate #Mac/Linux
.\nombreEntorno\Scripts\activate #Windows

```


### 3. Instala las dependencias
Instala las librerías necesarias usando el siguiente comando:
```bash
source nombreEntorno/bin/activate #Mac/Linux
.\nombreEntorno\Scripts\activate #Windows

```


### 4. Inicia la aplicación
Instala las librerías necesarias usando el siguiente comando:
```bash
uvicorn main:app --reload
```
Esto arrancará la API en el puerto 8000 por defecto. Puedes acceder a la API en http://localhost:8000.

## Uso de la API
### Endpoint de predicción
post/predict
Este endpoint recibe un objeto JSON con las siguientes características del dataset Iris:
Instala las librerías necesarias usando el siguiente comando:
```bash
{
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.4,
    "petal_width": 0.2
}

```
Y responde con un objeto JSON con la predicción de la especie:
```bash
{
    "prediction": "Setosa"
}
```

## Imagen de la interfaz
Aquí tienes una imagen del frontend de la aplicación

![Interfaz del Frontend](\images\Frontend.png)
