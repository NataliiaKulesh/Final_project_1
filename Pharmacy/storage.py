import json
import os


class PharmacyStorage:
    """
    Цей клас призначений для збереження та завантаження даних аптеки у файл.

    Атрибути:
        _medicine_file (str): Шлях до файлу для збереження даних про ліки.
        _user_file (str): Шлях до файлу для збереження даних про користувачів.
    """

    def __init__(self, medicine_file='data/medicines.txt', user_file='data/users.txt'):
        """
        Магічний метод, що ініціалізує об'єкт PharmacyStorage.

        Параметри:
            medicine_file (str): Шлях до файлу з даними про ліки. За замовчуванням 'data/medicines.txt'.
            user_file (str): Шлях до файлу з даними про користувачів. За замовчуванням 'data/users.txt'.
        """
        self._medicine_file = medicine_file
        self._user_file = user_file
        os.makedirs(os.path.dirname(self._medicine_file), exist_ok=True)
        os.makedirs(os.path.dirname(self._user_file), exist_ok=True)

    def save_medicines(self, medicines):
        """
        Метод для зберігання списку ліків у файл.

        Параметри:
            medicines (list): Список об'єктів Medicine для збереження.
        """
        data = [{"name": med.name, "manufacturer": med.manufacturer, "price": med.price} for med in medicines]
        print(f"Saving medicines: {data}")  # Debug print
        with open(self._medicine_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def save_users(self, users):
        """
        Метод для зберігання списку користувачів у файл.

        Параметри:
            users (list): Список об'єктів PharmacyUser для збереження.
        """
        data = [{"user_id": user.user_id, "name": user.name} for user in users]
        with open(self._user_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def load_medicines(self):
        """
        Метод, що вивантажує список ліків із файлу.

        Повертає:
            list: Список кортежів з даними про ліки у форматі (name, price, manufacturer).
        """
        if not os.path.exists(self._medicine_file):
            return []
        with open(self._medicine_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return [(item['name'], item['price'], item['manufacturer']) for item in data]

    def load_users(self):
        """
        Метод, що вивантажує список користувачів із файлу.

        Повертає:
            list: Список кортежів з даними про користувачів у форматі (user_id, name).
        """
        if not os.path.exists(self._user_file):
            return []
        with open(self._user_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return [(item['user_id'], item['name']) for item in data]
