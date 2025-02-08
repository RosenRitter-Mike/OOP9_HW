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


# ______Ex. 2_________
def factorial_func(num: int) -> int:
    if num < 0:
        # print("MathError: the factorial of a negative number is not defined")
        raise ValueError("MathError: the factorial of a negative number is not defined")
    elif num == 0 or num == 1:
        return 1
    else:
        return num * factorial_func(num - 1)


# ______Ex. 3_________
def digit_sum_func(num: int) -> int:
    if num < 0:
        return -1 * digit_sum_func(-1 * num)
    elif num == 0:
        return 0
    else:
        return num % 10 + digit_sum_func(num // 10)


# ______Ex. 4_________
def number_appearances_func(num_list: list, num: int) -> int:
    temp_list: list = num_list.copy()
    if len(num_list) == 0:
        return 0
    elif temp_list.pop() == num:
        return 1 + number_appearances_func(temp_list, num)
    else:
        return 0 + number_appearances_func(temp_list, num)



