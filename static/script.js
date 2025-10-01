document.getElementById('generate-btn').addEventListener('click', async () => {
    const topic = document.getElementById('topic-input').value;
    const outputDiv = document.getElementById('blog-output');
    
    if (!topic) {
        alert('Please enter a topic.');
        return;
    }

    outputDiv.innerText = 'Generating, please wait...';

    try {
        const response = await fetch('http://127.0.0.1:5000/generate-blog', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ topic: topic })
        });
        
        const data = await response.json();
        outputDiv.innerText = data.blog_post || data.error;

    } catch (error) {
        outputDiv.innerText = 'Failed to connect to the backend. Make sure it is running.';
        console.error('Error:', error);
    }
});