import logging
from logging_config import setup_logging
import os
import dotenv
from langchain_community.llms import Ollama
from langchain_groq import ChatGroq
from langchain.prompts import (
    PromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    ChatPromptTemplate,
    MessagesPlaceholder,
)
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough
from src.retriever.create_retriever import CreateRetriever
from src.chains.config import CHAT_MODEL_NAME, CULT_TEMPLATE_STR
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables import ConfigurableFieldSpec



setup_logging()

class CultFAQChain:
    def __init__(self):
        try:
            dotenv.load_dotenv()

            self.store = {}
            self.chat_model = ChatGroq(groq_api_key=os.getenv('GROQ_API_KEY'), model_name=CHAT_MODEL_NAME)
            # self.chat_model = Ollama(model="mistral")
            self.answers_retriever = CreateRetriever().get_retriever()
            self.cult_system_prompt = SystemMessagePromptTemplate(
                prompt=PromptTemplate(
                    input_variables=["context"],
                    template=CULT_TEMPLATE_STR,
                )
            )

            self.cult_human_prompt = HumanMessagePromptTemplate(
                prompt=PromptTemplate(
                    input_variables=["question"],
                    template="{question}",
                )
            )

            self.messages = [self.cult_system_prompt, self.cult_human_prompt]

            self.cult_prompt_template = ChatPromptTemplate(
                input_variables=["context", "question"],
                messages=self.messages,
            )

            self.cult_faq_chain = self.create_faq_chain()
            logging.info("CultFAQChain initialized successfully")
        except Exception as e:
            logging.error(f"Error initializing CultFAQChain: {e}")
            raise


    def create_faq_chain(self):
        try:
            faq_chain = {
                "context": self.answers_retriever,
                "question": RunnablePassthrough()
            } | self.cult_prompt_template | self.chat_model | StrOutputParser()
            return faq_chain
        except Exception as e:
            logging.error(f"Error creating FAQ chain: {e}")
            raise

    # def get_session_history(self, user_id: str, conversation_id: str) -> BaseChatMessageHistory:
    #     if (user_id, conversation_id) not in self.store:
    #         self.store[(user_id, conversation_id)] = ChatMessageHistory()
    #     return self.store[(user_id, conversation_id)]

    def get_chain(self):
        try:
            return self.cult_faq_chain
        except Exception as e:
            logging.error(f"Error retrieving FAQ chain: {e}")
            raise

    def invoke_chain(self, query:str): 
        response = self.cult_faq_chain.invoke({"input": query})
        return response
