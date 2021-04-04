type MapLetterNodeValue = {children: MapLetterNode, word?: string}
type MapLetterNode = Map<string, MapLetterNodeValue>

export class Trie {
    private nodes: MapLetterNode = new Map();

    public getNodes(): MapLetterNode {
        return this.nodes;
    }

    public insert(
        remainingLetters: string,
        previousWord: string = '',
        childrenNodes: MapLetterNode = this.nodes,
    ): MapLetterNode {
        if (remainingLetters.length === 0) {
            return this.nodes;
        }
        let nextRemainingLetters = remainingLetters.slice(1, remainingLetters.length),
            firstLetter = remainingLetters[0],
            currentWord: string = previousWord + firstLetter,
            childNode: MapLetterNodeValue = childrenNodes.get(firstLetter) ?? {children: new Map()};

        if (nextRemainingLetters.length == 0) {
            childNode.word = currentWord;
        }
        childrenNodes.set(firstLetter, childNode);

        return this.insert(nextRemainingLetters, currentWord, childrenNodes?.get(firstLetter)?.children as MapLetterNode);
    }
    public getSuggestions(suggestion: string): Set<string> {
        let currentLetterIndex = 0,
            currentNode: MapLetterNode = this.nodes;
        // get the suggestions tree
        while(currentLetterIndex !== suggestion.length) {
            let currentLetter = suggestion[currentLetterIndex];
            currentNode = currentNode?.get(currentLetter)?.children as MapLetterNode;
            currentLetterIndex += 1;

            if (currentNode == null) {
                break;
            }
        }

        // build the suggestions
        return this.searchSuggestions(currentNode);
    }

    public searchSuggestions(nodes: MapLetterNode, suggestions: Set<string> = new Set()): Set<string> {
        if (nodes == null) {
            return suggestions;
        }
        for (let currentNode of nodes.values()) {
            if (currentNode.word != null) {
                suggestions.add(currentNode.word as string);
            }
            this.searchSuggestions(currentNode.children as MapLetterNode, suggestions);
        }

        return suggestions;
    }
}
