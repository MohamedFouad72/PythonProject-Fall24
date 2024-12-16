# We Will Write Everything Here!!
from tkinter import *
from tkinter import ttk, messagebox

import tk

root = Tk()
root.title("My First Program")


#Order Screen
times_list = [f"{hour:02d}:{minute:02d}" for hour in range(24) for minute in range(60)]
root.geometry("500x400")
root.configure(bg="black")
root.title("Order Screen")
title=ttk.Label(root,text="Order",font=("Arial",20,"bold"))
title.pack(padx=10,pady=10)
column=("Time","Type","Quntity","price","Employee Name","The Check")
table=ttk.Treeview(root,column=column,show="headings",height=10)
table.heading("Time",text="Time")
table.heading("Type",text="Type")
table.heading("Quntity",text="Quntity")
table.heading("price",text="Price")
table.heading("Employee Name",text="Employee Name")
table.heading("The Check",text="The Check")
table.column("Time",width=100,anchor=CENTER)
table.column("Type",width=100,anchor=CENTER)
table.column("Quntity",width=100,anchor=CENTER)
table.column("price",width=100,anchor=CENTER)
table.column("Employee Name",width=100,anchor=CENTER)
table.column("The Check",width=100,anchor=CENTER)
time_entry=ttk.Combobox(root,width=40,values=times_list)
time_entry.set("Select Time")
time_entry.pack(padx=10,pady=10)
table.pack()
#inventory
def updatestockdisplay():
    for row in stocktree.get_children():
        stocktree.delete(row)
    for item in menuitems:
        stocktree.insert("", "end", values=(item["name"], item["stock"]))
def savechanges():
    try:
        selecteditemindex = stocktree.selection()[0]
        newname = nameentry.get()
        newstock = int(stockentry.get())
        if newname and newstock >= 0:
            itemname = stocktree.item(selecteditemindex)["values"][0]
            for item in menuitems:
                if item["name"] == itemname:
                    item["name"] = newname
                    item["stock"] = newstock
                    break
            updatestockdisplay()
            clearinputs()
            messagebox.showinfo("Changes Saved", "Item details have been updated successfully.")
        else:
            messagebox.showwarning("Invalid Input", "Please enter a valid name and stock quantity.")
    except IndexError:
        messagebox.showwarning("No Item Selected", "Please select an item to edit.")
    except ValueError:
        messagebox.showwarning("Invalid Stock", "Please enter a valid number for stock.")
def onitemselect(event, tk=None):
    selecteditem = stocktree.selection()
    if selecteditem:
        itemname = stocktree.item(selecteditem[0])["values"][0]
        itemstock = stocktree.item(selecteditem[0])["values"][1]
        nameentry.delete(0, tk.END)
        nameentry.insert(tk.END, itemname)
        stockentry.delete(0, tk.END)
        stockentry.insert(tk.END, itemstock)
def additem():
    newname = nameentry.get()
    try:
        newstock = int(stockentry.get())
        if newname and newstock >= 0:
            menuitems.append({"name": newname, "stock": newstock})
            updatestockdisplay()
            clearinputs()
            messagebox.showinfo("Item Added", f"Item '{newname}' has been added to the menu.")
        else:
            messagebox.showwarning("Invalid Input", "Please enter a valid name and stock quantity.")
    except ValueError:
        messagebox.showwarning("Invalid Stock", "Please enter a valid number for stock.")
def removeitem():
    try:
        selecteditemindex = stocktree.selection()[0]
        itemname = stocktree.item(selecteditemindex)["values"][0]
        for item in menuitems:
            if item["name"] == itemname:
                menuitems.remove(item)
                break
        updatestockdisplay()
        clearinputs()
        messagebox.showinfo("Item Removed", f"Item '{itemname}' has been removed from the menu.")
    except IndexError:
        messagebox.showwarning("No Item Selected", "Please select an item to remove.")
def clearinputs():
    nameentry.delete(0, tk.END)
    stockentry.delete(0, tk.END)
root = tk.Tk()
root.title("Restaurant Manager Menu - Stock Management System")
root.geometry("900x600")
root.config(bg="#1c1c1c")
menuitems = [
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
frame = tk.Frame(root, bg="#1c1c1c", bd=5)
frame.pack(pady=20, padx=20, fill="both", expand=True)
headerlabel = tk.Label(frame, text="Restaurant Stock Management", font=("Arial", 20, "bold"),
                        fg="white", bg="#1c1c1c")
headerlabel.grid(row=0, column=0, columnspan=3, pady=10)
stocktree = ttk.Treeview(frame, columns=("Item", "Stock"), show="headings", height=10)
stocktree.heading("Item", text="Food Item", anchor="w")
stocktree.heading("Stock", text="Stock", anchor="center")
stocktree.column("Item", width=200, anchor="w")
stocktree.column("Stock", width=100, anchor="center")
stocktree.grid(row=1, column=0, columnspan=3, pady=20)
namelabel = tk.Label(frame, text="Food Item Name:", bg="#1c1c1c", fg="white", font=("Arial", 12))
namelabel.grid(row=2, column=0, pady=5, sticky="w")
nameentry = tk.Entry(frame, font=("Arial", 12), width=20)
nameentry.grid(row=2, column=1, pady=5, padx=10, sticky="w")
stocklabel = tk.Label(frame, text="Stock Quantity:", bg="#1c1c1c", fg="white", font=("Arial", 12))
stocklabel.grid(row=3, column=0, pady=5, sticky="w")
stockentry = tk.Entry(frame, font=("Arial", 12), width=20)
stockentry.grid(row=3, column=1, pady=5, padx=10, sticky="w")
savebutton = tk.Button(frame, text="Save Changes", font=("Arial", 12), bg="#4CAF50", fg="white", width=20, command=savechanges)
savebutton.grid(row=4, column=0, columnspan=3, pady=10)
addbutton = tk.Button(frame, text="Add Item", font=("Arial", 12), bg="#2196F3", fg="white", width=20, command=additem)
addbutton.grid(row=5, column=0, columnspan=3, pady=10)
removebutton = tk.Button(frame, text="Remove Item", font=("Arial", 12), bg="#F44336", fg="white", width=20, command=removeitem)
removebutton.grid(row=6, column=0, columnspan=3, pady=10)
stocktree.bind("<<TreeviewSelect>>", onitemselect)
updatestockdisplay()
root.mainloop()