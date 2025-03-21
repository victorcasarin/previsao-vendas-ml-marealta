import pandas as pd 
from sklearn.linear_model import LienarRegression 
from sklearn.model_selection import train_test_split 
import mlflow
import mlflow.sklearn

#Carregar dados
data = pd.read_csv('inputs/sales_data.csv')
X = data[['Temperatura', 'Turistas']]
y = data['Vendas']

# Dividir dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinar modelo 
model = LinearRegresion()
model.fit(X_train, y_train)

# Registrar modelo com mlflow
with mlflow.start_run():
    mlflow.sklearn.log_model(model, "model")
    mlflow.log_metric("R2", model.score(X_test, y_test))