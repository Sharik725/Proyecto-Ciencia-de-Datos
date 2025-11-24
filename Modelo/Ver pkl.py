import pickle

with open(r"C:\Proyecto\Modelo\modelo_credito.pkl", "rb") as f:
    modelo = pickle.load(f)

print(modelo)
print("\nParámetros del modelo:\n", modelo.get_params())
