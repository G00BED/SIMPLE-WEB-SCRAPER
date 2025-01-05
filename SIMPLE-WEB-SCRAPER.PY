import requests
from bs4 import BeautifulSoup

# Prompt user for the website URL and keyword
url = input("Enter the website URL: ")
keyword = input("Enter the keyword to search for: ")

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all occurrences of the keyword in the HTML content
keyword_count = len(soup.find_all(result=lambda result: result and keyword in result))

# Print the number of occurrences of the keyword
print(f"The keyword '{keyword}' appears {keyword_count} times on the website.")
