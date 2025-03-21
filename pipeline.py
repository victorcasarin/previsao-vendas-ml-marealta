import subprocess

# Executar scripts em sequência
subprocess.run(["python", "data_preparation.py"])
subprocess.run(["python", "train_model.py"])
subprocess.run(["python", "predict.py"])