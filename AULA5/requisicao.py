import requests


API_BASE_URL = "https://api.cloudflare.com/client/v4/accounts/8991dd2b59d95b23a1812799718bb2f0/ai/run/"
headers = {"Authorization": "Bearer qHJsbe54HYRXaEHZ7tIDPO6EXO-HZVwNY3eGRTbW"}


def run(model, inputs):
    input = { "messages": inputs }
    response = requests.post(f"{API_BASE_URL}{model}", headers=headers, json=input)
    return response.json()


inputs = [
    { "role": "system", "content": "You are a friendly assistan that helps write stories" },
    { "role": "user", "content": "Write a short story about a llama that goes on a journey to find an orange cloud "}
];
output = run("@cf/meta/llama-3-8b-instruct", inputs)
print(output)