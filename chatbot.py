from google import genai

client = genai.Client()

question = input("You: ")

response = client.interactions.create(
    model="gemini-3.5-flash",
    input=question
)

print("Gemini:", response.output_text)