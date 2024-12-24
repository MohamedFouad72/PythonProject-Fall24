import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
import os


# Dictionary storing user credentials and roles
users = {
    "manager@pos.com": {"password": "1234", "role": "manager"},
    "staff@pos.com":   {"password": "5678", "role": "staff"}
}

# Sample menu items (used in Inventory screen)
menuItems = [
    {"name": "Meat", "stock": 1000},
    {"name": "Chicken", "stock": 850},
    {"name": "Pasta", "stock": 1500},
    {"name": "Cola", "stock": 2000},
    {"name": "Cola", "stock": 2000},
    {"name": "Tomatoes", "stock": 3500},
    {"name": "Sauces", "stock": 2500},
    {"name": "potatoes", "stock": 3000},
    {"name": "Bread", "stock": 1500},
    {"name": "Cheese", "stock": 2000},
    {"name": "Spices", "stock": 1000},
    {"name": "Milk", "stock": 5020},
    {"name": "Butter", "stock": 200},
    {"name": "Rice", "stock": 800},
    {"name": "Sugar", "stock": 200},
    {"name": "Oil", "stock": 4000},
    {"name": "Vinegar", "stock": 5000},
    {"name": "Ketchup", "stock": 500},
    {"name": "Mustard", "stock": 600},
    {"name": "Mayonnaise", "stock": 160},
    {"name": "Pickles", "stock": 560},
    {"name": "Flour", "stock": 450},
    {"name": "Eggs", "stock": 860},
    {"name": "Shrimp", "stock": 600},
    {"name": "Fish", "stock": 900},
    # ... etc ...
]

# ------------------ NO BUTTONS NAVBAR CREATOR ------------------ #
def create_navbar_buttonless_in_window(window, root):

    navbar = Frame(window, bg="#0D1B42", height=50)
    navbar.pack(side="top", fill="x")
    logo_path = "Images/cuisine control white png.png"
    if logo_path:
        loaded_img = Image.open(logo_path)
        loaded_img = loaded_img.resize((120, 120))
        logo_img = ImageTk.PhotoImage(loaded_img)

        logo_label = Label(navbar, image=logo_img, bg="#0D1B42")
        logo_label.image = logo_img  # Keep reference
        logo_label.pack(side="top", padx=10, pady=5)
    else:
        Label(navbar, text="CuisineControl", bg="#0D1B42", fg="white",
              font=("Arial", 14, "bold")).pack(side="left", padx=10)

# ------------------ ORDER WINDOW ------------------ #
def open_order_window(root):
    order_win = tk.Toplevel(root)
    order_win.title("Order Screen")
    order_win.geometry("700x600")
    order_win.configure(bg="#161B33")

    create_navbar_buttonless_in_window(order_win, root)

    title_label = ttk.Label(order_win, text="Order", font=("Arial", 20, "bold"),
                            background="#161B33", foreground="white")
    title_label.pack(padx=10, pady=10)

    times_list = [f"{hour:02d}:{minute:02d}" for hour in range(24) for minute in range(60)]
    time_entry = ttk.Combobox(order_win, width=40, values=times_list)
    time_entry.set("Select Time")
    time_entry.pack(padx=10, pady=10)

    # Create a Treeview
    columns = ("Time", "Type", "Quantity", "Price", "Employee Name", "The Check")
    table = ttk.Treeview(order_win, columns=columns, show="headings", height=10)
    table.heading("Time", text="Time")
    table.heading("Type", text="Type")
    table.heading("Quantity", text="Quantity")
    table.heading("Price", text="Price")
    table.heading("Employee Name", text="Employee Name")
    table.heading("The Check", text="The Check")

    # Column widths
    table.column("Time", width=100, anchor="center")
    table.column("Type", width=100, anchor="center")
    table.column("Quantity", width=100, anchor="center")
    table.column("Price", width=100, anchor="center")
    table.column("Employee Name", width=120, anchor="center")
    table.column("The Check", width=100, anchor="center")
    table.pack(padx=10, pady=10)
    close_button = tk.Button(order_win, text="Close", font=("Arial", 12),
                             command=order_win.destroy, bg="#FFFFFF", fg="#161B33")
    close_button.pack(pady=20)

