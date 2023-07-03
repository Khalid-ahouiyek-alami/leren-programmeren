let nummer1 = 0;
let nummer2 = 0;
let som = "";

function knop(number) {
    if (som === '') {
        nummer1 += parseInt(number);
    } else {
        nummer2 += parseInt(number);
    } 
    alert('Je hebt op de knop ' + number + ' gedrukt.');
    console.log(nummer1);
    console.log(nummer2);
}

function resultaat(einde) {
    som = einde;
    alert('Je hebt op de knop ' + som + ' gedrukt.');
}

function berekenen() {
    let answer = 0;
    if (som === '+') {
        answer = nummer1 + nummer2;
    } else if (som === '-') {
        answer = nummer1 - nummer2;
    }
    console.log(answer);
    alert(nummer1 + ' ' + som + ' ' + nummer2 + ' = ' + answer);
    nummer1 = answer
}