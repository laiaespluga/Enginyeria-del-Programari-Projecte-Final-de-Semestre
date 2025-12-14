import csv
from personal_shopper import PersonalShopper


# ---------- FUNCIONS DE PERSISTÈNCIA ----------

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


def save_users(users, filename="users.csv"):
    fieldnames = [
        "id",
        "nom",
        "email",
        "talla",
        "estils_preferits",
        "primera_comanda",
        "perfil_complet"
    ]

    with open(filename, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for user in users:
            writer.writerow({
                "id": user["id"],
                "nom": user["nom"],
                "email": user["email"],
                "talla": user["talla"],
                "estils_preferits": "|".join(user["estils_preferits"]),
                "primera_comanda": str(user["primera_comanda"]).lower(),
                "perfil_complet": str(user["perfil_complet"]).lower()
            })


# ---------- FUNCIONS DE DOMINI ----------

def find_user_by_name(users, name):
    for user in users:
        if user["nom"].lower() == name.lower():
            return user
    return None


def complete_user_profile(user: dict):
    print("\n--- Completar perfil d'estil ---")

    talla = input("Introdueix la teva talla (S/M/L/XL): ").strip().upper()
    estils = input(
        "Introdueix els teus estils preferits separats per comes "
        "(casual, formal, sport, elegant): "
    )

    user["talla"] = talla
    user["estils_preferits"] = [e.strip().lower() for e in estils.split(",")]
    user["perfil_complet"] = True

    print("Perfil completat correctament.")


# ---------- MAIN ----------

def main():
    print("=" * 60)
    print("Nova Vision - Software Engineering Solutions")
    print("Especialistes en desenvolupament de productes digitals")
    print("=" * 60)
    print()

    print("Benvingut a MyPersonalShopper")
    print("El teu servei de personal shopper en línia")
    print()

    products = load_products()
    users = load_users()

    user_name = input("Introdueix el teu nom d'usuari: ").strip()
    user = find_user_by_name(users, user_name)

    if not user:
        print("Usuari no trobat. Recorda que t'has de crear un perfil primer.")
        print("\nGràcies per utilitzar MyPersonalShopper. Fins aviat!")
        return

    print(f"\nHola {user['nom']}!")

    if not user["perfil_complet"]:
        print("El teu perfil no està complet.")
        complete_user_profile(user)
        save_users(users)

    personal_shopper = PersonalShopper(
        name="Juli Alafia",
        contact="juli.alafia@mypersonalshopper.com"
    )

    personal_shoppers = [
    {
        "name": "Juli Alafia",
        "contact": "juli.alafia@mypersonalshopper.com"
    },
    {
        "name": "Marc Vidal",
        "contact": "marc.vidal@mypersonalshopper.com"
    },
    {
        "name": "Laia Torres",
        "contact": "laia.torres@mypersonalshopper.com"
    }
    ]


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
            print("\n--- Contacte amb el teu Personal Shopper ---")
            message = input("Introdueix el teu missatge (o deixa-ho buit per obtenir el contacte): ").strip()
        
            if message:
                print("\nGràcies pel teu missatge!")
                print("La Juli et respondrà al més aviat possible.")
                print(f"Contacte directe: {personal_shopper.contact}")
            else:
                print(f"\nPots contactar directament amb la Juli a: {personal_shopper.contact}")

        elif option == "3":
            print("\n--- Canviar de Personal Shopper ---")
            print(f"Personal Shopper actual: {personal_shopper.name}")
            print("\nDisponibles:\n")
        
            for idx, ps in enumerate(personal_shoppers, start=1):
                print(f"{idx}. {ps['name']} ({ps['contact']})")
        
            choice = input("\nSelecciona el número del Personal Shopper: ").strip()
        
            if not choice.isdigit():
                print("Selecció no vàlida.")
                continue
        
            choice = int(choice)
        
            if 1 <= choice <= len(personal_shoppers):
                selected_ps = personal_shoppers[choice - 1]
        
                personal_shopper = PersonalShopper(
                    name=selected_ps["name"],
                    contact=selected_ps["contact"]
                )
        
                print(
                    f"\nAra el teu Personal Shopper és {personal_shopper.name} "
                    f"({personal_shopper.contact})"
                )

        elif option == "0":
            print("\nGràcies per utilitzar MyPersonalShopper. Fins aviat!")
            break

        else:
            print("\nOpció no vàlida. Torna-ho a intentar.")
        print("=" * 60)


if __name__ == "__main__":
    main()


        else:
            print("\nOpció no vàlida. Torna-ho a intentar.")


if __name__ == "__main__":
    main()
