import pandas as pd
import json

# Load the Excel file
excel_file = '/home/ubuntu/upload/INCOMEFORLIFEREPORT.xlsx'

# Get sheet names
xl = pd.ExcelFile(excel_file)
sheet_names = xl.sheet_names
print(f"Sheet names: {sheet_names}")

# Analyze each sheet
sheets_data = {}
for sheet in sheet_names:
    try:
        # Read the sheet
        df = pd.read_excel(excel_file, sheet_name=sheet)
        
        # Get basic info
        sheets_data[sheet] = {
            "columns": list(df.columns),
            "shape": df.shape,
            "sample_data": df.head(5).to_dict(orient='records')
        }
        
        print(f"\nSheet: {sheet}")
        print(f"Columns: {sheets_data[sheet]['columns']}")
        print(f"Shape: {sheets_data[sheet]['shape']}")
        print("Sample data:")
        print(df.head(5))
    except Exception as e:
        print(f"Error reading sheet {sheet}: {e}")

# Save the analysis to a JSON file for reference
with open('/home/ubuntu/income_planner/excel_analysis.json', 'w') as f:
    json.dump(sheets_data, f, indent=2, default=str)

print("\nAnalysis saved to excel_analysis.json")

