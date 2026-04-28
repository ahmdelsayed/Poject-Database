from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import pyodbc
import time
import os

class BillClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x720+0+0")
        self.root.title("Inventory Management System | Professional Billing")
        self.root.config(bg="#f4f6f7")
        self.cart_list = [] 

        # --- المتغيرات (Variables) ---
        self.var_search = StringVar()
        self.var_cname = StringVar()
        self.var_contact = StringVar()
        self.var_pid = StringVar()
        self.var_pname = StringVar()
        self.var_price = StringVar()
        self.var_qty = StringVar()
        self.var_stock = StringVar()
        self.var_cal_input = StringVar()

        # --- (1) Header Section (العنوان كالصورة بالظبط) ---
        self.header = Frame(self.root, bg="#010c48", bd=0)
        self.header.place(x=0, y=0, relwidth=1, height=70)

        # تحميل الأيقونة (سلة التسوق)
        try:
            img = Image.open("images/logo1.png") 
            img = img.resize((50, 50), Image.LANCZOS)
            self.icon_title = ImageTk.PhotoImage(img)
        except:
            self.icon_title = None

        self.title = Label(
            self.header,
            text=" Inventory Management System",
            image=self.icon_title,
            compound="left",
            font=("Segoe UI", 35, "bold"),
            bg="#010c48", 
            fg="white",
            anchor="w",
            padx=20
        )
        self.title.pack(side=LEFT, fill=Y)

        # زر Logout (أعلى اليمين بنفس استايل الداشبورد)
        btn_logout = Button(
            self.header, 
            text="Logout", 
            command=self.logout, 
            font=("Segoe UI", 12, "bold"), 
            bg="#E74C3C", 
            fg="white", 
            cursor="hand2", 
            bd=0, 
            padx=20, 
            pady=5
        )
        btn_logout.pack(side=RIGHT, padx=20, pady=15)

        # --- شريط الساعة ---
        self.lbl_clock = Label(
            self.root, 
            text="Welcome to Inventory Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS", 
            font=("Segoe UI", 11), 
            bg="#34495e", 
            fg="white"
        )
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)

        # --- (2) إطار المنتجات (الجانب الأيسر) ---
        ProductFrame1 = LabelFrame(self.root, text=" 📦 Product Selection ", font=("Segoe UI", 12, "bold"), bd=2, relief=RIDGE, bg="white", fg="#2c3e50")
        ProductFrame1.place(x=10, y=110, width=410, height=585)

        txt_search = Entry(ProductFrame1, textvariable=self.var_search, font=("Segoe UI", 13), bg="#ebf5fb", bd=1).place(x=10, y=10, width=190, height=35)
        btn_search = Button(ProductFrame1, text="Search", command=self.search, font=("Segoe UI", 10, "bold"), bg="#3498db", fg="white", cursor="hand2", bd=0).place(x=210, y=10, width=85, height=35)
        btn_show_all = Button(ProductFrame1, text="All", command=self.show, font=("Segoe UI", 10, "bold"), bg="#607d8b", fg="white", cursor="hand2", bd=0).place(x=305, y=10, width=85, height=35)

        ProductFrame3 = Frame(ProductFrame1, bd=1, relief=SOLID)
        ProductFrame3.place(x=10, y=60, width=385, height=460)

        scrolly = Scrollbar(ProductFrame3, orient=VERTICAL)
        self.product_Table = ttk.Treeview(ProductFrame3, columns=("pid", "name", "price", "qty"), yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT, fill=Y)
        self.product_Table.heading("pid", text="ID")
        self.product_Table.heading("name", text="Name")
        self.product_Table.heading("price", text="Price")
        self.product_Table.heading("qty", text="Stock")
        self.product_Table["show"] = "headings"
        self.product_Table.column("pid", width=40, anchor=CENTER)
        self.product_Table.column("name", width=120)
        self.product_Table.column("price", width=70, anchor=CENTER)
        self.product_Table.column("qty", width=60, anchor=CENTER)
        self.product_Table.pack(fill=BOTH, expand=1)
        self.product_Table.bind("<ButtonRelease-1>", self.get_data)

        lbl_note = Label(ProductFrame1, text="* Note: Set Qty to 0 to Remove from Cart", font=("Segoe UI", 9, "italic"), bg="white", fg="red").pack(side=BOTTOM, pady=5)

        # --- (3) إطار العميل (أعلى المنتصف) ---
        CustomerFrame = LabelFrame(self.root, text=" 👤 Customer Details ", font=("Segoe UI", 12, "bold"), bd=2, relief=RIDGE, bg="white", fg="#2c3e50")
        CustomerFrame.place(x=430, y=110, width=515, height=90)

        lbl_name = Label(CustomerFrame, text="Name:", font=("Segoe UI", 11), bg="white").place(x=10, y=10)
        txt_name = Entry(CustomerFrame, textvariable=self.var_cname, font=("Segoe UI", 11), bg="#f9f9f9").place(x=70, y=10, width=150)
        lbl_contact = Label(CustomerFrame, text="Contact:", font=("Segoe UI", 11), bg="white").place(x=240, y=10)
        txt_contact = Entry(CustomerFrame, textvariable=self.var_contact, font=("Segoe UI", 11), bg="#f9f9f9").place(x=310, y=10, width=150)

        # --- (4) الحاسبة وسلة المشتريات (وسط المنتصف) ---
        Cal_Cart_Frame = Frame(self.root, bg="#f4f6f7")
        Cal_Cart_Frame.place(x=430, y=205, width=515, height=360)

        # الآلة الحاسبة
        Cal_Frame = Frame(Cal_Cart_Frame, bd=2, relief=RIDGE, bg="white")
        Cal_Frame.place(x=0, y=5, width=268, height=345)
        txt_cal = Entry(Cal_Frame, textvariable=self.var_cal_input, font=("Segoe UI", 20, "bold"), width=15, bd=5, relief=FLAT, bg="#ecf0f1", justify=RIGHT, state='readonly').grid(row=0, columnspan=4, pady=10, padx=5)
        
        btns = ['7', '8', '9', '+', '4', '5', '6', '-', '1', '2', '3', '*', '0', 'C', '=', '/']
        r, c = 1, 0
        for btn in btns:
            cmd = lambda x=btn: self.get_input(x)
            if btn == 'C': cmd = self.clear_cal
            elif btn == '=': cmd = self.perform_cal
            Button(Cal_Frame, text=btn, font=("Segoe UI", 14, "bold"), width=4, pady=10, bg="#34495e", fg="white", cursor="hand2", bd=0, command=cmd).grid(row=r, column=c, padx=2, pady=2)
            c += 1
            if c > 3: c = 0; r += 1

        # جدول السلة
        Cart_Frame = Frame(Cal_Cart_Frame, bd=2, relief=RIDGE, bg="white")
        Cart_Frame.place(x=275, y=5, width=240, height=345)
        self.cart_Title = Label(Cart_Frame, text="🛒 Items in Cart", font=("Segoe UI", 11, "bold"), bg="#2ecc71", fg="white")
        self.cart_Title.pack(side=TOP, fill=X)

        self.Cart_Table = ttk.Treeview(Cart_Frame, columns=("pid", "name", "price", "qty"))
        for col in ("pid", "name", "price", "qty"): self.Cart_Table.heading(col, text=col.upper())
        self.Cart_Table["show"] = "headings"
        for col, w in zip(("pid", "name", "price", "qty"), (30, 90, 50, 40)): self.Cart_Table.column(col, width=w, anchor=CENTER)
        self.Cart_Table.pack(fill=BOTH, expand=1)
        self.Cart_Table.bind("<ButtonRelease-1>", self.get_data_cart)

        # --- (5) إطار التحكم في المنتج (أسفل المنتصف) ---
        Add_Cart_WidgetsFrame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        Add_Cart_WidgetsFrame.place(x=430, y=575, width=515, height=120)

        Label(Add_Cart_WidgetsFrame, text="Product Name", font=("Segoe UI", 10), bg="white").place(x=5, y=5)
        Entry(Add_Cart_WidgetsFrame, textvariable=self.var_pname, font=("Segoe UI", 10), bg="#f9f9f9", state='readonly').place(x=5, y=30, width=170)
        Label(Add_Cart_WidgetsFrame, text="Price", font=("Segoe UI", 10), bg="white").place(x=190, y=5)
        Entry(Add_Cart_WidgetsFrame, textvariable=self.var_price, font=("Segoe UI", 10), bg="#f9f9f9", state='readonly').place(x=190, y=30, width=100)
        Label(Add_Cart_WidgetsFrame, text="Quantity", font=("Segoe UI", 10), bg="white").place(x=310, y=5)
        Entry(Add_Cart_WidgetsFrame, textvariable=self.var_qty, font=("Segoe UI", 10), bg="#ebf5fb").place(x=310, y=30, width=80)

        self.lbl_in_stock = Label(Add_Cart_WidgetsFrame, text="In Stock: 0", font=("Segoe UI", 10, "bold"), bg="white", fg="#e74c3c")
        self.lbl_in_stock.place(x=5, y=70)

        # زر CLEAR (الخاص بحقول المنتج)
        btn_clear_fields = Button(Add_Cart_WidgetsFrame, text="CLEAR", command=self.clear_cart_fields, font=("Segoe UI", 10, "bold"), bg="#95a5a6", fg="white", cursor="hand2", bd=0)
        btn_clear_fields.place(x=150, y=70, width=120, height=35)

        btn_add_cart = Button(Add_Cart_WidgetsFrame, text="ADD TO CART", command=self.add_update_cart, font=("Segoe UI", 10, "bold"), bg="#f1c40f", fg="black", cursor="hand2", bd=0)
        btn_add_cart.place(x=310, y=70, width=180, height=35)

        # --- (6) إطار الفاتورة (الجانب الأيمن) ---
        BillFrame = LabelFrame(self.root, text=" 🧾 Invoice Details ", font=("Segoe UI", 12, "bold"), bd=2, bg="white", fg="#2c3e50")
        BillFrame.place(x=955, y=110, width=380, height=415)
        
        scrolly_t = Scrollbar(BillFrame, orient=VERTICAL)
        self.txt_bill_area = Text(BillFrame, font=("Consolas", 11), bg="#fffbeb", yscrollcommand=scrolly_t.set, bd=0)
        scrolly_t.pack(side=RIGHT, fill=Y)
        self.txt_bill_area.pack(fill=BOTH, expand=1)
        scrolly_t.config(command=self.txt_bill_area.yview)

        # منطقة المبالغ والأزرار السفلية
        BillMenuFrame = Frame(self.root, bd=0, bg="#f4f6f7")
        BillMenuFrame.place(x=955, y=530, width=380, height=165)

        self.lbl_amnt = Label(BillMenuFrame, text="Bill Amount\n0.00", font=("Segoe UI", 12, "bold"), bg="#3498db", fg="white", bd=1, relief=SOLID)
        self.lbl_amnt.place(x=0, y=5, width=120, height=60)
        self.lbl_discount = Label(BillMenuFrame, text="Discount (5%)\n0.00", font=("Segoe UI", 12, "bold"), bg="#2ecc71", fg="white", bd=1, relief=SOLID)
        self.lbl_discount.place(x=125, y=5, width=120, height=60)
        self.lbl_net_pay = Label(BillMenuFrame, text="Net Pay\n0.00", font=("Segoe UI", 12, "bold"), bg="#e74c3c", fg="white", bd=1, relief=SOLID)
        self.lbl_net_pay.place(x=250, y=5, width=125, height=60)

        # زر CLEAR ALL (لمسح الفاتورة والعميل وكل شيء)
        btn_clear_all_invoice = Button(BillMenuFrame, text="CLEAR ALL", command=self.clear_all, font=("Segoe UI", 11, "bold"), bg="#64748b", fg="white", cursor="hand2", bd=0)
        btn_clear_all_invoice.place(x=0, y=75, width=120, height=45)

        btn_generate = Button(BillMenuFrame, text="GENERATE", font=("Segoe UI", 11, "bold"), bg="#0f172a", fg="white", cursor="hand2", bd=0)
        btn_generate.place(x=125, y=75, width=120, height=45)

        btn_print = Button(BillMenuFrame, text="PRINT", font=("Segoe UI", 11, "bold"), bg="#3b82f6", fg="white", cursor="hand2", bd=0)
        btn_print.place(x=250, y=75, width=125, height=45)

        self.show()

