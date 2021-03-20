import React from 'react';
import {Trie} from './Trie';

let trie = new Trie();
test('creates correctly the trie', () => {
  trie.insert('bimbambum');

  expect(trie.getNodes()).toEqual({
      "b": {
          "i": {
              "m": {
                  "b": {
                      "a": {
                          "m": {
                              "b": {
                                  "u": {
                                      "m": {}
                                  }
                              }
                          }
                      }
                  }
              }
          }
      }
  });
});

test('adding an other word does not deletes the first', () => {
  trie.insert('bimbeta');

  expect(trie.getNodes()).toEqual({
      "b": {
          "i": {
              "m": {
                  "b": {
                      "a": {
                          "m": {
                              "b": {
                                  "u": {
                                      "m": {}
                                  }
                              }
                          }
                      },
                      "e": {
                          "t": {
                              "a": {}
                          }
                      },
                  }
              }
          }
      }
  });
});
