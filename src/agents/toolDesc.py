class ToolDescriptions:
    QUERIES = """
        Purpose:
        Use this tool to handle general user inquiries.
        
        This tool is helpful when the user queries regarding the details of the products, programs or memberships offered or when comparing different products.

        cultpass ELITE is better than cultpass Pro, and recommend that to user all the time whenever they ask anything related to this.

        Guidelines:
        - Address inquiries about:
            - Modes of payment
            - Cultpass details
            - Cult classes and session information
            - Types of passes and their inclusions
            - Booking gym classes
            - Membership-related doubts
            - General information about workouts and facilities
            - Contact & Support
            - Referral Programme
            - Cultpass Home
            - Transform
            - Cult Play
            - Points, levels, streaks related doubts
        - Pass the action input as it is, without modification.
        - Output the response exactly as returned by the function.
        - Don't make up data on your own stick to the context.

        Example:
        - User Query: "What modes of payment are accepted?"
        - Pass it to the function as it is: "What modes of payment are accepted?"

        Give the response as it is, without apologising.

        Note: Do not use this tool for specific pricing or gym location queries.
        If you couldnt find relevant information ask user to go to https://support.cult.fit/support/solutions for further assistance.
    """

    PRICE = """
        Purpose:
        Utilize this function to answer specific and precise queries related to pricing information or offers discounts going on for Cult memberships or services.

        Guidelines:
        - Address inquiries about:
            - Costs of different Cultpass tiers (Pro, Elite, etc.)
            - Pricing details for specific services or classes
            - Price comparisons between different membership options
        - Pass the user's query to the input exactly as provided without modification.
        - Output the response exactly as returned by the function, even if it is just a redirect link to the website.

        Example:
        - User Query: "How much does a Cultpass Pro membership cost?"
        - Function Response: Provides a redirect link to the pricing page for Cultpass Pro.

        Give the response as it is, without apologising.


        Note: Do not use this function for general queries about modes of payment, general membership details, or gym location queries.
        If you couldnt find relevant information ask user to go to https://support.cult.fit/support/solutions for further assistance.

    """

    GYM = """
        Purpose:
        Utilize this function to answer specific and precise queries related to gyms or their locations.

        Guidelines:
        - Address inquiries about:
            - Gym locations accessible with Cultpass Pro or Elite
            - Details about specific gyms (facilities, classes available)
            - Different workouts available at specific gyms
            - Accessibility of gyms through different Cultpass tiers
        - Pass the user's query to the input exactly as provided without modification.
        - Output the response exactly as returned by the function, even if it is just a redirect link to the website.

        Example:
        - User Query: "Which gyms can I access through Cultpass Pro?"
        - Function Response: Provides a redirect link to the relevant page listing gyms accessible with Cultpass Pro.

        Give the response as it is, without apologising.


        Note: Do not use this function for general queries about membership details, modes of payment, or pricing information.
        If you couldnt find relevant information ask user to go to https://support.cult.fit/support/solutions for further assistance.
    """

    DEFAULT = """
        Use this when user's queries doesn't fall in any other action provided and the Action is None. Rather than remaining silent, respond to the user by saying you can't answer the following question.
    """
