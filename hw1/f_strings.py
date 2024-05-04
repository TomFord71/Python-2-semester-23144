def format_number(number):
    # Округляем число до 3 знаков после запятой и форматируем как строку
    formatted_number = f"{number:.3f}"
    # Заменяем разделители тысяч на пробел
    formatted_number = formatted_number.replace(',', ' ').replace('.', ' .')
    # Центрируем строку в окне длиной 30 символов и заменяем пробелы вне строки на '*'
    return formatted_number.center(30, '*')

# Примеры использования
print(format_number(100))
print(format_number(123488482390.28174))