# ------------------ INVENTORY WINDOW ------------------ #
def open_inventory_window(root):

    inventory_win = tk.Toplevel(root)
    inventory_win.title("Inventory Screen")
    inventory_win.geometry("900x800")
    inventory_win.configure(bg="#161B33")

    create_navbar_buttonless_in_window(inventory_win, root)

    main_frame = Frame(inventory_win, bg="#161B33")
    main_frame.pack(expand=True)

    header_label = tk.Label(main_frame, text="Restaurant Stock Management",
                            font=("Arial", 20, "bold"), fg="white", bg="#161B33")
    header_label.pack(pady=10)

    content_frame = Frame(main_frame, bg="#161B33")
    content_frame.pack()

    stock_tree = ttk.Treeview(content_frame, columns=("Item", "Stock"), show="headings", height=10)
    stock_tree.heading("Item", text="Food Item", anchor="w")
    stock_tree.heading("Stock", text="Stock", anchor="center")
    stock_tree.column("Item", width=200, anchor="w")
    stock_tree.column("Stock", width=100, anchor="center")
    stock_tree.pack(pady=10)

    # Populate the tree
    for item in menuItems:
        stock_tree.insert("", "end", values=(item["name"], item["stock"]))

    name_label = tk.Label(content_frame, text="Food Item Name:", bg="#161B33", fg="white", font=("Arial", 12))
    name_label.pack(pady=5)
    name_entry = tk.Entry(content_frame, font=("Arial", 12), width=20)
    name_entry.pack()

    stock_label = tk.Label(content_frame, text="Stock Quantity:", bg="#161B33", fg="white", font=("Arial", 12))
    stock_label.pack(pady=5)
    stock_entry = tk.Entry(content_frame, font=("Arial", 12), width=20)
    stock_entry.pack()

    def on_item_select(event):
        selected = stock_tree.selection()
        if selected:
            item_name = stock_tree.item(selected[0])["values"][0]
            item_stock = stock_tree.item(selected[0])["values"][1]
            name_entry.delete(0, tk.END)
            name_entry.insert(tk.END, item_name)
            stock_entry.delete(0, tk.END)
            stock_entry.insert(tk.END, item_stock)

    stock_tree.bind("<<TreeviewSelect>>", on_item_select)

    def update_stock_display():
        stock_tree.delete(*stock_tree.get_children())
        for Item in menuItems:
            stock_tree.insert("", "end", values=(Item["name"], Item["stock"]))

    def clear_inputs():
        name_entry.delete(0, tk.END)
        stock_entry.delete(0, tk.END)

    def save_changes():
        try:
            selected_id = stock_tree.selection()[0]
            old_name = stock_tree.item(selected_id)["values"][0]
            new_name = name_entry.get()
            new_stock = int(stock_entry.get())
            if new_name and new_stock >= 0:
                for Item in menuItems:
                    if Item["name"] == old_name:
                        Item["name"] = new_name
                        Item["stock"] = new_stock
                        break
                update_stock_display()
                clear_inputs()
                messagebox.showinfo("Changes Saved", "Item details have been updated successfully.")
            else:
                messagebox.showwarning("Invalid Input", "Please enter a valid name and stock quantity.")
        except IndexError:
            messagebox.showwarning("No Item Selected", "Please select an item to edit.")
        except ValueError:
            messagebox.showwarning("Invalid Stock", "Please enter a valid number for stock.")

    def add_item():
        new_name = name_entry.get()
        try:
            new_stock = int(stock_entry.get())
            if new_name and new_stock >= 0:
                menuItems.append({"name": new_name, "stock": new_stock})
                update_stock_display()
                clear_inputs()
                messagebox.showinfo("Item Added", f"Item '{new_name}' has been added to the menu.")
            else:
                messagebox.showwarning("Invalid Input", "Please enter a valid name and stock quantity.")
        except ValueError:
            messagebox.showwarning("Invalid Stock", "Please enter a valid number for stock.")

    def remove_item():
        try:
            selected_id = stock_tree.selection()[0]
            item_name = stock_tree.item(selected_id)["values"][0]
            for Item in menuItems:
                if Item["name"] == item_name:
                    menuItems.remove(Item)
                    break
            update_stock_display()
            clear_inputs()
            messagebox.showinfo("Item Removed", f"Item '{item_name}' has been removed from the menu.")
        except IndexError:
            messagebox.showwarning("No Item Selected", "Please select an item to remove.")

    # Buttons for Inventory Management
    btn_frame = Frame(content_frame, bg="#161B33")
    btn_frame.pack(pady=10)

    save_button = tk.Button(btn_frame, text="Save Changes", font=("Arial", 12),
                            bg="#4CAF50", fg="white", width=15, command=save_changes)
    save_button.pack(side="left", padx=5)

    add_button = tk.Button(btn_frame, text="Add Item", font=("Arial", 12),
                           bg="#2196F3", fg="white", width=15, command=add_item)
    add_button.pack(side="left", padx=5)

    remove_button = tk.Button(btn_frame, text="Remove Item", font=("Arial", 12),
                              bg="#F44336", fg="white", width=15, command=remove_item)
    remove_button.pack(side="left", padx=5)

    # Close button at the bottom
    close_button = tk.Button(inventory_win, text="Close", font=("Arial", 12),
                             command=inventory_win.destroy, bg="#FFFFFF", fg="#161B33")
    close_button.pack(side="bottom", pady=10)

