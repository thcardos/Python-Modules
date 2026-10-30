import sys


def parse_argument(arg: str, inventory: dict[str, int]) -> None:
    parts = arg.split(":")
    if len(parts) != 2:
        print(f"Error - invalid parameter '{arg}'")
        return
    item_name = parts[0]
    item_quantity = parts[1]
    if item_name in inventory:
        print(f"Redundant item '{item_name}' - discarding")
        return
    try:
        quantity = int(item_quantity)
        inventory[item_name] = quantity
    except ValueError as error:
        print(f"Quantity error for '{item_name}': {error}")


def display_inventory_analysis(inventory: dict[str, int]) -> None:
    print(f"Got inventory: {inventory}")
    item_list = list(inventory.keys())
    print(f"Item list: {item_list}")
    total_quantity = sum(inventory.values())
    print(f"Total quantity of the {len(item_list)} items: {total_quantity}")
    for item_name in item_list:
        item_quantity = inventory[item_name]
        item_percent = item_quantity / total_quantity * 100
        print(f"Item {item_name} represents {round(item_percent, 1)}%")
    most_item = item_list[0]
    least_item = item_list[0]
    for item_name in item_list:
        if inventory[item_name] > inventory[most_item]:
            most_item = item_name
        if inventory[item_name] < inventory[least_item]:
            least_item = item_name
    print(f"Item most abundant: {most_item}", end=" ")
    print(f"with quantity {inventory[most_item]}")
    print(f"Item least abundant: {least_item}", end=" ")
    print(f"with quantity {inventory[least_item]}")


def ft_inventory_system() -> None:
    print("=== Inventory System Analysis ===")
    if len(sys.argv) > 1:
        inventory: dict[str, int] = {}
        for arg in sys.argv[1:]:
            parse_argument(arg, inventory)
        if inventory:
            display_inventory_analysis(inventory)
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


def main() -> None:
    ft_inventory_system()


if __name__ == "__main__":
    main()
