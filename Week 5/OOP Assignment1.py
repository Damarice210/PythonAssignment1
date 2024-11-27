# Base class: Smartphone
class Smartphone:
    def __init__(self, brand, model, storage, battery, price, display):
        self.brand = brand  # Public attribute
        self.model = model  # Public attribute
        self._storage = storage  # Protected attribute
        self.__battery = battery  # Private attribute
        self.price = price  # Public attribute
        self.display = display  # Public attribute

    # Method to display smartphone details
    def display_info(self):
        return (f"{self.brand} {self.model} with {self._storage}GB storage, "
                f"{self.display}-inch display priced at ${self.price}")

    # Encapsulation: Protected method to upgrade storage
    def _upgrade_storage(self, new_storage):
        self._storage = new_storage
        print(f"Storage upgraded to {self._storage}GB")

    # Encapsulation: Private method to check battery
    def __check_battery(self):
        return f"Battery level: {self.__battery}%"

    # Public method to access private method
    def get_battery_status(self):
        return self.__check_battery()

# Child class: GamingSmartphone
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, battery, price, display, gpu):
        super().__init__(brand, model, storage, battery, price, display)
        self.gpu = gpu  # Specific to GamingSmartphone

    # Override method to display gaming features
    def display_info(self):
        return (f"{self.brand} {self.model} (Gaming Edition) with {self.gpu} GPU, "
                f"{self._storage}GB storage, {self.display}-inch display, priced at ${self.price}")

# Creating objects
phone1 = Smartphone("Samsung", "Galaxy S21", 128, 90, 799, 6.2)
phone2 = GamingSmartphone("Apple", "iPhone 14 Pro Max", 256, 90, 1099, 6.7, "A16 Bionic GPU")

# Display details of phones

print(phone1.display_info())  # Samsung Galaxy S21 with 128GB storage, 6.2-inch display priced at $799

print(phone2.display_info())  # Apple iPhone 14 Pro Max (Gaming Edition) with A16 Bionic GPU, 256GB storage, 6.7-inch display, priced at $1099

# Access battery status (encapsulation)
print(phone1.get_battery_status())  # Battery level: 90%

# Upgrade storage using the protected method
phone1._upgrade_storage(256)  # Storage upgraded to 256GB