# ------------------ STAFF WINDOW ------------------ #
def open_staff_window(root):


    # Data for the staff window
    data = [
        {"Employee_Name": "Omar Ahmed",      "Salary": 8000,  "Age": 24,
         "Phone number": "01155935595",     "Date of appointment": "2/1/2020", "Job Type": "Full Time", "Job": "Cashier"},
        {"Employee_Name": "Ahmed Omar",     "Salary": 10000, "Age": 30,
         "Phone number": "01234587158",     "Date of appointment": "2/1/2019", "Job Type": "Full Time", "Job": "Chef"},
        {"Employee_Name": "Ali Fathy",      "Salary": 9000,  "Age": 24,
         "Phone number": "01245874610",     "Date of appointment": "2/1/2020", "Job Type": "Full Time", "Job": "Waiter"},
        {"Employee_Name": "Muhammad Ahmad", "Salary": 9500,  "Age": 25,
         "Phone number": "01157846912",     "Date of appointment": "2/1/2018", "Job Type": "Full Time", "Job": "Head Cashier"},
        {"Employee_Name": "Fathy Ali",      "Salary": 3000,  "Age": 20,
         "Phone number": "01157846912",     "Date of appointment": "2/1/2020", "Job Type": "Full Time", "Job": "Waiter"},
        {"Employee_Name": "Ahmad Muhammad", "Salary": 9500,  "Age": 25,
         "Phone number": "01157846912",     "Date of appointment": "2/1/2018", "Job Type": "Full Time", "Job": "Waiter"}
    ]

    staff_win = tk.Toplevel(root)
    staff_win.title("Employee Application")
    staff_win.geometry("1200x600")
    staff_win.configure(bg="#161B33")

    create_navbar_buttonless_in_window(staff_win, root)

    title = Label(staff_win, text="Employee Application", bg="#161B33", fg="white",
                  font=("Arial", 20, "bold"))
    title.pack(pady=5)

    column1 = [
        "Employee_Name", "Salary", "salary_deduction", "Age",
        "Phone number", "Date of appointment", "Job Type", "Job"
    ]


    staff_table = ttk.Treeview(staff_win, columns=column1, show="headings", height=10)
    for col in column1:
        staff_table.heading(col, text=col)
        staff_table.column(col, anchor="center", width=150)

    staff_table.pack(padx=10, pady=10)

    def load_data():
        staff_table.delete(*staff_table.get_children())
        for row in data:
            staff_table.insert(
                "",
                "end",
                values=(
                    row["Employee_Name"],
                    row["Salary"],
                    row.get("Salary_deduction", "N/A"),
                    row["Age"],
                    row["Phone number"],
                    row["Date of appointment"],
                    row["Job Type"],
                    row["Job"]
                )
            )

    load_data()

    # Deduction window logic (opens on top of staff_win)
    def open_deduction_window(refresh_main_table):
        deduction_win = Toplevel(staff_win)
        deduction_win.title("Salary_deduction")
        deduction_win.geometry("500x400")
        deduction_win.configure(bg="light blue")

        column2 = ["Employee_Name", "Salary", "Salary_deduction"]
        table2 = ttk.Treeview(deduction_win, columns=column2, show="headings", height=10)
        for c in column2:
            table2.heading(c, text=c, anchor="center")
            table2.column(c, anchor="center", width=150)
        table2.pack(padx=10, pady=10)

        for row in data:
            table2.insert(
                "",
                "end",
                values=(
                    row["Employee_Name"],
                    row["Salary"],
                    row.get("Salary_deduction", "N/A")
                )
            )

        deduction_label = Label(deduction_win, text="Deduction (%)",
                                font=("Arial", 20, "bold"), anchor="center")
        deduction_label.pack(padx=10, pady=10)

        deduction_entry = Entry(deduction_win)
        deduction_entry.pack(padx=10, pady=10)

        def apply_deduction():
            discount_value = deduction_entry.get()
            if not discount_value.isdigit():
                messagebox.showerror("Error", "Please enter a number")
                return
            discount_value = float(discount_value)
            if not (0 <= discount_value <= 100):
                messagebox.showerror("Error", "Please enter a number between 0 and 100")
                return

            selected_item = table2.selection()
            if not selected_item:
                messagebox.showerror("Error", "Please select an item")
                return

            for item in selected_item:
                employee_value = table2.item(item, "values")
                current_salary = float(employee_value[1])
                deduction_amt = current_salary * discount_value / 100
                new_salary = current_salary - deduction_amt

                for emp in data:
                    if emp["Employee_Name"] == employee_value[0]:
                        emp["Salary"] = new_salary
                        emp["Salary_deduction"] = deduction_amt

                table2.item(item, values=(
                    employee_value[0],
                    new_salary,
                    deduction_amt
                ))

                for child in staff_table.get_children():
                    row_values = staff_table.item(child, "values")
                    if row_values[0] == employee_value[0]:
                        staff_table.item(
                            child,
                            values=(
                                employee_value[0],
                                new_salary,
                                deduction_amt,
                                row_values[3],
                                row_values[4],
                                row_values[5],
                                row_values[6],
                                row_values[7]
                            )
                        )
                        break

            deduction_entry.delete(0, END)
            messagebox.showinfo("Success", "Salary deduction applied successfully.")

        apply_button = ttk.Button(deduction_win, text="Apply", command=apply_deduction)
        apply_button.pack(padx=10, pady=10)

        def close_return():
            deduction_win.destroy()
            staff_win.deiconify()
            refresh_main_table()

        close_button = ttk.Button(deduction_win, text="Close", command=close_return)
        close_button.pack(padx=10, pady=10)

    def deduction():

        open_deduction_window(load_data)

    deduction_button = ttk.Button(staff_win, text="Deduction", command=deduction)
    deduction_button.pack(padx=10, pady=10)

