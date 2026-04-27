from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import pyodbc
from tkcalendar import DateEntry 

class employeeClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x600+220+130") # زدنا الارتفاع قليلاً لراحة العين
        self.root.title("Inventory Management System | Employee Management")
        self.root.config(bg="#f4f6f7")
        self.root.focus_force()

        #================ Variables (No Change) =================
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()
        self.var_emp_id = StringVar()
        self.var_gender = StringVar()
        self.var_contact = StringVar()
        self.var_name = StringVar()
        self.var_dob = StringVar()
        self.var_doj = StringVar()
        self.var_email = StringVar()
        self.var_pass = StringVar()
        self.var_utype = StringVar()
        self.var_salary = StringVar()

        #--- Title Section ---
        title = Label(self.root, text="EMPLOYEE MANAGEMENT SYSTEM", font=("Segoe UI", 20, "bold"), bg="#2c3e50", fg="white", bd=5, relief=RIDGE)
        title.pack(side=TOP, fill=X, padx=10, pady=10)

        #--- Main Container Frame ---
        Main_Frame = Frame(self.root, bg="#f4f6f7")
        Main_Frame.pack(fill=BOTH, expand=1, padx=20)

        #--- Search Frame ---
        SearchFrame = LabelFrame(Main_Frame, text=" Search Employee ", font=("Segoe UI", 12, "bold"), bd=2, relief=RIDGE, bg="white", fg="#2c3e50")
        SearchFrame.place(x=0, y=0, width=1060, height=80)

        cmb_search = ttk.Combobox(SearchFrame, textvariable=self.var_searchby, values=("Select", "Email", "Name", "Contact"), state='readonly', justify=CENTER, font=("Segoe UI", 12))
        cmb_search.place(x=10, y=10, width=200, height=30)
        cmb_search.current(0)

        txt_search = Entry(SearchFrame, textvariable=self.var_searchtxt, font=("Segoe UI", 12), bg="#ebf5fb", bd=1).place(x=220, y=10, width=400, height=30)
        btn_search = Button(SearchFrame, text="Search Now", command=self.search, font=("Segoe UI", 11, "bold"), bg="#3498db", fg="white", cursor="hand2", bd=0).place(x=630, y=10, width=150, height=30)
        btn_all = Button(SearchFrame, text="Show All", command=self.show, font=("Segoe UI", 11, "bold"), bg="#607d8b", fg="white", cursor="hand2", bd=0).place(x=790, y=10, width=150, height=30)

        #--- Content Frame (Input Fields) ---
        InputFrame = Frame(Main_Frame, bg="white", bd=2, relief=RIDGE)
        InputFrame.place(x=0, y=90, width=1060, height=300)

        #--- Row 1 ---
        Label(InputFrame, text="Emp ID", font=("Segoe UI", 11), bg="white").place(x=30, y=20)
        txt_empid = Entry(InputFrame, textvariable=self.var_emp_id, font=("Segoe UI", 11), bg="#f9f9f9").place(x=130, y=20, width=200)

        Label(InputFrame, text="Gender", font=("Segoe UI", 11), bg="white").place(x=370, y=20)
        cmb_gender = ttk.Combobox(InputFrame, textvariable=self.var_gender, values=("Select", "Male", "Female", "Other"), state='readonly', justify=CENTER, font=("Segoe UI", 11))
        cmb_gender.place(x=480, y=20, width=200)
        cmb_gender.current(0)

        Label(InputFrame, text="Contact", font=("Segoe UI", 11), bg="white").place(x=710, y=20)
        txt_contact = Entry(InputFrame, textvariable=self.var_contact, font=("Segoe UI", 11), bg="#f9f9f9").place(x=820, y=20, width=200)

        #--- Row 2 ---
        Label(InputFrame, text="Full Name", font=("Segoe UI", 11), bg="white").place(x=30, y=65)
        txt_name = Entry(InputFrame, textvariable=self.var_name, font=("Segoe UI", 11), bg="#f9f9f9").place(x=130, y=65, width=200)

        Label(InputFrame, text="D.O.B", font=("Segoe UI", 11), bg="white").place(x=370, y=65)
        self.txt_dob = DateEntry(InputFrame, textvariable=self.var_dob, font=("Segoe UI", 11), date_pattern='dd-mm-yyyy', background='#2c3e50', foreground='white')
        self.txt_dob.place(x=480, y=65, width=200)

        Label(InputFrame, text="D.O.J", font=("Segoe UI", 11), bg="white").place(x=710, y=65)
        self.txt_doj = DateEntry(InputFrame, textvariable=self.var_doj, font=("Segoe UI", 11), date_pattern='dd-mm-yyyy', background='#2c3e50', foreground='white')
        self.txt_doj.place(x=820, y=65, width=200)

        #--- Row 3 ---
        Label(InputFrame, text="Email", font=("Segoe UI", 11), bg="white").place(x=30, y=110)
        txt_email = Entry(InputFrame, textvariable=self.var_email, font=("Segoe UI", 11), bg="#f9f9f9").place(x=130, y=110, width=200)

        Label(InputFrame, text="Password", font=("Segoe UI", 11), bg="white").place(x=370, y=110)
        txt_pass = Entry(InputFrame, textvariable=self.var_pass, font=("Segoe UI", 11), bg="#f9f9f9", show="*").place(x=480, y=110, width=200)

        Label(InputFrame, text="User Type", font=("Segoe UI", 11), bg="white").place(x=710, y=110)
        cmb_utype = ttk.Combobox(InputFrame, textvariable=self.var_utype, values=("Admin", "Employee"), state='readonly', justify=CENTER, font=("Segoe UI", 11))
        cmb_utype.place(x=820, y=110, width=200)
        cmb_utype.current(0)

        #--- Row 4 ---
        Label(InputFrame, text="Address", font=("Segoe UI", 11), bg="white").place(x=30, y=155)
        self.txt_address = Text(InputFrame, font=("Segoe UI", 11), bg="#f9f9f9", bd=1, relief=SOLID)
        self.txt_address.place(x=130, y=155, width=550, height=60)

        Label(InputFrame, text="Salary", font=("Segoe UI", 11), bg="white").place(x=710, y=155)
        txt_salary = Entry(InputFrame, textvariable=self.var_salary, font=("Segoe UI", 11), bg="#f9f9f9").place(x=820, y=155, width=200)

        #--- Buttons Frame ---
        btn_Frame = Frame(InputFrame, bg="white")
        btn_Frame.place(x=480, y=240, width=540, height=45)

        btn_add = Button(btn_Frame, text="Save", command=self.add, font=("Segoe UI", 11, "bold"), bg="#2ecc71", fg="white", cursor="hand2", bd=0).place(x=0, y=0, width=120, height=35)
        btn_update = Button(btn_Frame, text="Update", command=self.update, font=("Segoe UI", 11, "bold"), bg="#f1c40f", fg="white", cursor="hand2", bd=0).place(x=135, y=0, width=120, height=35)
        btn_delete = Button(btn_Frame, text="Delete", command=self.delete, font=("Segoe UI", 11, "bold"), bg="#e74c3c", fg="white", cursor="hand2", bd=0).place(x=270, y=0, width=120, height=35)
        btn_clear = Button(btn_Frame, text="Clear", command=self.clear, font=("Segoe UI", 11, "bold"), bg="#95a5a6", fg="white", cursor="hand2", bd=0).place(x=405, y=0, width=120, height=35)

        #--- Treeview Section ---
        emp_frame = Frame(self.root, bd=3, relief=RIDGE)
        emp_frame.place(x=20, y=410, width=1060, height=180)

        scrolly = Scrollbar(emp_frame, orient=VERTICAL)
        scrollx = Scrollbar(emp_frame, orient=HORIZONTAL)

        # Style the Treeview
        style = ttk.Style()
        style.configure("Treeview", font=("Segoe UI", 10), rowheight=25)
        style.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"))

        self.EmployeeTable = ttk.Treeview(emp_frame, columns=("eid", "name", "email", "gender", "contact", "dob", "doj", "pass", "utype", "address", "salary"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.EmployeeTable.xview)
        scrolly.config(command=self.EmployeeTable.yview)

        # Headings (No Change)
        self.EmployeeTable.heading("eid", text="EMP ID")
        self.EmployeeTable.heading("name", text="Name")
        self.EmployeeTable.heading("email", text="Email")
        self.EmployeeTable.heading("gender", text="Gender")
        self.EmployeeTable.heading("contact", text="Contact")
        self.EmployeeTable.heading("dob", text="D.O.B")
        self.EmployeeTable.heading("doj", text="D.O.J")
        self.EmployeeTable.heading("pass", text="Password")
        self.EmployeeTable.heading("utype", text="User Type")
        self.EmployeeTable.heading("address", text="Address")
        self.EmployeeTable.heading("salary", text="Salary")

        self.EmployeeTable["show"] = "headings"

        # Columns Width (Optimized)
        for col in self.EmployeeTable["columns"]:
            self.EmployeeTable.column(col, width=100, anchor=CENTER)

        self.EmployeeTable.pack(fill=BOTH, expand=1)
        self.EmployeeTable.bind("<ButtonRelease-1>", self.get_data)

        self.show()

    #================ FUNCTIONS (Same as yours, just cleaned up) =================
    
    # ... (باقي الدوال كما هي تماماً في كودك الأصلي لضمان الربط بالقاعدة)
    # ملاحظة: انقل دوال add, show, get_data, update, delete, clear, search هنا بنفس الكود الذي لديك.

    def add(self):
        con = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=AMD\\SQLEXPRESS;DATABASE=ims;Trusted_Connection=yes;TrustServerCertificate=yes;')
        cur = con.cursor()
        try:
            if self.var_name.get() == "":
                messagebox.showerror("Error", "Employee Name must be required", parent=self.root)
            else:
                cur.execute("""INSERT INTO employee 
                            (name, email, gender, contact, dob, doj, pass, utype, address, salary) 
                            VALUES (?,?,?,?,?,?,?,?,?,?)""", 
                            (
                                self.var_name.get(),
                                self.var_email.get(),
                                self.var_gender.get(),
                                self.var_contact.get(),
                                self.var_dob.get(),
                                self.var_doj.get(),
                                self.var_pass.get(),
                                self.var_utype.get(),
                                self.txt_address.get('1.0', END).strip(), 
                                self.var_salary.get(),
                            ))
                con.commit()
                messagebox.showinfo("Success", "Employee Added Successfully", parent=self.root)
                self.show()
                self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)
        finally:
            con.close()

    def show(self):
        con = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=AMD\\SQLEXPRESS;DATABASE=ims;Trusted_Connection=yes;TrustServerCertificate=yes;')
        cur = con.cursor()
        try:
            cur.execute("select eid, name, email, gender, contact, dob, doj, pass, utype, address, salary from employee")
            rows = cur.fetchall()
            self.EmployeeTable.delete(*self.EmployeeTable.get_children())
            for row in rows:
                self.EmployeeTable.insert('', END, values=list(row))
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)
        finally:
            con.close()

    def get_data(self, ev):
        f = self.EmployeeTable.focus()
        content = (self.EmployeeTable.item(f))
        row = content['values']
        if len(row) != 0:
            self.var_emp_id.set(row[0])
            self.var_name.set(row[1])
            self.var_email.set(row[2])
            self.var_gender.set(row[3])
            self.var_contact.set(row[4])
            self.txt_dob.set_date(row[5])
            self.txt_doj.set_date(row[6])
            self.var_pass.set(row[7])
            self.var_utype.set(row[8])
            self.txt_address.delete('1.0', END)
            self.txt_address.insert(END, row[9])
            self.var_salary.set(row[10])

    def update(self):
        con = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=AMD\\SQLEXPRESS;DATABASE=ims;Trusted_Connection=yes;TrustServerCertificate=yes;')
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror("Error", "Employee ID Must be required", parent=self.root)
            else:
                cur.execute("select * from employee where eid=?", (self.var_emp_id.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Employee ID", parent=self.root)
                else:
                    cur.execute("update employee set name=?, email=?, gender=?, contact=?, dob=?, doj=?, pass=?, utype=?, address=?, salary=? where eid=?", (
                        self.var_name.get(), self.var_email.get(), self.var_gender.get(),
                        self.var_contact.get(), self.var_dob.get(), self.var_doj.get(),
                        self.var_pass.get(), self.var_utype.get(), self.txt_address.get('1.0', END).strip(),
                        self.var_salary.get(), self.var_emp_id.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Employee Updated Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)
        finally:
            con.close()

    def delete(self):
        con = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=AMD\\SQLEXPRESS;DATABASE=ims;Trusted_Connection=yes;TrustServerCertificate=yes;')
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror("Error", "Employee ID Must be required", parent=self.root)
            else:
                cur.execute("select * from employee where eid=?", (self.var_emp_id.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Employee ID", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                    if op == True:
                        cur.execute("delete from employee where eid=?", (self.var_emp_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Employee Deleted Successfully", parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)
        finally:
            con.close()

    def clear(self):
        self.var_emp_id.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_contact.set("")
        self.var_dob.set("")
        self.var_doj.set("")
        self.var_pass.set("")
        self.var_utype.set("Admin")
        self.txt_address.delete('1.0', END)
        self.var_salary.set("")
        self.var_searchtxt.set("")
        self.var_searchby.set("Select")
        self.show()

    def search(self):
        con = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=AMD\\SQLEXPRESS;DATABASE=ims;Trusted_Connection=yes;TrustServerCertificate=yes;')
        cur = con.cursor()
        try:
            if self.var_searchby.get() == "Select":
                messagebox.showerror("Error", "Select Search By Option", parent=self.root)
            elif self.var_searchtxt.get() == "":
                messagebox.showerror("Error", "Search input should be required", parent=self.root)
            else:
                cur.execute("select * from employee where " + self.var_searchby.get() + " LIKE '%" + self.var_searchtxt.get() + "%'")
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                    for row in rows:
                        self.EmployeeTable.insert('', END, values=list(row))
                else:
                    messagebox.showerror("Error", "No record found!!!", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)
        finally:
            con.close()

if __name__=="__main__":
    root = Tk()
    obj = employeeClass(root)
    root.mainloop()