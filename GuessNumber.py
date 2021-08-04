import numpy as np


def game_core_v2(number):
    count = 1
    list_numbers = [number for num in range(1, 101)]
    predict = list_numbers[49]
    mx, mn = list_numbers[-1], list_numbers[0]
    while number != predict:
        count += 1
        if number > predict:
            mn = predict
        elif number < predict:
            mx = predict + 1
        predict = mn + (mx - mn) // 2
        return count