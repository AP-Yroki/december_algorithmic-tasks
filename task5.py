def removeDuplicates(nums):
    # значение 2 так как первые два элемента массива всегда остаются без
    # изменений.
    validation = 2

    # Начинаем с третьего элемента массива, так как первые два элемента уже
    # "стабильны".
    for i in range(2, len(nums)):
        # Проверка на уникальность позиции.
        if nums[i] != nums[validation - 2]:
            # Если да, то присваиваем nums[i] к позиции stable и увеличиваем
            # stable.
            nums[validation] = nums[i]
            validation += 1

    # Проходим по оставшейся части массива и устанавливаем значение '_' для
    # элементов, которые не будут показаны.
    for i in range(validation, len(nums)):
        nums[i] = '_'

    # Возвращаем результаты.
    return f"Output: {validation}, nums = {nums}"


nums = [1, 1, 1, 2, 2, 3]


print(removeDuplicates(nums))