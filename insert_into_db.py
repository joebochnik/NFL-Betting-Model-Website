import pandas as pd
from sqlalchemy import create_engine

# Database connection setup
engine = create_engine('mysql+pymysql://root:Trooper2311@localhost/betting_model')

# Load the Excel file
file_path = '2024_picks_summary_0.8-final.xlsx'

# Read all sheets; returns a dict of DataFrames
data = pd.read_excel(file_path, sheet_name=None)

# Define a mapping of Excel column names to database column names
column_mapping = {
    'team_home': 'home_team',
    'team_away': 'away_team',
    'spread':'spread',
    'team':'pick',
    'score_home':'home_score',
    'score_away': 'away_score',
    'probability': 'probability',
}



# Loop over the dictionary to process each sheet
week = 1
for sheet_name, df in data.items():
    if week == 19:
        break
    default_values = {
        'week': week,  # Example
        'season': 2024  # Assuming 'spread' is a DB column not in Excel and needs a default
    }
    print(f"Processing sheet: {sheet_name}")

    # Rename columns based on the mapping
    df.rename(columns=column_mapping, inplace=True)

    # Using .assign() to add default values. It will add new columns or replace them if they already exist.
    df = df.assign(**default_values)

    # Ensure the DataFrame only contains the columns that exist in the database
    df = df[list(column_mapping.values()) + list(default_values.keys())]  # Adding keys of default values to ensure they are included


    df.dropna(inplace=True)
    # Print the DataFrame to understand what data looks like if needed
    print(df.head())

    # Insert the data into the database
    df.to_sql('ATSPicks', con=engine, if_exists='append', index=False)
    week+=1
    print(f"Data from sheet {sheet_name} inserted into database.")
    

# Optional: confirm completion
print("All sheets have been processed and data inserted.")
