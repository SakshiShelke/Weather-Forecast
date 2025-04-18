import pandas as pd
import random
from datetime import datetime, timedelta
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Function to handle the Google Sheets API authentication with the updated JSON filename
def authenticate_google_sheets():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("weather-forecast-456611-cb8ce5579c6c.json", scope)
    client = gspread.authorize(creds)
    return client

# Function to handle the synthetic data generation without Date column
def generate_synthetic_data():
    # Define the specific dates you want to cycle through
    specific_dates = ['2025-04-12', '2025-04-13', '2025-04-11', '2025-04-10']
    
    # Create a list to store the generated data
    synthetic_data = []
    
    # Loop to generate 100 rows
    for i in range(100):
        date = specific_dates[i % len(specific_dates)]  # Cycle through the specific dates
        
        # Generate random values for the weather attributes
        min_temp = round(random.uniform(5.0, 15.0), 1)
        max_temp = round(random.uniform(16.0, 30.0), 1)
        temp = round(random.uniform(min_temp, max_temp), 1)
        humidity = random.randint(30, 80)
        pressure = round(random.uniform(1000, 1030), 1)
        
        # Append the generated row to the list
        synthetic_data.append([date, min_temp, max_temp, temp, humidity, pressure])
    
    # Convert the list of data to a pandas DataFrame
    df = pd.DataFrame(synthetic_data, columns=['Date', 'MinTemp', 'MaxTemp', 'Temp', 'Humidity', 'Pressure'])
    return df

# Function to update Google Sheets (assuming the credentials file and Google Sheets access are set up)
def update_google_sheet(recent_data, sheet_name='Weather Data'):
    # Authenticate Google Sheets client
    client = authenticate_google_sheets()  # Using the updated JSON file
    
    # Open the Google Sheet
    try:
        sheet = client.open('weather-forecast').sheet1
    except gspread.exceptions.SpreadsheetNotFound:
        print(f"Spreadsheet 'weather-forecast' not found.")
        return
    
    # Clear the existing sheet (if needed) and update with the new data
    sheet.clear()
    
    # Clean the data (handle NaN values)
    cleaned_data = clean_data(recent_data)
    
    # Update the Google Sheet with the cleaned data (headers + rows)
    sheet.update([cleaned_data.columns.values.tolist()] + cleaned_data.values.tolist())
    print("✅ Data updated successfully to Google Sheet.")

# Function to handle NaN values and ensure they are replaced
def clean_data(df):
    # Replace NaN values with None (None is compatible with Google Sheets API)
    df = df.where(pd.notnull(df), None)
    return df

# Main function to run the process
def main():
    try:
        # Generate synthetic weather data (100 rows with 4 specific dates)
        df = generate_synthetic_data()
        
        # Print sample output (first few rows)
        print("✅ Sample Output:")
        print(df.head())
        
        # Update Google Sheet with the generated data
        update_google_sheet(df)
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
  
