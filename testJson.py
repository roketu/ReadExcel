import requests
import json

api_key = "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"

# Define the API endpoint and header
endpoint = "https://api.openai.com/v1/engines/text-davinci-002/completions"
header = {
  "Content-Type": "application/json",
  "Authorization": f"Bearer {api_key}"
}

# Define the request data
data = {
  "prompt": "Hello, how are you today?",
  "max_tokens": 1024,
  "n": 1,
  "stop": None,
  "temperature": 0.5
}

# Make the API request
response = requests.post(endpoint, headers=header, data=json.dumps(data))

# Get the response data
response_data = response.json()

# Get the first response from the API
message = response_data["choices"][0]["text"]
print(message)