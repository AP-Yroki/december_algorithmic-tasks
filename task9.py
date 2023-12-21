def asteroidCollision(asteroids):
    stack = []

    for asteroid in asteroids:
        # Пока стек не пуст и текущий астероид направлен влево
        while stack and asteroid < 0:
            # Проверяем астероиды в стеке
            top = stack.pop()

            # Определяем, какой астероид взорвется
            if top == -asteroid:
                # Оба астероида взрываются, прерываем цикл
                break
            elif top > -asteroid:
                # Текущий астероид взрывается, возвращаем в стек предыдущий
                # астероид
                stack.append(top)
                # Прерываем цикл, так как текущий астероид взорвет предыдущий
                break
        else:
            # Если стек пуст или текущий астероид направлен вправо,
            # добавляем его в стек
            stack.append(asteroid)

    return stack

# Примеры использования
print(asteroidCollision([5, 10, -5]))
print(asteroidCollision([8, -8]))