# We Will Write Everything Here!!
from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
root = Tk()
root.title("My First Program")


#Order Screen
times_list = [f"{hour:02d}:{minute:02d}" for hour in range(24) for minute in range(60)]
root.geometry("500x400")
root.configure(bg="black")
root.title("Order Screen")
title=ttk.Label(root,text="Order",font=("Arial",20,"bold"))
title.pack(padx=10,pady=10)
column=("Time","Type","Quantity","price","Employee Name","The Check")
table=ttk.Treeview(root, column=column,show="headings",height=10)
table.heading("Time",text="Time")
table.heading("Type",text="Type")
table.heading("Quantity",text="Quantity")
table.heading("price",text="Price")
table.heading("Employee Name",text="Employee Name")
table.heading("The Check",text="The Check")
table.column("Time",width=100,anchor=CENTER)
table.column("Type",width=100,anchor=CENTER)
table.column("Quantity",width=100,anchor=CENTER)
table.column("price",width=100,anchor=CENTER)
table.column("Employee Name",width=100,anchor=CENTER)
table.column("The Check",width=100,anchor=CENTER)
time_entry=ttk.Combobox(root,width=40,values=times_list)
time_entry.set("Select Time")
time_entry.pack(padx=10,pady=10)
table.pack()
#inventory
def update_stock_display():
    for row in stockTree.get_children():
        stockTree.delete(row)
    for item in menuItems:
        stockTree.insert("", "end", values=(item["name"], item["stock"]))
def save_changes():
    try:
        selected_item_index = stockTree.selection()[0]
        newname = nameEntry.get()
        newStock = int(stockEntry.get())
        if newname and newStock >= 0:
            itemName = stockTree.item(selected_item_index)["values"][0]
            for item in menuItems:
                if item["name"] == itemName:
                    item["name"] = newname
                    item["stock"] = newStock
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
def on_item_select(event, tk=None):
    selectedItem = stockTree.selection()
    if selectedItem:
        itemName = stockTree.item(selectedItem[0])["values"][0]
        itemStock = stockTree.item(selectedItem[0])["values"][1]
        nameEntry.delete(0, tk.END)
        nameEntry.insert(tk.END, itemName)
        stockEntry.delete(0, tk.END)
        stockEntry.insert(tk.END, itemStock)
def add_item():
    newname = nameEntry.get()
    try:
        newStock = int(stockEntry.get())
        if newname and newStock >= 0:
            menuItems.append({"name": newname, "stock": newStock})
            update_stock_display()
            clear_inputs()
            messagebox.showinfo("Item Added", f"Item '{newname}' has been added to the menu.")
        else:
            messagebox.showwarning("Invalid Input", "Please enter a valid name and stock quantity.")
    except ValueError:
        messagebox.showwarning("Invalid Stock", "Please enter a valid number for stock.")
def remove_item():
    try:
        selectedItemIndex = stockTree.selection()[0]
        itemName = stockTree.item(selectedItemIndex)["values"][0]
        for item in menuItems:
            if item["name"] == itemName:
                menuItems.remove(item)
                break
        update_stock_display()
        clear_inputs()
        messagebox.showinfo("Item Removed", f"Item '{itemName}' has been removed from the menu.")
    except IndexError:
        messagebox.showwarning("No Item Selected", "Please select an item to remove.")
def clear_inputs():
    nameEntry.delete(0, END)
    stockEntry.delete(0, END)


root.geometry("900x600")
root.config(bg="#1c1c1c")
menuItems = [
    {"name": "Meat", "stock": 1000},
    {"name": "Chicken", "stock": 850},
    {"name": "Pasta", "stock": 1500},
    {"name": "Cola", "stock": 2000},
    {"name": "Tomatoes", "stock": 3500},
    {"name": "Sauces", "stock" : 2500},
    {"name": "potatoes","stock" : 3000},
    {"name": "Bread","stock": 1500},
    {"name": "Cheese" ,"stock":2000},
    {"name": "Spices","stock": 1000},
    {"name": "Milk" , "stock": 5020},
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
frame = Frame(root, bg="#1c1c1c", bd=5)
frame.pack(pady=20, padx=20, fill="both", expand=True)
headerLabel = Label(frame, text="Restaurant Stock Management", font=("Arial", 20, "bold"),
                    fg="white", bg="#1c1c1c")
headerLabel.grid(row=0, column=0, columnspan=3, pady=10)
stockTree = ttk.Treeview(frame, columns=("Item", "Stock"), show="headings", height=10)
stockTree.heading("Item", text="Food Item", anchor="w")
stockTree.heading("Stock", text="Stock", anchor="center")
stockTree.column("Item", width=200, anchor="w")
stockTree.column("Stock", width=100, anchor="center")
stockTree.grid(row=1, column=0, columnspan=3, pady=20)
nameLabel = Label(frame, text="Food Item Name:", bg="#1c1c1c", fg="white", font=("Arial", 12))
nameLabel.grid(row=2, column=0, pady=5, sticky="w")
nameEntry = Entry(frame, font=("Arial", 12), width=20)
nameEntry.grid(row=2, column=1, pady=5, padx=10, sticky="w")
stockLabel = Label(frame, text="Stock Quantity:", bg="#1c1c1c", fg="white", font=("Arial", 12))
stockLabel.grid(row=3, column=0, pady=5, sticky="w")
stockEntry = Entry(frame, font=("Arial", 12), width=20)
stockEntry.grid(row=3, column=1, pady=5, padx=10, sticky="w")
saveButton = Button(frame, text="Save Changes", font=("Arial", 12), bg="#4CAF50", fg="white", width=20, command=save_changes)
saveButton.grid(row=4, column=0, columnspan=3, pady=10)
addButton = Button(frame, text="Add Item", font=("Arial", 12), bg="#2196F3", fg="white", width=20, command=add_item)
addButton.grid(row=5, column=0, columnspan=3, pady=10)
removeButton = Button(frame, text="Remove Item", font=("Arial", 12), bg="#F44336", fg="white", width=20, command=remove_item)
removeButton.grid(row=6, column=0, columnspan=3, pady=10)
stockTree.bind("<<TreeviewSelect>>", on_item_select)
update_stock_display()

root.mainloop()