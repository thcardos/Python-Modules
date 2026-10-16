def ft_count_harvest_iterative():
    days_total = int(input("Days until harvest: "))
    days_left = 1
    while days_left <= days_total:
        print(f"Day {days_left}")
        days_left = days_left+1
    print("Harvest time!")
