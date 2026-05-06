from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import pyodbc 

class categoryClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x600+220+130")
        self.root.title("Inventory Management System | Category Module")
        self.root.config(bg="#f8fafc")
        self.root.focus_force()

        # --- (Variables) ---
        self.var_cat_id = StringVar()
        self.var_name = StringVar()

        # --- Header Section ---
        Header_Frame = Frame(self.root, bg="#0f172a", bd=0)
        Header_Frame.pack(side=TOP, fill=X)
        
    
        title = Label(Header_Frame, text="📑 PRODUCT CATEGORY MANAGEMENT", font=("Segoe UI", 18, "bold"), bg="#0f172a", fg="white", pady=15)
        title.pack()

        # --- Management Frame (Input Area) ---
        Manage_Frame = Frame(self.root, bg="white", bd=1, relief=GROOVE)
        Manage_Frame.place(x=50, y=80, width=1000, height=130)

        lbl_instr = Label(Manage_Frame, text="Enter New Category Name:", font=("Segoe UI", 12, "bold"), bg="white", fg="#334155").place(x=30, y=20)
        
        txt_name = Entry(Manage_Frame, textvariable=self.var_name, font=("Segoe UI", 14), bg="#f1f5f9", bd=0)
        txt_name.place(x=30, y=55, width=450, height=35)

        Frame(Manage_Frame, bg="#3b82f6").place(x=30, y=90, width=450, height=2)

        # Buttons
        btn_add = Button(Manage_Frame, text="➕ Add Category", command=self.add, font=("Segoe UI", 11, "bold"), bg="#10b981", fg="white", cursor="hand2", bd=0).place(x=500, y=55, width=160, height=37)
        btn_delete = Button(Manage_Frame, text="🗑️ Delete Selected", command=self.delete, font=("Segoe UI", 11, "bold"), bg="#ef4444", fg="white", cursor="hand2", bd=0).place(x=670, y=55, width=160, height=37)

        # --- Table Section ---
        Table_Frame = Frame(self.root, bd=1, relief=RIDGE, bg="white")
        Table_Frame.place(x=50, y=220, width=1000, height=150)

        scrolly = Scrollbar(Table_Frame, orient=VERTICAL)
        scrollx = Scrollbar(Table_Frame, orient=HORIZONTAL)

        # Treeview Styling
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", background="white", rowheight=30, font=("Segoe UI", 10))
        style.configure("Treeview.Heading", background="#e2e8f0", font=("Segoe UI", 10, "bold"))

        self.categoryTable = ttk.Treeview(Table_Frame, columns=("cid", "name"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.categoryTable.xview)
        scrolly.config(command=self.categoryTable.yview)

        self.categoryTable.heading("cid", text="CATEGORY ID")
        self.categoryTable.heading("name", text="CATEGORY NAME")
        self.categoryTable["show"] = "headings"
        
        self.categoryTable.column("cid", width=100, anchor=CENTER)
        self.categoryTable.column("name", width=800, anchor=W)
        self.categoryTable.pack(fill=BOTH, expand=1)
        self.categoryTable.bind("<ButtonRelease-1>", self.get_data)

        # --- Images Section (Modern Banner Style) ---

        try:
            self.im1 = Image.open("images/category.png") 
            self.im1 = self.im1.resize((1000, 200), Image.LANCZOS)
            self.im1 = ImageTk.PhotoImage(self.im1)
            self.lbl_im1 = Label(self.root, image=self.im1, bd=0, bg="#f8fafc")
            self.lbl_im1.place(x=50, y=380)

        except Exception as ex:
            Label(self.root, text="[ Nano Banana Banner ]", bg="#cbd5e1", fg="#64748b").place(x=50, y=380, width=1000, height=200)
        
        self.show()

# ================= (Logic) =================

    def get_connection(self):
        return pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=***\\SQLEXPRESS;DATABASE=***;Trusted_Connection=yes;TrustServerCertificate=yes;')

    def add(self):
        con = self.get_connection()
        cur = con.cursor()
        try:
            if self.var_name.get() == "":
                messagebox.showerror("Error", "Category Name must be required", parent=self.root)
            else:
                cur.execute("select * from category where name=?", (self.var_name.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "Category already present, try different", parent=self.root)
                else:
                    cur.execute("insert into category (name) values(?)", (self.var_name.get(),))
                    con.commit()
                    messagebox.showinfo("Success", "Category Added Successfully", parent=self.root)
                    self.show()
                    self.var_name.set("")
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)
        finally:
            con.close()

    def show(self):
        con = self.get_connection()
        cur = con.cursor()
        try:
            cur.execute("select * from category")
            rows = cur.fetchall()
            self.categoryTable.delete(*self.categoryTable.get_children())
            for row in rows:
                self.categoryTable.insert('', END, values=list(row))
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)
        finally:
            con.close()

    def get_data(self, ev):
        f = self.categoryTable.focus()
        content = (self.categoryTable.item(f))
        row = content['values']
        if len(row) != 0:
            self.var_cat_id.set(row[0])
            self.var_name.set(row[1])

    def delete(self):
        con = self.get_connection()
        cur = con.cursor()
        try:
            if self.var_cat_id.get() == "":
                messagebox.showerror("Error", "Please select category from list", parent=self.root)
            else:
                cur.execute("select * from category where cid=?", (self.var_cat_id.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Category", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                    if op == True:
                        cur.execute("delete from category where cid=?", (self.var_cat_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Category Deleted Successfully", parent=self.root)
                        self.show()
                        self.var_cat_id.set("")
                        self.var_name.set("")
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)
        finally:
            con.close()

if __name__=="__main__":
    root = Tk()
    obj = categoryClass(root)
    root.mainloop()
