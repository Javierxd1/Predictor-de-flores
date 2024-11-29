import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

#Carga del dataset
data = pd.read_csv("data/iris.csv")
#print(data.head())

#print(data['species'].value_counts())

#Mapear las especies a datos númericos
data['species'] = data['species'].map({
    "setosa":0,
    "versicolor":1,
    "virginica":2
})

#print(data['species'].value_counts())

#Definir los labels de x y y para entrenar el modelo
X = data.drop(labels="species",axis=1)
y= data['species']

X_train,X_test,y_train,y_test = train_test_split(X,y, test_size=0.2,random_state=42)

#Modelo: Creación y entrenamiento
model = RandomForestClassifier()
model.fit(X_train,y_train)

#Predicciones
y_pred = model.predict(X_test)
print(y_pred)

#Evaluación del modelo
accuracy = accuracy_score(y_test,y_pred)
print(accuracy)

joblib.dump(model,filename='model/model.pkl')