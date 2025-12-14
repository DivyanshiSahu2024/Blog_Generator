document.getElementById('generate-btn').addEventListener('click', async () => {
    const topic = document.getElementById('topic-input').value;
    const outputDiv = document.getElementById('blog-output');
    const imageEl = document.getElementById('blog-image');
    const generateBtn = document.getElementById('generate-btn');
    const copyBtn = document.getElementById('copy-btn');

    if (!topic) {
        alert('Please enter a topic.');
        return;
    }

    // Show loading state and disable button
    outputDiv.innerText = 'Generating text and image (this may take 10-15 seconds)...';
    generateBtn.disabled = true;
    generateBtn.innerText = 'Just a moment...'; 
    imageEl.style.display = 'none';

    try {
        const response = await fetch('/generate-blog', { // Use relative URL
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ topic: topic })
        });

        const data = await response.json();

        // 1. Handle Image
        if (data.image_url) {
            imageEl.src = data.image_url;
            imageEl.style.display = 'block';
        }
        // 2. Handle Blog Post Text
        if (data.blog_post) {
        outputDiv.innerHTML = marked.parse(data.blog_post);
        copyBtn.style.display = 'block';
        } else {
        outputDiv.innerText = data.error;
        }

    } catch (error) {
        outputDiv.innerText = 'Failed to connect to the backend or an error occurred.';
        console.error('Error:', error);
    } finally {
        // Restore button state
        generateBtn.disabled = false;
        generateBtn.innerText = 'Generate'; // Restore button text
    }
});

// ADD THIS NEW EVENT LISTENER AT THE BOTTOM
document.getElementById('copy-btn').addEventListener('click', () => {
    const content = document.getElementById('blog-output').innerText;
    
    navigator.clipboard.writeText(content).then(() => {
        // Optional: Change button text temporarily to show success
        const btn = document.getElementById('copy-btn');
        const originalText = btn.innerText;
        btn.innerText = 'Copied! ✅';
        
        setTimeout(() => {
            btn.innerText = originalText;
        }, 2000);
    }).catch(err => {
        console.error('Failed to copy: ', err);
    });
});
