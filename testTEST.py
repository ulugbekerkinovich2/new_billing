import json
from collections import defaultdict
import pandas as pd

# Load the JSON data from the file
json_file_path = 'tavsiya_qilinganlar3.json_result.json'
with open(json_file_path, 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# Extract the list of entries
entries = data['content']

# Group entries by pinfl
groups = defaultdict(list)
for entry in entries:
    groups[entry['pinfl']].append(entry)

# Find duplicates
duplicates = {pinfl: group for pinfl, group in groups.items() if len(group) > 1}

# Create a DataFrame to display duplicates
duplicates_df = pd.DataFrame([
    {
        'PINFL': pinfl,
        'Count': len(group),
        'Entries': group
    }
    for pinfl, group in duplicates.items()
])

# Display the DataFrame to the user
import ace_tools as tools
tools.display_dataframe_to_user(name="Duplicates Grouped by PINFL", dataframe=duplicates_df)
