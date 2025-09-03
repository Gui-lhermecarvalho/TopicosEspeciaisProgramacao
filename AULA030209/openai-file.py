from openai import OpenAI

client = OpenAI()

response = client.responses.create(
  model="gpt-4o-mini",
  input="Quantos mundiais o Corinthians tem?",
  store=True,
)

print(response.output_text);
