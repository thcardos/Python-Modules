def ft_count_harvest_recursive():
    days_total = int(input("Days until harvest: "))
    days_left = 1

    def counter(days_left):
        if days_left == days_total:
            print(f"Day {days_total}")
            print("Harvest time!")
        else:
            print(f"Day {days_left}")
            counter(days_left+1)
    counter(days_left)
