import random


def ft_data_alchemist() -> None:
    names = ["Alice", "bob", "Charlie", "dylan",
             "Emma", "Gregory", "john", "kevin", "Liam"]
    print(f"Initial list of players: {names}\n")
    capitalize_names = [player.capitalize() for player in names]
    print(f"New list with all names capitalized: {capitalize_names}\n")
    only_capitalized = [player for player in names if player[0].isupper()]
    print(f"New list of capitalized names only: {only_capitalized}\n")
    score_dictionary = {player: random.randint(
        1, 1000) for player in capitalize_names}
    print(f"Score dict: {score_dictionary}\n")
    score_average = round(sum(score_dictionary.values()) /
                          len(score_dictionary.values()), 2)
    print(f"Score average is {score_average}\n")
    high_scores = {player: score for player,
                   score in score_dictionary.items() if score > score_average}
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    print("=== Game Data Alchemist ===\n")
    ft_data_alchemist()
