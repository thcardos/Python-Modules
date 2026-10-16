class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def check_plant() -> None:
    raise PlantError("The tomato plant is wilting!")


def check_water() -> None:
    raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
    specific_tests = [(check_plant, PlantError), (check_water, WaterError)]
    for function, error_type in specific_tests:
        try:
            print(f"Testing {error_type.__name__}...")
            function()
        except error_type as error:
            print(f"Caught {error_type.__name__}: {error}")
            print()
    print("Testing catching all garden errors...")
    for function in [check_plant, check_water]:
        try:
            function()
        except GardenError as error:
            print(f"Caught GardenError: {error}")


def ft_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===")
    print()
    test_custom_errors()
    print()
    print("All custom error types work correctly!")


def main() -> None:
    ft_custom_errors()


if __name__ == "__main__":
    main()
