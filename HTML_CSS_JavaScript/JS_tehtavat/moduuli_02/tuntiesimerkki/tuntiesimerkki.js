'use strict';

// Taulukot (array)
// Alkioiden tietotyypit voi olla mitä vaan. (kuin muuttujissakin)
const items = ['eka', 2, 3.3, [1, 2, 3], true];
console.log(items);

// Alkion arvo saadaan alkion indeksiin viittaamalla
console.log(items[3]);

// Alkion arvo voidaan lisätä tai muuttaa alkion indeksiin viittaamalla.
items[3] = 99;
console.log(items[3]);
items[9] = '10. alkion esimerkkiarvo';
console.log(items);
// Viitataan indeksiin, jolla ei ole alkiota. (tuloksena saadaan "undefined")
console.log(items[6]);
// Arrayn koko.
console.log(items.length);

for (let i = 0; i < items.length; i++) {
    console.log(i + '. alkion arvo on ' + items[i]);
}

// sama for-of:lla
for (const item of items) {
    console.log(item);
}

// Ei tulosteta tyhjiä alkioita.
for (const item of items) {
    if (item) { // undefined on epätotuudellinen (false) [vaihtoehtoisesti "item != undefined"]
        console.log(item);
    }
}

// Taulukoiden metodeita
const names = ['Frank', 'Scott', 'Jasmine', 'Don'];
const ages = [13, 8, 102, 46];
console.log(names);
// Järjestää aakkosjärjestykseen (numerot eivät järjesty oikein)
names.sort();
console.log(names);
// Järjestä numerojärjestykseen
ages.sort((a, b) => a-b);
console.log(ages);
ages.sort();
console.log(ages);
// käännä järj. ympäri
ages.reverse();
console.log(ages);
// Lisää uusi nimi taulukon loppuun.
names.push('Iines');
console.log(names);
// Lisää uusi nimi taulukon alkuun.
names.unshift('Hessu');
console.log(names);
// Poistaa viimeisen alkion.
const lastNameInArr = names.pop();
console.log('Taulukosta poistettiin: ' + lastNameInArr);
console.log(names);
// Poistaa ja palauttaa ensimmäisen alkion.
names.shift();
console.log(names);
// Onko taulukossa ko. arvo?
console.log(names.includes('Iines'));
console.log(names.includes('don'));
console.log(names.includes('Don'));

// JS objektit/oliot
// olioliteraali on tietorakenne kuin Pythonin sanakirja.

const person = {name: 'Iines', age: 34};
console.log('person olio: ', person);
// Ominaisuuksien arvojen muuttaminen (kuin sijoitus).
person['age'] = 36;
person.name = 'Iines Ankka';
// Ominaisuuksien (property) lisääminen
person.profession = 'student';
console.log('person olio', person);
// Tietyn ominaisuuden arvon hakeminen.
console.log(person.name + ' on ' + person['age'] + ' vuotta');

const person2 = {
    name: 'Iines',
    age: 34,
    getInfo: function() {
        return this.name + ' on ' + this['age'] + ' vuotta';
    },
}

console.log(person2.getInfo())