# ------------------ Menu WINDOW ------------------ #
def open_menu_window(root):
    menu_win = tk.Toplevel(root)
    menu_win.title("Restaurant Menu")
    menu_win.geometry("900x700")
    menu_win.configure(bg="#161B33")

    # Keep references to images and cart items within the window object
    menu_win.image_refs = []
    menu_win.cart_items = []  # List to store cart items (each item is a dict)

    create_navbar_buttonless_in_window(menu_win, root)

    # =========== Define Nested Function: Open Cart Window ===========
    def open_cart_window():
        cart_win = tk.Toplevel(menu_win)
        cart_win.title("Cart")
        cart_win.geometry("500x400")
        cart_win.configure(bg="#161B33")

        # Cart Title
        tk.Label(cart_win, text="Your Cart", font=("Arial", 20, "bold"),
                 bg="#161B33", fg="white").pack(pady=10)

        # Define a Treeview to show cart items
        columns = ("Item Name", "Price")
        cart_table = ttk.Treeview(cart_win, columns=columns, show="headings", height=8)
        cart_table.heading("Item Name", text="Item Name")
        cart_table.heading("Price", text="Price")
        cart_table.column("Item Name", anchor="center", width=200)
        cart_table.column("Price", anchor="center", width=100)
        cart_table.pack(pady=10)

        # Function to populate (or re-populate) the cart table
        def load_cart_items():
            cart_table.delete(*cart_table.get_children())
            for item in menu_win.cart_items:
                cart_table.insert("", "end", values=(item["name"], f"${item['price']:.2f}"))

        load_cart_items()

        # Clear the cart items
        def clear_cart():
            menu_win.cart_items.clear()
            load_cart_items()

        # Checkout function
        def checkout_cart():
            if menu_win.cart_items:
                messagebox.showinfo("Checkout", "Checked out successfully!")
                menu_win.cart_items.clear()
                load_cart_items()
            else:
                messagebox.showinfo("Checkout", "Cart is already empty.")

        # Buttons for clearing and checkout
        btn_frame = tk.Frame(cart_win, bg="#161B33")
        btn_frame.pack(pady=10)

        clear_btn = tk.Button(btn_frame, text="Clear", bg="#F44336", fg="white",
                              font=("Arial", 12), command=clear_cart)
        clear_btn.pack(side="left", padx=5)

        checkout_btn = tk.Button(btn_frame, text="Checkout", bg="#4CAF50", fg="white",
                                 font=("Arial", 12), command=checkout_cart)
        checkout_btn.pack(side="left", padx=5)

    # =========== Add a Button to Open the Cart Window at the Top ===========
    cart_button = tk.Button(menu_win, text="View Cart", font=("Arial", 12, "bold"),
                            bg="#2196F3", fg="white", command=open_cart_window)
    cart_button.pack(pady=10)

    # =========== Sample Menu Items with Categories ===========
    menu_items = {
        "Food Items": [
            {"name": "Burger", "price": 9.99, "image": "Images/burger.jpg"},
            {"name": "Pizza",  "price": 12.50, "image": "Images/pizza.jpg"},
            {"name": "Pasta",  "price": 8.75,  "image": "Images/pasta.jpg"},
            {"name": "Sushi",  "price": 14.99, "image": "Images/sushi.jpg"},
            {"name": "Steak",  "price": 19.99, "image": "Images/steak.jpg"},
        ],
        "Drinks": [
            {"name": "Water",  "price": 1.50,  "image": "Images/water.jpg"},
            {"name": "Juice",  "price": 3.75,  "image": "Images/juice.jpg"},
            {"name": "Soda",   "price": 2.50,  "image": "Images/soda.jpg"},
            {"name": "Coffee", "price": 2.25,  "image": "Images/coffee.jpg"},
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

    # Helper function to add an item to cart
    def add_to_cart(item_dict):
        menu_win.cart_items.append(item_dict)
        messagebox.showinfo("Cart", f"Added {item_dict['name']} to cart!")

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

            # Image Loading
            try:
                image_path = os.path.abspath(item["image"])
                if os.path.exists(image_path):
                    pil_image = Image.open(image_path).resize((150, 150))
                    tk_image = ImageTk.PhotoImage(pil_image)
                    menu_win.image_refs.append(tk_image)  # Prevent garbage collection
                    img_label = tk.Label(item_frame, image=tk_image, bg="#1F2C4D")
                    img_label.pack(pady=5)
                    print(image_path)
                else:
                    raise FileNotFoundError(f"Image not found: {image_path}")
            except Exception as e:
                print(f"Error loading image for {item['name']}: {e}")
                tk.Label(item_frame, text="[No Image]", bg="#1F2C4D", fg="white").pack(pady=5)

            # Item Name
            name_label = tk.Label(item_frame, text=item["name"], font=("Arial", 14, "bold"),
                                  bg="#1F2C4D", fg="white")
            name_label.pack(pady=2)

            # Item Price
            price_label = tk.Label(item_frame, text=f"${item['price']:.2f}", font=("Arial", 12),
                                   bg="#1F2C4D", fg="#AAAAAA")
            price_label.pack(pady=2)

            # Add to Cart Button
            buy_button = tk.Button(item_frame, text="Add to Cart",
                                   font=("Arial", 10, "bold"),
                                   bg="#4CAF50", fg="white",
                                   command=lambda i=item: add_to_cart(i))
            buy_button.pack(pady=5)

# ------------------ MAIN WINDOW (LOGIN) ------------------ #
def main_window():
    global root
    root = tk.Tk()
    root.title("Cuisine Control - Login")
    root.geometry("900x600")
    root.configure(bg="#161B33")

    create_navbar_buttonless_in_window(root, root)



    # ============= LOGIN FRAME =============
    login_frame = Frame(root, bg="#161B33")
    login_frame.pack(fill="both", expand=True)

    Label(login_frame, text="Login", font=("Arial", 24, "bold"), bg="#161B33", fg="white").pack(pady=20)

    # Email
    email_label = Label(login_frame, text="Email:", font=("Arial", 14, "bold"), bg="#161B33", fg="white")
    email_label.pack(pady=5)
    email_entry = Entry(login_frame, width=40, font=("Arial", 12))
    email_entry.pack(pady=5)

    # Password
    password_label = Label(login_frame, text="Password:", font=("Arial", 14, "bold"), bg="#161B33", fg="white")
    password_label.pack(pady=5)
    password_entry = Entry(login_frame, width=40, font=("Arial", 12), show="*")
    password_entry.pack(pady=5)

    # ============= POST-LOGIN FRAME =============
    post_login_frame = Frame(root, bg="#161B33")
    # We'll pack this frame only after successful login

    Label(post_login_frame, text="Welcome!", font=("Arial", 24, "bold"), bg="#161B33", fg="white").pack(pady=20)

    def open_order():
        open_order_window(root)

    def open_inventory():
        open_inventory_window(root)

    def open_staff():
        open_staff_window(root)

    def open_menu():
        open_menu_window(root)


    def show_role_buttons(role):
        """Show the buttons relevant to the user’s role on the main screen."""
        if role == "manager":
            manager_inventory_button = tk.Button(post_login_frame, text="Go to Inventory Screen",
                                                 font=("Arial", 14), command=open_inventory,
                                                 bg="#FFFFFF", fg="#161B33")
            manager_inventory_button.pack(pady=10)

            staff_screen_button = tk.Button(post_login_frame, text="Go to Staff Screen",
                                            font=("Arial", 14), command=open_staff,
                                            bg="#FFFFFF", fg="#161B33")
            staff_screen_button.pack(pady=10)

            order_screen_button = tk.Button(post_login_frame, text="Go to Order Screen",
                                            font=("Arial", 14), command=open_order,
                                            bg="#FFFFFF", fg="#161B33")
            order_screen_button.pack(pady=10)

            menu_screen_button = tk.Button(post_login_frame, text="Go to Menu Screen",
                                           font=("Arial", 14), command=open_menu,
                                           bg="#FFFFFF", fg="#161B33")
            menu_screen_button.pack(pady=10)

        elif role == "staff":
            order_screen_button = tk.Button(post_login_frame, text="Go to Order Screen",
                                            font=("Arial", 14), command=open_order,
                                            bg="#FFFFFF", fg="#161B33")
            order_screen_button.pack(pady=10)

            menu_screen_button = tk.Button(post_login_frame, text="Go to Menu Screen",
                                            font=("Arial", 14), command=open_menu,
                                            bg="#FFFFFF", fg="#161B33")
            menu_screen_button.pack(pady=10)

    def attempt_login():
        email = email_entry.get().strip().lower()
        pwd   = password_entry.get().strip()

        if email in users:
            if users[email]["password"] == pwd:
                user_role = users[email]["role"]
                messagebox.showinfo("Login Successful", f"Welcome, {user_role.capitalize()}!")
                login_frame.pack_forget()
                post_login_frame.pack(fill="both", expand=True)
                show_role_buttons(user_role)
            else:
                messagebox.showerror("Login Failed", "Incorrect password.")
        else:
            messagebox.showerror("Login Failed", "User not found.")

    login_button = Button(login_frame, text="Login", font=("Arial", 14),
                          fg="#161B33", bg="white", command=attempt_login)
    login_button.pack(pady=10)
    root.mainloop()
# ---- Start the application ----
if __name__ == "__main__":
    main_window()
#dont change anything