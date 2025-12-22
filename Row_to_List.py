"""
Column A List Formatter (Excel & CSV)
------------------------------------
Uploads an Excel or CSV file in Google Colab,
extracts values from Column A (A2:A),
removes blanks and duplicates,
and prints a formatted Python list.
"""


import pandas as pd
from google.colab import files

# Step 1: Choose file (click upload)
uploaded = files.upload()
file_name = next(iter(uploaded))

# Step 2: Read file based on extension
if file_name.lower().endswith(('.xlsx', '.xls')):
    df = pd.read_excel(file_name, header=None)
elif file_name.lower().endswith('.csv'):
    df = pd.read_csv(file_name, header=None)
else:
    raise ValueError("❌ Unsupported file format. Upload Excel or CSV only.")

# Step 3: Take Column A, skip first row (A2:A)
values = (
    df.iloc[1:, 0]   # Column A from row 2
      .dropna()
      .astype(str)
      .unique()
      .tolist()
)

# Step 4: Formatting
VALUES_PER_LINE = 5  # change as needed

print("\nList = [")
for i in range(0, len(values), VALUES_PER_LINE):
    print(
        "    " +
        ", ".join(f"'{v}'" for v in values[i:i + VALUES_PER_LINE]) +
        ","
    )
print("]")
