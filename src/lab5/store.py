import os

class Order:
    def __init__(self, order_id, products, customer_name, address, phone, priority):
        self.order_id = order_id
        self.products = products
        self.customer_name = customer_name
        self.address = address
        self.phone = phone
        self.priority = priority

    def validate(self):
        errors = []

        # Validate address
        if not self.address or len(self.address.split('. ')) != 4:
            errors.append((1, self.address or "no data"))

        # Validate phone number
        if not self.phone or not self.is_valid_phone():
            errors.append((2, self.phone or "no data"))

        return errors

    def is_valid_phone(self):
        if self.phone.startswith('+'):
            parts = self.phone[1:].split('-')
            return (
            len(parts) == 5 and
            all(part.isdigit() for part in parts) and
            len(parts[0]) == 1 and  
            len(parts[1]) == 3 and
            len(parts[2]) == 3 and  
            len(parts[3]) == 2 and  
            len(parts[4]) == 2      
        )
    
        return False

    def format_products(self):
        product_counts = {}
        for product in self.products.split(', '):
            product_counts[product] = product_counts.get(product, 0) + 1
        return ', '.join(
            f"{product} x{count}" if count > 1 else product
            for product, count in product_counts.items()
        )

    def format_address(self):
        parts = self.address.split('. ')
        return '. '.join(parts[1:]) if len(parts) == 4 else "no data"

    def to_valid_string(self):
        return f"{self.order_id};{self.format_products()};{self.customer_name};{self.format_address()};{self.phone};{self.priority}"

    def __lt__(self, other):
        if self.address.split('. ')[0] == other.address.split('. ')[0]:
            priority_order = {"MAX": 1, "MIDDLE": 2, "LOW": 3}
            return priority_order[self.priority] < priority_order[other.priority]
        return self.address.split('. ')[0] < other.address.split('. ')[0]


def parse_orders(file_path):
    orders = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split(';')
            if len(parts) == 6:
                orders.append(Order(*parts))
    return orders


def save_invalid_orders(orders, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        for order in orders:
            errors = order.validate()
            for error_type, error_value in errors:
                file.write(f"{order.order_id};{error_type};{error_value}\n")


def save_valid_orders(orders, file_path):
    valid_orders = [order for order in orders if not order.validate()]
    valid_orders.sort()
    with open(file_path, 'w', encoding='utf-8') as file:
        for order in valid_orders:
            file.write(order.to_valid_string() + '\n')


if __name__ == "__main__":
    base_path = os.path.join("src", "lab5", "ftxt")
    input_file = os.path.join(base_path, 'order.txt')
    valid_file = os.path.join(base_path, 'order_country.txt')
    invalid_file = os.path.join(base_path, 'non_valid_orders.txt')

    orders = parse_orders(input_file)
    save_invalid_orders(orders, invalid_file)
    save_valid_orders(orders, valid_file)

    print("Done")




