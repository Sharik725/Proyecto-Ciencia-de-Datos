import pandas as pd

def load_data(path="Data/RAW/UCI_Credit_Card.csv"):
    """Carga el dataset original."""
    df = pd.read_csv(path)
    return df

def clean_data(df):
    """Limpieza básica del dataset."""
    df = df.dropna()  # eliminar filas con valores faltantes
    return df

def save_processed(df, path="Data/Processed/clean_data.csv"):
    """Guardar datos limpios."""
    df.to_csv(path, index=False)
