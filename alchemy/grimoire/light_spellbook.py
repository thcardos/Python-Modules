from . import light_validator


def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    validator = light_validator.validate_ingredients(ingredients)
    if "VALID" in validator:
        return f"Spell recorded: {spell_name} ({validator})"
    return (f"Spell rejected: {spell_name} ({validator})")
