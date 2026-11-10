from alchemy.grimoire import light_spell_record


def test_kaboom() -> None:
    test = light_spell_record("Fantasy", "(Earth, wind and fire")
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    print(f"Testing record light spell: {test}")


if __name__ == "__main__":
    test_kaboom()