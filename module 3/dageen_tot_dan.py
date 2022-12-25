x = 0
Dagen = ["ma","di","wo","do","vr","za","zo"]# dit is een list met alle dagen
Dagen_input = int(input("welke dag is het: ma=1 di=2 wo=3 do=4 vr=5 za=6 zo=7: ")) -1 #die -1 staat er omdat als je dat niet doet dan print het een dag meer dan dat je wilt
while x <= Dagen_input:
    print(Dagen[x])
    x = x + 1