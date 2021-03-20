import React from 'react';
import './App.css';
import {Trie} from './Trie';

function App() {
    let trie = new Trie();

    trie.insert('bimbambum');
    return <div className='App'>yoloo</div>;
}

export default App;
