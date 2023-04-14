import Header from './components/Header';
import logo from './logo.svg';
import '../src/index.css'
import './App.css';
import Main from './components/Main';
import Sidebar from './components/Sidebar';
import Send from './components/Send';

function App() {
  return (
    <body> 
     <Header />
     <Main />
     <Sidebar />
     <Send />
    </body>
  )
}

export default App;
