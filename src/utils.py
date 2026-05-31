import os
import sys

import numpy as np
import pandas as pd
import dill
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV
from src.exception import CustomException


def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
    
'''
1. file_path → where you want to save the object.
2. obj → the object you want to save (model, preprocessor, scaler, etc.).
3. os.path.dirname() extracts the folder name from the complete path.
4. Why is this useful in an ML project?
    -After training:
    preprocessor = ColumnTransformer(...)
    model = RandomForestRegressor(...)

    -You don't want to retrain every time.

    -So you save them:
    save_object(
        "artifacts/preprocessor.pkl",
        preprocessor
    )

    save_object(
        "artifacts/model.pkl",
        model
    )
'''

def evaluate_models(X_train,y_train,X_test,y_test,models):
    try:
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]

            model.fit(X_train,y_train)

            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)

            train_model_accuracy = r2_score(y_train, y_train_pred)
            test_model_accuracy = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_model_accuracy

        return report
    except Exception as e:
        raise CustomException(e,sys)

