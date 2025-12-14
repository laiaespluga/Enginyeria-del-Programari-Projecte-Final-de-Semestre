import random

class PersonalShopper:
    def __init__(self, name: str, contact: str):
        self.name = name
        self.contact = contact

    def select_outfit(self, user_profile: dict, products: list) -> list:
        talla = user_profile["talla"]
        estils = user_profile["estils_preferits"]

        # 1 Intentar trobar 5 peces d'un sol estil
        for estil in estils:
            same_style = [
                p for p in products
                if p["talla"] == talla and p["estil"] == estil
            ]
            if len(same_style) >= 5:
                return random.sample(same_style, 5)

        # 2 Barrejar només estils preferits
        preferred_style_products = [
            p for p in products
            if p["talla"] == talla and p["estil"] in estils
        ]

        if len(preferred_style_products) >= 5:
            return random.sample(preferred_style_products, 5)

        # 3 Fallback: qualsevol peça de la mateixa talla
        same_size_products = [
            p for p in products
            if p["talla"] == talla
        ]

        return random.sample(
            same_size_products,
            min(5, len(same_size_products))
        )

