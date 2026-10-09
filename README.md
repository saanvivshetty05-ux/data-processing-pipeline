
# Data Processing Pipeline

## Project Overview
This project is a Python-based data processing pipeline that reads raw data from CSV and JSON files, cleans and transforms the data, and generates structured output.

## Features
- Reads CSV and JSON files
- Handles missing values
- Converts data types
- Validates age and marks
- Removes duplicate records
- Logs processing activities
- Uses JSON configuration
- Handles errors

## Technologies Used
- Python
- CSV and JSON
- Logging
- Visual Studio Code
- Git and GitHub

## Project Structure
- main.py - Main processing program
- config.json - Configuration settings
- data/raw_students.csv - Sample input data
- data/processed_students.csv - Processed output
- logs/pipeline.log - Log file
- requirements.txt - Dependencies

## Setup Instructions
1. Install Python 3.10 or later.
2. Download or clone this repository.
3. Open the project folder in VS Code.
4. Open the terminal.
5. Run the following command:

python main.py

## Output
The program generates a cleaned CSV file with standardized values and removes duplicate records.

## Error Handling
The pipeline handles missing values, invalid numbers, out-of-range marks, and missing input files.

## Author
SAANVI V SHETTY