import pickle


# Load trained model
model = pickle.load(open("crop_model.pkl", "rb"))


def predict_crop(
    nitrogen,
    phosphorus,
    potassium,
    temperature,
    humidity,
    ph,
    rainfall
):

    prediction = model.predict(
        [[
            nitrogen,
            phosphorus,
            potassium,
            temperature,
            humidity,
            ph,
            rainfall
        ]]
    )

    return prediction[0]