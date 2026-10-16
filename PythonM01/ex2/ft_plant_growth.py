class Plant:
    def __init__(
        self,
        day: int,
        name: str,
        height: float,
        age: int,
        total: float
    ) -> None:
        self.day = day
        self.name = name
        self.height = height
        self.age_days = age
        self.total = total

    def grow(self) -> None:
        self.height += self.total
        self.height = round(self.height, 2)

    def age(self) -> None:
        self.day += 1
        self.age_days += 1

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age_days} days old")
        while self.day < 7:
            print(f"=== Day {self.day} ===")
            self.grow()
            self.age()
            print(f"{self.name}: {self.height}cm, {self.age_days} days old")
        if self.day == 7:
            print(f"=== Day {self.day} ===")
            self.grow()
            self.age()
            print(f"{self.name}: {self.height}cm, {self.age_days} days old")
            print(f"Growth this week: {round(self.total * 7, 2)}cm")


def ft_plant_growth(plant: str) -> None:
    rose = Plant(1, "Rose", 25.0, 30, 0.8)
    sunflower = Plant(1, "Sunflower", 80, 45, 0.7)
    cactus = Plant(1, "Cactus", 15, 120, 10)

    if plant == "rose":
        print("=== Garden Plant Growth ===")
        rose.show()
    if plant == "sunflower":
        print("=== Garden Plant Growth ===")
        sunflower.show()
    if plant == "cactus":
        print("=== Garden Plant Growth ===")
        cactus.show()


def main() -> None:
    ft_plant_growth("rose")


if __name__ == "__main__":
    main()
