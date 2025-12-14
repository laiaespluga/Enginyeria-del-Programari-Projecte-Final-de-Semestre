import random

class PersonalShopper:
    def __init__(self, name: str, contact: str):
        self.name = name
        self.contact = contact

    def select_outfit(self, user_profile: dict, products: list) -> list:
        """
        Selecciona 5 peces basant-se en el perfil de l'usuari.

        user_profile: {
            "talla": str,
            "estils_preferits": list[str]
        }

        products: llista de dicts amb claus:
            id, tipus, talla, estil, preu
        """

        talla = user_profile["talla"]
        estils = user_profile["estils_preferits"]

        # 1. Productes que compleixen talla i estil
        matching_products = [
            p for p in products
            if p["talla"] == talla and p["estil"] in estils
        ]

        selected = []

        # 2. Seleccionem fins a 5
        if len(matching_products) >= 5:
            selected = random.sample(matching_products, 5)
        else:
            selected = matching_products.copy()

            # 3. Si no n'hi ha prou, omplim amb qualsevol de la mateixa talla
            remaining = [
                p for p in products
                if p["talla"] == talla and p not in selected
            ]

            needed = 5 - len(selected)
            selected.extend(random.sample(remaining, min(needed, len(remaining))))

        return selected
