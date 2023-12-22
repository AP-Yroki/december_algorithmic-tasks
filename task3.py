def knightDialer(n):
    # Модуль 10^9 + 7
    mod = 10 ** 9 + 7

    # Возможные ходы коня для каждой цифры
    panels = {
        0: [4, 6],
        1: [6, 8],
        2: [7, 9],
        3: [4, 8],
        4: [0, 3, 9],
        5: [],  # 5 ходы отсутсвуют
        6: [0, 1, 7],
        7: [2, 6],
        8: [1, 3],
        9: [2, 4]
    }

    # Массив ways для хранения количества способов для каждой цифры
    ways = [1] * 10

    # Итерация по количеству прыжков
    for _ in range(n - 1):
        # Создаем новый массив для следующего шага
        new_ways = [0] * 10

        # Итерируемся по каждой цифре
        for i in range(10):
            # Для каждой цифры добавляем количество способов из предыдущей цифры,
            # учитывая возможные ходы коня

            for panel in panels[i]:
                new_ways[panel] = (new_ways[panel] + ways[i])

        # Обновляем ways для следующего шага
        ways = new_ways

    # Возвращаем общее количество способов по модулю 10^9 + 7
    return sum(ways) % mod



result = knightDialer(3)
print(result)


print(5 % 2)