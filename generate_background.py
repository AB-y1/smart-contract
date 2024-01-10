import openai

# Seting OpenAI API key
openai.api_key = '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'

# Craft a prompt to generate variations of the certificate background
prompt = "Generate a beautiful certificate background with Full Name, Logo, Date, and other relevant information."

# Make a request to OpenAI API
response = openai.Completion.create(
  engine="text-davinci-003",
  prompt=prompt,
  max_tokens=150
)

# Print the response for debugging
print(response)

# Extract the generated certificate background from the response
certificate_background = response['choices'][0]['text']

# Save the certificate background to a file
with open("certificate_background.txt", "w") as f:
    f.write(certificate_background)



from openai import OpenAI
client = OpenAI()

response = client.images.generate(
  model="dall-e-3",
  prompt="a beautiful certificate base background with Full Name, Logo, Date.",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url
