#Here We Will Write Any Code That Needs Testing
# from tkinter import *
# from tkinter import ttk,messagebox
# from PIL import Image, ImageTk
# root = Tk()
# root.geometry("500x400")
# root.title("Order Menu")
# root.configure(bg="black")
# photo=ImageTk.PhotoImage(file="project.png")
# image_label=Label(image=photo)
# image_label.pack()
# image_label.image=photo
# title2=Label(root,text="Cuisine Control",bg="black",fg="white")
# title2.pack()
# title2=Label(root,text="FOOD MENU",bg="black",fg="orange",font=("Arial",20,"bold"))
# title2.pack()
# root.mainloop()
#
import tkinter as tk
from tkinter import messagebox

def add_to_cart(item, price):
    cart.append((item, price))
    messagebox.showinfo("Cart", f"{item} has been added to your cart!")

def view_cart():
    cart_window = tk.Toplevel(root)
    cart_window.title("Cart")

    for idx, (item, price) in enumerate(cart, start=1):
        tk.Label(cart_window, text=f"{idx}. {item} - ${price:.2f}").pack()

    tk.Button(cart_window, text="Generate Invoice", command=lambda: generate_invoice(cart_window)).pack()

def generate_invoice(cart_window):
    cart_window.destroy()
    invoice_window = tk.Toplevel(root)
    invoice_window.title("Invoice")

    restaurant_name = "Delicious Eats"
    phone_number = "123-456-7890"
    tax_rate = 0.15

    tk.Label(invoice_window, text=restaurant_name, font=("Arial", 16, "bold")).pack()
    tk.Label(invoice_window, text=f"Phone: {phone_number}", font=("Arial", 12)).pack()

    total_before_tax = sum(price for _, price in cart)
    tax_amount = total_before_tax * tax_rate
    total_with_tax = total_before_tax + tax_amount

    invoice_frame = tk.Frame(invoice_window)
    invoice_frame.pack()

    headers = ["Item", "Quantity", "Unit Price"]
    for col, header in enumerate(headers):
        tk.Label(invoice_frame, text=header, font=("Arial", 10, "bold"), borderwidth=1, relief="solid").grid(row=0, column=col)

    for row, (item, price) in enumerate(cart, start=1):
        tk.Label(invoice_frame, text=item, borderwidth=1, relief="solid").grid(row=row, column=0)
        tk.Label(invoice_frame, text="1", borderwidth=1, relief="solid").grid(row=row, column=1)
        tk.Label(invoice_frame, text=f"${price:.2f}", borderwidth=1, relief="solid").grid(row=row, column=2)

    tk.Label(invoice_window, text=f"Subtotal: ${total_before_tax:.2f}").pack()
    tk.Label(invoice_window, text=f"Tax ({tax_rate * 100}%): ${tax_amount:.2f}").pack()
    tk.Label(invoice_window, text=f"Total: ${total_with_tax:.2f}", font=("Arial", 12, "bold")).pack()

root = tk.Tk()
root.title("Menu")

cart = []

menu_items = {
    "Food": [
        ("Burger", 5.99),
        ("Pizza", 8.99),
        ("Pasta", 7.99),
    ],
    "Drinks": [
        ("Coke", 1.99),
        ("Juice", 2.99),
        ("Water", 0.99),
    ],
    "Salads": [
        ("Greek Salad", 4.99),
        ("Caesar Salad", 5.49),
        ("Garden Salad", 3.99),
    ],
}

for category, items in menu_items.items():
    tk.Label(root, text=category, font=("Arial", 14, "bold")).pack()
    for item, price in items:
        tk.Button(root, text=f"{item} - ${price:.2f}", command=lambda i=item, p=price: add_to_cart(i, p)).pack()

tk.Button(root, text="View Cart", command=view_cart, bg="blue", fg="white").pack()

root.mainloop()
