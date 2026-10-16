def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    if operation_number == 1:
        10/0
    if operation_number == 2:
        open('/non/existent/file')
    if operation_number == 3:
        "str" + 42
    else:
        return


def test_error_types() -> None:
    tests = [0, 1, 2, 3, 4]
    for fail in tests:
        try:
            print(f"Testing operation {fail}...")
            garden_operations(fail)
        except ValueError as error:
            print(f"Caught ValueError: {error}")
        except ZeroDivisionError as error:
            print(f"Caught ZeroDivisionError: {error}")
        except FileNotFoundError as error:
            print(f"Caught FileNotFoundError: {error}")
        except TypeError as error:
            print(f"Caught TypeError: {error}")
        else:
            print("Operation completed successfully")
    try:
        garden_operations(0)
    except (ValueError, ZeroDivisionError, FileNotFoundError):
        print("\nAll error types tested successfully!")


def ft_different_errors() -> None:
    print("=== Garden Error Types Demo ===")
    test_error_types()


def main() -> None:
    ft_different_errors()


if __name__ == "__main__":
    main()
