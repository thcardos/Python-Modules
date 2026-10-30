import sys


def ft_ancient_text() -> None:
    if len(sys.argv) == 2:
        print("=== Cyber Archives Recovery ===")
        print(f"Accessing file '{sys.argv[1]}'")
        try:
            file = open(sys.argv[1])
            read_text = file.read()
            print("---\n")
            print(f"{read_text}")
            print("---")
            file.close()
            print(f"File '{sys.argv[1]}' closed.")
        except OSError as error:
            print(f"Error opening file '{sys.argv[1]}': {error}")
    else:
        print("Usage: ft_ancient_text.py <file>")


if __name__ == "__main__":
    ft_ancient_text()
