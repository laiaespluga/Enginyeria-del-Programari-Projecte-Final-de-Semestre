import csv
import random

# -----------------------------
# FUNCIÓ 1: crear users.csv
# -----------------------------
def crear_users_csv():
    filename = "users.csv"

    headers = [
        "id",
        "nom",
        "email",
        "talla",
        "estils_preferits",
        "primera_comanda",
        "perfil_complet"
    ]

    rows = [
        [1, "Joan Campoy", "joan.campoy@email.com", "M", "casual|sport", True, True],
        [2, "Maria Soler", "maria.soler@email.com", "S", "elegant|formal", False, True],
        [3, "Alex Riera", "alex.riera@email.com", "L", "casual", False, False],
        [4, "Laura Puig", "laura.puig@email.com", "M", "formal|elegant", True, True],
    ]

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(rows)

    print("users.csv creat correctament")


# -----------------------------
# FUNCIÓ 2: crear products.csv
# -----------------------------
def crear_products_csv():
    # Diccionari amb tipus de peça, possibles estils i categoria
    TIPUS_ESTILS_CATEGORIA = {
        # roba superior
        "samarreta": (["casual", "sport"], "superior"),
        "camisa": (["formal", "elegant", "casual"], "superior"),
        "americana": (["formal", "elegant"], "superior"),
        "jaqueta": (["casual", "sport", "elegant"], "superior"),
        "sudadera": (["casual", "sport"], "superior"),
        "top": (["casual", "formal"], "superior"),

        # roba inferior
        "pantalons": (["formal", "elegant", "casual"], "inferior"),
        "texans": (["casual", "sport"], "inferior"),
        "xandall": (["casual", "sport"], "inferior"),
        "faldilla": (["formal","elegant"], "inferior"),

        # peces completes
        "vestit": (["formal", "elegant"], "superior"),

        # calçat
        "sabates": (["formal", "elegant"], "calçat"),
        "vamba": (["formal", "elegant"], "calçat"),
        "botes": (["formal", "elegant"], "calçat"),

        # accessoris
        "ulleres": (["casual", "elegant", "sport"], "accessoris"),
        "barret": (["casual", "elegant", "sport"], "accessoris"),
        "gorra": (["casual", "sport"], "accessoris"),
        "guants": (["elegant", "casual", "sport"], "accessoris")
    }

    TIPUS = list(TIPUS_ESTILS_CATEGORIA.keys())
    TALLES = ["S", "M", "L", "XL"]
    PREUS = [
        19.99, 29.99, 39.99,
        49.99, 59.99,
        79.99, 99.99, 129.99
    ]

    NUM_PRODUCTES = 40

    with open("products.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["id", "tipus", "talla", "estil", "preu", "categoria"])
    
        product_id = 1
    
        for _ in range(NUM_PRODUCTES):
            tipus = random.choice(TIPUS)
            estils_possibles, categoria = TIPUS_ESTILS_CATEGORIA[tipus]
            estil = random.choice(estils_possibles)
            preu = random.choice(PREUS)
    
            if categoria == "accessoris":
                for talla in TALLES:
                    writer.writerow([product_id, tipus, talla, estil, preu, categoria])
                    product_id += 1
            else:
                talla = random.choice(TALLES)
                writer.writerow([product_id, tipus, talla, estil, preu, categoria])
                product_id += 1

    print("products.csv creat correctament")


# -----------------------------
# MAIN
# -----------------------------
def main():
    crear_users_csv()
    crear_products_csv()


if __name__ == "__main__":
    main()

