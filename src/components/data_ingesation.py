import os
import sys
from src.exception import CustomException
from src.logger import logging

import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    
    train_data_path: str= os.path.join('artifacts','train.csv')
    test_data_path: str=os.path.join('artifacts','test.csv')
    raw_data_path: str=os.path.join('artifacts','raw.csv')

class DataIngestion:
    def __init__ (self):
   
        self.ingestion_config = DataIngestionConfig()

    def initiate_dataIngesation(self):

        logging.info("Enetered the data ingestion method")

        try:

            data = pd.read_csv('Notebook/data/data.csv')
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)
            data.to_csv(self.ingestion_config.raw_data_path,index= False,header=True)

            logging.info("Train Test split initiated")

            train,test = train_test_split(data,test_size= 0.2,random_state=42)

            train.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Ingestion of data is completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__ == "__main__":
    obj = DataIngestion()
    train,test = obj.initiate_dataIngesation()

