from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from openai import OpenAI
from dotenv import load_dotenv  

load_dotenv()  # <-- Add this line to load variables from .env

# Initialize the Flask application
app = Flask(__name__)
CORS(app)  # This allows your frontend to communicate with the backend

# Securely get your OpenAI API key from environment variables
# Make sure you have set this in your system
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def create_blog_post(topic):
    """Generates a blog post using the OpenAI API."""
    prompt = f"""
    Write a compelling and informative blog post about "{topic}".

    The blog post should have the following structure:
    1.  **Catchy Title:** An engaging title for the post.
    2.  **Introduction:** Briefly introduce the topic and why it's relevant.
    3.  **Main Body:** At least three distinct points, each explained in its own paragraph.
    4.  **Conclusion:** Summarize the main points and offer a concluding thought.

    The tone should be enthusiastic and easy to understand.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that writes excellent blog posts."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {e}"

@app.route('/generate-blog', methods=['POST'])
def generate_blog():
    """API endpoint to generate a blog post."""
    data = request.get_json()
    topic = data.get('topic')

    if not topic:
        return jsonify({"error": "No topic was provided."}), 400

    blog_post = create_blog_post(topic)
    return jsonify({"blog_post": blog_post})

if __name__ == '__main__':
    app.run(debug=True, port=5000)