def felbontas(szam:int):
    ora = 0
    perc = 0
    mp = 0
    if (szam < 60):
        mp = szam
    elif (szam < 3600):
        perc = szam // 60
        mp = szam % 60
    else:
        ora = szam // 3600
        perc = (szam % 3600) // 60
        mp = szam % 60
    print(f"{szam}mp -> {ora}ó, {perc}p, {mp}mp")

def visszafele(ora:int, perc:int, mp:int):
    szam:int=0
    szam += ora*3600
    szam += perc*60
    szam += mp
    print(f"{ora}ó, {perc}p, {mp}, -> {szam}mp")