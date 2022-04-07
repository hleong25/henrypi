import './App.css';
import React from 'react';
import { VideoControlComponent } from './video/VideoControl';

function App() {
  // const [videoToggle, setVideoToggle] = React.useState(true);

  return (
    <div className="App">
      <VideoControlComponent />
    </div>
  );
}

export default App;
