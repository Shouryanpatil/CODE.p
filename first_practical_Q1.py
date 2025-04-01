import re
import os

# Define pattern
pattern = r'[a-z]\s+\(\s*\d+\s*\)\s+[A-Z]+\s+\d+'

# Define file path
file_path = r"D:\SJP\Clg\Practical\SY Bioinformatics\Transcriptomics and Proteomics\motif_1.txt"

# Check if file exists
if not os.path.exists(file_path):
    print("Error: File not found! Check the file path.")
else:
    # Open file with UTF-8 encoding
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        matches = re.findall(pattern, text)

    # Print matches
    for match in matches:
        print(match)
