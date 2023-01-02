import * as fs from 'fs';

const rock = 'A';
const paper = 'B';
const scissors = 'C';

const scores: any = {
    rock: 1,
    paper: 2,
    scissors: 3,
    'lost': 0,
    'draw': 3,
    'win': 6,
    'X': 1,
    'Y': 2,
    'Z': 3
}

const selfLookup: any = {
    'X': rock,
    'Y': paper,
    'Z': scissors

}

const determineWinner = (opponenet: string, self: string): number => {
    const selfRock = 'X';
    const selfPaper = 'Y';
    const selfScissors = 'Z';

    if (opponenet === selfLookup[self]) {
        return +scores['draw'] + +scores[self];
    }

    if (opponenet === scissors) {
        return self === selfRock ? +scores[self] + +scores['win'] : +scores[self] + +scores['lost'];
    }

    if (opponenet === paper) {
        return self === selfScissors ? +scores[self] + +scores['win'] : +scores[self] + +scores['lost'];
    } 
    if (opponenet === rock) {
        return self === selfPaper ? +scores[self] + +scores['win'] : +scores[self] + +scores['lost'];
    }

    return 0;
}

let scoreTotals: number[] = [];

let input = fs.readFileSync('input.txt', 'utf-8').split('\n');

for (const line of input) {
    scoreTotals.push(determineWinner(line[0], line[2]));
}
console.log(scoreTotals);
console.log(scoreTotals.reduce((a,b) => a + b)); //10404