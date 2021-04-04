import React from 'react';
import {Trie} from './Trie';

// let exampleTrie = {
//     b: {
//         word: 'b',
//         children: {
//             i: {
//                 word: 'bi',
//                 children: {
//                     m: {
//                         word: 'bim',
//                         children: {
//                             b: {
//                                 word: 'bimb',
//                                 children: {
//                                     a: {
//                                         word: 'bimba',
//                                         children: {
//                                             m: {
//                                                 word: 'bimbam',
//                                                 children: {
//                                                     b: {
//                                                         word: 'bimbamb',
//                                                         children: {
//                                                             u: {
//                                                                 word: 'bimbambu',
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

    expect(JSON.stringify(trie.getNodes())).toMatchSnapshot();
});

test('creates correctly the  trie', () => {
    trie.insert('bimbeta');

    expect(JSON.stringify(trie.getNodes())).toMatchSnapshot();
});

test('gets the suggestions', () => {
    expect(trie.getSuggestions('bim')).toMatchSnapshot();
});

