import * as fs from 'fs';

const rock = 'A';
const paper = 'B';
const scissors = 'C';

const scores: any = {
    'A': 1,
    'B': 2,
    'C': 3,
    'lost': 0,
    'draw': 3,
    'win': 6
}

const determineChoice = (opponenet: string, self: string): number => {
    if (self === 'Y') {
        return +scores['draw'] + +scores[opponenet];
    }

    if (opponenet === scissors) {
        return self === 'Z' ? +scores[rock] + +scores['win'] : +scores[paper] + +scores['lost'];
    }

    if (opponenet === paper) {
        return self === 'Z' ? +scores[scissors] + +scores['win'] : +scores[rock] + +scores['lost'];
    } 
    if (opponenet === rock) {
        return self === 'Z' ? +scores[paper] + +scores['win'] : +scores[scissors] + +scores['lost'];
    }

    return 0;
}

let scoreTotals: number[] = [];

let input = fs.readFileSync('input.txt', 'utf-8').split('\n');

for (const line of input) {
    scoreTotals.push(determineChoice(line[0], line[2]));
}

console.log(scoreTotals.reduce((a,b) => a + b)); //10334