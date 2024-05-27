import logging
from logging_config import setup_logging

setup_logging()

class GetGym:
    def __init__(self):
        self.url = "curefit://allgyms"
        logging.info("GetGym initialized with URL")

    def get_gym(self, query: str):
        try:
            logging.info(f"Received query: {query}")
            return f"You can see the details about gyms here: {self.url} (Scroll down to the 'cult Centers' section!)"
        except Exception as e:
            logging.error(f"Error processing query '{query}': {e}")
            return "There was an error processing your request. Please try again later."

