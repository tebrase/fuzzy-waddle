import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import Sammenlikning from './components/sammenlikning';


class App extends Component {
  render() {
    return (
      <div className="App">        
        <MuiThemeProvider>
          <Sammenlikning />
        </MuiThemeProvider>
      </div>
    );
  }
}

export default App;
