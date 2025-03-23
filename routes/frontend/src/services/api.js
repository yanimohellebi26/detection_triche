export async function analyzeVideo(file) {
    const formData = new FormData();
    formData.append('file', file);
  
    const res = await fetch('http://127.0.0.1:8000/analyze_video/', {
      method: 'POST',
      body: formData,
    });
  
    return res.json();
  }
  