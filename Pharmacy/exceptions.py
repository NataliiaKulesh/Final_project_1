"""
Модуль для визначення власних виключень для системи керування аптекою.
- PharmacyException: базовий клас для всіх виключень в аптеці.
- MedicineNotAvailableException: виключення для ситуацій, коли ліки не доступні.
- UserNotRegisteredException: виключення для ситуацій, коли користувач не зареєстрований.
"""

class PharmacyException(Exception):
    """Базовий клас для всіх виключень в аптеці."""
    pass


class MedicineNotAvailableException(PharmacyException):
    """Виключення для ситуацій, коли ліки не доступні"""
    pass


class UserNotRegisteredException(PharmacyException):
    """Виключення для випадків, коли користувач не зареєстрований."""
    pass
