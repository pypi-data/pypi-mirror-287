from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
import numpy as np
from . import CONTINIOUS_FEATURES, CATEGORICAL_FEATURES, TARGET_FEATURE


def preprocess_data(dataset_raw):
    # Define features
    continuous_features = CONTINIOUS_FEATURES
    categorical_features = CATEGORICAL_FEATURES

    # Split the data into train and test sets
    train_data, test_data = train_test_split(
        dataset_raw, test_size=0.2, random_state=42
    )

    # Preprocess continuous features
    X_train_cont, X_test_cont, imputer_cont, scaler = preprocess_cont_features(
        train_data, test_data, continuous_features
    )

    # Preprocess categorical features
    X_train_cat, X_test_cat, imputer_cat, encoder = preprocess_cat_features(
        train_data, test_data, categorical_features
    )

    # Combine processed features
    X_train_processed = np.hstack((X_train_cont, X_train_cat))
    X_test_processed = np.hstack((X_test_cont, X_test_cat))

    # Extract target variable
    y_train = train_data[TARGET_FEATURE]
    y_test = test_data[TARGET_FEATURE]

    return (
        X_train_processed,
        X_test_processed,
        y_train,
        y_test,
        scaler,
        encoder
    )


def preprocess_cont_features(X_train, X_test, continuous_features):
    imputer_cont = SimpleImputer(strategy='median')
    scaler = StandardScaler()

    imputer_cont.fit(X_train[continuous_features])
    X_train_cont_imputed = imputer_cont.transform(X_train[continuous_features])
    X_test_cont_imputed = imputer_cont.transform(X_test[continuous_features])

    scaler.fit(X_train_cont_imputed)
    X_train_cont = scaler.transform(X_train_cont_imputed)
    X_test_cont = scaler.transform(X_test_cont_imputed)

    return X_train_cont, X_test_cont, imputer_cont, scaler


def preprocess_cat_features(X_train, X_test, categorical_features):
    imputer_cat = SimpleImputer(strategy='most_frequent')
    encoder = OneHotEncoder(handle_unknown='ignore', sparse_output=False)

    imputer_cat.fit(X_train[categorical_features])
    X_train_cat_imputed = imputer_cat.transform(X_train[categorical_features])
    X_test_cat_imputed = imputer_cat.transform(X_test[categorical_features])

    encoder.fit(X_train_cat_imputed)
    X_train_cat = encoder.transform(X_train_cat_imputed)
    X_test_cat = encoder.transform(X_test_cat_imputed)

    return X_train_cat, X_test_cat, imputer_cat, encoder
