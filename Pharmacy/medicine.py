import re
from .exceptions import PharmacyException


class MedicineNameDescriptor:
    """
    Дескриптор який надає назву для ліків і перевіряє чи задано назву.

    Методи:
        __get__(self, instance, owner): Повертає назву ліків.
        __set__(self, instance, value): Перевіряє, чи назва ліків не порожня та відповідає шаблону.
    """
    def __get__(self, instance, owner):
        return instance._name

    def __set__(self, instance, value):
        if not value or not re.match(r'^[A-Za-z0-9\s]+$', value):
            raise ValueError("Enter the name of the medicine")
        instance._name = value


class Medicine:
    """
    Клас який описує ліки.

    Атрибути:
        name (str): Назві ліків, в дескрипторі відбувається перевірка правильності вводу.
        price (float): Вартість ліків.
        manufacturer (str): Виробник ліків.
        _is_available (bool): Доступність ліків (True, якщо є в наявності).

    Методи:
        __str__(): Для виводу інформації про ліки.
        dispense(): Метод для встановлення доступності ліків (False).
        restock(): Метод для встановлення доступності ліків (True).
    """

    name = MedicineNameDescriptor()

    def __init__(self, name, price, manufacturer):
        """
        Ініціалізація об'єкта ліків.

        Параметри:
            name (str): Назва ліків.
            price (float): Ціна ліків.
            manufacturer (str): Виробник ліків.
        """
        self.name = name
        self.price = price
        self.manufacturer = manufacturer
        self._is_available = True

    def __str__(self):
        """
        Використовується для виводу інформації про ліки у текстовому вигляді.

        Формат: "<name> by <manufacturer>, Price: <price> UAH"
        """
        return f"{self.name} by {self.manufacturer}, Price: {self.price} UAH"  # Тепер є manufacturer

    @property
    def price(self):
        """float: Ціна ліків. Має бути додатною величиною."""
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Price must be positive")
        self._price = value

    @property
    def is_available(self):
        """bool: Повертає відмітку чи доступні ліки (True/False)."""
        return self._is_available

    @is_available.setter
    def is_available(self, value):
        if not isinstance(value, bool):
            raise ValueError("is_available must be a boolean value")
        self._is_available = value

    def dispense(self):
        """
        Ставить відмітку на ліках які вже продані як недоступні (False)

        Генерує:
            PharmacyException: Якщо ліки вже недоступні.
        """
        if not self._is_available:
            raise PharmacyException("Medicine is out of stock")
        self._is_available = False

    def restock(self):
        """Позначає доступні ліки (True)."""
        self._is_available = True


class RecipeMedicine(Medicine):
    """
    Клас, який визначає рецептурні ліки.

    Наслідує:
            Medicine

    Атрибути:
            requires_recipe (bool): Чи потрібен рецепт.

    Методи:
            __str__(): Перевизначений метод, з додатковою інформацією про наявність рецепта.
        """

    def __init__(self, name, price, manufacturer, requires_recipe):
        """
        Ініціалізація об'єкта ліків з рецептом

        Параметри:
            name (str): Назва ліків.
            price (float): Ціна ліків.
            manufacturer (str): Виробник ліків.
            requires_recipe (bool): Необхідність додавання рецепту.
        """
        super().__init__(name, price, manufacturer)
        self.requires_recipe = requires_recipe

    def __str__(self):
        """
            Використовується для виводу інформації про ліки з рецептом у текстовому вигляді.

            Формат: "<base_info>, Requires Prescription" або "<base_info>, Over the Counter"
        """
        base_info = super().__str__()
        recipe_info = "Requires Prescription" if self.requires_recipe else "Over the Counter"
        return f"{base_info}, {recipe_info}"
