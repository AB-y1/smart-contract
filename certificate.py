# from openai import OpenAI
# client = OpenAI(api_key="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")

from openai import OpenAI

# authentication section
def read_api_key(file_path='api_key.txt'):
    with open(file_path, 'r') as file:
        return file.read().strip()

api_key = read_api_key(r"C:\Users\HP\Desktop\api_key.txt")
client = OpenAI(api_key=api_key)
response = client.images.generate(
  model="dall-e-3",
  prompt= """an image that describes the certificate from 10 Academy with the logo and space in the middle for full name and space for date
          also make it simple and clear and don't put too much design so it will be readable. 
          also make it in frontend perspective and right spelling""",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url
print("Generated Image URL:", image_url)
