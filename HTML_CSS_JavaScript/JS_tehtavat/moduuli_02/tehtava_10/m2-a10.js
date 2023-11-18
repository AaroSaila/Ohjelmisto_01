'use strict';


function makeArrayOfCandidates() {
    const candidates = [];
    const number_of_candidates = parseInt(prompt('Number of candidates: '));

    for (let i = 1; i <= number_of_candidates; i++) {
        const candidate_name = prompt(`Name for candidate ${i}: `);
        candidates.push({name: candidate_name, votes: 0});
    }
    return candidates;
}


function voting(candidates_array) {
    const number_of_voters = parseInt(prompt('How many voters? '));

    for (let i = 1; i <= number_of_voters; i++) {
        const vote = prompt(`Vote of voter ${i}: `);
        /* console.log(vote);
        console.log(candidates_array); */
        for (let p = 0; p < candidates_array.length; p++) {
            /* console.log('pöö') */
            if (vote == candidates_array[p]['name']) {
                candidates_array[p]['votes'] += 1;
                /* console.log(candidates_array); */
            }
        }
    }
    return candidates_array;
}


function displayVotingResults(input_array) {
    console.log(
        `The winner is ${input_array[0]['name']} with ${input_array[0]['votes']} votes.`
    );
    console.log('results:')
    for (let i = 0; i < input_array.length; i++) {
        console.log(
            `${input_array[i]['name']}: ${input_array[i]['votes']}`
        );
    }
}


const candidates = makeArrayOfCandidates();
console.log(candidates);
const voting_results = voting(candidates);
voting_results.sort((a, b) => {b - a});
displayVotingResults(voting_results);
 