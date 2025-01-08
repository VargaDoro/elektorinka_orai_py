def felbontas(szam:int):
    ora:int = 0
    perc:int = 0
    mp:int = 0
    while (szam > 0):
        n:int=1
        if (szam < 60):
            mp = szam
            n += 1
        elif (szam < 3600):
            perc = szam // 60
            mp = szam % 60
            n += 1
        else:
            ora = szam // 3600
            perc = (szam % 3600) // 60
            mp = szam % 60
            n += 1
    print(f"{szam*n:>3}mp -> {ora*n:>3}ó, {perc*n:>3}p, {mp*n:>3}mp")

def visszafele(ora:int, perc:int, mp:int):
    szam:int=0
    szam += ora*3600
    szam += perc*60
    szam += mp
    print(f"{ora}ó, {perc}p, {mp}, -> {szam}mp")