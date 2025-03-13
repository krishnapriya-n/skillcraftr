from flask import Flask, request, jsonify
import openai
import creds  # Import creds.py

app = Flask(__name__)

# Set OpenAI API key
openai.api_key = creds.OPENAI_API_KEY

# Topics allowed
ALLOWED_TOPICS = [
    "career", "job", "study", "education", "skills", "resume",
    "interview", "university", "certifications", "courses", 
    "internships", "freelancing"
]

# Function to check if the query is related to career/study
def is_related_to_career(query):
    return any(topic in query.lower() for topic in ALLOWED_TOPICS)

# Function to generate chatbot response
def chatbot(prompt):
    if not is_related_to_career(prompt):
        return "I can only help with career and study-related questions! 😊"

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message["content"].strip()
    
    except Exception as e:
        return f"Error: {str(e)}"

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message")

    if not user_message:
        return jsonify({"response": "Please enter a message."})
    
    return jsonify({"response": chatbot(user_message)})

if __name__ == "__main__":
    print("Career Chatbot is running! Type 'quit' or 'exit' to stop.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit"]:
            break
        print("Bot:", chatbot(user_input))

if __name__ == '__main__':
    app.run(debug=True)
