def apiAction(query_type: str):
    action_map = {
        "Gym": {"url": "curefit://allgyms", "actionType": "NAVIGATION", "title": "goto"},
        "Price": {"url": "curefit://fl_listpage?pageId=Elite_lp_sale&hideTitle=true", "actionType": "NAVIGATION", "title": "goto"},
        "Queries": {"url": "curefit://fl_support", "actionType": "NAVIGATION", "title": "goto"},
        "Default": {"url": "curefit://fl_support", "actionType": "NAVIGATION", "title": "goto"}
    }
    default_action = {"url": "https://www.cult.fit", "actionType": "NAVIGATION", "title": "goto"}
    action = action_map.get(query_type, default_action)
    return [action]
