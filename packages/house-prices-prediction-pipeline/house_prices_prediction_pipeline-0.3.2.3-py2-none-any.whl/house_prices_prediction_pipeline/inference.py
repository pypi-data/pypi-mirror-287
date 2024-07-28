import pandas as pd
import numpy as np
import joblib
from ._config import FEATURES, CONTINUOUS_FEATURES, CATEGORICAL_FEATURES
from ._config import OUTPUT_DIR

__all__ = ['make_predictions']


def load_transformers(model_dir: str):
    numeric_transformer = joblib.load(
        model_dir + 'numerical_scaler.joblib'
    )
    categorical_transformer = joblib.load(
        model_dir + 'categorical_encoder.joblib'
    )
    return numeric_transformer, categorical_transformer


def make_predictions(input_data: pd.DataFrame) -> np.ndarray:

    output_dir = OUTPUT_DIR()
    features = FEATURES()
    continuous_features = CONTINUOUS_FEATURES()
    categorical_features = CATEGORICAL_FEATURES()

    numeric_transformer, categorical_transformer = load_transformers(
        output_dir
    )

    # Load the model
    model = joblib.load(output_dir + 'model.joblib')

    # Preprocess input data

    X = input_data[features]

    X_numeric = numeric_transformer.transform(X[continuous_features])
    X_categorical = categorical_transformer.transform(X[categorical_features])
    X_final = np.concatenate([X_numeric, X_categorical], axis=1)

    # Make predictions
    predictions = model.predict(X_final)
    return predictions
