import requests
import json

# Your Google Search API key
api_key = "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"

# Your search query
query = "How to parse JSON data in Python"

# Build the API endpoint URL
url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx=017576662512468239146:omuauf_lfve&q={query}"

# Make the API request
response = requests.get(url)

# Parse the JSON data
data = json.loads(response.text)

# Access the search results
for item in data["items"]:
    print(item["title"])
    print(item["link"])
