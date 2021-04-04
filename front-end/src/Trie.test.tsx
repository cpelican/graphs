import React from 'react';
import {Trie} from './Trie';

// let exampleTrie = {
//     b: {
//         children: {
//             i: {
//                 children: {
//                     m: {
//                         children: {
//                             b: {
//                                 children: {
//                                     a: {
//                                         children: {
//                                             m: {
//                                                 children: {
//                                                     b: {
//                                                         children: {
//                                                             u: {
//                                                                 children: {
//                                                                     m: {
//                                                                         word: 'bimbambum',
//                                                                     },
//                                                                 },
//                                                             },
//                                                         },
//                                                     },
//                                                 },
//                                             },
//                                         },
//                                     },
//                                 },
//                             },
//                         },
//                     },
//                 },
//             },
//         },
//     },
// };
let trie = new Trie();

test('creates correctly the  trie', () => {
    trie.insert('bimbambum');

    expect(trie.getNodes()).toMatchSnapshot();
});

test('creates correctly the  trie', () => {
    trie.insert('bimbeta');

    expect(trie.getNodes()).toMatchSnapshot();
});

test('gets the suggestions', () => {
    expect(trie.getSuggestions('bim')).toMatchSnapshot();
});
