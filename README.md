# Weather-Forecast
🌦️ Synthetic Weather Data Generator & Uploader
Author: Sakshi Shelke
Last Updated: April 2025

This Python script generates synthetic weather data and uploads it directly to a Google Sheet. It's perfect for testing weather-based dashboards, machine learning models, or just learning how to interact with Google Sheets using Python.

📋 Features
✅ Generates 100 rows of realistic synthetic weather data

✅ Cycles through 4 specific past dates

✅ Uploads data directly to a Google Sheet

✅ Handles authentication securely using Google API credentials

✅ Cleans data to ensure compatibility with Google Sheets

🛠️ Technologies Used
Python 🐍

Pandas

Random

Google Sheets API (gspread)

OAuth2 Client for authentication

📦 Requirements
Install the required Python packages:

bash
Copy
Edit
pip install pandas gspread oauth2client
Make sure you have a Google Cloud project with Sheets API enabled, and a service account JSON file (e.g., weather-forecast-456611-cb8ce5579c6c.json).

📁 File Structure
bash
Copy
Edit
weather_script/
│
├── weather_script.py       # Main script
├── weather-forecast-456611-cb8ce5579c6c.json  # Google API credentials
└── README.md               # This file
🚀 How to Run
Set up your Google Sheet

Create a Google Sheet named weather-forecast

Share it with your service account email (found in the credentials JSON)

Run the script

bash
Copy
Edit
python weather_script.py
Check your Google Sheet
You’ll see 100 rows of generated weather data uploaded and cleaned!

📊 Sample Output
plaintext
Copy
Edit
        Date  MinTemp  MaxTemp  Temp  Humidity  Pressure
0  2025-04-12     7.5     27.1  17.5        62    1015.4
1  2025-04-13     9.2     25.3  18.1        55    1021.7
2  2025-04-11     6.8     22.4  17.9        60    1009.6
3  2025-04-10    10.1     28.2  19.5        70    1002.8
4  2025-04-12     5.9     24.6  18.3        53    1010.1
🧹 Data Cleaning
Before uploading, the script ensures:

All NaN values are replaced with None for Google Sheets compatibility.

⚠️ Notes
The script assumes your Google Sheet has editing access for the service account.

The entire sheet will be cleared and replaced with new data on each run.

You can modify the specific_dates list or expand it for more variation.

🙋‍♀️ About the Author
Sakshi Shelke
Python developer | Data enthusiast | Building tools to make weather data fun and accessible 🌦️
