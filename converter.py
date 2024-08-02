import pandas as pd
import json
import os

def fix_photo_url(url):
    # Replace double slashes with a single slash, except for the "http://" or "https://"
    return url.replace('//', '/').replace("'/\'", "'/")

def excel_to_json(excel_file_path, json_file_path):
    # Check if the file exists
    if not os.path.exists(excel_file_path):
        print(f"Error: The file {excel_file_path} does not exist.")
        return

    # Read the Excel file
    df = pd.read_excel(excel_file_path)

    # Fix the Photo URLs
    # if 'Photo' in df.columns:
    #     df['Photo'] = df['Photo'].apply(fix_photo_url)

    # Convert the DataFrame to a JSON string with non-ASCII characters preserved
    json_data = df.to_json(orient='records', force_ascii=False, indent=4)

    # Save the JSON string to a file
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json_file.write(json_data)

    print(f'Excel file has been converted to JSON and saved as {json_file_path}')

# Define the file paths
# excel_file_path = '1719214006811.xls'  # or 'your_excel_file.xls'
# json_file_path = '1719214006811.json'

# # Convert Excel to JSON
# excel_to_json(excel_file_path, json_file_path)
