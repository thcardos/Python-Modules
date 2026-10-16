class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age

    def get_name(self) -> str:
        return self._name

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_name(self, name: str) -> None:
        self._name = name

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height
            print(f"Height updated: {round(self._height)}cm")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = age
            print(f"Age updated: {self._age} days")


def ft_garden_security() -> None:
    rose = Plant("Rose", 15.0, 10)
    print("=== Garden Security System ===")

    print(f"Plant created: {rose.get_name()}:", end=" ")
    print(f"{rose.get_height()}cm, {rose.get_age()} days old\n")

    rose.set_height(25.0)
    rose.set_age(30)
    print()
    rose.set_height(-42)
    rose.set_age(-67)
    print()

    print(f"Current state: {rose.get_name()}:", end=" ")
    print(f"{rose.get_height()}cm, {rose.get_age()} days old")


def main() -> None:
    ft_garden_security()


if __name__ == "__main__":
    main()
