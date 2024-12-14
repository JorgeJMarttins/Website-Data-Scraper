# Import necessary libraries
import requests  # Used for making HTTP requests to the API
import pandas as pd  # Used for data manipulation (CSV, dataframes)

# Function to fetch data from an API
def fetch_data(api_url):
    """
    Fetches data from the provided API URL.
    Arguments:
    api_url -- the URL of the API endpoint
    
    Returns:
    response -- the response object from the API request
    """
    response = requests.get(api_url)  # Sending GET request
    if response.status_code == 200:
        return response.json()  # Returning the data in JSON format if the request is successful
    else:
        return None  # Returning None if the request fails

# Function to process data and save it to CSV
def process_and_save_data(data, file_name):
    """
    Processes the fetched data and saves it to a CSV file.
    Arguments:
    data -- the data to be processed
    file_name -- the name of the CSV file to save data
    
    Returns:
    None
    """
    df = pd.DataFrame(data)  # Convert the data to a pandas DataFrame
    df.to_csv(file_name, index=False)  # Save the DataFrame to a CSV file

# Example usage
api_url = 'https://api.example.com/data'  # API endpoint URL
data = fetch_data(api_url)  # Fetching data from the API
if data:
    process_and_save_data(data, 'data.csv')  # Processing and saving the data to a CSV file
else:
    print("Failed to fetch data from the API.")  # Printing error message if data is not fetched
