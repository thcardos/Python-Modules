def input_temperature(temp_str: str) -> int:
    print(f"Input data is '{temp_str}'")
    temp = int(temp_str)
    if temp > 40:
        raise Exception(f"{temp}°C is too hot for plants (max 40°C)")
    if temp < 0:
        raise Exception(f"{temp}°C is too cold for plants (min 0°C)")
    return temp


def test_temperature() -> None:
    inputs = ["25", "abc", "100", "-50"]
    for element in inputs:
        try:
            temp_value = input_temperature(element)
            print(f"Temperature is now {temp_value}°C")
            print()
        except Exception as e:
            print(f"Caught input_temperature error: {e}")
            print()
    print("All tests completed - program didn't crash!")


def ft_raise_exception() -> None:
    print("=== Garden Temperature ===")
    print()
    test_temperature()


def main() -> None:
    ft_raise_exception()


if __name__ == "__main__":
    main()
