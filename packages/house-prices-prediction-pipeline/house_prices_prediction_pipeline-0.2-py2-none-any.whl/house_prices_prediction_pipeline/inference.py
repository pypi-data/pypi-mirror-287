import pandas as pd
import numpy as np
import joblib
from . import FEATURES, CONTINIOUS_FEATURES, CATEGORICAL_FEATURES, OUTPUT_DIR


def load_transformers(model_dir: str):
    numeric_transformer = joblib.load(
        model_dir + 'numerical_scaler.joblib'
    )
    categorical_transformer = joblib.load(
        model_dir + 'categorical_encoder.joblib'
    )
    return numeric_transformer, categorical_transformer


def make_predictions(input_data: pd.DataFrame) -> np.ndarray:
    numeric_transformer, categorical_transformer = load_transformers(
        OUTPUT_DIR
    )

    # Load the model
    model = joblib.load(OUTPUT_DIR + 'model.joblib')

    # Preprocess input data

    X = input_data[FEATURES]

    X_numeric = numeric_transformer.transform(X[CONTINIOUS_FEATURES])
    X_categorical = categorical_transformer.transform(X[CATEGORICAL_FEATURES])
    X_final = np.concatenate([X_numeric, X_categorical], axis=1)

    # Make predictions
    predictions = model.predict(X_final)
    return predictions
