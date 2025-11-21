import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

<<<<<<< HEAD
def train_model(df, save=False, model_path="../Modelo/modelo_credito.pkl"):
    # Entrena el modelo usando regresión logística con datos estandarizados
=======
def train_model(df, model_path="../Modelo/modelo_credito.pkl"):
    #Entrena el modelo usando regresión logística con datos estandarizados.
>>>>>>> 83bf10f4a79ffd5e60da5ea06fa9b450fa907385

    target_col = "default.payment.next.month"

    # Separar variables
    X = df.drop(target_col, axis=1)
    y = df[target_col]

    # División
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Escalado de datos
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

<<<<<<< HEAD
    # Modelo
=======
    # Modelo con más iteraciones
>>>>>>> 83bf10f4a79ffd5e60da5ea06fa9b450fa907385
    model = LogisticRegression(
        max_iter=1000,
        solver="lbfgs"
    )

    model.fit(X_train_scaled, y_train)

    # Guardar SOLO si el usuario lo pide
    if save:
        import os
        os.makedirs(os.path.dirname(model_path), exist_ok=True)

        joblib.dump({
            "model": model,
            "scaler": scaler,
            "columns": X.columns.tolist()
        }, model_path)

    return model, scaler, X_test_scaled, y_test
