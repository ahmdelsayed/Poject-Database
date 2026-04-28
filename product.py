from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import pyodbc 

class productClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x650+220+50")
        self.root.title("Advanced Inventory System | Product Management")
        self.root.config(bg="#f4f6f7")
        self.root.focus_force()

        #================ Variables =================
        self.var_cat = StringVar()
        self.var_sup = StringVar()
        self.cat_list = []
        self.sup_list = []
        self.fetch_cat_sup() 

        self.var_pid = StringVar()
        self.var_name = StringVar()
        self.var_price = StringVar()
        self.var_qty = StringVar()
        self.var_status = StringVar()
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()

        #--- Header Section ---
        Header_Frame = Frame(self.root, bg="#0f172a", bd=0)
        Header_Frame.pack(side=TOP, fill=X)
        
        title = Label(Header_Frame, text="📦 PRODUCT INVENTORY MANAGEMENT", font=("Segoe UI", 18, "bold"), bg="#0f172a", fg="white", pady=15)
        title.pack()

        #--- Left Panel (Data Entry) ---
        Product_Frame = LabelFrame(self.root, text=" 📝 Manage Product Details ", font=("Segoe UI", 12, "bold"), bd=2, relief=RIDGE, bg="white", fg="#2c3e50")
        Product_Frame.place(x=10, y=80, width=450, height=540)

        # Labels & Input Fields
        lbl_category = Label(Product_Frame, text="Category", font=("Segoe UI", 11), bg="white").place(x=30, y=40)
        cmb_cat = ttk.Combobox(Product_Frame, textvariable=self.var_cat, values=self.cat_list, state='readonly', justify=CENTER, font=("Segoe UI", 11))
        cmb_cat.place(x=150, y=40, width=240, height=30)
        cmb_cat.set("Select")

        lbl_supplier = Label(Product_Frame, text="Supplier", font=("Segoe UI", 11), bg="white").place(x=30, y=90)
        cmb_sup = ttk.Combobox(Product_Frame, textvariable=self.var_sup, values=self.sup_list, state='readonly', justify=CENTER, font=("Segoe UI", 11))
        cmb_sup.place(x=150, y=90, width=240, height=30)
        cmb_sup.set("Select")

        lbl_name = Label(Product_Frame, text="Product Name", font=("Segoe UI", 11), bg="white").place(x=30, y=140)
        txt_name = Entry(Product_Frame, textvariable=self.var_name, font=("Segoe UI", 11), bg="#f9f9f9", bd=1, relief=SOLID).place(x=150, y=140, width=240, height=30)

        lbl_price = Label(Product_Frame, text="Price / Unit", font=("Segoe UI", 11), bg="white").place(x=30, y=190)
        txt_price = Entry(Product_Frame, textvariable=self.var_price, font=("Segoe UI", 11), bg="#f9f9f9", bd=1, relief=SOLID).place(x=150, y=190, width=240, height=30)

        lbl_qty = Label(Product_Frame, text="Quantity", font=("Segoe UI", 11), bg="white").place(x=30, y=240)
        txt_qty = Entry(Product_Frame, textvariable=self.var_qty, font=("Segoe UI", 11), bg="#f9f9f9", bd=1, relief=SOLID).place(x=150, y=240, width=240, height=30)
        
        lbl_status = Label(Product_Frame, text="Status", font=("Segoe UI", 11), bg="white").place(x=30, y=290)
        cmb_status = ttk.Combobox(Product_Frame, textvariable=self.var_status, values=("Active", "Inactive"), state='readonly', justify=CENTER, font=("Segoe UI", 11))
        cmb_status.place(x=150, y=290, width=240, height=30)
        cmb_status.current(0)

        # Buttons with icons style
        btn_Frame = Frame(Product_Frame, bg="white")
        btn_Frame.place(x=10, y=360, width=415, height=130)

        btn_add = Button(btn_Frame, text="SAVE PRODUCT", command=self.add, font=("Segoe UI", 10, "bold"), bg="#2ecc71", fg="white", cursor="hand2", bd=0).place(x=20, y=10, width=175, height=40)
        btn_update = Button(btn_Frame, text="UPDATE DATA", command=self.update, font=("Segoe UI", 10, "bold"), bg="#f1c40f", fg="white", cursor="hand2", bd=0).place(x=215, y=10, width=175, height=40)
        btn_delete = Button(btn_Frame, text="DELETE RECORD", command=self.delete, font=("Segoe UI", 10, "bold"), bg="#e74c3c", fg="white", cursor="hand2", bd=0).place(x=20, y=65, width=175, height=40)
        btn_clear = Button(btn_Frame, text="CLEAR FORM", command=self.clear, font=("Segoe UI", 10, "bold"), bg="#95a5a6", fg="white", cursor="hand2", bd=0).place(x=215, y=65, width=175, height=40)

        #--- Right Panel (Search & Table) ---
        SearchFrame = LabelFrame(self.root, text=" 🔍 Search Product ", font=("Segoe UI", 12, "bold"), bd=2, relief=RIDGE, bg="white", fg="#2c3e50")
        SearchFrame.place(x=480, y=80, width=600, height=80)

        cmb_search = ttk.Combobox(SearchFrame, textvariable=self.var_searchby, values=("Select", "Category", "Supplier", "Name"), state='readonly', justify=CENTER, font=("Segoe UI", 11))
        cmb_search.place(x=10, y=10, width=150, height=30)
        cmb_search.current(0)

        txt_search = Entry(SearchFrame, textvariable=self.var_searchtxt, font=("Segoe UI", 12), bg="#ebf5fb", bd=1).place(x=170, y=10, width=250, height=30)
        btn_search = Button(SearchFrame, text="Search Now", command=self.search, font=("Segoe UI", 10, "bold"), bg="#3498db", fg="white", cursor="hand2", bd=0).place(x=430, y=10, width=150, height=30)

        # Table Section
        p_frame = Frame(self.root, bd=3, relief=RIDGE, bg="white")
        p_frame.place(x=480, y=170, width=600, height=450)

        scrolly = Scrollbar(p_frame, orient=VERTICAL)
        scrollx = Scrollbar(p_frame, orient=HORIZONTAL)

        # Treeview Styling
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", background="white", foreground="#2c3e50", rowheight=30, fieldbackground="white", font=("Segoe UI", 10))
        style.map("Treeview", background=[('selected', '#3498db')])
        style.configure("Treeview.Heading", background="#e2e8f0", font=("Segoe UI", 10, "bold"), borderwidth=0)

        self.productTable = ttk.Treeview(p_frame, columns=("pid", "Category", "Supplier", "name", "price", "qty", "status"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.productTable.xview)
        scrolly.config(command=self.productTable.yview)

        self.productTable.heading("pid", text="P ID")
        self.productTable.heading("Category", text="Category")
        self.productTable.heading("Supplier", text="Supplier")
        self.productTable.heading("name", text="Product Name")
        self.productTable.heading("price", text="Price")
        self.productTable.heading("qty", text="Qty")
        self.productTable.heading("status", text="Status")

        self.productTable["show"] = "headings"
        for col in self.productTable["columns"]:
            self.productTable.column(col, width=90, anchor=CENTER)

        self.productTable.pack(fill=BOTH, expand=1)
        self.productTable.bind("<ButtonRelease-1>", self.get_data)

        self.show()

# ================= الوظائف (Functions) =================

    def get_connection(self):
        return pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=AMD\\SQLEXPRESS;DATABASE=ims;Trusted_Connection=yes;TrustServerCertificate=yes;')

    def fetch_cat_sup(self):
        self.cat_list.append("Empty")
        self.sup_list.append("Empty")
        con = self.get_connection()
        cur = con.cursor()
        try:
            cur.execute("select name from category")
            cat = cur.fetchall()
            if len(cat) > 0:
                del self.cat_list[:]
                self.cat_list.append("Select")
                for i in cat:
                    self.cat_list.append(i[0])
            
            cur.execute("select name from supplier")
            sup = cur.fetchall()
            if len(sup) > 0:
                del self.sup_list[:]
                self.sup_list.append("Select")
                for i in sup:
                    self.sup_list.append(i[0])
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def add(self):
        con = self.get_connection()
        cur = con.cursor()
        try:
            if self.var_cat.get() == "Select" or self.var_sup.get() == "Select" or self.var_name.get() == "":
                messagebox.showerror("Error", "All fields are required", parent=self.root)
            else:
                cur.execute("insert into product (Category, Supplier, name, price, qty, status) values(?,?,?,?,?,?)", (
                    self.var_cat.get(),
                    self.var_sup.get(),
                    self.var_name.get(),
                    self.var_price.get(),
                    self.var_qty.get(),
                    self.var_status.get(),
                ))
                con.commit()
                messagebox.showinfo("Success", "Product Added Successfully", parent=self.root)
                self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)
        finally:
            con.close()

    def show(self):
        con = self.get_connection()
        cur = con.cursor()
        try:
            cur.execute("select * from product")
            rows = cur.fetchall()
            self.productTable.delete(*self.productTable.get_children())
            for row in rows:
                self.productTable.insert('', END, values=list(row))
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)
        finally:
            con.close()

    def get_data(self, ev):
        f = self.productTable.focus()
        content = (self.productTable.item(f))
        row = content['values']
        if len(row) != 0:
            self.var_pid.set(row[0])
            self.var_cat.set(row[1])
            self.var_sup.set(row[2])
            self.var_name.set(row[3])
            self.var_price.set(row[4])
            self.var_qty.set(row[5])
            self.var_status.set(row[6])

    def update(self):
        con = self.get_connection()
        cur = con.cursor()
        try:
            if self.var_pid.get() == "":
                messagebox.showerror("Error", "Select product from list", parent=self.root)
            else:
                cur.execute("update product set Category=?, Supplier=?, name=?, price=?, qty=?, status=? where pid=?", (
                    self.var_cat.get(),
                    self.var_sup.get(),
                    self.var_name.get(),
                    self.var_price.get(),
                    self.var_qty.get(),
                    self.var_status.get(),
                    self.var_pid.get()
                ))
                con.commit()
                messagebox.showinfo("Success", "Product Updated Successfully", parent=self.root)
                self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)
        finally:
            con.close()

    def delete(self):
        con = self.get_connection()
        cur = con.cursor()
        try:
            if self.var_pid.get() == "":
                messagebox.showerror("Error", "Select product from list", parent=self.root)
            else:
                op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                if op == True:
                    cur.execute("delete from product where pid=?", (self.var_pid.get(),))
                    con.commit()
                    messagebox.showinfo("Delete", "Product Deleted Successfully", parent=self.root)
                    self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)
        finally:
            con.close()

    def clear(self):
        self.var_cat.set("Select")
        self.var_sup.set("Select")
        self.var_name.set("")
        self.var_price.set("")
        self.var_qty.set("")
        self.var_status.set("Active")
        self.var_pid.set("")
        self.var_searchtxt.set("")
        self.var_searchby.set("Select")
        self.show()

    def search(self):
        con = self.get_connection()
        cur = con.cursor()
        try:
            if self.var_searchby.get() == "Select":
                messagebox.showerror("Error", "Select Search By Option", parent=self.root)
            elif self.var_searchtxt.get() == "":
                messagebox.showerror("Error", "Search input required", parent=self.root)
            else:
                cur.execute("select * from product where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.productTable.delete(*self.productTable.get_children())
                    for row in rows:
                        self.productTable.insert('', END, values=list(row))
                else:
                    messagebox.showerror("Error", "No record found!!!", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)
        finally:
            con.close()

if __name__=="__main__":
    root = Tk()
    obj = productClass(root)
    root.mainloop()