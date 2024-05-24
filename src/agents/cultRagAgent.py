import logging
import dotenv
import os
from logging_config import setup_logging
from langchain.agents import create_react_agent, Tool, AgentExecutor
from langchain.tools import StructuredTool
from langchain.pydantic_v1 import BaseModel, Field
from langchain import hub
from langchain_community.llms import Ollama
from langchain_groq import ChatGroq
from src.agents.toolDesc import ToolDescriptions
from src.tools.getPrice import PriceRetriever
from src.tools.getGym import GetGym
from src.chains.cultFaqChain import CultFAQChain
from src.tools.getDefault import GetDefault
from src.agents.config import AGENT_MODEL, AGENT_PROMPT,CHAT_MODEL_NAME
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

setup_logging()

dotenv.load_dotenv()


class CultAgentExecutor:
    def __init__(self):
        try:
            self.cult_faq_chain = CultFAQChain()
            self.gym_instance = GetGym()
            self.price_instance = PriceRetriever()
            self.default_instance = GetDefault()

            self.tools = [
                StructuredTool.from_function(
                    name="Queries",
                    func=self.cult_faq_chain.invoke_chain,
                    description=ToolDescriptions.QUERIES,
                ),
                StructuredTool.from_function(
                    name="Price",
                    func=self.price_instance.get_price,
                    description=ToolDescriptions.PRICE
                ),
                StructuredTool.from_function(
                    name="Gym",
                    func=self.gym_instance.get_gym,
                    description=ToolDescriptions.GYM
                ),
                # Tool(
                #     name="Default",
                #     func=self.default_instance.get_default,
                #     description=ToolDescriptions.DEFAULT
                # )
            ]

            self.agent_prompt = hub.pull(AGENT_PROMPT)


            self.prompt = ChatPromptTemplate.from_messages(
                [
                    (
                        "system",
                        "You are very powerful assistant. Based on the history and context provided answer the questions.",
                    ),

                    MessagesPlaceholder(variable_name="chat_history"),

                    ("user", "Answer the following questions as best you can form the context. You have access to the following tools:\n\n{tools}\n\nUse the following format:\n\nQuestion: the input question you must answer\nThought: you should always think about what to do\nAction: the action to take, should be one of [{tool_names}]\nAction Input: the input to the action\nObservation: the result of the action\n... (this Thought/Action/Action Input/Observation can repeat N times)\nThought: I now know the final answer\nFinal Answer: the final answer to the original input question without apologising, repsond with whatever the tools provide.\n\nBegin!\n\nQuestion: {input}\nThought:{agent_scratchpad}"),
                ]
            )

            # self.agent_chat_model = Ollama(model=AGENT_MODEL)
            self.agent_chat_model = ChatGroq(groq_api_key=os.getenv('GROQ_API_KEY'), model_name=CHAT_MODEL_NAME)
            
            self.cult_agent = self.create_agent()
            self.cult_agent_executor = self.create_executor()
            logging.info("CultAgentExecutor initialized successfully")
        except Exception as e:
            logging.error(f"Error initializing CultAgentExecutor: {e}")
            raise

    def create_agent(self):
        try:
            agent = create_react_agent(
                llm=self.agent_chat_model,
                prompt=self.prompt,
                tools=self.tools,
            )

            logging.info("React agent created successfully")
            return agent
        except Exception as e:
            logging.error(f"Error creating React agent: {e}")
            raise

    def create_executor(self):
        try:
            executor = AgentExecutor(
                agent=self.cult_agent,
                tools=self.tools,
                return_intermediate_steps=False,
                verbose=True,
                handle_parsing_errors=True
            )
            logging.info("AgentExecutor created successfully")
            return executor
        except Exception as e:
            logging.error(f"Error creating AgentExecutor: {e}")
            raise

    def get_executor(self):
        try:
            return self.cult_agent_executor
        except Exception as e:
            logging.error(f"Error getting AgentExecutor: {e}")
            raise
