let cars = [

 
    "Audi A3",
    "BMW 3 Series",
    "Chevrolet Camaro",
    "Dodge Charger",
    "Ford Mustang",
    "Honda Civic",
    "Infiniti Q50",
    "Jaguar F-Type",
    "Kia Optima",
    "Lamborghini Huracan",
    "Mercedes-Benz C-Class",
    "Ferrari F8 Tributo",
    "Nissan Altima",
    "Porsche 911",
    "Range Rover Evoque",
    "Subaru Impreza",
    "Ferrari SF90 Stradale",
    "Tesla Model S",
    "Toyota Corolla",
    "Volkswagen Golf",
    "Acura NSX",
    "Bentley Continental",
    "Cadillac Escalade",
    "Ferrari 488 GTB",
    "Dodge Challenger",
    "Ferrari 458",
    "GMC Sierra",
    "Hyundai Elantra",
    "Jeep Grand Cherokee",
    "Ferrari SF90 Stradale",
    "Koenigsegg Agera",
    "Lexus LS",
    "Maserati GranTurismo",
    "Nissan GT-R",
    "Pagani Huayra",
    "Rolls-Royce Ghost",
    "Smart ForTwo",
    "Tesla Model X",
    "Toyota Prius",
    "Volkswagen Jetta",
    "Alfa Romeo Giulia",
    "Bugatti Chiron",
    "Chevrolet Corvette",
    "Ferrari Portofino",
    "Fiat 500",
    "GMC Yukon",
    "Honda Accord",
    "Jaguar XJ",
    "Kia Soul",
    "Lamborghini Aventador",
    "Mercedes-Benz E-Class",
    "Nissan gtr",
    "Porsche Panamera",
    "Range Rover Sport",
    "Subaru Legacy",
    "Tesla Model 3",
    "Toyota supra",
    "Volkswagen Passat"
    ];


let mijn_lijst = document.createElement('ul');
document.body.appendChild(mijn_lijst);
let mijn_item = document.createElement('li'); 
mijn_lijst.appendChild(mijn_item);

cars.sort();
for (let x = 0; x<cars.length; x++){
    let mijn_item = document.createElement('li')
    mijn_item.innerHTML= cars[x]
    if (cars)
    mijn_lijst.appendChild(mijn_item)
}



