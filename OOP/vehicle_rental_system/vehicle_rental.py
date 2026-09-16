"""
Mini Vehicle Rental Application — Demonstrates Inheritance with Vehicle, Car & Bike.

This module models a vehicle rental system where a base Vehicle class is
extended by Car and Bike child classes, each adding specific attributes.
"""


class Vehicle:
    """
    Base class representing a rental vehicle.

    Attributes:
        vehicle_number   : Unique registration number.
        brand            : Brand of the vehicle.
        model            : Model of the vehicle.
        rental_price_per_day : Rental cost per day in dollars.
    """

    def __init__(self, vehicle_number, brand, model, rental_price_per_day):
        """
        Constructor for Vehicle.

        Args:
            vehicle_number (str): Unique registration number.
            brand (str): Vehicle brand.
            model (str): Vehicle model.
            rental_price_per_day (float): Rental cost per day in dollars.
        """
        self.vehicle_number = vehicle_number
        self.brand = brand
        self.model = model
        self.rental_price_per_day = rental_price_per_day

    def show_vehicle_details(self):
        """Print the shared vehicle details to the console."""
        print(f"Vehicle No:     {self.vehicle_number}")
        print(f"Brand:          {self.brand}")
        print(f"Model:          {self.model}")
        print(f"Rental Price:   ${self.rental_price_per_day}/day")

    def calculate_rent(self, days):
        """
        Calculate the total rental cost for a given number of days.

        Args:
            days (int): Number of rental days.

        Returns:
            float: Total rent, or 0.0 if the duration is invalid.

        Validation:
            - Uses the static method is_valid_rental_days().
        """
        # Validation: number of rental days must be greater than zero
        if not Vehicle.is_valid_rental_days(days):
            print(f"Invalid rental duration: {days} days. Must be greater than zero.")
            return 0.0

        return self.rental_price_per_day * days

    @staticmethod
    def is_valid_rental_days(days):
        """
        Check whether a rental duration is valid.

        Args:
            days (int): Number of rental days to validate.

        Returns:
            bool: True if days is greater than zero, False otherwise.
        """
        return days > 0


class Car(Vehicle):
    """
    Child class representing a car, inheriting from Vehicle.

    Inherits all Vehicle attributes and methods.
    Adds:
        seats : Number of seats in the car.
    """

    def __init__(self, vehicle_number, brand, model, rental_price_per_day, seats):
        """
        Constructor for Car.

        Calls the parent __init__ with super(), then sets the seat count.

        Args:
            vehicle_number (str): Unique registration number.
            brand (str): Car brand.
            model (str): Car model.
            rental_price_per_day (float): Rental cost per day in dollars.
            seats (int): Number of seats.
        """
        # Reuse the parent constructor to set shared attributes
        super().__init__(vehicle_number, brand, model, rental_price_per_day)

        # Car-specific attribute
        self.seats = seats

    def show_vehicle_details(self):
        """
        Override the parent method to include the seat count.
        Calls super().show_vehicle_details() first, then prints car info.
        """
        # Reuse parent's show_vehicle_details method
        super().show_vehicle_details()
        print(f"Seats:          {self.seats}")


class Bike(Vehicle):
    """
    Child class representing a bike, inheriting from Vehicle.

    Inherits all Vehicle attributes and methods.
    Adds:
        engine_capacity : Engine capacity in cc.
    """

    def __init__(self, vehicle_number, brand, model, rental_price_per_day, engine_capacity):
        """
        Constructor for Bike.

        Calls the parent __init__ with super(), then sets engine capacity.

        Args:
            vehicle_number (str): Unique registration number.
            brand (str): Bike brand.
            model (str): Bike model.
            rental_price_per_day (float): Rental cost per day in dollars.
            engine_capacity (int): Engine capacity in cc.
        """
        # Reuse the parent constructor to set shared attributes
        super().__init__(vehicle_number, brand, model, rental_price_per_day)

        # Bike-specific attribute
        self.engine_capacity = engine_capacity

    def show_vehicle_details(self):
        """
        Override the parent method to include engine capacity.
        Calls super().show_vehicle_details() first, then prints bike info.
        """
        # Reuse parent's show_vehicle_details method
        super().show_vehicle_details()
        print(f"Engine Capacity: {self.engine_capacity} cc")


if __name__ == "__main__":
    # --- Create Car objects ---
    car1 = Car("KA-01-1234", "Toyota",  "Corolla",       3500, 5)
    car2 = Car("KA-02-5678", "Hyundai", "Creta",         4200, 5)

    # --- Create Bike objects ---
    bike1 = Bike("KA-03-9012", "Royal Enfield", "Classic 350",  1200, 350)
    bike2 = Bike("KA-04-3456", "Honda",         "Activa 6G",     800, 110)

    # --- Display all vehicles ---
    all_vehicles = [car1, car2, bike1, bike2]

    print("=" * 45)
    print("VEHICLE FLEET")
    print("=" * 45)

    for vehicle in all_vehicles:
        print(f"\n--- {vehicle.__class__.__name__} ---")
        vehicle.show_vehicle_details()

    # --- Demonstrate rental duration validation (static method) ---
    print("\n" + "=" * 45)
    print("RENTAL DURATION VALIDATION (Static Method)")
    print("=" * 45)
    for days in [0, -3, 5]:
        print(f"Valid for {days} days?  {Vehicle.is_valid_rental_days(days)}")

    # --- Calculate rents for several vehicles ---
    print("\n" + "=" * 45)
    print("RENT CALCULATION")
    print("=" * 45)
    print(f"{car1.brand} {car1.model} for 3 days:    ${car1.calculate_rent(3)}")
    print(f"{car2.brand} {car2.model} for 5 days:    ${car2.calculate_rent(5)}")
    print(f"{bike1.brand} {bike1.model} for 2 days:    ${bike1.calculate_rent(2)}")
    print(f"{bike2.brand} {bike2.model} for 7 days:    ${bike2.calculate_rent(7)}")

    # --- Demonstrate invalid duration handling ---
    print("\n" + "=" * 45)
    print("INVALID DURATION DEMO")
    print("=" * 45)
    print(f"{bike1.brand} {bike1.model} for 0 days:   ${bike1.calculate_rent(0)}")