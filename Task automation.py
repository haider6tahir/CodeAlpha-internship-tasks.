
#PYTHON SCRIPT FOR AUTOMATE MY TASKS:

#ORGANISE FILES:
import os
import shutil
def organize_files(source_dir):
    # Create the target directories if they don't exist
    os.makedirs(os.path.join(source_dir, 'Images Files'), exist_ok=True)
    os.makedirs(os.path.join(source_dir, 'pdf files'), exist_ok=True)
    for filename in os.listdir(source_dir):
        if filename.endswith('.jpg'):
            shutil.move(os.path.join(source_dir, filename), os.path.join(source_dir, 'Images Files', filename))
        elif filename.endswith('.pdf'):
            shutil.move(os.path.join(source_dir, filename), os.path.join(source_dir, 'pdf files', filename))
organize_files('D:/Haider')




#DATA CLEANING:

import pandas as pd

def clean_data(file_path):
    try:
        # Load the data
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return
    except pd.errors.EmptyDataError:
        print(f"Error: The file '{file_path}' is empty.")
        return
    except pd.errors.ParserError:
        print(f"Error: The file '{file_path}' could not be parsed.")
        return

    # Remove duplicate rows
    df.drop_duplicates(inplace=True)

    # Fill missing values using forward fill
    df.ffill(inplace=True)  # Forward fill

    # Standardize column names
    df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]

    # Save the cleaned data
    cleaned_file_path = file_path.replace('.csv', '_cleaned.csv')
    try:
        df.to_csv(cleaned_file_path, index=False)
        print(f"Cleaned data saved to {cleaned_file_path}")
    except Exception as e:
        print(f"Error: Could not save the cleaned data. {e}")

# Specify the path to your CSV file
file_path = 'data.csv.csv'
clean_data(file_path)









