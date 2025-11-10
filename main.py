# main.py
from models.user import Passenger, Driver, Admin

def main():
    while True:
        print("\n=== Taxi Booking System ===")
        print("1. Register as Passenger")
        print("2. Login as Passenger")
        print("3. Register as Driver")
        print("4. Login as Driver")
        print("5. Login as Admin")
        print("0. Exit")

        choice = input("Select option: ")

        if choice == "1":
            name = input("Name: ")
            username = input("Username: ")
            password = input("Password: ")
            contact = input("Contact: ")

            passenger = Passenger(name, username, password, contact)
            passenger.register()

        elif choice == "2":
            username = input("Username: ")
            password = input("Password: ")
            passenger = Passenger()
            if passenger.login(username, password):
                print(f"Welcome, {passenger._name}!")
                passenger_menu(passenger)
            else:
                print("Login failed!")

        elif choice == "3":
            name = input("Name: ")
            username = input("Username: ")
            password = input("Password: ")
            contact = input("Contact: ")
            driver = Driver()
            if driver.register(name, username, password, contact):
                print("Driver registered successfully!")
            else:
                print("Registration failed. Username may already exist.")

        elif choice == "4":
            username = input("Username: ")
            password = input("Password: ")
            driver = Driver()
            if driver.login(username, password):
                print(f"Welcome, {driver._name}!")
                driver_menu(driver)
            else:
                print("Login failed!")

        elif choice == "5":
            username = input("Admin Username: ")
            password = input("Admin Password: ")
            admin = Admin()
            if admin.login(username, password):
                print(f"Welcome, Admin {admin._name}!")
                admin_menu(admin)
            else:
                print("Login failed!")

        elif choice == "0":
            print("Exiting system.")
            break

        else:
            print("Invalid choice. Try again.")


# Passenger submenu
def passenger_menu(passenger):
    while True:
        print("\n--- Passenger Menu ---")
        print("1. Create Booking")
        print("2. View Booking History")
        print("3. Cancel Booking")
        print("0. Logout")
        choice = input("Select option: ")

        if choice == "1":
            pickup = input("Pickup Location: ")
            drop = input("Drop Location: ")
            price = float(input("Price: "))
            booking = passenger.create_booking(pickup, drop, price)
            print("Booking created:", booking)

        elif choice == "2":
            bookings = passenger.view_booking_history()
            for b in bookings:
                print(b)

        elif choice == "3":
            booking_id = int(input("Booking ID to cancel: "))
            result = passenger.cancel_booking(booking_id)
            if result:
                print("Booking cancelled:", result)
            else:
                print("Cancellation failed.")

        elif choice == "0":
            break
        else:
            print("Invalid option.")


# Driver submenu
def driver_menu(driver):
    while True:
        print("\n--- Driver Menu ---")
        print("1. View Current Bookings")
        print("2. Update Booking Status")
        print("3. View Booking History")
        print("0. Logout")
        choice = input("Select option: ")

        if choice == "1":
            bookings = driver.view_current_bookings()
            for b in bookings:
                print(b)

        elif choice == "2":
            booking_id = int(input("Booking ID to update: "))
            status = input("New Status (Ongoing/Completed): ")
            result = driver.update_booking_status(booking_id, status)
            if result:
                print("Booking updated:", result)
            else:
                print("Update failed.")

        elif choice == "3":
            bookings = driver.view_booking_history()
            for b in bookings:
                print(b)

        elif choice == "0":
            break
        else:
            print("Invalid option.")


# Admin submenu
def admin_menu(admin):
    while True:
        print("\n--- Admin Menu ---")
        print("1. Assign Driver to Booking")
        print("2. View All Bookings")
        print("3. Cancel Booking")
        print("0. Logout")
        choice = input("Select option: ")

        if choice == "1":
            booking_id = int(input("Booking ID: "))
            driver_id = int(input("Driver ID: "))
            result = admin.assign_driver_to_booking(booking_id, driver_id)
            if result:
                print("Driver assigned:", result)
            else:
                print("Assignment failed.")

        elif choice == "2":
            bookings = admin.view_all_bookings()
            for b in bookings:
                print(b)

        elif choice == "3":
            booking_id = int(input("Booking ID to cancel: "))
            result = admin.cancel_booking(booking_id)
            if result:
                print("Booking cancelled:", result)
            else:
                print("Cancellation failed.")

        elif choice == "0":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
