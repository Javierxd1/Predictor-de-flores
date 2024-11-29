# iris_predictor
Breve proyecto en el que se formula una API que hace una petición de datos del dataset Iris y regresa una predicción con los datos ingresados. El endpoint se construye con FastAPi

Para inciar el proyecto, cree un entorno virtual

Python -m venv nombreEntorno

Luego de ello, active el entorno

    source venv/bin/activate (Para Mac)

    .\venv\Scripts\activate (Para Windows)

Finalmente, instale las liberias necesarias

    pip install -r requirements.txt

Luego, inicie la aplicación
    uvicorn main:app --reload



