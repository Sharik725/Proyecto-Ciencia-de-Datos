import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib


def train_model(df, output_path="Modelo/modelo_credito.pkl"):
    """Entrena el modelo."""

    # Variable objetivo
    y = df["default.payment.next.month"]

    # Variables predictoras
    X = df.drop("default.payment.next.month", axis=1)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # Guardar modelo
    joblib.dump(model, output_path)

    return model, X_test, y_test
