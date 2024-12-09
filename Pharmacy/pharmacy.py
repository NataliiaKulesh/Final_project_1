from .medicine import Medicine, RecipeMedicine
from .user import PharmacyUser
from .exceptions import PharmacyException, MedicineNotAvailableException, UserNotRegisteredException
from .storage import PharmacyStorage


class Pharmacy:
    """
    Клас для керування аптекою.

    Атрибути:
        _medicines (list): Список ліків, доступних в аптеці.
        _users (list): Список зареєстрованих користувачів.
        _storage (PharmacyStorage): Об'єкт для збереження даних аптеки.

    Методи:
        add_medicine(name, price, manufacturer, requires_recipe=False): Додає новий препарат до аптеки.
        register_user(user_id, name): Реєструє нового користувача.
        dispense_medicine(user_id, name): Видає ліки користувачу.
        save_pharmacy_data(): Зберігає дані аптеки у сховище.
        load_pharmacy_data(): Завантажує дані аптеки зі сховища.
        view_users(): Виводить список усіх користувачів.
        remove_medicine(name): Видаляє ліки з аптеки за назвою.
        get_all_medicines(): Повертає список усіх ліків.
    """

    def __init__(self):
        """Ініціалізує об'єкти аптеки порожніми списками."""
        self._medicines = []
        self._users = []
        self._storage = PharmacyStorage()

    def add_medicine(self, name, price, manufacturer, requires_recipe=False):
        """
        Додає новий препарат до аптеки.

        Параметри:
            name (str): Назва ліків.
            price (float): Ціна ліків.
            manufacturer (str): Виробник ліків.
            requires_recipe (bool): Чи потрібен рецепт на ліки. (False/True).
        """
        if requires_recipe:
            self._medicines.append(RecipeMedicine(name, price, manufacturer, requires_recipe))
        else:
            self._medicines.append(Medicine(name, price, manufacturer))
        print(f"Medicine '{name}' added successfully.")

    def register_user(self, user_id, name):
        """
        Метод для реєстрації нового користувача.

        Параметри:
            user_id (int): Унікальний ідентифікатор користувача.
            name (str): Ім'я користувача.
        """
        self._users.append(PharmacyUser(user_id, name))

    def dispense_medicine(self, user_id, name):
        """
        Метод який видає ліки користувачу.

        Параметри:
            user_id (int): Ідентифікатор користувача.
            name (str): Назва ліків.

        Генерує:
            UserNotRegisteredException: Виключення, якщо користувач не зареєстрований.
            MedicineNotAvailableException: Виключення, якщо ліки відсутні.
        """
        user = next((u for u in self._users if u.user_id == user_id), None)
        if not user:
            raise UserNotRegisteredException(f"User with ID '{user_id}' is not registered.")

        medicine = next((m for m in self._medicines if m.name == name), None)
        if not medicine:
            raise MedicineNotAvailableException(f"Medicine '{name}' not found in the pharmacy.")

        if not medicine.is_available:
            raise MedicineNotAvailableException(f"Medicine '{name}' is out of stock.")

        user.purchase_medicine(medicine)

    def save_pharmacy_data(self):
        """Зберігає дані про ліки та користувачів у сховище."""
        self._storage.save_medicines(self._medicines)
        self._storage.save_users(self._users)

    def load_pharmacy_data(self):
        """Завантажує дані про ліки та користувачів із сховища."""
        for name, manufacturer, price in self._storage.load_medicines():
            self.add_medicine(name, float(price), manufacturer)

        for user_id, name in self._storage.load_users():
            self.register_user(user_id, name)

    def view_users(self):
        """Виводить інформацію про всіх зареєстрованих користувачів."""
        for user in self._users:
            print(user)

    def remove_medicine(self, name):
        """
        Метод для видалення ліків з аптеки за назвою.

        Параметри:
            name (str): Назва ліків які потрібно видалити.
        """
        medicine = next((m for m in self._medicines if m.name == name), None)
        if not medicine:
            print(f"Medicine '{name}' not found.")
            return
        self._medicines.remove(medicine)
        print(f"Medicine '{name}' removed successfully.")

    def get_all_medicines(self):
        """
        Геттер для виведення списку усіх ліків.

        Повертає:
            list: Список об'єктів Medicine.
        """
        return self._medicines
