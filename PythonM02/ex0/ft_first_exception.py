def input_temperature(temp_str: str) -> int:
    print(f"Input data is '{temp_str}'")
    temp = int(temp_str)
    return temp


def test_temperature() -> None:
    inputs = ["25", "abc"]
    for element in inputs:
        try:
            temp_value = input_temperature(element)
            print(f"Temperature is now {temp_value}°C")
            print()
        except ValueError as e:
            print(f"Caught input_temperature error: {e}")
            print()
    print("All tests completed - program didn't crash!")


def ft_first_exception() -> None:
    print("=== Garden Temperature ===")
    print()
    test_temperature()


def main() -> None:
    ft_first_exception()


if __name__ == "__main__":
    main()