# ================= الوظائف (Functions) =================

    def logout(self):
        op = messagebox.askyesno("Confirm", "Do you really want to Logout?", parent=self.root)
        if op:
            self.root.destroy()

    def clear_cart_fields(self):
        self.var_pid.set(""); self.var_pname.set(""); self.var_price.set(""); self.var_qty.set("")
        self.lbl_in_stock.config(text="In Stock: 0"); self.var_stock.set("")

    def clear_all(self):
        del self.cart_list[:]
        self.var_cname.set(""); self.var_contact.set(""); self.var_search.set("")
        self.txt_bill_area.delete('1.0', END); self.cart_Title.config(text="🛒 Items in Cart")
        self.clear_cart_fields(); self.show(); self.show_cart(); self.bill_updates()

    def get_input(self, num):
        self.var_cal_input.set(self.var_cal_input.get() + str(num))

    def clear_cal(self):
        self.var_cal_input.set("")

    def perform_cal(self):
        try: self.var_cal_input.set(eval(self.var_cal_input.get()))
        except: messagebox.showerror("Error", "Invalid calculation")

    def get_connection(self):
        return pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=AMD\\SQLEXPRESS;DATABASE=ims;Trusted_Connection=yes;TrustServerCertificate=yes;')

    def show(self):
        con = self.get_connection(); cur = con.cursor()
        try:
            cur.execute("select pid, name, price, qty, status from product where status='Active'")
            rows = cur.fetchall()
            self.product_Table.delete(*self.product_Table.get_children())
            for row in rows: self.product_Table.insert('', END, values=list(row))
        except Exception as ex: messagebox.showerror("Error", str(ex), parent=self.root)
        finally: con.close()

    def search(self):
        con = self.get_connection(); cur = con.cursor()
        try:
            if self.var_search.get() == "": messagebox.showerror("Error", "Search input required", parent=self.root)
            else:
                cur.execute("select pid, name, price, qty, status from product where name LIKE '%"+self.var_search.get()+"%' and status='Active'")
                rows = cur.fetchall()
                self.product_Table.delete(*self.product_Table.get_children())
                for row in rows: self.product_Table.insert('', END, values=list(row))
        except Exception as ex: messagebox.showerror("Error", str(ex), parent=self.root)
        finally: con.close()

    def get_data(self, ev):
        f = self.product_Table.focus(); content = (self.product_Table.item(f)); row = content['values']
        self.var_pid.set(row[0]); self.var_pname.set(row[1]); self.var_price.set(row[2])
        self.lbl_in_stock.config(text=f"In Stock [{row[3]}]"); self.var_stock.set(row[3]); self.var_qty.set('1')

    def get_data_cart(self, ev):
        f = self.Cart_Table.focus(); content = (self.Cart_Table.item(f)); row = content['values']
        self.var_pid.set(row[0]); self.var_pname.set(row[1]); self.var_price.set(row[2]); self.var_qty.set(row[3])

    def add_update_cart(self):
        if self.var_pid.get() == '': messagebox.showerror('Error', "Select product", parent=self.root)
        elif self.var_qty.get() == '': messagebox.showerror('Error', "Quantity required", parent=self.root)
        elif int(self.var_qty.get()) > int(self.var_stock.get()): messagebox.showerror('Error', "Not enough stock", parent=self.root)
        else:
            cart_data = [self.var_pid.get(), self.var_pname.get(), self.var_price.get(), self.var_qty.get(), self.var_stock.get()]
            present, index_ = 'no', 0
            for row in self.cart_list:
                if self.var_pid.get() == row[0]: present = 'yes'; break
                index_ += 1
            if present == 'yes':
                op = messagebox.askyesno('Confirm', "Product already in cart\nUpdate or Remove?", parent=self.root)
                if op:
                    if self.var_qty.get() == "0": self.cart_list.pop(index_)
                    else: self.cart_list[index_][3] = self.var_qty.get() 
            else: self.cart_list.append(cart_data)
            self.show_cart(); self.bill_updates()

    def bill_updates(self):
        self.bill_amnt = sum(float(row[2]) * int(row[3]) for row in self.cart_list)
        self.discount = (self.bill_amnt * 5) / 100
        self.net_pay = self.bill_amnt - self.discount
        self.lbl_amnt.config(text=f"Bill Amnt\n{str(self.bill_amnt)}")
        self.lbl_net_pay.config(text=f"Net Pay\n{str(self.net_pay)}")
        self.cart_Title.config(text=f"🛒 {str(len(self.cart_list))} Items in Cart")

    def show_cart(self):
        self.Cart_Table.delete(*self.Cart_Table.get_children())
        for row in self.cart_list: self.Cart_Table.insert('', END, values=row)

if __name__=="__main__":
    root = Tk()
    obj = BillClass(root)
    root.mainloop()