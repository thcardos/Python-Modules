def secure_archive(
    filename: str,
    action: str = "read",
    content: str = ""
) -> tuple[bool, str]:
    try:
        if action == "read":
            with open(filename, 'r') as file:
                content = file.read()
                return (True, content)
        elif action == "write":
            with open(filename, 'w') as file:
                file.write(content)
                return (True, 'Content successfully written to file')
        else:
            return (False, f"Invalid action: '{action}'")
    except OSError as error:
        return (False, str(error))


def ft_vault_security() -> None:
    print("=== Cyber Archives Security ===")
    print()
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))
    print()
    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/shadow"))
    print()
    print("Using 'secure_archive' to read from a regular file:")
    original_text = secure_archive("ancient_fragment.txt")
    print(original_text)
    print()
    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive("new_file.txt", "write", original_text[1]))


if __name__ == "__main__":
    ft_vault_security()
