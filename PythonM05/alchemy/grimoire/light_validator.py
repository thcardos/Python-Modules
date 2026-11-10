from . import light_spellbook


def validate_ingredients(ingredients: str) -> str:
    ok_ingredients = light_spellbook.light_spell_allowed_ingredients()
    lower_ingredients = ingredients.lower()

    for each in ok_ingredients:
        if each in lower_ingredients:
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"