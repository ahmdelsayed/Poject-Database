from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import pyodbc 

class supplierClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x570+220+130")
        self.root.title("Inventory Management System | Supplier Management")
        self.root.config(bg="#f4f6f7")
        self.root.focus_force()

        # --- (Variables) ---
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()
        self.var_sup_invoice = StringVar()
        self.var_name = StringVar()
        self.var_contact = StringVar()

        # --- Title ---
        Header_Frame = Frame(self.root, bg="#0f172a", bd=0)
        Header_Frame.pack(side=TOP, fill=X)
        
        title = Label(Header_Frame, text="📦 SUPPLIER RELATIONSHIP MANAGEMENT", font=("Segoe UI", 18, "bold"), bg="#0f172a", fg="white", pady=15)
        title.pack()

        # --- Left Panel (Entry Fields) ---
        Left_Frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        Left_Frame.place(x=10, y=70, width=400, height=480)

        subtitle = Label(Left_Frame, text="Manage Supplier Details", font=("Segoe UI", 13, "bold"), bg="#34495e", fg="white")
        subtitle.pack(side=TOP, fill=X)

        # Labels & Entry Fields
        lbl_invoice = Label(Left_Frame, text="Invoice No.", font=("Segoe UI", 11), bg="white").place(x=20, y=50)
        txt_invoice = Entry(Left_Frame, textvariable=self.var_sup_invoice, font=("Segoe UI", 11), bg="#f9f9f9", bd=1, relief=SOLID).place(x=130, y=50, width=240, height=28)

        lbl_name = Label(Left_Frame, text="Supplier Name", font=("Segoe UI", 11), bg="white").place(x=20, y=100)
        txt_name = Entry(Left_Frame, textvariable=self.var_name, font=("Segoe UI", 11), bg="#f9f9f9", bd=1, relief=SOLID).place(x=130, y=100, width=240, height=28)

        lbl_contact = Label(Left_Frame, text="Contact No.", font=("Segoe UI", 11), bg="white").place(x=20, y=150)
        txt_contact = Entry(Left_Frame, textvariable=self.var_contact, font=("Segoe UI", 11), bg="#f9f9f9", bd=1, relief=SOLID).place(x=130, y=150, width=240, height=28)

        lbl_desc = Label(Left_Frame, text="Description", font=("Segoe UI", 11), bg="white").place(x=20, y=200)
        self.txt_desc = Text(Left_Frame, font=("Segoe UI", 11), bg="#f9f9f9", bd=1, relief=SOLID)
        self.txt_desc.place(x=130, y=200, width=240, height=100)

        # --- Buttons Frame ---
        btn_Frame = Frame(Left_Frame, bg="white")
        btn_Frame.place(x=10, y=330, width=380, height=120)

        btn_add = Button(btn_Frame, text="Save", command=self.add, font=("Segoe UI", 11, "bold"), bg="#2196f3", fg="white", cursor="hand2", bd=0).place(x=10, y=10, width=170, height=40)
        btn_update = Button(btn_Frame, text="Update", command=self.update, font=("Segoe UI", 11, "bold"), bg="#4caf50", fg="white", cursor="hand2", bd=0).place(x=190, y=10, width=170, height=40)
        btn_delete = Button(btn_Frame, text="Delete", command=self.delete, font=("Segoe UI", 11, "bold"), bg="#f44336", fg="white", cursor="hand2", bd=0).place(x=10, y=60, width=170, height=40)
        btn_clear = Button(btn_Frame, text="Clear", command=self.clear, font=("Segoe UI", 11, "bold"), bg="#607d8b", fg="white", cursor="hand2", bd=0).place(x=190, y=60, width=170, height=40)

        # --- Right Panel (Search & Table) ---
        Right_Frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        Right_Frame.place(x=420, y=70, width=665, height=480)

        # Search Area
        lbl_search = Label(Right_Frame, text="Search by Invoice No:", font=("Segoe UI", 11, "bold"), bg="white").place(x=10, y=15)
        txt_search = Entry(Right_Frame, textvariable=self.var_searchtxt, font=("Segoe UI", 12), bg="#f9f9f9", bd=1, relief=SOLID).place(x=180, y=15, width=350, height=30)
        btn_search = Button(Right_Frame, text="🔍 Search", command=self.search, font=("Segoe UI", 10, "bold"), bg="#3498db", fg="white", cursor="hand2", bd=0).place(x=540, y=15, width=110, height=30)

        # --- Supplier Table ---
        Table_Frame = Frame(Right_Frame, bd=1, relief=SOLID)
        Table_Frame.place(x=10, y=60, width=640, height=400)

        scrolly = Scrollbar(Table_Frame, orient=VERTICAL)
        scrollx = Scrollbar(Table_Frame, orient=HORIZONTAL)

        # Style the Treeview
        style = ttk.Style()
        style.configure("Treeview", font=("Segoe UI", 10), rowheight=25, background="#ffffff")
        style.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"))

        self.SupplierTable = ttk.Treeview(Table_Frame, columns=("invoice", "name", "contact", "desc"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.SupplierTable.xview)
        scrolly.config(command=self.SupplierTable.yview)

        self.SupplierTable.heading("invoice", text="Invoice No.")
        self.SupplierTable.heading("name", text="Supplier Name")
        self.SupplierTable.heading("contact", text="Contact No.")
        self.SupplierTable.heading("desc", text="Description")

        self.SupplierTable["show"] = "headings"

        self.SupplierTable.column("invoice", width=100, anchor=CENTER)
        self.SupplierTable.column("name", width=150)
        self.SupplierTable.column("contact", width=120, anchor=CENTER)
        self.SupplierTable.column("desc", width=250)
        self.SupplierTable.pack(fill=BOTH, expand=1)
        self.SupplierTable.bind("<ButtonRelease-1>", self.get_data)

        self.show()

# ================= (Functions) =================

    def get_connection(self):
        return pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=***\\SQLEXPRESS;DATABASE=ims;Trusted_Connection=yes;TrustServerCertificate=yes;')

    def add(self):
        con = self.get_connection()
        cur = con.cursor()
        try:
            if self.var_sup_invoice.get() == "":
                messagebox.showerror("Error", "Invoice No. must be required", parent=self.root)
            else:
                cur.execute("select * from supplier where invoice=?", (self.var_sup_invoice.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "Invoice No. already assigned, try different", parent=self.root)
                else:
                    cur.execute("insert into supplier (invoice, name, contact, desc_info) values(?,?,?,?)", (
                         self.var_sup_invoice.get(),
                         self.var_name.get(),
                         self.var_contact.get(),
                         self.txt_desc.get('1.0', END).strip(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Supplier Added Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)
        finally:
            con.close()

    def show(self):
        con = self.get_connection()
        cur = con.cursor()
        try:
            cur.execute("select * from supplier")
            rows = cur.fetchall()
            self.SupplierTable.delete(*self.SupplierTable.get_children())
            for row in rows:
                self.SupplierTable.insert('', END, values=list(row))
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)
        finally:
            con.close()

    def get_data(self, ev):
        f = self.SupplierTable.focus()
        content = (self.SupplierTable.item(f))
        row = content['values']
        if len(row) != 0:
            self.var_sup_invoice.set(row[0])
            self.var_name.set(row[1])
            self.var_contact.set(row[2])
            self.txt_desc.delete('1.0', END)
            self.txt_desc.insert(END, row[3])

    def update(self):
        con = self.get_connection()
        cur = con.cursor()
        try:
            if self.var_sup_invoice.get() == "":
                messagebox.showerror("Error", "Invoice No. must be required", parent=self.root)
            else:
                cur.execute("select * from supplier where invoice=?", (self.var_sup_invoice.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Invoice No.", parent=self.root)
                else:
                    cur.execute("update supplier set name=?, contact=?, desc_info=? where invoice=?", (
                        self.var_name.get(),
                        self.var_contact.get(),
                        self.txt_desc.get('1.0', END).strip(),
                        self.var_sup_invoice.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Supplier Updated Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)
        finally:
            con.close()

    def delete(self):
        con = self.get_connection()
        cur = con.cursor()
        try:
            if self.var_sup_invoice.get() == "":
                messagebox.showerror("Error", "Invoice No. must be required", parent=self.root)
            else:
                cur.execute("select * from supplier where invoice=?", (self.var_sup_invoice.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Invoice No.", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                    if op == True:
                        cur.execute("delete from supplier where invoice=?", (self.var_sup_invoice.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Supplier Deleted Successfully", parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)
        finally:
            con.close()

    def clear(self):
        self.var_sup_invoice.set("")
        self.var_name.set("")
        self.var_contact.set("")
        self.txt_desc.delete('1.0', END)
        self.var_searchtxt.set("")
        self.show()

    def search(self):
        con = self.get_connection()
        cur = con.cursor()
        try:
            if self.var_searchtxt.get() == "":
                messagebox.showerror("Error", "Invoice No. should be required", parent=self.root)
            else:
                cur.execute("select * from supplier where invoice=?", (self.var_searchtxt.get(),))
                row = cur.fetchone()
                if row != None:
                    self.SupplierTable.delete(*self.SupplierTable.get_children())
                    self.SupplierTable.insert('', END, values=list(row))
                else:
                    messagebox.showerror("Error", "No record found!!!", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)
        finally:
            con.close()

if __name__=="__main__":
    root = Tk()
    obj = supplierClass(root)
    root.mainloop()
