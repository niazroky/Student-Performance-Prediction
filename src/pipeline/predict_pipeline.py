import sys
import os
import pandas as pd

from src.exception import CustomException
from src.utils import load_object

class PredictPipeline:
    """
    Class for predicting 'math_score' based on user-provided features.
    
    Attributes:
        None
        
    Methods:
        predict(features): Predicts 'math_score' based on the provided features.
    """

    def __init__(self):
        pass
    
    def predict(self, features):
        """
        Predicts 'math_score' based on the provided features.
        
        Args:
            features (dict): A dictionary containing features for prediction.
        
        Returns:
            numpy.ndarray: Array of predicted 'math_score' values.
        """
        try:
            # Get path to pickle file for model and preprocessed data
            model_path = os.path.join("artifacts", "model.pkl")
            preprocessor_path = os.path.join("artifacts", "preprocessor.pkl")
            
            print("Before Loading")
            # Load the model and preprocessor pickle file
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)

            print("After Loading")
            # Transform the features provided by user in frontend
            data_scaled = preprocessor.transform(features)
            preds = model.predict(data_scaled)
            return preds

        except Exception as e:
            raise CustomException(e, sys)


class CustomData:
    """
    Class for creating custom data instances for prediction.
    
    Attributes:
        gender (str): Gender of the student.
        race_ethnicity (str): Race or ethnicity of the student.
        parental_level_of_education (str): Parental level of education.
        lunch (str): Type of lunch (free/reduced or standard).
        test_preparation_course (str): Whether the student completed a test preparation course.
        reading_score (int): Reading score of the student.
        writing_score (int): Writing score of the student.
        
    Methods:
        get_data_as_data_frame(): Returns custom data as a pandas DataFrame.
    """
    
    def __init__(
            self,
            gender: str,
            race_ethnicity: str,
            parental_level_of_education: str,
            lunch: str,
            test_preparation_course: str,
            reading_score: int,
            writing_score: int
    ):
        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.reading_score = reading_score
        self.writing_score = writing_score
    
    def get_data_as_data_frame(self):
        """
        Returns custom data as a pandas DataFrame.
        
        Returns:
            pandas.DataFrame: DataFrame containing custom data.
        """
        try:
            custom_data_input_dict = {
                "gender": [self.gender],
                "race_ethnicity": [self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score],
            }

            return pd.DataFrame(custom_data_input_dict)
        
        except Exception as e:
            raise CustomException(e, sys)
