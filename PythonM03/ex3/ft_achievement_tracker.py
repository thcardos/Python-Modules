import random


PNK = "\033[1;95m"
CYN = "\033[96m"
BK = "\033[5m"
END = "\033[0m"


def gen_player_achievements(ach_pack: list[str]) -> set[str]:
    random_number = random.randrange(1, 14)
    return set(random.sample(ach_pack, random_number))


def ft_achievement_tracker() -> None:
    ach_pack = ["1.Crafting Genius", "2.Strategist", "3.World Savior",
                "4.Speed Runner", "5.Survivor", "6.Master Explorer",
                "7.Treasure Hunter", "8.Unstoppable", "9.First Steps",
                "10.Collector Supreme", "11.Untouchable", "12.Sharp Mind",
                "13.Boss Slayer"]
    players: dict[str, set[str]] = {
        "Alice": gen_player_achievements(ach_pack),
        "Bob": gen_player_achievements(ach_pack),
        "Charlie": gen_player_achievements(ach_pack),
        "Dylan": gen_player_achievements(ach_pack),
    }
    for player_name, player_ach in players.items():
        print(f"{PNK}Player {player_name}:{END} {player_ach}")
    distinct_ach = set().union(*players.values())
    print()
    print(f"{PNK}All distinct achievements:{END} {distinct_ach}")
    print()
    sets_list = list(players.values())
    common_ach = sets_list[0].intersection(*sets_list[1:])
    print(f"{PNK}Common achievements:{END} {common_ach}")
    print()
    for current_player, current_ach in players.items():
        only_ach = set(current_ach)
        for other_player, other_ach in players.items():
            if current_player != other_player:
                only_ach = only_ach.difference(other_ach)
        print(f"{PNK}Only {current_player} has:{END} {only_ach}")
    print()
    for player_name, player_ach in players.items():
        missing_ach = distinct_ach.difference(player_ach)
        print(f"{PNK}{player_name} is missing:{END} {missing_ach}")


def main() -> None:
    print(f"{BK}{CYN}=== Achievement Tracker System ==={END}")
    print()
    ft_achievement_tracker()


if __name__ == "__main__":
    main()
