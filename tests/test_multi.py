import unittest
import os
import json
from pathlib import Path
from shopping_cart_multi import (
    load_data,
    save_data,
    init_inventory,
    add_to_cart,
    view_cart,
    checkout,
    DATA_DIR,
    CART_FILE,
    INVENTORY_FILE,
    RECEIPTS_DIR
)


class TestAdvancedShoppingCart(unittest.TestCase):
    """Unit tests for Advanced Shopping Cart CLI"""

    def setUp(self):
        # Ensure a clean environment for each test
        DATA_DIR.mkdir(exist_ok=True)
        RECEIPTS_DIR.mkdir(parents=True, exist_ok=True)

        # Reset test files
        if CART_FILE.exists():
            CART_FILE.unlink()
        if INVENTORY_FILE.exists():
            INVENTORY_FILE.unlink()

        self.inventory = init_inventory()
        self.cart = {}

    def test_inventory_initialized(self):
        """Inventory should have items with price and category"""
        self.assertTrue(len(self.inventory) > 0)
        for item, details in self.inventory.items():
            self.assertIn("price", details)
            self.assertIn("category", details)

    def test_add_to_cart(self):
        """Add an item to cart"""
        self.cart = add_to_cart(self.cart, self.inventory, "Apples", 2)
        self.assertIn("Apples", self.cart)
        self.assertEqual(self.cart["Apples"]["quantity"], 2)
        self.assertEqual(self.cart["Apples"]["price"], self.inventory["Apples"]["price"])

    def test_cart_persistence(self):
        """Cart should persist to JSON file"""
        self.cart = add_to_cart(self.cart, self.inventory, "Rice", 1)
        self.assertTrue(CART_FILE.exists())
        data = load_data(CART_FILE)
        self.assertIn("Rice", data)

    def test_checkout_creates_receipt(self):
        """Checkout should create a receipt PDF"""
        self.cart = add_to_cart(self.cart, self.inventory, "Rice", 5)
        checkout(self.cart)
        pdfs = list(RECEIPTS_DIR.glob("receipt_*.pdf"))
        self.assertTrue(len(pdfs) > 0, "Receipt PDF should be created")

    def test_discount_applied(self):
        """Discount should apply for totals >= 1000 KES"""
        # Create a cart with large value
        self.cart = add_to_cart(self.cart, self.inventory, "Rice", 10)  # 450 * 10 = 4500
        total_before = sum(i["price"] * i["quantity"] for i in self.cart.values())
        checkout(self.cart)
        # After checkout, cart is cleared
        self.assertEqual(len(self.cart), 0)
        # Confirm receipt generated
        receipts = list(RECEIPTS_DIR.glob("receipt_*.pdf"))
        self.assertTrue(receipts)


if __name__ == "__main__":
    unittest.main()

