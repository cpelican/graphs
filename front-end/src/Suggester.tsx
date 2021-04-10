import React from 'react';
import {Trie} from './Trie';

interface SuggesterProps {
    suggestions: string[];
}

interface SuggesterState {
    currentSuggestions: Set<string>;
    inputValue: string;
}

export class Suggester extends React.Component<SuggesterProps, SuggesterState> {
    private suggestions = new Trie();
    private emptySet: Set<string> = new Set<string>();

    constructor(props: SuggesterProps) {
        super(props);
        props.suggestions.forEach((suggestion: string) => {
            this.suggestions.insert(suggestion);
        });
        this.state = {
            currentSuggestions: this.emptySet,
            inputValue: '',
        };
    }

    private handleOnChange = (event: React.SyntheticEvent<HTMLInputElement>): void => {
        let element: HTMLInputElement = event.target as HTMLInputElement;

        if ((element?.value ?? '') === '') {
            this.setState({currentSuggestions: this.emptySet, inputValue: ''});
            return;
        }
        this.setState({
            currentSuggestions: this.suggestions.getSuggestions(element.value.toLowerCase()),
            inputValue: element.value,
        });
    };

    private handleSingleSuggestionClick(s: string): void {
        this.setState({inputValue: s, currentSuggestions: this.emptySet});
    }

    private handleReset = (): void => {
        this.setState({inputValue: '', currentSuggestions: this.emptySet});
    };

    private renderSingleSuggestion = (s: string, i: number) => {
        return (
            <li
                key={s + i}
                className='p-2 cursor-pointer hover:bg-gray-100'
                onClick={() => this.handleSingleSuggestionClick(s)}
            >
                {s}
            </li>
        );
    };

    private renderCurrentSuggestions(): React.ReactNode {
        return Array.from(this.state.currentSuggestions).map(this.renderSingleSuggestion);
    }

    public render(): React.ReactNode {
        let suggesterClassName = `${
                this.state.currentSuggestions.size === 0 ? 'hidden' : ''
            } trie-suggester-suggestions max-h-80 overflow-auto max-w-xl w-80 border rounded-md text-xs text-gray-400`,
            resetButtonClassName = `${
                this.state.inputValue == ''
                    ? ' cursor-default border-gray-300 text-gray-300'
                    : 'border-gray-400 text-gray-400 hover:shadow'
            } flex items-center focus:outline-none justify-center w-10 h-10 mr-2 focus:shadow border rounded-full focus:shadow-outline hover:shadow-outline`;
        return (
            <div className='trie-suggester flex-col items-center'>
                <div className='flex'>
                    <input
                        onChange={this.handleOnChange}
                        className='flex-1 block max-w-xl w-80 p-2 mr-1 focus:outline-none focus:shadow rounded-md text-sm border-solid border border-gray-400 text-gray-700'
                        placeholder='Why, How, When, Where, If, Can, Is ???'
                        value={this.state.inputValue}
                    />
                    <button
                        disabled={this.state.inputValue == ''}
                        onClick={this.handleReset}
                        className={resetButtonClassName}
                    >
                        <svg className='w-4 h-4 fill-current' viewBox='0 0 20 20'>
                            <path d='M15.898,4.045c-0.271-0.272-0.713-0.272-0.986,0l-4.71,4.711L5.493,4.045c-0.272-0.272-0.714-0.272-0.986,0s-0.272,0.714,0,0.986l4.709,4.711l-4.71,4.711c-0.272,0.271-0.272,0.713,0,0.986c0.136,0.136,0.314,0.203,0.492,0.203c0.179,0,0.357-0.067,0.493-0.203l4.711-4.711l4.71,4.711c0.137,0.136,0.314,0.203,0.494,0.203c0.178,0,0.355-0.067,0.492-0.203c0.273-0.273,0.273-0.715,0-0.986l-4.711-4.711l4.711-4.711C16.172,4.759,16.172,4.317,15.898,4.045z'></path>
                        </svg>
                    </button>
                </div>
                <ul className={suggesterClassName}>{this.renderCurrentSuggestions()}</ul>
            </div>
        );
    }
}
