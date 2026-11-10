from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    ok_ingredients = dark_spell_allowed_ingredients()
    lower_ingredients = ingredients.lower()

    for each in ok_ingredients:
        if each in lower_ingredients:
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"