import React, { useState, useEffect } from 'react';
import VermeilOrb from './components/VermeilOrb';
import { Mic, Terminal, ShieldAlert, Cpu } from 'lucide-react';
import './App.css';

function App() {
  const [orbState, setOrbState] = useState('idle');
  const [logs, setLogs] = useState(["System initialized...", "Connecting to Neural Core...", "Vermeil Online."]);

  // Simulate some activity for demo purposes since we don't have real WebSocket yet
  useEffect(() => {
    const timer = setInterval(() => {
      // Randomly switch states to demonstrate
      const states = ['idle', 'listening', 'speaking', 'processing'];
      const randomState = states[Math.floor(Math.random() * states.length)];
      setOrbState(randomState);

      if (randomState === 'speaking') {
        setLogs(prev => [...prev, "Vermeil: Processing query..."]);
      }
    }, 5000);
    return () => clearInterval(timer);
  }, []);

  return (
    <div className="app-container">
      <div className="overlay"></div>

      <header className="header">
        <div className="logo">VERMEIL<span className="version">v2.0</span></div>
        <div className="status-bar">
          <span><Cpu size={16} /> SYSTEM: NORMAL</span>
          <span><ShieldAlert size={16} /> SECURITY: ACTIVE</span>
        </div>
      </header>

      <main className="main-content">
        <div className="orb-container">
          <VermeilOrb state={orbState} />
        </div>

        <div className="interaction-area">
          <div className={`status-indicator ${orbState}`}>
            {orbState.toUpperCase()}
          </div>
        </div>
      </main>

      <div className="terminal-window">
        <div className="terminal-header">
          <Terminal size={14} /> <span>/vermeil/logs/sys.log</span>
        </div>
        <div className="terminal-body">
          {logs.map((log, i) => (
            <div key={i} className="log-entry">
              <span className="timestamp">{new Date().toLocaleTimeString()}</span> {log}
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

export default App;
