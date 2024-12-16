# # We Will Write Everything Here!!
# from tkinter import *
# from PIL import ImageTk, Image
# root1 = Tk()
# root1.title("My First Program")






# root1.mainloop()
#Order Screen
from tkinter import *
from tkinter import ttk
root = Tk()
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

root.mainloop()