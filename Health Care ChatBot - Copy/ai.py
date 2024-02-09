from flask import Flask, request, jsonify
import openai  # Example for OpenAI GPT-3

app = Flask(__name__)

# Set up your OpenAI API key
openai.api_key = 'YOUR_API_KEY'


@app.route('/get_bot_response', methods=['POST'])
def get_bot_response():
    user_message = request.json['user_message']

    # Call the OpenAI API with the user's message
    response = openai.Completion.create(
        engine="davinci",  # or another GPT-3 engine
        prompt=user_message,
        max_tokens=100
    )

    bot_response = response['choices'][0]['text']

    return jsonify({'bot_response': bot_response})


if __name__ == '__main__':
    app.run(debug=True)
