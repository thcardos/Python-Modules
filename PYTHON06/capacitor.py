from ex3 import TransformCreatureFactory
from ex3.creature import Creature, TransformCapability


def test_transform_entity(entity: Creature) -> None:
    print(entity.describe())
    print(entity.attack())
    if isinstance(entity, TransformCapability):
        print(entity.transform())
        print(entity.attack())
        print(entity.revert())


def capacitor_main() -> None:
    print("Testing Creature with transform capability")
    factory = TransformCreatureFactory()

    print("base:")
    base = factory.create_base()
    test_transform_entity(base)

    print("\nevolved:")
    evolved = factory.create_evolved()
    test_transform_entity(evolved)


if __name__ == "__main__":
    capacitor_main()
