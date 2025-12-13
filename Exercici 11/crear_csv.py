import csv
import random

TIPUS = [
    # roba superior
    "samarreta",
    "camisa",
    "americana",
    "jaqueta",

    # roba inferior
    "pantalons",
    "texans",
    "xandall",

    # peces completes
    "vestit",

    # calçat
    "sabates",

    # accessoris
    "ulleres",
    "barret",
    "guants"
]

TALLES = ["S", "M", "L", "XL"]
ESTILS = ["casual", "formal", "sport", "elegant"]

PREUS = [
    19.99, 29.99, 39.99,
    49.99, 59.99,
    79.99, 99.99, 129.99
]

NUM_PRODUCTES = 20  # pots canviar el número

with open("products.csv", mode="w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "tipus", "talla", "estil", "preu"])

    for i in range(1, NUM_PRODUCTES + 1):
        writer.writerow([
            i,
            random.choice(TIPUS),
            random.choice(TALLES),
            random.choice(ESTILS),
            random.choice(PREUS)
        ])

print("products.csv creat correctament")




"""
CSV USERS:
id,nom,email,talla,estils_preferits,primera_comanda,perfil_complet
1,Joan Campoy,joan.campoy@email.com,M,casual|sport,true,true
2,Maria Soler,maria.soler@email.com,S,elegant|formal,false,true
3,Alex Riera,alex.riera@email.com,L,casual,false,false
4,Laura Puig,laura.puig@email.com,M,formal|elegant,true,true

"""
