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
    TIPUS = [
        # roba superior
        "samarreta", "camisa", "americana", "jaqueta",

        # roba inferior
        "pantalons", "texans", "xandall",

        # peces completes
        "vestit",

        # calçat
        "sabates",

        # accessoris
        "ulleres", "barret", "guants"
    ]

    TALLES = ["S", "M", "L", "XL"]
    ESTILS = ["casual", "formal", "sport", "elegant"]

    PREUS = [
        19.99, 29.99, 39.99,
        49.99, 59.99,
        79.99, 99.99, 129.99
    ]

    NUM_PRODUCTES = 20

    with open("products.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
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


# -----------------------------
# MAIN
# -----------------------------
def main():
    crear_users_csv()
    crear_products_csv()


if __name__ == "__main__":
    main()
