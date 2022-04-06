import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src="/api/video/9000/snapshot" className="snapshot9000" alt="snapshot9000" />
        <img src="/api/video/9000/stream" className="stream9000" alt="stream9000" />

        <img src="/api/video/9001/snapshot" className="snapshot9001" alt="snapshot9001" />
        <img src="/api/video/9001/stream" className="stream9001" alt="stream9001" />
      </header>
    </div>
  );
}

export default App;
