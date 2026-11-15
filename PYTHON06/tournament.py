from ex3 import CreatureFactory, FlameFactory, TransformCreatureFactory
from ex3.creature import Creature
from ex4 import (
    AggressiveStrategy,
    BattleStrategy,
    NormalStrategy,
    StrategyError,
)


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    combatants: list[tuple[Creature, BattleStrategy]] = []
    for factory, strategy in opponents:
        combatants.append((factory.create_base(), strategy))

    for i in range(len(combatants)):
        for j in range(i + 1, len(combatants)):
            fighter1, strategy1 = combatants[i]
            fighter2, strategy2 = combatants[j]
            print("\n* Battle *")
            print(
                f"{fighter1.describe()} vs. "
                f"{fighter2.describe()} now fight!"
            )
            try:
                strategy1.act(fighter1)
                strategy2.act(fighter2)
            except StrategyError as err:
                print(f"Battle error, aborting tournament: {err}")
                return


def tournament_main() -> None:
    flame_factory = FlameFactory()
    transform_factory = TransformCreatureFactory()

    normal = NormalStrategy()
    aggressive = AggressiveStrategy()

    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Shiftling+Aggressive) ]")
    battle([
        (flame_factory, normal),
        (transform_factory, aggressive),
    ])

    print("\nTournament 1 (error)")
    print("[ (Shiftling+Aggressive), (Flameling+Aggressive) ]")
    battle([
        (transform_factory, aggressive),
        (flame_factory, aggressive),
    ])


if __name__ == "__main__":
    tournament_main()
