import os
import sys

import numpy as np
import pandas as pd
import dill
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