from flask import Flask, render_template, request, jsonify
from openai import OpenAI

app = Flask(__name__)
client = OpenAI()

@app.route('/')
def index():
    print('Rendering index.html')
    return render_template('index.html')

@app.route('/generate_image', methods=['POST'])
def generate_image():
    print('Received request to generate image.')
    try:
        # Make API request
        response = client.images.generate(
            model="dall-e-3",
            prompt="photo realistic image of a bear playing the upright bass leaning on a tree, in a jazz band",
            size="1024x1024",
            quality="standard",
            n=1,
        )
        image_url = response.data[0].url
        print('Generated image URL:', image_url)
        return jsonify({'image_url': image_url})
    except Exception as e:
        print('Error generating image:', e)
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
