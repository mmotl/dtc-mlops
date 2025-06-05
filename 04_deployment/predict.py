import pickle

with open('models/lin_reg.bin', 'rb') as file:
    dv, model = pickle.load(file)

def predict(features):
    """
    Predict the target variable using the loaded model and vectorizer.
    
    :param features: A dictionary containing the features for prediction.
    :return: The predicted value.
    """
    X = dv.transform(features)
    y_pred = model.predict(X)
    return y_pred
