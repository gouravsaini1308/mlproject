'''
The main purpose of the data transformation is basically to do feature engineering 
plus data cleaning.If we really want to change some of the data set, convert 
categorical features into a numerical features
'''

import sys
import os
import pandas as pd
import numpy as np

from dataclasses import dataclass
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from src.exception import CustomException
from src.logger import logging
from src.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts', "preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()  ## The purpose of creating:
        ## Is to make the configuration values available throughout the DataTransformation class.

    def get_data_transformer_object(self):
        '''
        This function is responsible of data transformation
        This is just to create all pickle files, which will basically be 
        responsible for converting categorical into numerical. It will also 
        probably perform standard scalar and all.
        '''
        try:
            numericals_columns = ['writing_score', 'reading_score']
            categorical_columns = [
                'gender',
                'race_ethnicity',
                'parental_level_of_education',
                'lunch',
                'test_preparation_course'
            ]

            num_pipleline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy='median')),  ## Missing value is handled where
                    ("scaler", StandardScaler())
                ]
            )

            cat_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy='most_frequent')),  ## Missing value is handled where
                    ("one_hot_encoder", OneHotEncoder()),
                    ("scaler", StandardScaler(with_mean=False))
                ]
            )

            logging.info(f"Numerical columns: {numericals_columns}")
            logging.info(f"categorical columns: {categorical_columns}")

            preprocessor = ColumnTransformer(
                [
                    ("num_pipeline", num_pipleline, numericals_columns),
                    ("cat_pipeline", cat_pipeline, categorical_columns)
                ]
            )

            return preprocessor

        except Exception as e:
            raise CustomException(e,sys)
            
    def initiate_data_transformation(self,train_path,test_path):
        ## That basically means I'm starting my data transformation inside this function.

        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("Read train and test data completed")

            preprocessing_obj = self.get_data_transformer_object()

            target_column_name = 'math_score'
            numerical_columns = ['writing_score', 'reading_score']

            input_feature_train_df = train_df.drop(columns=[target_column_name],axis=1)
            target_feature_train_df = train_df[target_column_name]

            input_feature_test_df = test_df.drop(columns=[target_column_name], axis=1)
            target_feature_test_df = test_df[target_column_name]

            logging.info(
                f"Appling preprocessing object on training dataframe and testing dataframe"
            )

            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)

            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]

            test_arr = np.c_[
                input_feature_test_arr, np.array(target_feature_test_df)
            ]
            '''
            np.c_ is a NumPy utility used to concatenate arrays column-wise (along the second axis).
            It is commonly used to combine multiple 1-D or 2-D arrays into a single matrix.
            '''

            logging.info("Saved preprocessing object")

            save_object(
                file_path = self.data_transformation_config.preprocessor_obj_file_path,
                obj = preprocessing_obj
            )

            return(
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path
            )

        except Exception as e:
            raise CustomException(e,sys)
        


