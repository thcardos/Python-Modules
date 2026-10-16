import sys

RED = "\033[1;31m"
GRN = "\033[1;32m"
PNK = "\033[1;95m"
CYN = "\033[96m"
YLW = "\033[93m"
LGR = "\033[1;30m"
END = "\033[0m"
BK = "\033[5m"


def input_score(score_str: str) -> int:
    score = int(score_str)
    return score


def ps_management(score_data: list[int]) -> None:
    players = len(score_data)
    total_score = sum(score_data)
    average_score = total_score / players
    high_score = max(score_data)
    low_score = min(score_data)
    range_score = high_score - low_score

    print(f" {LGR}Total players: {YLW}{players:<18}{PNK}")
    print(f" {LGR}Total score: {YLW}{total_score}")
    print(f" {LGR}Average score: {YLW}{average_score}")
    print(f" {LGR}High score: {BK}{GRN}{high_score}{END}")
    print(f" {LGR}Low score: {BK}{RED}{low_score}{END}")
    print(f" {LGR}Score range: {YLW}{range_score}")
    print(f"{PNK}╚══════════════════════════════════════════════════╝")


def ft_score_analytics() -> None:
    print(f"{PNK}╔══════════════════════════════════════════════════╗")
    print(f"║{BK}  {CYN}👾⋆˚☆˖°👾  PLAYER  SCORE  ANALYTICS  👾⋆˚☆˖°👾", end="")
    print(f"{END}{PNK}  ║")
    print("╚══════════════════════════════════════════════════╝")
    score_list: list[int] = []
    for arg in sys.argv[1:]:
        try:
            score_list = score_list + [input_score(arg)]
        except ValueError:
            print(f"{LGR}Invalid parameter: {YLW}'{arg}'")
    if score_list:
        print(f" {LGR}Scores processed: {YLW}{score_list}")
        ps_management(score_list)
    else:
        print(f"{RED}No scores provided.", end=" ")
        print("Usage: python3 ft_score_analytics.py <score1> <score2> ...")


def main() -> None:
    ft_score_analytics()


if __name__ == "__main__":
    main()
