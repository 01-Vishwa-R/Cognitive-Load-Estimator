import joblib

def load_models():
    return {
        "intrinsic": joblib.load("models/intrinsic_model.pkl"),
        "extraneous": joblib.load("models/extraneous_model.pkl"),
        "germane": joblib.load("models/germane_model.pkl"),
    }

def predict_load(input_data):
    models = load_models()

    intrinsic = models["intrinsic"].predict([input_data])[0]
    extraneous = models["extraneous"].predict([input_data])[0]
    germane = models["germane"].predict([input_data])[0]

    return intrinsic, extraneous, germane