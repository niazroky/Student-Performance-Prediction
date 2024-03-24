import os
import sys

from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

# from src.components.model_trainer import ModelTrainerConfig
# from src.components.model_trainer import ModelTrainer



@dataclass
class DataIngestConfig:
    """
    Data class to hold configuration settings for data ingestion.

    Attributes:
        train_data_path (str): Path to the training data file.
        test_data_path (str): Path to the testing data file.
        raw_data_path (str): Path to the raw data file.
    """
    train_data_path: str=os.path.join("artifacts", "train.csv")
    test_data_path: str=os.path.join("artifacts", "test.csv")
    raw_data_path: str=os.path.join("artifacts", "data.csv")

class DataIngestion:
    """
    Class for handling data ingestion process.

    Methods:
        __init__(): Initializes DataIngestion class.
        initiate_data_ingestion(): Initiates the data ingestion process.
    """
    def __init__(self):
        """
        Initializes DataIngestion class.
        
        Attributes:
            ingestion_config (DataIngestConfig): Configuration settings for data ingestion.
        """
        self.ingestion_config=DataIngestConfig()

    def initiate_data_ingestion(self):
        """
        Initiates the data ingestion process.

        Reads the dataset, splits it into training and testing sets, and saves them to CSV files.

        Returns:
            Tuple[str, str]: Paths to the training and testing data files.
        """
        # Log entry into the data ingestion method
        logging.info("Entered the data ingestion method or component")

        try:
            # Read dataset from CSV file
            df = pd.read_csv("notebook\data\stud.csv")
            logging.info("Read the dataset as dataframe")

            # Create directories for storing ingested data if they do not exist
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            # Save raw dataset to CSV file
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            # Perform train-test split
            logging.info("Train test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            # Save training and testing sets to CSV files
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            # Log completion of data ingestion
            logging.info("Ingestion of the data is completed")

            # Return paths to training and testing data files
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            # If an exception occurs during data ingestion, raise CustomException
            raise CustomException(e, sys)



if __name__ == "__main__":
    # Create instance of DataIngestion class and initiate data ingestion process
    obj=DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()

    data_transformation = DataTransformation()
    data_transformation.initiate_data_transformation(train_data, test_data)

