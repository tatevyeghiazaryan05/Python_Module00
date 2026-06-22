def ft_count_harvest_recursive() -> None:
    day = int(input("Days until harvest: "))
    ft_helper(1, day)
    print("Harvest time!")


def ft_helper(current: int, day: int) -> None:
    print(f"Day {current}")
    if current < day:
        ft_helper(current + 1, day)
