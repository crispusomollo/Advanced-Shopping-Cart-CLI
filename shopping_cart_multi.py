#!/usr/bin/env python3
"""
Advanced Shopping Cart CLI with Command-Line Flags
Author: Chris Origi
License: MIT
"""

import json
import argparse
from datetime import datetime
from pathlib import Path

# ✅ Safe color import
try:
    from termcolor import colored
except ImportError:
    def colored(text, color=None, attrs=None):
        return text

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# ---------- Paths ----------
DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)
CART_FILE = DATA_DIR / "cart.json"
INVENTORY_FILE = DATA_DIR / "inventory.json"
RECEIPTS_DIR = DATA_DIR / "receipts"
RECEIPTS_DIR.mkdir(parents=True, exist_ok=True)


# ---------- Utility ----------
def load_data(file_path):
    if file_path.exists():
        try:
            with open(file_path, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {}
    return {}


def save_data(file_path, data):
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)


def init_inventory():
    """Create or reset inventory."""
    inventory = {
        "Apples": {"price": 120, "category": "Fruits"},
        "Rice": {"price": 450, "category": "Groceries"},
        "Milk": {"price": 200, "category": "Dairy"},
        "Bread": {"price": 150, "category": "Bakery"},
        "Eggs": {"price": 20, "category": "Dairy"},
    }
    save_data(INVENTORY_FILE, inventory)
    return inventory


def repair_inventory(inventory):
    """Auto-repair missing keys."""
    repaired = False
    for name, details in inventory.items():
        if "category" not in details:
            details["category"] = "General"
            repaired = True
        if "price" not in details:
            details["price"] = 0
            repaired = True
    if repaired:
        save_data(INVENTORY_FILE, inventory)
        print(colored("🛠 Inventory repaired and updated.", "yellow"))
    return inventory


# ---------- Core Features ----------
def generate_receipt(cart, total, discount, grand_total):
    now = datetime.now().strftime("%Y%m%d_%H%M%S")
    receipt_file = RECEIPTS_DIR / f"receipt_{now}.pdf"
    c = canvas.Canvas(str(receipt_file), pagesize=letter)
    c.setFont("Helvetica", 12)
    c.drawString(200, 750, "Advanced Shopping Cart Receipt")
    c.drawString(50, 730, f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    y = 700
    c.drawString(50, y, "Item")
    c.drawString(250, y, "Price")
    c.drawString(350, y, "Qty")
    c.drawString(450, y, "Total")
    y -= 20
    for name, details in cart.items():
        subtotal = details['price'] * details['quantity']
        c.drawString(50, y, name)
        c.drawString(250, y, f"{details['price']:.2f}")
        c.drawString(350, y, str(details['quantity']))
        c.drawString(450, y, f"{subtotal:.2f}")
        y -= 20
    y -= 20
    c.drawString(50, y, f"Subtotal: {total:.2f}")
    y -= 20
    c.drawString(50, y, f"Discount: {discount:.2f}")
    y -= 20
    c.drawString(50, y, f"Grand Total: {grand_total:.2f}")
    c.save()
    print(colored(f"🧾 Receipt saved to {receipt_file}", "green"))


def view_inventory(inventory):
    inventory = repair_inventory(inventory)
    print(colored("\nAvailable Inventory:", "yellow", attrs=["bold"]))
    for name, details in inventory.items():
        print(f"- {name} ({details['category']}): {details['price']} KES")


def add_to_cart(cart, inventory, item, quantity):
    item = item.title()
    if item not in inventory:
        print(colored("❌ Item not found in inventory!", "red"))
        return cart

    if item in cart:
        cart[item]["quantity"] += quantity
    else:
        cart[item] = {"price": inventory[item]["price"], "quantity": quantity}

    save_data(CART_FILE, cart)
    print(colored(f"✅ {item} x{quantity} added to cart!", "green"))
    return cart


def view_cart(cart):
    if not cart:
        print(colored("🛒 Cart is empty.", "red"))
        return
    print(colored("\nYour Cart:", "cyan", attrs=["bold"]))
    total = 0
    for item, details in cart.items():
        subtotal = details['price'] * details['quantity']
        total += subtotal
        print(f"- {item}: {details['quantity']} x {details['price']} = {subtotal} KES")
    print(colored(f"\nTotal: {total} KES", "green"))


def checkout(cart):
    if not cart:
        print(colored("🛒 Cart is empty.", "red"))
        return
    total = sum(details["price"] * details["quantity"] for details in cart.values())
    discount = total * 0.1 if total >= 1000 else 0
    if discount:
        print(colored(f"💰 10% discount applied! You saved {discount:.2f} KES", "green"))
    grand_total = total - discount
    print(colored(f"Grand Total: {grand_total:.2f} KES", "yellow", attrs=["bold"]))
    generate_receipt(cart, total, discount, grand_total)
    cart.clear()
    save_data(CART_FILE, cart)


# ---------- CLI Parser ----------
def parse_args():
    parser = argparse.ArgumentParser(
        description="Advanced Shopping Cart CLI (Interactive + Flag mode)"
    )
    parser.add_argument("--inventory", action="store_true", help="View available inventory")
    parser.add_argument("--add", nargs=2, metavar=("ITEM", "QTY"), help="Add item and quantity")
    parser.add_argument("--view-cart", action="store_true", help="View cart contents")
    parser.add_argument("--checkout", action="store_true", help="Perform checkout and generate receipt")
    return parser.parse_args()


# ---------- Main ----------
def main():
    args = parse_args()
    cart = load_data(CART_FILE)
    inventory = load_data(INVENTORY_FILE)
    if not inventory:
        inventory = init_inventory()

    # --- Non-interactive flag mode ---
    if any(vars(args).values()):
        if args.inventory:
            view_inventory(inventory)
        if args.add:
            item, qty = args.add
            try:
                qty = int(qty)
                cart = add_to_cart(cart, inventory, item, qty)
            except ValueError:
                print(colored("❌ Quantity must be a number.", "red"))
        if args.view_cart:
            view_cart(cart)
        if args.checkout:
            checkout(cart)
        return

    # --- Interactive mode ---
    while True:
        print(colored("\n=== Advanced Shopping Cart CLI ===", "cyan", attrs=["bold"]))
        print("1. View Inventory")
        print("2. Add Item to Cart")
        print("3. View Cart")
        print("4. Checkout")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            view_inventory(inventory)
        elif choice == "2":
            item = input("Enter item name: ")
            qty = input("Enter quantity: ")
            try:
                qty = int(qty)
                cart = add_to_cart(cart, inventory, item, qty)
            except ValueError:
                print(colored("❌ Invalid quantity!", "red"))
        elif choice == "3":
            view_cart(cart)
        elif choice == "4":
            checkout(cart)
        elif choice == "5":
            print(colored("👋 Goodbye!", "cyan"))
            break
        else:
            print(colored("Invalid choice! Try again.", "red"))


if __name__ == "__main__":
    main()
