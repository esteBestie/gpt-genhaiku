const { OpenAI } = require('openai');

const openai = new OpenAI('your-api-key'); // Replace 'your-api-key' with your actual API key

async function generateImage() {
  try {
    const response = await openai.createImage({
      model: "dall-e-3",
      prompt: "a white siamese cat",
      n: 1,
      quality: "hd",
      size: "1024x1024",
    });
    const image_url = response.data.data[0].url;
    console.log('Generated image URL:', image_url);
    return image_url;
  } catch (error) {
    console.error('Error generating image:', error);
    throw error; // Re-throw the error to handle it outside this function if needed
  }
}

// Call the asynchronous function
generateImage()
  .then(image_url => {
    // Handle the generated image URL
    console.log('Generated image URL:', image_url);
  })
  .catch(error => {
    // Handle errors
    console.error('Error:', error);
  });
