class Plant:
    class Stats:
        def __init__(self) -> None:
            self.__grow_count = 0
            self.__age_count = 0
            self.__show_count = 0

        def record_grow(self) -> None:
            self.__grow_count += 1

        def record_age(self) -> None:
            self.__age_count += 1

        def record_show(self) -> None:
            self.__show_count += 1

        def display(self) -> None:
            print(
                f"Stats: {self.__grow_count} grow, "
                f"{self.__age_count} age, "
                f"{self.__show_count} show"
            )

    def __init__(self, name: str, height: float, age_days: int) -> None:
        self._name = name
        self._height = height
        self._age_days = age_days
        self._stats = self.Stats()

    def get_name(self) -> str:
        return self._name

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age_days

    def grow(self, amount: int = 1) -> None:
        self._height += amount
        self._stats.record_grow()

    def age(self, days: int = 1) -> None:
        self._age_days += days
        self._stats.record_age()

    def show(self) -> None:
        self._stats.record_show()
        print(f"{self._name}:", end=" ")
        print(f"{round(self._height, 2)}cm,", end=" ")
        print(f"{self._age_days} days old")

    def display_stats(self) -> None:
        print(f"[statistics for {self._name}]")
        self._stats.display()

    @staticmethod
    def check_age(age_days: int) -> bool:
        return age_days > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)


class Flower(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age_days: int,
        color: str
    ) -> None:
        super().__init__(name, height, age_days)
        self._color = color
        self._bloomed = False

    def bloom(self) -> None:
        self._bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        if self._bloomed:
            print(f"{self.get_name()} is blooming beautifully!")
        else:
            print(f"{self.get_name()} has not bloomed yet")


class Seed(Flower):
    def __init__(
        self,
        name: str,
        height: float,
        age_days: int,
        color: str,
        seeds_count: int,
    ) -> None:
        super().__init__(name, height, age_days, color)
        self._seeds_count = seeds_count

    def show(self) -> None:
        super().show()
        if self._bloomed:
            print(f"Seeds: {self._seeds_count}")
        else:
            print("Seeds: 0")


class Tree(Plant):
    class Stats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self.__shade_count = 0

        def record_shade(self) -> None:
            self.__shade_count += 1

        def display(self) -> None:
            super().display()
            print(f"{self.__shade_count} shade")

    def __init__(
        self,
        name: str,
        height: float,
        age_days: int,
        trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age_days)
        self._trunk_diameter = trunk_diameter
        self._stats: Tree.Stats = self.Stats()

    def produce_shade(self) -> None:
        print(f"Tree {self.get_name()} now produces a shade of", end=" ")
        print(f"{round(self.get_height(), 1)}cm long and", end=" ")
        print(f"{round(self._trunk_diameter, 1)}cm wide.")
        self._stats.record_shade()

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter}cm")


def display_plant_stats(plant: Plant) -> None:
    plant.display_stats()


def ft_garden_analytics() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.check_age(30)}")
    print(f"Is 400 days more than a year? -> {Plant.check_age(400)}\n")
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    display_plant_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow(8)
    rose.bloom()
    rose.show()
    display_plant_stats(rose)
    print()

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_plant_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_plant_stats(oak)
    print()

    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow", 42)
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30)
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    display_plant_stats(sunflower)
    print()

    print("=== Anonymous")
    anonymous = Plant.create_anonymous()
    anonymous.show()
    display_plant_stats(anonymous)


def main() -> None:
    ft_garden_analytics()


if __name__ == "__main__":
    main()
