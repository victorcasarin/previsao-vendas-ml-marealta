import pandas as pd 
import numpy as np 


#Gerar dados fictícios
np.random.seed(42)
temperatures = np.random.randint(20, 40, size=100) 
tourists = np.random.randint(50, 200, size=100)
sales = 30 + 1.5 * temperatures + 0.8 * tourists + np.random.normal(0,10, size=100)

#Criar DataFrame
data = pd.DataFrame({'Temperatura': temperatures, 'Turistas': tourists, 'Vendas': sales})

# Salvar dados em um arquivo CSV
data.to_csv('inputs/sales_data.csv', index=False)