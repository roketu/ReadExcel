import requests
import openAIkey

def generate_text(prompt):
    API_KEY = openAIkey.getOpenAIkey()
    model = "text-davinci-002"
    prompt = (f"{prompt}"
             )

    response = requests.post(f"https://api.openai.com/v1/engines/{model}/jobs",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}",
            "OpenAI-Organization": "org-RSVSByya6GGtj7j4aPYWDG1q"
        },
        json={
            "prompt": prompt,
            "max_tokens": 1024,
            "temperature": 0.5,
        },
    )

    if response.status_code != 200:
        raise ValueError("Failed to generate text")

    result = response.json()["choices"][0]["text"]
    return result.strip()