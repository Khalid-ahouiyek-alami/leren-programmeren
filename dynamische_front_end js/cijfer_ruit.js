let opgegeven_cijfer = parseInt(prompt("voer een getal in: "))
let cijfer_regel = "";

for (let x = 1; x <= opgegeven_cijfer;x++){
    for (let y = 1; y <= x;y++){
        cijfer_regel += y + "";
    }
    cijfer_regel += "<br>";
}
for (let x = opgegeven_cijfer -1; x >= 1;x--){
    for (let y = 1; y <= x;y++){
        cijfer_regel += y + "";
    }
    cijfer_regel += "<br>";
}


