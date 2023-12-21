def encrypt_gronsfeld_russian(message, key):
    encrypted_message = ""

    for i, char in enumerate(message):
        # Повторяем ключ циклически, чтобы сделать его таким же длиным, как и сообщение
        current_key = int(key[i % len(key)])

        # Если символ - буква, сдвигаем ее в соответствии с ключом
        if char.isalpha():
            # Определяем базовый символ (А для верхнего регистра, а для нижнего)
            base_char = 'А' if char.isupper() else 'а'
            # Сдвигаем символ с учетом базового символа и ключа
            shifted_char = chr((ord(char) - ord(base_char) + current_key) % 32 + ord(base_char))
            encrypted_message += shifted_char
        else:
            # Если символ не буква, оставляем его без изменений
            encrypted_message += char

    return f"Шифровка: {encrypted_message}"


message = "СОВЕРШЕННОСЕКРЕТНО"
key = "314314314314314314"
print(encrypt_gronsfeld_russian(message, key))