import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Welcome to ROI!</h1>
        </header>
        <p className="App-intro">
          Your one-stop overview of your current positions and ROI!
        </p>
      </div>
    );
  }
}

export default App;
