import math


def get_player_pos() -> tuple[float, float, float]:
    message = "Enter new coordinates as floats in format 'x,y,z': "
    while True:
        raw_input = input(message)
        parts = raw_input.split(",")
        if len(parts) != 3:
            print("Invalid syntax")
            continue
        coords: list[float] = []
        no_error = True
        for item in parts:
            clean_item = item.strip()
            try:
                coords = coords + [float(clean_item)]
            except ValueError as error:
                print(f"Error on parameter '{clean_item}': {error}")
                no_error = False
                break
        if no_error:
            return (coords[0], coords[1], coords[2])


def ft_coordinate_system() -> None:
    print("=== Game Coordinate System ===")
    print()
    print("Get a first set of coordinates")
    pos1 = get_player_pos()
    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")
    distance = math.sqrt(pos1[0] ** 2 + pos1[1] ** 2 + pos1[2] ** 2)
    print(f"Distance to center: {round(distance, 4)}")
    print()
    print("Get a second set of coordinates")
    pos2 = get_player_pos()
    distance = math.sqrt((pos2[0] - pos1[0]) ** 2 +
                         (pos2[1] - pos1[1]) ** 2 + (pos2[2] - pos1[2]) ** 2)
    print(f"Distance between the 2 sets of coordinates: {round(distance, 4)}")


def main() -> None:
    ft_coordinate_system()


if __name__ == "__main__":
    main()
