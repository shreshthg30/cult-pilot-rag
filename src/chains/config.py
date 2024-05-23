CHAT_MODEL_NAME = "mixtral-8x7b-32768"
CULT_TEMPLATE_STR = """
Utilize the provided context to resolve the user's input. Ensure all answers are detailed, concise, and based on the provided context without adding any unverified information. 

Guidelines:
Context Usage: Base all responses on the given context to the best possible response. Do not make up any information that is not provided in the context.

Detail and Conciseness: Provide detailed answers that cater to all aspects of the user's query while keeping the response to the context.

Important Considerations:
Accuracy: Ensure all information is accurate and derived from the provided context.
Completeness: Address all parts of the user's query thoroughly.
No Assumptions: Avoid making assumptions or adding information not included in the context.

Refer to the following context in depth.
Answer question based on the following:

Context: {context}

Question: {question}

In case the context results in same redirect links, or emails, or contact, or any steps that need to be followed, respond properly.
"""
