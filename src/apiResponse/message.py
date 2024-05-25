def apiMessage(query_type: str, response: str) -> str:
    response_map = {
        "Gym": "You can follow the given link.",
        "Price": "You can follow the given link.",
        "Queries": response,
        "Default": response
    }

    if query_type in response_map:
        return response_map[query_type]
    else:
        raise ValueError("Invalid query type provided.")
