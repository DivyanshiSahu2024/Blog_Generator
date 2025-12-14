from flask import Flask, request, jsonify, render_template
import os
from openai import OpenAI
from dotenv import load_dotenv
import urllib.parse
# Load environment variables from a .env file
load_dotenv()

# Initialize the Flask application
# The static_folder and template_folder arguments tell Flask where to find your frontend files.
app = Flask(__name__, static_folder='static', template_folder='templates')

# Initialize the OpenAI client
# It's crucial that the OPENAI_API_KEY is set in your environment.
try:
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
except Exception as e:
    print(f"Error: Could not initialize OpenAI client. Make sure your API key is set. Details: {e}")
    client = None

def create_blog_post(topic):
    """
    Generates a blog post using the OpenAI API based on a given topic.
    """
    if not client:
        return "OpenAI client is not configured. Please check your API key."

    # A detailed prompt to guide the language model
    prompt = f"""
    Write a compelling and informative blog post about "{topic}".

    The blog post must have the following structure:
    1.  **Catchy Title:** An engaging title for the post.
    2.  **Introduction:** Briefly introduce the topic and why it's relevant.
    3.  **Main Body:** At least three distinct points, each explained in its own paragraph with clear headings.
    4.  **Conclusion:** Summarize the main points and offer a concluding thought or call to action.

    The tone should be enthusiastic, encouraging, and easy to understand.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that writes excellent, well-structured blog posts."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"An error occurred during OpenAI API call: {e}")
        return f"An error occurred while generating the blog post: {e}"
    
def create_blog_image(topic):
    """
    Generates a free AI image using Pollinations.ai based on the topic.
    """
    try:
        # 1. Clean the prompt for the URL
        encoded_topic = urllib.parse.quote(topic)
        
        # 2. Construct the URL
        # Pollinations generates images on the fly based on the URL text
        image_url = f"https://image.pollinations.ai/prompt/realistic%20blog%20header%20image%20about%20{encoded_topic}?width=1024&height=1024&nologo=true"
        
        print(f"Generated Image URL: {image_url}")
        return image_url
        
    except Exception as e:
        print(f"Image generation error: {e}")
        return None

# API endpoint for generating the blog post
@app.route('/generate-blog', methods=['POST'])
def generate_blog():
    """
    Receives a topic from the frontend, generates a blog post, and returns it as JSON.
    """
    data = request.get_json()
    topic = data.get('topic')

    if not topic:
        return jsonify({"error": "No topic was provided."}), 400

    blog_post = create_blog_post(topic)
    image_url = create_blog_image(topic)
    return jsonify({"blog_post": blog_post, "image_url": image_url})


# Route to serve the main HTML page
@app.route('/')
def index():
    """
    Serves the main frontend page (index.html).
    """
    return render_template('index.html')

# This block allows you to run the app directly for local development
if __name__ == '__main__':
    # Use waitress for a more production-ready local server on Windows
    # On other systems, Gunicorn is recommended for production.
    try:
        from waitress import serve
        serve(app, host="0.0.0.0", port=5000)
    except ImportError:
        # Fallback to Flask's built-in server if waitress is not installed
        app.run(debug=True, port=5000)
