_is_setup_done = False
_CONFIG = {}

def setup(features, continuous_features, categorical_features, target_feature, output_dir):
    global _CONFIG, _is_setup_done
    _CONFIG = {
        "FEATURES": features,
        "CONTINIOUS_FEATURES": continuous_features,
        "CATEGORICAL_FEATURES": categorical_features,
        "TARGET_FEATURE": target_feature,
        "OUTPUT_DIR": output_dir,
    }
    _is_setup_done = True
    post_setup()

def check_setup():
    if not _is_setup_done:
        raise RuntimeError("Package is not set up. Call house_prices_prediction_pipeline.setup() first.")

def post_setup():
    print("Setup completed successfully with the following configuration:")
    print(get_config())

def get_config():
    check_setup()
    return _CONFIG

@property
def FEATURES():
    return get_config()["FEATURES"]

@property
def CONTINIOUS_FEATURES():
    return get_config()["CONTINIOUS_FEATURES"]

@property
def CATEGORICAL_FEATURES():
    return get_config()["CATEGORICAL_FEATURES"]

@property
def TARGET_FEATURE():
    return get_config()["TARGET_FEATURE"]

@property
def OUTPUT_DIR():
    return get_config()["OUTPUT_DIR"]
