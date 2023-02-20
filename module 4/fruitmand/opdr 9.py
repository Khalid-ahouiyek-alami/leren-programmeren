from fruitmand import fruitmand

kleuren = ""
for i in range(6): #hier staat er een range omdat het 6 keer moet herhalen omdat er 7 fruiten zijn maar de druif word er uit gehaald 
    if fruitmand[i].get("color") not in kleuren:  #hier pakt hij elke kleur van elke fruit behalve de druif 
        kleuren += fruitmand[i].get("color") + " "
    if fruitmand[i].get("name") == "druif": #omdat er in de opdracht staat geen druif bij 7/8 word het uit de list gehaald/delete
        del fruitmand[i] 
print(f"{kleuren} {fruitmand}") # hier print hij de hele fruitmand en elke kleur van de fruit zonder de druif