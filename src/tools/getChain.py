import logging
from logging_config import setup_logging
from src.chains.cultFaqChain import CultFAQChain


setup_logging()

class GetChain:
    def __init__(self):
        self.chain_instance = CultFAQChain();
        self.chain = self.chain_instance.get_chain();
        logging.info(f"Chain Initialised successfully")

    def get_chain(self, query: str):
        try:
            logging.info(f"Received query: {query}")
            response = self.chain.invoke(query)
            return response
        except Exception as e:
            logging.error(f"Error processing query '{query}': {e}")
            return "There was an error processing your request. Please try again later."

