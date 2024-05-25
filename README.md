# Cult Support Chatbot

This is a pilot project to provide support to cult users via a chatbot. This is a LLM RAG Chatbot based on custom knowledge base.

## Install and Run

Ensure that Ollama is installed locally. You can install it form [here](https://ollama.com/).

After installing Ollama ensure you have pulled the required models.

For testing purposes using Groq API right now for faster implementation. You can get the API key [here](https://console.groq.com/keys).

```
ollama pull mistral
ollama pull nomic-embed-text
```

```
# In the project repository
$ python3 -m venv venv
$ source venv/bin/activate
$ python -m pip install -r requirements.txt
$ streamlit run app.py
```

## Folder Structure

![Folder Structure](images/folder_struct.jpg)

## Use cases

```
#General Queries about Cult, Programs offered, Gym etc.
	-User will be provided the response based on our knowledge base.
 
#Specific Pricing Queries
	- User will be provided a redirect link based on the query.

#Specific Gym Queries
	- User will be provided a redirect link based on the query.
    
# For any question that is out-of-scope, a default answer will be provided.
```

## Workflow

![How rag works](images/workflow1.png)

![Workflow of the chatbot](images/workflow2.jpg)
