from openai import OpenAI

client = OpenAI()

try:
    # Make API request
    response = client.images.generate(
        model="dall-e-3",
        prompt="Tiny hand in mine,Strength grows with each wobbly step, My heart, forever his",
        size="1024x1024",
        quality="hd",
        n=1,
    )

    # Check if response object is valid
    if response is not None:
        # Check if response contains data
        if len(response.data) > 0:
            # Check if data contains image URL
            if hasattr(response.data[0], 'url'):
                # Get and print image URL
                image_url = response.data[0].url
                print("Generated Image URL:", image_url)
            else:
                print("No image URL found in the response.")
        else:
            print("No data returned in the response.")
    else:
        print("No response received from the API.")

except Exception as e:
    # Print any errors that occur
    print("An error occurred:", str(e))