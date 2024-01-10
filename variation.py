
from openai import OpenAI

# authentication section
def read_api_key(file_path='api_key.txt'):
    with open(file_path, 'r') as file:
        return file.read().strip()

api_key = read_api_key(r"C:\Users\HP\Desktop\api_key.txt")
client = OpenAI(api_key=api_key)

# main code
response = client.images.create_variation(
    image=open("best-generated-cerificate-openai.png", "rb"),
    n=1,
    size="1024x1024"
)

image_url = response.data[0].url
print("Generated Image URL:", image_url)
