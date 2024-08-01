# add_turnout_tier function

def add_turnout_tier(df, numeric_column):
    """
    Adds a new categorical column 'turnout_tier' to the DataFrame based on the numeric_column.

    Parameters:
    df (pandas.DataFrame): The DataFrame containing the numeric column.
    numeric_column (str): The name of the numeric column to base the 'turnout_tier' on.

    Returns:
    pandas.DataFrame: The DataFrame with the new 'turnout_tier' column added.

    Turnout Tier Criteria:
    - > 80: "Very likely to vote regardless of campaign"
    - 70-79: "Turnout Tier 1"
    - 50-69: "Turnout Tier 2"
    - 30-59: "Turnout Tier 3"
    - < 30: "Very unlikely to vote regardless of campaign"

    Example:
    >>> data = {'voter_score': [85, 75, 60, 45, 25]}
    >>> df = pd.DataFrame(data)
    >>> df = add_turnout_tier(df, 'voter_score')
    >>> print(df)
       voter_score                                      turnout_tier
    0           85  Very likely to vote regardless of campaign
    1           75                                     Turnout Tier 1
    2           60                                     Turnout Tier 2
    3           45                                     Turnout Tier 3
    4           25  Very unlikely to vote regardless of campaign
    """
    def categorize_turnout(value):
        if value > 80:
            return "Very likely to vote regardless of campaign"
        elif 70 <= value <= 79:
            return "Turnout Tier 1"
        elif 50 <= value <= 69:
            return "Turnout Tier 2"
        elif 30 <= value <= 59:
            return "Turnout Tier 3"
        else:
            return "Very unlikely to vote regardless of campaign"

    df['turnout_tier'] = df[numeric_column].apply(categorize_turnout)
    return df

# Example usage:
# data = {
#     'voter_score': [85, 75, 60, 45, 25]
# }
# df = pd.DataFrame(data)
# df = add_turnout_tier(df, 'voter_score')
# print(df)
