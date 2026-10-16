import sys


def ft_command_quest() -> None:
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    arg_count = 1

    if sys.argv[1:]:
        print(f"Arguments received: {len(sys.argv[1:])}")
        while arg_count <= len(sys.argv[1:]):
            print(f"Argument {arg_count}: {sys.argv[arg_count]}")
            arg_count += 1
    else:
        print("No arguments provided!")
    print(f"Total arguments: {len(sys.argv)}")


def main() -> None:
    ft_command_quest()


if __name__ == "__main__":
    main()
