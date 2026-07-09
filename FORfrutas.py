frutas = ["manzana","pera","uva","manzana","pera","uva","manzana","pera","piña","manzana","pera","borojó"]



for fruta in set(frutas):
    cantidad = frutas.count(fruta)
    if cantidad >= 2:
        print(f"{fruta}: {cantidad} veces")
    else:
        print(f"{fruta}: {cantidad} vez")