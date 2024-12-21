import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = tk.Tk()
def open_menu_window(root):
    menu_win = tk.Toplevel(root)
    menu_win.title("Restaurant Menu")
    menu_win.geometry("900x700")
    menu_win.configure(bg="#161B33")



    # Sample menu items with categories
    menu_items = {
        "Food Items": [
            {"name": "Burger", "price": 9.99, "image": "Images/burger.jpg"},
            {"name": "Pizza", "price": 12.50, "image": "Images/pizza.jpg"},
            {"name": "Pasta", "price": 8.75, "image": "Images/pasta.jpg"},
            {"name": "Sushi", "price": 14.99, "image": "Images/sushi.jpg"},
            {"name": "Steak", "price": 19.99, "image": "Images/steak.jpg"},
        ],
        "Drinks": [
            {"name": "Water", "price": 1.50, "image": "Images/water.jpg"},
            {"name": "Juice", "price": 3.75, "image": "Images/juice.jpg"},
            {"name": "Soda", "price": 2.50, "image": "Images/soda.jpg"},
            {"name": "Coffee", "price": 2.25, "image": "Images/coffee.jpg"},
        ]
    }

    # Scrollable Frame
    canvas = tk.Canvas(menu_win, bg="#161B33")
    scrollbar = tk.Scrollbar(menu_win, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="#161B33")

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    image_refs = []

    for category, items in menu_items.items():
        category_label = tk.Label(scrollable_frame, text=category,
                                  font=("Arial", 20, "bold"), bg="#161B33", fg="#FFFFFF")
        category_label.pack(pady=10, anchor="w", padx=20)

        category_frame = tk.Frame(scrollable_frame, bg="#161B33")
        category_frame.pack(padx=20, pady=10, fill="x")

        for i, item in enumerate(items):
            item_frame = tk.Frame(category_frame, bg="#1F2C4D", bd=3, relief="raised")
            item_frame.grid(row=i // 2, column=i % 2, padx=10, pady=10, sticky="nsew")
            category_frame.columnconfigure(i % 2, weight=1)

            try:
                pil_image = Image.open(item["image"]).resize((150, 150))
                tk_image = ImageTk.PhotoImage(pil_image)
                print("imported")
            except Exception as e:
                print(f"Error loading image for {item['name']}: {e}")
                tk_image = None

            if tk_image:
                image_refs.append(tk_image)
                img_label = tk.Label(item_frame, image=tk_image, bg="#1F2C4D")
                img_label.pack(pady=5)
            else:
                tk.Label(item_frame, text="[No Image]", bg="#1F2C4D", fg="white").pack(pady=5)

            name_label = tk.Label(item_frame, text=item["name"], font=("Arial", 14, "bold"),
                                  bg="#1F2C4D", fg="white")
            name_label.pack(pady=2)

            price_label = tk.Label(item_frame, text=f"${item['price']:.2f}", font=("Arial", 12),
                                   bg="#1F2C4D", fg="#AAAAAA")
            price_label.pack(pady=2)

            buy_button = tk.Button(item_frame, text="Add to Cart", font=("Arial", 10, "bold"),
                                   bg="#4CAF50", fg="white")
            buy_button.pack(pady=5)

    root.mainloop()

open_menu_window(root)