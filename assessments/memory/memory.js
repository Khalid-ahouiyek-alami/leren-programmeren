


function shuffle(array) {
    let currentIndex = array.length,  randomIndex;
  
    // While there remain elements to shuffle.
    while (currentIndex != 0) {
  
      // Pick a remaining element.
      randomIndex = Math.floor(Math.random() * currentIndex);
      currentIndex--;
  
      // And swap it with the current element.
      [array[currentIndex], array[randomIndex]] = [array[randomIndex], array[currentIndex]];
    }
  
    return array;
  }
  
const images= [
  "foto1.jpeg",
  "foto2.jpeg",
  "foto3.jpeg",
  "foto4.jpeg",
  "foto5.jpeg",
  "foto6.jpeg",
  "foto7.jpeg",
  "foto8.jpeg",
  "foto9.jpeg",
  "foto10.jpeg",
];
let images2 = shuffle(images)

for (x = 0; x<10; x++){
  naam = document.getElementById('buttons');
  let fotos = document.createElement('img');
  fotos.setAttribute('onclick', 'click()')
  fotos.src= 'background.png';
  fotos.afbeelding = images[x]
  naam.appendChild(fotos)
  fotos.onclick= click
}

  function click(e){
    console.log(this.afbeelding)
    this.src = this.afbeelding
}
for (x = 0; x<10; x++){
  naam = document.getElementById('buttons');
  let fotos = document.createElement('img');
  fotos.setAttribute('onclick', 'click()')
  fotos.src= 'background.png';
  fotos.afbeelding = images2[x]
  naam.appendChild(fotos)
  fotos.onclick= click
}
