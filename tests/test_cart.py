import unittest
import json
from pathlib import Path
from shopping_cart_multi import (
    load_data,
    save_data,
    init_inventory,
    DATA_DIR
)


class TestCartHelpers(unittest.TestCase):
    """Tests for file and helper functions in the Advanced Shopping Cart CLI."""

    def setUp(self):
        self.temp_file = DATA_DIR / "temp_test.json"
        if self.temp_file.exists():
            self.temp_file.unlink()

    def tearDown(self):
        if self.temp_file.exists():
            self.temp_file.unlink()

    def test_save_and_load_data(self):
        """save_data() should correctly write and load_data() should read JSON"""
        sample = {"Apples": {"price": 120, "category": "Fruits"}}
        save_data(self.temp_file, sample)
        loaded = load_data(self.temp_file)
        self.assertEqual(sample, loaded)

    def test_load_data_missing_file(self):
        """load_data() should return an empty dict for missing files"""
        if self.temp_file.exists():
            self.temp_file.unlink()
        result = load_data(self.temp_file)
        self.assertEqual(result, {})

    def test_load_data_invalid_json(self):
        """load_data() should handle invalid JSON gracefully"""
        with open(self.temp_file, "w") as f:
            f.write("{invalid json}")
        result = load_data(self.temp_file)
        self.assertEqual(result, {})

    def test_init_inventory_creates_valid_inventory(self):
        """init_inventory() should return dict with categories and prices"""
        inventory = init_inventory()
        self.assertTrue(isinstance(inventory, dict))
        self.assertIn("Apples", inventory)
        details = inventory["Apples"]
        self.assertIn("price", details)
        self.assertIn("category", details)
        self.assertIsInstance(details["price"], (int, float))
        self.assertIsInstance(details["category"], str)


if __name__ == "__main__":
    unittest.main()

