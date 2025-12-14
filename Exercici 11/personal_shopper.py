
class PersonalShopper:
    def __init__(self, name: str, contact: str):
        self.name = name
        self.contact = contact

    def select_outfit(self, user_profile: dict, products: list) -> list:
        talla = user_profile["talla"]
        estils = user_profile["estils_preferits"]

        selected = []
        used_categories = set()

        # 1 Intentar trobar peces d'un sol estil
        for estil in estils:
            for p in products:
                if p["talla"] != talla or p["estil"] != estil:
                    continue

                if p["categoria"] in ["superior", "inferior", "calçat"]:
                    if p["categoria"] in used_categories:
                        continue
                    used_categories.add(p["categoria"])

                selected.append(p)
                if len(selected) == 5:
                    return selected

        # 2 Barrejar només estils preferits
        for p in products:
            if p["talla"] != talla or p["estil"] not in estils:
                continue

            if p in selected:
                continue

            if p["categoria"] in ["superior", "inferior", "calçat"]:
                if p["categoria"] in used_categories:
                    continue
                used_categories.add(p["categoria"])

            selected.append(p)
            if len(selected) == 5:
                return selected

        # 3 Preguntar si vol completar amb altres estils
        if len(selected) < 5:
            print(
                "No hi ha més peces del teu estil."
            )
            choice = input(
                f"Vols fer la comanda amb {len(selected)} o amb 5? "
            ).strip().lower()
        
            if choice != "5":
                return selected

        # 4 Fallback: qualsevol peça de la mateixa talla
        for p in products:
            if p["talla"] != talla:
                continue

            if p in selected:
                continue

            if p["categoria"] in ["superior", "inferior", "calçat"]:
                if p["categoria"] in used_categories:
                    continue
                used_categories.add(p["categoria"])

            selected.append(p)
            if len(selected) == 5:
                break

        return selected
