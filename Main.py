import tkinter as tk
from tkinter import ttk, messagebox
from PIL import ImageTk, Image

class MainMenuFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="black")
        self.controller = controller
        tk.Label(self, text="Main Menu", font=("Arial", 24, "bold"), bg="black", fg="white").pack(pady=40)

        # Button to go to Order Screen
        tk.Button(self, text="Go to Order Screen", font=("Arial", 14),
                  command=lambda: controller.show_frame(OrderFrame)).pack(pady=10)

        # Button to go to Inventory Screen
        tk.Button(self, text="Go to Inventory Screen", font=("Arial", 14),
                  command=lambda: controller.show_frame(InventoryFrame)).pack(pady=10)

        # You can add more navigation buttons as needed.


class OrderFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="black")
        self.controller = controller

        self.controller.title("Order Screen")

        title = ttk.Label(self, text="Order", font=("Arial", 20, "bold"), background="black", foreground="white")
        title.pack(padx=10, pady=10)

        # Times list for Combobox
        times_list = [f"{hour:02d}:{minute:02d}" for hour in range(24) for minute in range(60)]

        columns = ("Time", "Type", "Quantity", "price", "Employee Name", "The Check")
        self.table = ttk.Treeview(self, column=columns, show="headings", height=10)
        self.table.heading("Time", text="Time")
        self.table.heading("Type", text="Type")
        self.table.heading("Quantity", text="Quantity")
        self.table.heading("price", text="Price")
        self.table.heading("Employee Name", text="Employee Name")
        self.table.heading("The Check", text="The Check")

        self.table.column("Time", width=100, anchor="center")
        self.table.column("Type", width=100, anchor="center")
        self.table.column("Quantity", width=100, anchor="center")
        self.table.column("price", width=100, anchor="center")
        self.table.column("Employee Name", width=100, anchor="center")
        self.table.column("The Check", width=100, anchor="center")

        time_entry = ttk.Combobox(self, width=40, values=times_list)
        time_entry.set("Select Time")
        time_entry.pack(padx=10, pady=10)

        self.table.pack()

        # Button to return to Main Menu
        tk.Button(self, text="Back to Main Menu", font=("Arial", 12),
                  command=lambda: controller.show_frame(MainMenuFrame)).pack(pady=20)


class InventoryFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#1c1c1c")
        self.controller = controller
        self.menuItems = [
            {"name": "Meat", "stock": 1000},
            {"name": "Chicken", "stock": 850},
            {"name": "Pasta", "stock": 1500},
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
        ]

        frame = tk.Frame(self, bg="#1c1c1c", bd=5)
        frame.pack(pady=20, padx=20, fill="both", expand=True)

        headerLabel = tk.Label(frame, text="Restaurant Stock Management", font=("Arial", 20, "bold"),
                               fg="white", bg="#1c1c1c")
        headerLabel.grid(row=0, column=0, columnspan=3, pady=10)

        self.stockTree = ttk.Treeview(frame, columns=("Item", "Stock"), show="headings", height=10)
        self.stockTree.heading("Item", text="Food Item", anchor="w")
        self.stockTree.heading("Stock", text="Stock", anchor="center")
        self.stockTree.column("Item", width=200, anchor="w")
        self.stockTree.column("Stock", width=100, anchor="center")
        self.stockTree.grid(row=1, column=0, columnspan=3, pady=20)

        nameLabel = tk.Label(frame, text="Food Item Name:", bg="#1c1c1c", fg="white", font=("Arial", 12))
        nameLabel.grid(row=2, column=0, pady=5, sticky="w")
        self.nameEntry = tk.Entry(frame, font=("Arial", 12), width=20)
        self.nameEntry.grid(row=2, column=1, pady=5, padx=10, sticky="w")

        stockLabel = tk.Label(frame, text="Stock Quantity:", bg="#1c1c1c", fg="white", font=("Arial", 12))
        stockLabel.grid(row=3, column=0, pady=5, sticky="w")
        self.stockEntry = tk.Entry(frame, font=("Arial", 12), width=20)
        self.stockEntry.grid(row=3, column=1, pady=5, padx=10, sticky="w")

        saveButton = tk.Button(frame, text="Save Changes", font=("Arial", 12), bg="#4CAF50", fg="white", width=20,
                               command=self.save_changes)
        saveButton.grid(row=4, column=0, columnspan=3, pady=10)

        addButton = tk.Button(frame, text="Add Item", font=("Arial", 12), bg="#2196F3", fg="white", width=20,
                              command=self.add_item)
        addButton.grid(row=5, column=0, columnspan=3, pady=10)

        removeButton = tk.Button(frame, text="Remove Item", font=("Arial", 12), bg="#F44336", fg="white", width=20,
                                 command=self.remove_item)
        removeButton.grid(row=6, column=0, columnspan=3, pady=10)

        backButton = tk.Button(self, text="Back to Main Menu", font=("Arial", 12),
                               command=lambda: controller.show_frame(MainMenuFrame))
        backButton.pack(pady=10)

        self.stockTree.bind("<<TreeviewSelect>>", self.on_item_select)
        self.update_stock_display()

    def update_stock_display(self):
        for row in self.stockTree.get_children():
            self.stockTree.delete(row)
        for item in self.menuItems:
            self.stockTree.insert("", "end", values=(item["name"], item["stock"]))

    def save_changes(self):
        try:
            selected_item_index = self.stockTree.selection()[0]
            newname = self.nameEntry.get()
            newStock = int(self.stockEntry.get())
            if newname and newStock >= 0:
                itemName = self.stockTree.item(selected_item_index)["values"][0]
                for item in self.menuItems:
                    if item["name"] == itemName:
                        item["name"] = newname
                        item["stock"] = newStock
                        break
                self.update_stock_display()
                self.clear_inputs()
                messagebox.showinfo("Changes Saved", "Item details have been updated successfully.")
            else:
                messagebox.showwarning("Invalid Input", "Please enter a valid name and stock quantity.")
        except IndexError:
            messagebox.showwarning("No Item Selected", "Please select an item to edit.")
        except ValueError:
            messagebox.showwarning("Invalid Stock", "Please enter a valid number for stock.")

    def on_item_select(self, event):
        selectedItem = self.stockTree.selection()
        if selectedItem:
            itemName = self.stockTree.item(selectedItem[0])["values"][0]
            itemStock = self.stockTree.item(selectedItem[0])["values"][1]
            self.nameEntry.delete(0, tk.END)
            self.nameEntry.insert(tk.END, itemName)
            self.stockEntry.delete(0, tk.END)
            self.stockEntry.insert(tk.END, itemStock)

    def add_item(self):
        newname = self.nameEntry.get()
        try:
            newStock = int(self.stockEntry.get())
            if newname and newStock >= 0:
                self.menuItems.append({"name": newname, "stock": newStock})
                self.update_stock_display()
                self.clear_inputs()
                messagebox.showinfo("Item Added", f"Item '{newname}' has been added to the menu.")
            else:
                messagebox.showwarning("Invalid Input", "Please enter a valid name and stock quantity.")
        except ValueError:
            messagebox.showwarning("Invalid Stock", "Please enter a valid number for stock.")

    def remove_item(self):
        try:
            selectedItemIndex = self.stockTree.selection()[0]
            itemName = self.stockTree.item(selectedItemIndex)["values"][0]
            for item in self.menuItems:
                if item["name"] == itemName:
                    self.menuItems.remove(item)
                    break
            self.update_stock_display()
            self.clear_inputs()
            messagebox.showinfo("Item Removed", f"Item '{itemName}' has been removed from the menu.")
        except IndexError:
            messagebox.showwarning("No Item Selected", "Please select an item to remove.")

    def clear_inputs(self):
        self.nameEntry.delete(0, tk.END)
        self.stockEntry.delete(0, tk.END)


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("My POS Application")
        self.geometry("900x600")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Dictionary to hold our frames
        self.frames = {}

        for F in (MainMenuFrame, OrderFrame, InventoryFrame):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Show the Main Menu frame first
        self.show_frame(MainMenuFrame)

    def show_frame(self, frame_class):
        frame = self.frames[frame_class]
        frame.tkraise()


if __name__ == "__main__":
    app = App()
    app.mainloop()
