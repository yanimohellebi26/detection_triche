import React from 'react';
import VideoFeed from '../components/VideoFeed';
import AudioFeed from '../components/AudioFeed';
import Alerts from '../components/Alerts';

const Dashboard = () => {
  return (
    <div>
      <h1>Dashboard</h1>
      <VideoFeed />
      <AudioFeed />
      <Alerts />
    </div>
  );
};

export default Dashboard;