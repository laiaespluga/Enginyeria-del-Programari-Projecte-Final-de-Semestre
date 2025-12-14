import csv
from personal_shopper import PersonalShopper


# ---------- FUNCIONS AUXILIARS ----------

def load_products(filename="products.csv"):
    products = []
    with open(filename, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["preu"] = float(row["preu"])
            products.append(row)
    return products


def load_users(filename="users.csv"):
    users = []
    with open(filename, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["primera_comanda"] = row["primera_comanda"].lower() == "true"
            row["perfil_complet"] = row["perfil_complet"].lower() == "true"
            row["estils_preferits"] = row["estils_preferits"].split("|")
            users.append(row)
    return users


def find_user_by_name(users, name):
    for user in users:
        if user["nom"].lower() == name.lower():
            return user
    return None


# ---------- MAIN ----------

def main():
    # Introducció empresa
    print("=" * 60)
    print("Nova Vision - Software Engineering Solutions")
    print("Especialistes en desenvolupament de productes digitals")
    print("=" * 60)
    print()

    # Introducció producte
    print("Benvingut a MyPersonalShopper")
    print("El teu servei de personal shopper en línia")
    print()

    # Carregar dades
    products = load_products()
    users = load_users()

    # Login simple
    user_name = input("Introdueix el teu nom d'usuari: ").strip()
    user = find_user_by_name(users, user_name)

    if not user:
        print("Usuari no trobat. Finalitzant programa.")
        return

    print(f"\nHola {user['nom']}!")

    # Comprovar perfil
    if not user["perfil_complet"]:
        print("El teu perfil no està complet.")
        print("Cal completar-lo abans de fer una comanda.")
        # Aquí en el futur es demanaran dades
        return

    # Crear Personal Shopper (simulat)
    personal_shopper = PersonalShopper(
        name="Juli Alafia",
        contact="juli.alafia@mypersonalshopper.com"
    )

    # Menú principal
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Fer una comanda")
        print("2. Parlar amb el meu Personal Shopper")
        print("3. Canviar de Personal Shopper")
        print("0. Sortir")

        option = input("Selecciona una opció: ").strip()

        if option == "1":
            print("\nEl teu Personal Shopper està seleccionant les peces...")
            outfit = personal_shopper.select_outfit(
                user_profile={
                    "talla": user["talla"],
                    "estils_preferits": user["estils_preferits"]
                },
                products=products
            )

            print("\nS'han seleccionat les següents peces:")
            for p in outfit:
                print(
                    f"- {p['tipus']} | "
                    f"Talla: {p['talla']} | "
                    f"Estil: {p['estil']} | "
                    f"Preu: {p['preu']} €"
                )

        elif option == "2":
            # FUTUR: comunicació amb el Personal Shopper
            pass

        elif option == "3":
            # FUTUR: canvi de Personal Shopper
            pass

        elif option == "0":
            print("Gràcies per utilitzar MyPersonalShopper. Fins aviat!")
            break

        else:
            print("Opció no vàlida. Torna-ho a intentar.")


if __name__ == "__main__":
    main()
