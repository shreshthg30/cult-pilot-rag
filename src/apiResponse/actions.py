def apiAction(query_type: str):
    action_map = {
        "Gym": {"url": "https://www.cult.fit/gym", "actionType": "NAVIGATION", "title": "goto"},
        "Price": {"url": "https://www.cult.fit/pricing", "actionType": "NAVIGATION", "title": "goto"},
        "Queries": {"url": "https://www.cult.fit/help", "actionType": "NAVIGATION", "title": "goto"},
        "Default": {"url": "https://www.cult.fit", "actionType": "NAVIGATION", "title": "goto"}
    }
    default_action = {"url": "https://www.cult.fit", "actionType": "NAVIGATION", "title": "goto"}
    action = action_map.get(query_type, default_action)
    return [action]
