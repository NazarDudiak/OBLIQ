// import logo from './logo.svg';
import './App.css';
import {Fragment} from "react";
import Header from "./appHeader/Header";
import Home from './appHome/Home';



function App() {
  return (
    <Fragment>
      <Header/>
      <Home/>
      {/* <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div> */}
    </Fragment>
  );
}

export default App;
