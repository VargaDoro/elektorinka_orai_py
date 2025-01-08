import metodusok
import etelek

metodusok.felbontas(59)
metodusok.felbontas(63)
metodusok.felbontas(125)
metodusok.felbontas(3672)
metodusok.felbontas(11502)
print()
metodusok.visszafele(0, 0, 59)
metodusok.visszafele(0, 1, 3)
metodusok.visszafele(0, 2, 5)
metodusok.visszafele(1, 1, 12)
print()

from etelek import Kirat
from etelek import Etelek
etelek_lista=Kirat("etelek_.txt")
Kirat.kiir(etelek_lista)
Kirat.atlag_elkido(etelek_lista)
atlag = etelek_lista.atlag_elkido()
print(f"Átlag elkészítési idő: {atlag} perc")