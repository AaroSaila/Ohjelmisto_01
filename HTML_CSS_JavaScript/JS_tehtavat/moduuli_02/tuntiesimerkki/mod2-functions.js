'use strict';


function do_something(name) {
    console.log('moi' + name);
}


const doSomething2 = function(name) {
    console.log('moi täältäkin', name)
};


const doSomething3 = (name) => {
    console.log('moi nuolifunktiosta', name)
};


do_something('Iines');
doSomething2('Don');
doSomething3('Jones');

// Lottorivin arvonta ja palautusarvo.
// arvotaan 7 numeron lottorivi, pallot 1 - 40
// Palautetaan rivi kerrallaan taulukkona (esim. [3, 6, 23, 34, 35, 38, 40])
function generateLotteryRow(numberCount, maxValue) {
    const lotteryRow = [];
    while (lotteryRow.length < numberCount) {
        const number = Math.floor(Math.random() *maxValue + 1);
        if (!lotteryRow.includes(number)) {
            lotteryRow.push(number);
        }               
    }
    return lotteryRow.sort((num1, num2) => num1 - num2);
}


const myRow = generateLotteryRow();
console.log(myRow);

// Luodaan lottokuponki, jossa n-määrä rivejä.
function createLotteryTicket(rowCount) {
    const ticket = [];
    for (let i = 0; i < rowCount; i++) {
        const row = generateLotteryRow(7, 40);
        ticket.push(row);
    }
    return ticket;
}


const myTicket = createLotteryTicket(5);
console.log(myTicket);
// tulostetaan 2. kupongin 3. numero
console.log(myTicket[1][4]);


/* value scopes / näkyvyysalue */
{

    const muuttuja = 0;
    let muuttuja2 = 'uusi arvo';
    {
        const muuttuja = 'a';
        let muuttuja2 = 'vielä uudempi arvo';
        console.log(muuttuja);
        console.log(muuttuja2);
    }
    console.log(muuttuja);
    console.log(muuttuja2);
}