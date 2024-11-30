from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import numpy as np

#Cargar el modelo entrenado
model = joblib.load('model/model.pkl')

#Creación de la instancia de Fast API

app = FastAPI()

#Definición del modelo de requerimiento de los datos (De acuerdo con los datos de entrenamiento)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir solicitudes desde cualquier origen
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos HTTP
    allow_headers=["*"],  # Permitir todos los encabezados
)

class PredictedRequest(BaseModel):
    sepal_length:float
    sepal_width:float
    petal_length:float
    petal_width:float

# Definición del endpoind de predicción
@app.post("/predict")
async def Predictor(request:PredictedRequest):
    data = np.array([[request.sepal_length,
                      request.sepal_width,
                      request.petal_length,
                      request.petal_width
                      ]])
    prediction = model.predict(data)
    species_map = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}
    return {"prediction": species_map[int(prediction[0])]}


@app.get('/')
async def root():
    return{"Bienvenido al clasificador usando FastAPI"}