# Website Data Scraper

This project demonstrates how to fetch data from an API, process it, and save it to a CSV file using Python.

## Requirements

- Python 3.x
- `requests` library for HTTP requests
- `pandas` library for data manipulation

## Installation

To install the necessary dependencies, you can use pip:
pip install requests pandas

## Usage

1. Replace `api_url` with the actual API endpoint from which you want to fetch data.
2. The script will fetch the data from the API, process it, and save it into a CSV file (`data.csv` by default).

### Example Code

```python
api_url = 'https://api.example.com/data'  # API endpoint URL
data = fetch_data(api_url)  # Fetching data from the API
if data:
    process_and_save_data(data, 'data.csv')  # Processing and saving the data to a CSV file
else:
    print("Failed to fetch data from the API.")  # Printing error message if data is not fetched
