interface Letter {
    [key: string]: Letter;
}

export class Trie {
    private nodes: Letter = {};

    public getNodes(): Letter {
        return this.nodes;
    }

    public insert(remainingLetters: string, childrenNodes: Letter = this.nodes): Letter {
        if (remainingLetters.length === 0) {
            return this.nodes;
        }
        let nextRemainingLetters = remainingLetters.slice(1, remainingLetters.length);
        childrenNodes[remainingLetters[0]] = childrenNodes[remainingLetters[0]] ?? {};
        return this.insert(nextRemainingLetters, childrenNodes[remainingLetters[0]]);
    }
}
