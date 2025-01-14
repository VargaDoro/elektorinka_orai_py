class Etelek:
    def __init__(self, nev, elk_ido):
        self.nev = nev
        try:
            # Megpróbáljuk az elk_ido-t egész számra konvertálni.
            self.elk_ido = int(elk_ido)
        except ValueError:
            # Ha nem sikerül a konverzió, alapértelmezett értéket adunk neki.
            self.elk_ido = 0
        
    def __str__(self):
        return f"{self.nev}: {self.elk_ido}"

class Kirat:
    def __init__(self, fajlnev):
        self.etelek_lista = []
        self._beolvas(fajlnev)

    def _beolvas(self, fajlnev):
        with open(fajlnev, "r", encoding="utf-8") as file:
            for sor in file:
                sor = sor.strip()
                if '$' in sor:
                    nev, elk_ido = sor.split('$')
                    etel = Etelek(nev, elk_ido)
                    self.etelek_lista.append(etel)
                  
    def kiir(self):
        for etel in self.etelek_lista:
            print(etel)

    def atlag_elkido(self):
        if self.etelek_lista:
            return sum(etel.elk_ido for etel in self.etelek_lista) // len(self.etelek_lista)
        return 0
