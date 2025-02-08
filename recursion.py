# ______Ex. 1_________
def range_func(start: int, final: int, jump: int) -> None:
    if jump > 0:
        if final < start:
            print()
            return
    elif jump < 0:
        if final > start:
            print()
            return
    else:
        print("invalid jump\nexiting function")
        return

    print(start, end=" ")
    range_func(start + jump, final, jump)


# ______Ex. 1 test_________
print("=" * 9, " Ex.1 test", "=" * 9)
range_func(8, 15, 3)
range_func(10, 0, -1)
range_func(10, 2, 0)


# ______Ex. 2_________
def factorial_func(num: int) -> int:
    if num < 0:
        print("MathError: the factorial of a negative number is not defined")
    elif num == 1 or num == 0:
        return 1
    else:
        return num * factorial_func(num - 1)


# ______Ex. 2 test_________
print("=" * 9, " Ex.2 test", "=" * 9)
print(f"n! of 5 = {factorial_func(5)}")
print(f"n! of 2 = {factorial_func(2)}")
print(f"n! of 0 = {factorial_func(0)}")
print(f"n! of -3 = {factorial_func(-3)}")


# ______Ex. 3_________
def digit_sum_func(num: int) -> int:
    if num < 0:
        return -1 * digit_sum_func(-1 * num)
    elif num == 0:
        return 0
    else:
        return num % 10 + digit_sum_func(num // 10)


# ______Ex. 3 test_________
print("=" * 9, " Ex.3 test", "=" * 9)
print(f"digit sum of 86 = {digit_sum_func(86)}")
print(f"digit sum of 404 = {digit_sum_func(404)}")
print(f"digit sum of 0 = {digit_sum_func(0)}")
print(f"digit sum of -3456 = {digit_sum_func(-3456)}")


# ______Ex. 4_________
def number_appearances_func(num_list: list, num: int) -> int:
    if len(num_list) == 0:
        return 0
    elif num_list.pop() == num:
        return 1 + number_appearances_func(num_list, num)
    else:
        return 0 + number_appearances_func(num_list, num)


# ______Ex. 4 test_________
print("=" * 9, " Ex.4 test", "=" * 9)
list_numbers: list = [1, -1, 2, -2, 0, -1, -2, -3, 1000, -2, 0]
print(f"list: {list_numbers}\n"
      f"number_appear_func: {number_appearances_func(list_numbers.copy(), -2)}"
      f"\nlist.count(-2): {list_numbers.copy().count(-2)}\n"
      f"Are the results similar:{list_numbers.copy().count(-2) == number_appearances_func(list_numbers.copy(), -2)}")
