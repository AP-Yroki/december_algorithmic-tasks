def calculate_details(N, K, M):
    total_details = 0

    while N >= K:
        # Изготавливаем заготовки
        num_billets = N // K
        total_details += num_billets * (K // M)

        # Сплавляем остатки с предыдущего цикла
        remaining_material = N % K
        N = remaining_material + num_billets * (K % M)

    return f'Количество деталей: {total_details}'


print(calculate_details(100, 10, 5))