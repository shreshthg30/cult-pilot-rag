import logging
import streamlit as st
import time
import re
from logging_config import setup_logging
from src.agents.cultRagAgent import CultAgentExecutor

setup_logging()

def get_or_create_agent():
    if 'agent' not in st.session_state:
        try:
            cult_agent_executor_instance = CultAgentExecutor()
            st.session_state['agent'] = cult_agent_executor_instance.get_executor()
            logging.info("Agent created and stored in session state")
        except Exception as e:
            logging.error(f"Error creating agent: {e}")
            st.error("There was an error initializing the agent. Please refresh the page to try again.")
            return None
    return st.session_state.get('agent', None)

def clean_input(sentence):
    try:
        sentence = sentence.lower()
        sentence = re.sub(r'[^\w\s]', '', sentence)
        sentence = ' '.join(sentence.split())
        logging.info("Input cleaned successfully")
        return sentence
    except Exception as e:
        logging.error(f"Error cleaning input: {e}")
        st.error("There was an error cleaning the input. Please try again.")
        return sentence

st.title("Customer Service Chatbot")
st.write("Welcome to our customer service chatbot. Please type your question below and click 'Submit' to get an answer.")

question = st.text_input("Question", placeholder="Type your question here...", help="Enter any queries you have and press submit.")


executor = get_or_create_agent()

if st.button('Submit') and question:
    start_time = time.time()
    with st.spinner('Searching for your answer...'):
        cleaned_question = clean_input(question)
        if cleaned_question:
            answer = executor.invoke({"input": cleaned_question})
            # print(st.session_state.chat_history)
            st.text_area("Answer", value=answer['output'], height=300, disabled=True)
            logging.info("Answer processed and displayed")
        else:
            st.error("Please enter a valid question.")
    end_time = time.time()
    execution_time = end_time - start_time
    st.success(f"Execution time: {execution_time:.2f} seconds")