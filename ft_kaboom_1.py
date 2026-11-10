def test_kaboom() -> None:
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
    try:
        from alchemy.grimoire.dark_spellbook import dark_spell_record  # noqa: F401
    except ImportError as e:
        print(f"Caught expected error: {e}")


if __name__ == "__main__":
    test_kaboom()