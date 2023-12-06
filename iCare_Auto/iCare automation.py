import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup


df = pd.read_csv('Desktop/iCare.csv')
df = df[df['Austin Url'].notnull()]
df = df[['AA Login', 'Assisted iCare Required', 'Austin Url', 'Incident Id', 'Manager Login','Shift Code','Days Case Open']]

host = 'https://fclm-portal.amazon.com/?warehouseId=SWF1'
port = 443
family = socket.AF_INET  # Use IPv4


base_url = 'https://fclm-portal.amazon.com/employee/timeDetails?warehouseId=SWF1&employeeId='
df['On site'] = ''

# Iterate over rows and update the 'On site' column based on scraping
for index, row in df.iterrows():
    # Construct the URL with the 'Login' value
    url = f"{base_url}{row['AA Login']}"

    print(url)

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the tr tags with class 'function-seg indirect'
        tr_tags_indirect = soup.find_all('tr', class_='function-seg indirect')

        # Update the 'On site' column based on the presence of the tr tags
        df.at[index, 'On site'] = 'Yes' if tr_tags_indirect else 'No'
    else:
        # If the request was not successful, set 'On site' to 'Error'
        df.at[index, 'On site'] = 'Error'


for index, row in df.iterrows():
    print(f"Row {index + 1}:")
    for column in df.columns:
        print(f"  {column}: {row[column]}")

