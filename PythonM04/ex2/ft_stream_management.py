import sys


def ft_stream_management() -> None:
    if len(sys.argv) == 2:
        print("=== Cyber Archives Recovery & Preservation ===")
        print(f"Accessing file '{sys.argv[1]}'")
        try:
            file = open(sys.argv[1])
            read_text = file.read()
            print("---\n")
            print(f"{read_text}")
            print("---")
            file.close()
            print(f"File '{sys.argv[1]}' closed.")
            changed_text = read_text.replace("\n", "#\n")
            print()
            print("Transform data:")
            print("---\n")
            print(f"{changed_text}")
            print("---")
            print("Enter new file name (or empty): ", end="")
            sys.stdout.flush()
            file_name = sys.stdin.readline().replace("\n", "")
            if file_name:
                print(f"Saving data to '{file_name}'")
                try:
                    new_file = open(file_name, "w")
                    new_file.write(changed_text)
                    print(f"Data saved in file '{file_name}'.")
                    new_file.close()
                except OSError as error:
                    print(
                        f"[STDERR] Error opening file '{file_name}': {error}",
                        file=sys.stderr)
                    print("Data not saved.")
            else:
                print("Not saving data.")

        except OSError as error:
            print(
                f"[STDERR] Error opening file '{sys.argv[1]}': {error}",
                file=sys.stderr)
    else:
        print("Usage: ft_stream_management.py <file>")


if __name__ == "__main__":
    ft_stream_management()
