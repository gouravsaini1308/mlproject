import os
import sys
import pandas as pd
from src.exception import customException
from src.logger import logging


from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class dataingestionconfig:
    train_data_path: str=os.path.join('artifacts',"train.csv")
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"raw.csv")

    '''
    These are the input that we are giving to data ingestion config and now data
    data ingestion component knwo where to save the train data, test data and 
    raw data
    '''

class dataingestion:
    def __init__(self):
        self.ingestion_config = dataingestionconfig()

    def initiate_data_ingestion(self):
        logging.info("Enter the data ingestion method or component")
        try:

            ## Read the dataset from anywhere, where we have read it from csv file
            df = pd.read_csv('notebook/data/stud.csv')
            logging.info("Read the dataset as dataframe")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            logging.info("Train Test split initiated")

            train_set,test_set = train_test_split(df, test_size=0.2, random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True) 
            logging.info("Ingestion of the data is completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise customException(e,sys)


if __name__== "__main__":
    obj=dataingestion()
    obj.initiate_data_ingestion()
