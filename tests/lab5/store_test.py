import unittest
from unittest.mock import mock_open, patch
from src.lab5.store import Order, parse_orders, save_invalid_orders, save_valid_orders

class TestOrder(unittest.TestCase):
    def test_order_validation_valid(self):
        order = Order(
            order_id="1",
            products="apple, orange, banana",
            customer_name="John Doe",
            address="1. City. Street. Building",
            phone="+1-123-456-78-90",
            priority="MAX"
        )
        self.assertEqual(order.validate(), [])

    def test_order_validation_invalid_address(self):
        order = Order(
            order_id="2",
            products="apple",
            customer_name="Jane Doe",
            address="InvalidAddress",
            phone="+1-123-456-78-90",
            priority="LOW"
        )
        self.assertIn((1, "InvalidAddress"), order.validate())

    def test_order_validation_invalid_phone(self):
        order = Order(
            order_id="3",
            products="apple",
            customer_name="Jack Doe",
            address="1. City. Street. Building",
            phone="123456",
            priority="MIDDLE"
        )
        self.assertIn((2, "123456"), order.validate())

    def test_format_products(self):
        order = Order(
            order_id="4",
            products="apple, apple, banana",
            customer_name="Jill Doe",
            address="1. City. Street. Building",
            phone="+1-123-456-78-90",
            priority="MAX"
        )
        self.assertEqual(order.format_products(), "apple x2, banana")

    def test_format_address(self):
        order = Order(
            order_id="5",
            products="banana",
            customer_name="Jake Doe",
            address="1. City. Street. Building",
            phone="+1-123-456-78-90",
            priority="LOW"
        )
        self.assertEqual(order.format_address(), "City. Street. Building")

    def test_to_valid_string(self):
        order = Order(
            order_id="6",
            products="apple, banana",
            customer_name="Joe Doe",
            address="1. City. Street. Building",
            phone="+1-123-456-78-90",
            priority="MIDDLE"
        )
        self.assertEqual(
            order.to_valid_string(),
            "6;apple, banana;Joe Doe;City. Street. Building;+1-123-456-78-90;MIDDLE"
        )

    def test_order_comparison(self):
        order1 = Order(
            order_id="7",
            products="apple",
            customer_name="Ann",
            address="1. City. Street. Building",
            phone="+1-123-456-78-90",
            priority="MAX"
        )
        order2 = Order(
            order_id="8",
            products="banana",
            customer_name="Bob",
            address="1. City. Street. Building",
            phone="+1-123-456-78-90",
            priority="LOW"
        )
        self.assertTrue(order1 < order2)

class TestFileOperations(unittest.TestCase):
    @patch("builtins.open", new_callable=mock_open, read_data="1;apple, banana;John Doe;1. City. Street. Building;+1-123-456-78-90;MAX\n")
    def test_parse_orders(self, mock_file):
        orders = parse_orders("dummy_path")
        self.assertEqual(len(orders), 1)
        self.assertEqual(orders[0].customer_name, "John Doe")

    @patch("builtins.open", new_callable=mock_open)
    def test_save_invalid_orders(self, mock_file):
        orders = [
            Order("1", "apple", "John Doe", "InvalidAddress", "+1-123-456-78-90", "MAX"),
            Order("2", "banana", "Jane Doe", "1. City. Street. Building", "InvalidPhone", "LOW")
        ]
        save_invalid_orders(orders, "dummy_path")
        mock_file.assert_called_once_with("dummy_path", "w", encoding="utf-8")
        mock_file().write.assert_any_call("1;1;InvalidAddress\n")
        mock_file().write.assert_any_call("2;2;InvalidPhone\n")

    @patch("builtins.open", new_callable=mock_open)
    def test_save_valid_orders(self, mock_file):
        orders = [
            Order("1", "apple", "John Doe", "1. City. Street. Building", "+1-123-456-78-90", "MAX"),
            Order("2", "banana", "Jane Doe", "1. City. Street. Building", "+1-123-456-78-90", "LOW")
        ]
        save_valid_orders(orders, "dummy_path")
        mock_file.assert_called_once_with("dummy_path", "w", encoding="utf-8")
        mock_file().write.assert_any_call("1;apple;John Doe;City. Street. Building;+1-123-456-78-90;MAX\n")
        mock_file().write.assert_any_call("2;banana;Jane Doe;City. Street. Building;+1-123-456-78-90;LOW\n")

if __name__ == "__main__":
    unittest.main()
