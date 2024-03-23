import sys
from src.logger import logging  # Import the logging module for error logging

def error_message_detail(error, error_detail: sys):
    """
    Generate a detailed error message including filename, line number, and error message.
    
    Args:
        error (Exception): The exception object.
        error_detail (sys): System-specific details of the error.
        
    Returns:
        str: Detailed error message.
    """
    _, _, exc_tb = error_detail.exc_info()  # Get information about the last exception that occurred
    file_name = exc_tb.tb_frame.f_code.co_filename  # Extract the filename where the error occurred
    error_message = f"Error occurred in Python script name [{file_name}] line number [{exc_tb.tb_lineno}] error message [{str(error)}]"

    return error_message


class CustomException(Exception):
    """
    Custom exception class with detailed error logging.
    """
    def __init__(self, error_message, error_detail: sys):
        """
        Initialize the CustomException object.
        
        Args:
            error_message (str): The error message.
            error_detail (sys): System-specific details of the error.
        """
        super().__init__(error_message)  # Call the superclass constructor
        self.error_message = error_message_detail(error_message, error_detail=error_detail)  # Generate detailed error message

    def __str__(self):
        """
        Return the error message as a string.
        
        Returns:
            str: Error message.
        """
        return self.error_message
