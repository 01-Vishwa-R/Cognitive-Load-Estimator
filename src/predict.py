import joblib

def load_models():
    return {
        "intrinsic": joblib.load("models/intrinsic.pkl"),
        "extraneous": joblib.load("models/extraneous.pkl"),
        "germane": joblib.load("models/germane.pkl"),
    }

def predict_load(input_data):
    models = load_models()

    intrinsic = models["intrinsic"].predict([input_data])[0]
    extraneous = models["extraneous"].predict([input_data])[0]
    germane = models["germane"].predict([input_data])[0]

    return intrinsic, extraneous, germane