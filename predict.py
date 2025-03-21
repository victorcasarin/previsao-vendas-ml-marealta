import mlflow.sklearn 
import pandas as pd 

#Carregar modelo
model = mlflow.sklearn.load_model("runs:/<RUN_ID>/model") #Substitua <RUN_ID> pelo ID da execução do MLflow 

# Fazer previsão 
temperature = float(input("Digite a temperatura (em °C): "))
tourists = int(input("Digite o número de turistas: "))
prediction = model.predict([[tempreature, tourists]])
print(f'Previsão de vendas: {prediction[0]:.2f} bebidas')