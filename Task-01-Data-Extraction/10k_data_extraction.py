import re
import json

def extract_financial_metrics(file_path):
    """Extracts key financial metrics from a 10-K text snippet."""
    with open(file_path, 'r') as file:
        text = file.read()

    # Define regex patterns to find values (looks for $ and numbers)
    patterns = {
        "Total Revenue (in millions)": r"Total Revenue of \$([0-9,]+)",
        "Operating Expenses (in millions)": r"Operating Expenses.*?\$([0-9,]+)",
        "Net Income (in millions)": r"Net Income.*?\$([0-9,]+)",
        "Diluted EPS": r"Diluted Earnings Per Share.*?\$([0-9.]+)"
    }

    extracted_data = {}
    
    for metric, pattern in patterns.items():
        match = re.search(pattern, text)
        if match:
            # Clean the extracted string (remove commas) and convert to float
            value = match.group(1).replace(',', '')
            extracted_data[metric] = float(value)
        else:
            extracted_data[metric] = None

    return extracted_data

if __name__ == "__main__":
    input_file = "mock_10k_snippet.txt"
    output_file = "extracted_metrics.json"
    
    print("Extracting data from 10-K snippet...")
    metrics = extract_financial_metrics(input_file)
    
    # Save the cleaned data to a JSON file for Task 2
    with open(output_file, 'w') as f:
        json.dump(metrics, f, indent=4)
        
    print(f"Extraction complete. Data saved to {output_file}")
    print(json.dumps(metrics, indent=4))
