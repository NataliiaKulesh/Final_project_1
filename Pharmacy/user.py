from Pharmacy.exceptions import PharmacyException


class PharmacyUser:
    """
    Клас, який представляє користувача аптеки.

    Атрибути:
        _user_id (int): Унікальний ідентифікатор користувача.
        _name (str): Ім'я користувача.
        _purchased_medicines (list): Список придбаних ліків.
    """

    def __init__(self, user_id, name):
        """
        Магічний метод, призначений для ініціалізації об'єкту PharmacyUser.

        Параметри:
            user_id (int): Унікальний ідентифікатор користувача.
            name (str): Ім'я користувача.
        """
        self._user_id = user_id
        self._name = name
        self._purchased_medicines = []

    def purchase_medicine(self, medicine):
        """
        Метод, що додає ліки до списку придбаних користувачем.

        Параметри:
            medicine (Medicine): Об'єкт ліків, які видаються користувачеві.

        Викликає:
            PharmacyException: Виняток, якщо наприклад користувач намагається придбати більше ніж 5 ліків.
        """
        if len(self._purchased_medicines) >= 5:
            raise PharmacyException("User cannot purchase more than 5 medicines")
        medicine.dispense()
        self._purchased_medicines.append(medicine)

    @property
    def user_id(self):
        """
        Метод, що повертає унікальний ідентифікатор користувача.

        Повертає:
            int: Ідентифікатор користувача.
        """
        return self._user_id

    @property
    def name(self):
        """
        Метод, що повертає ім'я користувача.

        Повертає:
            str: Ім'я користувача.
        """
        return self._name

    def __str__(self):
        """
        Магічний метод, що повертає текстове представлення користувача.

        Повертає:
            str: Рядок у форматі "User ID: {user_id}, Name: {name}".
        """
        return f"User ID: {self.user_id}, Name: {self.name}"
