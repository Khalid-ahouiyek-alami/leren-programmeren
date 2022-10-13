zin = input("voer een zin in")
woord = ''
zin2 =''

for c in zin:

     if c == " ":
        zin2 += woord + " " + woord + " " 
     woord ='' 
else :
    woord += c

zin2 += woord + " " + woord

print(zin2)