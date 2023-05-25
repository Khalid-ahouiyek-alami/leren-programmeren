EASY_TEXT = """Ik hou van programmeren. Programmeren is leuk. 
Ik kan veel dingen maken met programmeren. Ik kan een website maken. 
Ik kan een spel maken. Ik kan een chatbot maken. 
Programmeren is niet moeilijk. Ik moet alleen de juiste code schrijven. 
De code moet logisch zijn. De code moet foutloos zijn. Werkende code maakt mij blij. 
Niet-werkende code chagerijnig. Programmeren is een avontuur. Ik leer elke dag iets nieuws met programmeren."""

DIFFICULT_TEXT = """Programmeren is een geweldige activiteit, die je in staat stelt om je creativiteit, 
logica en probleemoplossend vermogen te gebruiken, om allerlei soorten applicaties te maken, 
die nuttig, vermakelijk of zelfs levensveranderend kunnen zijn, afhankelijk van je doel en publiek. 
Het is ook een uitdagende bezigheid, die je voortdurend leert om nieuwe talen, technieken en concepten te leren, 
die je helpen om je code efficiënter, eleganter en robuuster te maken, zonder dat je je ooit hoeft te vervelen of te herhalen. 
Bovendien is het een leuke hobby, die je veel voldoening en plezier kan geven, als je ziet hoe je ideeën tot leven komen op het scherm, als je de interactie met je gebruikers ziet of 
als je de reacties van je vrienden en familie ziet, als je ze verrast met je eigen creaties.
"""

ALLOWED_IN_WORD = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-"

# depending on the type of text you wish you get an easy, difficult or text from file.
def getText(choice: str) -> str:
    if choice == 'easy':
        return EASY_TEXT
    elif choice == 'difficult':
        return DIFFICULT_TEXT
    else:
        return getFileContentAsString(choice)

def getFileContentAsString(textFile: str) -> str:
    with open(textFile, 'r') as file:
        content = file.read()
    return content

# opdracht 1
def getNumberOfCharacters(text: str) -> int:
    teller = 0
    for x in text:
        if x in ALLOWED_IN_WORD:
            teller+=1
    return teller

# opdracht 2
def getNumberOfSentences(text: str) -> int:
    teller = 0
    for x in text:
        if x == "." or x == "!" or x=="?":
            teller+=1
    return teller
              
# opdracht 3
def getNumberOfWords(text: str) -> int:
    aantal_woorden = len(text.split())
    return aantal_woorden


def AVI_berekener(text:str)-> int:   
    aantal_zinnen=getNumberOfSentences(text)
    aantal_woorden=getNumberOfWords(text)
    G_w_p_z=abs(aantal_zinnen/aantal_woorden)
    AVI_score=0
    if G_w_p_z < 7:
        AVI_score=5
    elif G_w_p_z==8:
        AVI_score=6
    elif G_w_p_z==9:
        AVI_score=7
    elif G_w_p_z==10:
        AVI_score=8
    elif G_w_p_z==11:
        AVI_score=11
    elif G_w_p_z > 11:
        AVI_score=12
    return AVI_score