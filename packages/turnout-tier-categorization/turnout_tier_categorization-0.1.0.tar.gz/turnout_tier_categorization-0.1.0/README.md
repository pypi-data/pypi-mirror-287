# Turnout Tier Categorization

This Python script contains a function `add_turnout_tier` that adds a new categorical column called `turnout_tier` to a pandas DataFrame. The categorization is based on the values in a specified numeric column.

## Function Description

### `add_turnout_tier`

Adds a new categorical column `turnout_tier` to the DataFrame based on the specified numeric column.

#### Parameters:

- `df` (pandas.DataFrame): The DataFrame containing the numeric column.
- `numeric_column` (str): The name of the numeric column to base the `turnout_tier` on.

#### Returns:

- pandas.DataFrame: The DataFrame with the new `turnout_tier` column added.

### Turnout Tier Criteria:

- **> 80**: "Very likely to vote regardless of campaign"
- **70-79**: "Turnout Tier 1"
- **50-69**: "Turnout Tier 2"
- **30-59**: "Turnout Tier 3"
- **< 30**: "Very unlikely to vote regardless of campaign"

## Usage

### Example

```python
import pandas as pd

# Define the function
def add_turnout_tier(df, numeric_column):
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

# Example usage
data = {
    'voter_score': [85, 75, 60, 45, 25]
}
df = pd.DataFrame(data)
df = add_turnout_tier(df, 'voter_score')
print(df)
