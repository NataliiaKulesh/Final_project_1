import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'Pharmacy'))
from Pharmacy.exceptions import PharmacyException, MedicineNotAvailableException, UserNotRegisteredException
from Pharmacy.medicine import Medicine
from Pharmacy.pharmacy import Pharmacy


def main():
    """
    Головна функція для запуску системи управління аптекою.

    Реалізує простий текстовий інтерфейс для роботи з такими функціями:
        1. Додавання ліків.
        2. Видача ліків.
        3. Перегляд наявних ліків.
        4. Реєстрація користувачів.
        5. Перегляд зареєстрованих користувачів.
        6. Видалення ліків.
        7. Вихід із програми.

    Всі зміни в даних автоматично зберігаються в файлах *.txt.
    """
    pharmacy = Pharmacy()
    print("Welcome to the pharmacy system!")

    while True:
        print("\n1. Add Medicine")
        print("2. Dispense Medicine")
        print("3. View Medicines")
        print("4. Register User")
        print("5. View Users")
        print("6. Remove Medicines")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter medicine name: ")
            price = float(input("Enter price: "))
            manufacturer = input("Enter manufacturer: ")
            requires_recipe = input("Requires prescription? (yes/no): ").lower() == "yes"
            pharmacy.add_medicine(name, price, manufacturer, requires_recipe)
            pharmacy.save_pharmacy_data()

        elif choice == "2":
            medicine_name = input("Enter medicine name to dispense: ")
            medicine = next((med for med in pharmacy._medicines if med.name == medicine_name), None)
            if medicine:
                medicine.dispense()
                print(f"{medicine_name} has been dispensed.")
            else:
                print(f"Medicine {medicine_name} not found.")

        elif choice == "3":
            print("\nMedicines in Pharmacy:")
            for medicine in pharmacy.get_all_medicines():
                print(
                    f"Name: {medicine.name}, Manufacturer: {medicine.manufacturer}, Price: {medicine.price}, Requires Prescription: {medicine.requires_recipe}")

        elif choice == "4":
            user_id = input("Enter user ID: ")
            name = input("Enter user name: ")
            pharmacy.register_user(user_id, name)
            print(f"User {name} registered.")
            pharmacy.save_pharmacy_data()

        elif choice == "5":
            print("\nRegistered Users:")
            pharmacy.view_users()

        elif choice == "6":
            name = input("Enter medicine name to remove: ")
            pharmacy.remove_medicine(name)
            pharmacy.save_pharmacy_data()

        elif choice == "7":
            break

        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
