# AI Blog Post Generator ✍️

A full-stack web application that leverages Artificial Intelligence to automatically generate engaging blog posts and matching header images. Built with **Flask**, **OpenAI GPT**, and **Pollinations.ai**.

## 🚀 Live Demo
https://bloggen-kfzr.onrender.com/

## ✨ Features

* **Content Generation:** Generates structured blog posts (Title, Introduction, Key Points, Conclusion) using OpenAI's **GPT-4o-mini**.
* **Image Generation:** Automatically creates context-aware header images using **Pollinations.ai** (No API key required for images).
* **Markdown Support:** Renders the blog output with proper formatting (Bold, Headings, Lists) using `Marked.js`.
* **User Tools:**
    * 📋 **One-Click Copy:** Easily copy the blog text to your clipboard.
    * 🖼️ **Download Image:** Save the generated image locally.
* **Modern UI:** Features a responsive design with **Glassmorphism** effects, animated gradients, and loading states.

## 🛠️ Tech Stack

* **Frontend:** HTML5, CSS3, JavaScript (Vanilla)
* **Backend:** Python, Flask
* **AI Models:**
    * Text: OpenAI GPT-4o-mini
    * Images: Pollinations.ai (Stable Diffusion)
* **Deployment:** Render (Gunicorn)

## ⚙️ Installation & Local Setup

Follow these steps to run the project locally on your machine.

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/Blog_Generator.git](https://github.com/YOUR_USERNAME/Blog_Generator.git)
cd Blog_Generator
```
### 2. Install Dependencies
Make sure you have Python installed. Then run:

```Bash
pip install -r requirements.txt
```
### 3. Set Up Environment Variables
Create a file named .env in the root directory and add your OpenAI API key:
``` OPENAI_API_KEY=sk-your-openai-api-key-here ```

### 4. Run the Application
``` Bash
python app.py
```
Open your browser and navigate to: http://127.0.0.1:5000

### 📂 Project Structure
/Blog_Generator
*   ├── static/
*   │   ├── style.css        # Animations and Glassmorphism styles
*   │   └── script.js        # Frontend logic (Fetch API, DOM manipulation)
*   ├── templates/
*   │   └── index.html       # Main user interface
*   ├── app.py               # Flask backend & AI integration
*   ├── requirements.txt     # Python dependencies
*   ├── .env                 # API Keys (Not shared)
*   └── README.md            # Project documentation

###  🚀 Deployment
This project is configured for easy deployment on Render.
1. Push your code to GitHub.
2. Create a new Web Service on Render.
3. Connect your repository.
4. Build Command: pip install -r requirements.txt
5. Start Command: gunicorn app:app
6. Add your OPENAI_API_KEY in the Render Environment Variables settings.


### 🤝 Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.
1. Fork the repository.
2. Create your feature branch (git checkout -b feature/AmazingFeature).
3. Commit your changes (git commit -m 'Add some AmazingFeature').
4. Push to the branch (git push origin feature/AmazingFeature).
5. Open a Pull Request.

### 📄 License
This project is open-source and available under the MIT License.


### Next Step for You:
1.  Create a new file in VS Code named `README.md`.
2.  Paste the code above into it.
3.  Replace `YOUR_USERNAME` and the `[Link to your live Render app here]` with your actual details.
4.  Push it to GitHub:
    ```bash
    git add README.md
    git commit -m "Add documentation"
    git push
    ```
<img width="1795" height="864" alt="Screenshot 2025-12-16 141052" src="https://github.com/user-attachments/assets/d0c69b31-39fc-4448-a0b2-901023a87029" />
<img width="1875" height="864" alt="Screenshot 2025-12-16 141117" src="https://github.com/user-attachments/assets/c75a4119-6a2f-40ad-aa2f-704c327def7b" />


    
