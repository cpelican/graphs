
interface LetterNode {
    [key: string]: {
        children?: LetterNode;
        word?: string;
    };
}

export class Trie {
    private nodes: LetterNode = {};

    public getNodes(): LetterNode {
        return this.nodes;
    }

    public insert(
        remainingLetters: string,
        previousWord: string = '',
        childrenNodes: LetterNode = this.nodes,
    ): LetterNode {
        if (remainingLetters.length === 0) {
            return this.nodes;
        }
        let nextRemainingLetters = remainingLetters.slice(1, remainingLetters.length),
            firstLetter = remainingLetters[0],
            currentWord: string = previousWord + firstLetter,
            emptyNode = {children: {}};
        childrenNodes[firstLetter] = childrenNodes[firstLetter] ?? emptyNode;
        if (nextRemainingLetters.length == 0) {
            childrenNodes[firstLetter].word = currentWord
        }
        return this.insert(nextRemainingLetters, currentWord, childrenNodes[firstLetter].children);
    }

    public getSuggestions(suggestion: string): Set<string> {
        let currentLetterIndex = 0,
            currentNode: LetterNode = this.nodes;
        // get the suggestions tree
        while(currentLetterIndex !== suggestion.length) {
            let currentLetter = suggestion[currentLetterIndex];
            currentNode = currentNode[currentLetter].children as LetterNode;
            currentLetterIndex += 1;

            if (currentNode == null) {
                break;
            }
        }

        // build the suggestions
        return this.searchTree(currentNode);
    }

    public searchTree(nodes: LetterNode, suggestions: Set<string> = new Set()): Set<string> {
        if (nodes == null) {
            return suggestions;
        }
        Object.keys(nodes).forEach((letter: string) => {
            let currentNode = nodes[letter];
            if (currentNode.word != null) {
                suggestions.add(currentNode.word as string);
            }
            this.searchTree(currentNode.children as LetterNode, suggestions);
        });

        return suggestions;
    }
}
