import React, { useState } from 'react';
import axios from 'axios';

const VideoFeed = () => {
  const [videoFile, setVideoFile] = useState(null);
  const [response, setResponse] = useState(null);

  const handleFileChange = (e) => {
    setVideoFile(e.target.files[0]);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append('file', videoFile);

    try {
      const res = await axios.post('/api/analyze_video', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      setResponse(res.data);
    } catch (error) {
      console.error('Error uploading video:', error);
    }
  };

  return (
    <div>
      <h2>Video Feed</h2>
      <form onSubmit={handleSubmit}>
        <input type="file" onChange={handleFileChange} />
        <button type="submit">Upload</button>
      </form>
      {response && <div>{JSON.stringify(response)}</div>}
    </div>
  );
};

export default VideoFeed;