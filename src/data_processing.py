import os


def clean_data(df):
    #Limpia los datos
    df = df.dropna()
    return df


def save_processed(df, path="Data/Processed/clean_data.csv"):
    #Guarda el dataframe limpio en una ruta dada
    #Crea las carpetas si no existen


    # Crear carpeta si no existe
    directory = os.path.dirname(path)
    if directory != "" and not os.path.exists(directory):
        os.makedirs(directory)

    # Guardar archivo correctamente
    df.to_csv(path, index=False)


