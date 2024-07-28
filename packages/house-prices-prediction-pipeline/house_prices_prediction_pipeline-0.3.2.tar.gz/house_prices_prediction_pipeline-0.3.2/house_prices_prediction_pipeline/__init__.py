_is_setup_done = False
_features = None
_continuous_features = None
_categorical_features = None
_target_feature = None
_output_dir = None


def setup(features: list, continuous_features: list,
          categorical_features: list, target_feature: str, output_dir: str):
    global _is_setup_done, _features, _continuous_features
    global _categorical_features, _target_feature, _output_dir
    _features = features
    _continuous_features = continuous_features
    _categorical_features = categorical_features
    _target_feature = target_feature
    _output_dir = output_dir
    _is_setup_done = True


def check_setup():
    if not _is_setup_done:
        raise RuntimeError("Package is not set up. Call setup() first.")


def ensure_setup(func):
    def wrapper(*args, **kwargs):
        check_setup()
        return func(*args, **kwargs)
    return wrapper


@ensure_setup
def FEATURES():
    return _features


@ensure_setup
def CONTINUOUS_FEATURES():
    return _continuous_features


@ensure_setup
def CATEGORICAL_FEATURES():
    return _categorical_features


@ensure_setup
def TARGET_FEATURE():
    return _target_feature


@ensure_setup
def OUTPUT_DIR():
    return _output_dir
