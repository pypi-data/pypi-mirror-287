import joblib
import numpy as np
import pandas as pd
from house_prices.preprocess import preprocess_data
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_squared_log_error
from . import OUTPUT_DIR


def compute_rmsle(
    y_test: np.ndarray,
    y_pred: np.ndarray,
    precision: int = 2
) -> str:
    rmsle = np.sqrt(mean_squared_log_error(y_test, y_pred))
    return str(round(rmsle, precision))


def build_model(data: pd.DataFrame) -> dict[str, str]:
    X_train, X_test, y_train, y_test, numeric_transformer, \
        categorical_transformer = preprocess_data(data)

    # Train the model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Save the trained model and transformers
    joblib.dump(model, OUTPUT_DIR + 'model.joblib')
    joblib.dump(numeric_transformer, OUTPUT_DIR + 'numerical_scaler.joblib')
    joblib.dump(categorical_transformer,
                OUTPUT_DIR + 'categorical_encoder.joblib')

    # Predict house prices
    predictions = model.predict(X_test)

    # Calculate RMSE
    rmse = np.sqrt(mean_squared_error(y_test, predictions))

    # Calculate RMSLE
    rmsle = compute_rmsle(y_test, predictions)

    return {'rmse': str(rmse), 'rmsle': rmsle}
