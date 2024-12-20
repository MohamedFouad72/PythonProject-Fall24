#Here We Will Write Any Code That Needs Testing
#The staff:
from tkinter import *
from tkinter import ttk,messagebox
data=[
    {"Employee_Name": "Omar Ahmed", "Salary": 8000, "Age": 24,
     "Phone number": "01155935595", "Date of appointment": "2/1/2020", "Job Type": "Full Time", "Job": "Cashier"},
    {"Employee_Name": "Ahmed Omar","Salary": 10000 , "Age": 30,
     "Phone number": "01234587158", "Date of appointment": "2/1/2019", "Job Type": "Full Time", "Job": "Chef"},
    {"Employee_Name": "Ali Fathy","Salary": 9000 , "Age": 24,
     "Phone number": "01245874610", "Date of appointment": "2/1/2020", "Job Type": "Full Time", "Job": "Waiter"},
    {"Employee_Name": "Muhammad Ahmad", "Salary": 9500, "Age": 25,
     "Phone number": "01157846912", "Date of appointment": "2/1/2018", "Job Type": "Full Time", "Job": "Head Cashier"},
    {"Employee_Name": "Fathy Ali", "Salary": 3000, "Age": 20,
     "Phone number": "01157846912","Date of appointment": "2/1/2020" , "Job Type": "Full Time", "Job": "Waiter"},
    {"Employee_Name": "Ahmad Muhammad", "Salary": 9500, "Age": 25,
     "Phone number": "01157846912","Date of appointment": "2/1/2018" , "Job Type": "Full Time", "Job": "Waiter"}]
def open_window():
    global root,table1
    root=Tk()
    root.geometry("500x400")
    root.title("Employee Application")
    root.configure(bg="black")
    column1=["Employee_Name", "Salary", "salary_deduction", "Age", "Phone number", "Date of appointment", "Job Type", "Job"]
    title =Label(root,text="Employee Application",bg="black",fg="white",font=("Arial",20,"bold"))
    title.pack(pady=5)
    table1=ttk.Treeview(root,column=column1,show="headings",height=10)
    for column in column1:
        table1.heading(column,text=column)
        table1.column(column,anchor="center",width=150)
    def load_data():
        table1.delete(*table1.children)
        for row in data:
            table1.insert("","end",values=(row["Employee_Name"],row["Salary"],row.get("Salary_deduction","N/A"),
                                           row["Age"],row["Phone number"],row["Date of appointment"],row["Job Type"],row["Job"]))
    load_data()
    table1.pack(padx=10, pady=10)
    def deduction():
        root.withdraw()
        open_deduction_window(load_data)
    deduction_button=ttk.Button(root,text="Deduction",command=deduction)
    deduction_button.pack(padx=10,pady=10)
    root.mainloop()
def open_deduction_window(refresh_main_table):
    global table1
    Salary_deduction=Toplevel()
    Salary_deduction.title("Salary_deduction")
    Salary_deduction.geometry("500x400")
    Salary_deduction.configure(bg="light blue")
    column2=["Employee_Name", "Salary", "Salary_deduction"]
    table2=ttk.Treeview(Salary_deduction,column=column2,show="headings",height=10)
    for column in column2:
        table2.heading(column,text=column,anchor="center")
        table2.column(column,anchor="center",width=150)
    table2.pack(padx=10, pady=10)
    for row in data:
        table2.insert("","end",values=(row["Employee_Name"],row["Salary"],row.get("Salary_deduction","N/A")))
    table2.pack(padx=10,pady=10)
    deduction_label=Label(Salary_deduction,text="Deduction (%)",font=("Arial",20,"bold"),anchor="center")
    deduction_label.pack(padx=10,pady=10)
    dededuction_entry=Entry(Salary_deduction)
    dededuction_entry.pack(padx=10,pady=10)
    def apply():
        discount_value=dededuction_entry.get()
        if not discount_value.isdigit():
            messagebox.showerror("Error","please enter a number")
            return
        discount_value = float(discount_value)
        if not (0 <= discount_value<=100):
            messagebox.showerror("Error","please enter a number between 0 and 100")
            return
        selected_item=table2.selection()
        if not selected_item:
            messagebox.showerror("Error","please select an item")
            return
        for item in selected_item:
            employee_value=table2.item(item,"value")
            current_salary=float(employee_value[1])
            deduction=current_salary*discount_value/100
            new_salary=current_salary-deduction
            for name in data:
                if name["Employee_Name"] == employee_value[0]:
                    name["Salary"]=new_salary
                    name["Salary_deduction"]=deduction
            table2.item(item,values=(employee_value[0],new_salary,deduction))
            for child in table1.get_children():
                row_values = table1.item(child, "values")
                if row_values[0] == employee_value[0]:
                    table1.item(child, values=( employee_value[0],new_salary,deduction,row_values[3],row_values[4],row_values[5],row_values[6], row_values[7]))
                    break
        dededuction_entry.delete(0,END)
        messagebox.showinfo("Success","Salary deduction applied successfully.")
    apply_button=ttk.Button(Salary_deduction,text="apply",command=apply)
    apply_button.pack(padx=10,pady=10)
    def close_return():
        Salary_deduction.destroy()
        root.deiconify()
        refresh_main_table()
    close_button=ttk.Button(Salary_deduction,text="close",command=close_return)
    close_button.pack(padx=10,pady=10)
open_window()







