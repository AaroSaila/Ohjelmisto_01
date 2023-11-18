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
        for (let p = 0; p < candidates_array.length; p++) {
            if (vote == candidates_array[p]['name']) {
                candidates_array[p]['votes'] += 1;
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
const voting_results = voting(candidates);
voting_results.sort((a, b) => {
    return b.votes - a.votes;
 });
displayVotingResults(voting_results);
 