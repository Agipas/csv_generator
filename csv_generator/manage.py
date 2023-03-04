#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'csv_generator.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

# TODO:
# 1 створити сторінку з інформацією про схему
#   - можна видалити схему
#   - подивитися поля слеми і колонки
#   - згенерувати файл
#   - подивитися згенеровані файли
# 2 дати пожливість показати мої таблички
# 3 заборонити редагування,видалення чужих табличок, і на всі інші функції поставити обмеження
# 4 генерувати файли
# 5 не залогіненому користувачеві заборонити все
# 6 для кожного поля в формі нормально нормала описати стиль а не в фор(циклі)
# 7 не показувати від-до для всіх полів, тільки для інтежерів
# 8 налаштувати ордер полів для колмс
# 9 розділити на інклуди таблички в хтмл
