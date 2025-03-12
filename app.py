from flask import Flask, request, jsonify, render_template
import openai
import creds  # Import creds.py

app = Flask(__name__, template_folder=".")

# Set OpenAI API key from creds.py
openai.api_key = creds.OPENAI_API_KEY

ALLOWED_TOPICS = ["career", "job", "study", "education", "skills", "resume", "interview", "university", "certifications", "courses", "internships", "freelancing"]

def is_related_to_career(query):
    return any(topic in query.lower() for topic in ALLOWED_TOPICS)

@app.route('/')
def index():
    return render_template('chatbot.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message")

    if not user_message:
        return jsonify({"response": "Please enter a message."})

    if not is_related_to_career(user_message):
        return jsonify({"response": "I can only help with career and study-related questions! 😊"})

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful career and study guidance assistant."},
            {"role": "user", "content": user_message}
        ]
    )

    chatbot_response = response['choices'][0]['message']['content']
    return jsonify({"response": chatbot_response})

if __name__ == '__main__':
    app.run(debug=True)
