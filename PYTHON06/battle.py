from ex3 import CreatureFactory, FlameFactory, TransformCreatureFactory


def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())

    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())


def battle(factory1: CreatureFactory, factory2: CreatureFactory) -> None:
    print("Testing battle")
    fighter1 = factory1.create_base()
    fighter2 = factory2.create_base()
    print(f"{fighter1.describe()} vs. {fighter2.describe()} fight!")
    print(fighter1.attack())
    print(fighter2.attack())


def battle_main() -> None:
    flame_factory = FlameFactory()
    transform_factory = TransformCreatureFactory()

    test_factory(flame_factory)
    print()
    test_factory(transform_factory)
    print()
    battle(flame_factory, transform_factory)


if __name__ == "__main__":
    battle_main()
