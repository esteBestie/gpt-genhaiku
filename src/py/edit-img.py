from openai import OpenAI

client = OpenAI()

print("Sending request to OpenAI API...")
try:
    response = client.images.edit(
        model="dall-e-2",
        image=open("/Users/estebansuarez/Desktop/dev/gpt-genhaiku/twins.png", "rb"),
        prompt="Transform this image into an anime-style depiction of people in a bar.",
        n=1,
        size="1024x1024"
    )
    print("Received response from OpenAI API.")
    if response.status == "success":
        print("API request successful.")
        try:
            image_url = response.data[0].url
            print("Edited image URL:", image_url)
            # Download and inspect the edited image here
        except Exception as e:
            print("Error occurred while processing response:", e)
    else:
        print("API request failed with error:", response.error)
except Exception as e:
    print("Error occurred while sending request to OpenAI API:", e)
