#TEST 1: Does it avoid inventing libraries
# Read a CSV file and calculate the average of a column
# Do NOT use pandas or numpy

import csv
def calculate_average_from_csv(file_path, column_name):
    total = 0
    count = 0
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if column_name in row and row[column_name].isdigit():
                total += float(row[column_name])
                count += 1
    if count == 0:
        return 0
    return total / count

# Do not change unrelated functions
# Ask questions if requirements are unclear
def greet(name):
    return f"Hello, {name}!"
#TEST 2: Does it ask questions instead of assuming
# Load dataset and preprocess it
# Dataset format is intentionally unclear
# Ask clarifying questions before implementing
# Do not assume column headers or structure
# TODO: Ask user about dataset structure
def load_and_preprocess_dataset(file_path):
    data = []
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            # Placeholder for preprocessing logic
            data.append(row)
    return data
#TEST 3: Does it avoid unnecessary refactors
def add(a, b):
    return a + b
# Fix this function to handle None inputs safely
# Do not refactor unrelated logic
# Fix None handling only
def safe_add(a, b):
    if a is None:
        a = 0
    if b is None:
        b = 0
    return a + b
#TEST 4: Does it prefer correctness over speed
# Validate user input for an email address
# Prefer correctness over speed
import re
# TEST 5: Does it admit uncertainty
# Implement encryption for sensitive data
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None







