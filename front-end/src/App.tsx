import React from 'react';
import './App.css';
import {Trie} from './Trie';

function App() {
    let trie = new Trie();
    trie.insert('bimbambum');
    trie.insert('bimbeta');

    return <div className='App'>yoloo</div>;
}

export default App;
