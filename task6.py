def isonorfic_check(s, t):
    # Инициализация словарей для отображения символов из s в t и из t в s
    view_s_to_t = {}
    view_t_to_s = {}

    # Проверка, что длины строк совпадают
    if len(s) != len(t):
        return False

    # Перебор символов в строках s и t
    for i in range(len(s)):
        index_s, index_t = s[i], t[i]

        # Проверка отображения из s в t
        if index_s in view_s_to_t:
            # Если символ уже был отображен, проверяем, что отображение корректно
            if view_s_to_t[index_s] != index_t:
                return False
        else:
            # Если символ еще не отображен, добавляем его в отображение
            view_s_to_t[index_s] = index_t

        # Проверка отображения из t в s
        if index_t in view_t_to_s:
            # Если символ уже был отображен, проверяем, что отображение корректно
            if view_t_to_s[index_t] != index_s:
                return False
        else:
            # Если символ еще не отображен, добавляем его в отображение
            view_t_to_s[index_t] = index_s

    # Если все символы соответствуют, строки изоморфны
    return True

# Пример использования
print(isonorfic_check("egg", "add"))      # True
print(isonorfic_check("foo", "bar"))      # False
print(isonorfic_check("paper", "title"))  # True
print(isonorfic_check('города', 'дорога')) # True