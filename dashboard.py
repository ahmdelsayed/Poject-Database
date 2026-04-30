from tkinter import *
from PIL import Image, ImageTk 
from employee import employeeClass
import pyodbc
from supplier import supplierClass
from category import categoryClass
from product import productClass
from sales import salesClass
import time
import os
import sys

class IMS:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1425x750+0+0")
        self.root.title("Inventory Management System")
        
        # استلام الصلاحيات
        self.user_role = sys.argv[1] if len(sys.argv) > 1 else "Admin"

        self.is_dark_mode = False
        self.themes = {
            "light": {
                "bg": "#F4F7F6",
                "header": "#2C3E50",
                "menu_bg": "#FFFFFF",
                "menu_text": "#2F3640",
                "card_bg": "#3498DB",
                "text": "black",
                "clock_bg": "#34495E"
            },
            "dark": {
                "bg": "#1E1E1E",
                "header": "#000000",
                "menu_bg": "#2D2D2D",
                "menu_text": "#ECF0F1",
                "card_bg": "#34495E",
                "text": "white",
                "clock_bg": "#121212"
            }
        }

        self.primary_color = self.themes["light"]["header"]
        self.secondary_color = "#1ABC9C" 
        self.logout_color = "#E74C3C"

        self.root.config(bg=self.themes["light"]["bg"])

        # Window tracking to prevent multiple windows
        self.employee_win = None
        self.supplier_win = None
        self.category_win = None
        self.product_win = None
        self.sales_win = None

        # == Header ==
        self.header = Frame(self.root, bg=self.primary_color, bd=0)
        self.header.place(x=0, y=0, relwidth=1, height=70)

        try:
            img = Image.open("images/logo1.png")
            img = img.resize((45, 45), Image.LANCZOS)
            self.icon_title = ImageTk.PhotoImage(img)
        except:
            self.icon_title = None

        self.title = Label(
            self.header,
            text="Inventory Management System",
            image=self.icon_title,
            compound="left",
            font=("Segoe UI", 30, "bold"),
            bg=self.primary_color,
            fg="white",
            anchor="w",
            padx=20
        )
        self.title.pack(side=LEFT, fill=Y)

        # == Header Buttons ==
        btn_logout = Button(self.header, text="Logout", font=("Segoe UI", 12, "bold"), bg=self.logout_color, fg="white", cursor="hand2", bd=0, padx=15, pady=5, command=self.logout)
        btn_logout.pack(side=RIGHT, padx=20, pady=15)

        self.btn_theme = Button(self.header, text="🌙 Dark Mode", font=("Segoe UI", 10, "bold"), bg="#F1C40F", fg="black", cursor="hand2", bd=0, padx=10, command=self.toggle_theme)
        self.btn_theme.pack(side=RIGHT, padx=5, pady=15)

        # == Clock ==
        self.lbl_clock = Label(self.root, text="Welcome to IMS\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS", font=("Segoe UI", 11), bg=self.themes["light"]["clock_bg"], fg="white")
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)

        # == Left Menu ==
        self.LeftMenu = Frame(self.root, bd=0, bg=self.themes["light"]["menu_bg"], highlightthickness=1, highlightbackground="#DCDDE1")
        self.LeftMenu.place(x=0, y=100, width=220, relheight=1)

        try:
            self.MenuLogo = Image.open("images/menu_im.png")
            self.MenuLogo = self.MenuLogo.resize((180, 180), Image.LANCZOS)
            self.MenuLogo = ImageTk.PhotoImage(self.MenuLogo)
            self.lbl_menuLogo = Label(self.LeftMenu, image=self.MenuLogo, bg=self.themes["light"]["menu_bg"])
            self.lbl_menuLogo.pack(side=TOP, pady=10)
        except:
            self.lbl_menuLogo = Label(self.LeftMenu, bg=self.themes["light"]["menu_bg"])
            self.lbl_menuLogo.pack(side=TOP, pady=10)

        self.lbl_menu_title = Label(self.LeftMenu, text="MAIN MENU", font=("Segoe UI", 15, "bold"), bg=self.secondary_color, fg="white")
        self.lbl_menu_title.pack(side=TOP, fill=X, pady=(0, 10))

        # == Menu Buttons ==
        self.menu_btns = []
        self.btn_employee = Button(self.LeftMenu, text="  Employee", anchor="w", font=("Segoe UI", 14), bg=self.themes["light"]["menu_bg"], fg=self.themes["light"]["menu_text"], bd=0, cursor="hand2", pady=10, command=self.employee)
        self.btn_employee.pack(side=TOP, fill=X); self.menu_btns.append(self.btn_employee)

        self.btn_supplier = Button(self.LeftMenu, text="  Supplier", anchor="w", font=("Segoe UI", 14), bg=self.themes["light"]["menu_bg"], fg=self.themes["light"]["menu_text"], bd=0, cursor="hand2", pady=10, command=self.supplier)
        self.btn_supplier.pack(side=TOP, fill=X); self.menu_btns.append(self.btn_supplier)

        self.btn_category = Button(self.LeftMenu, text="  Category", anchor="w", font=("Segoe UI", 14), bg=self.themes["light"]["menu_bg"], fg=self.themes["light"]["menu_text"], bd=0, cursor="hand2", pady=10, command=self.category)
        self.btn_category.pack(side=TOP, fill=X); self.menu_btns.append(self.btn_category)

        self.btn_product = Button(self.LeftMenu, text="  Products", anchor="w", font=("Segoe UI", 14), bg=self.themes["light"]["menu_bg"], fg=self.themes["light"]["menu_text"], bd=0, cursor="hand2", pady=10, command=self.product)
        self.btn_product.pack(side=TOP, fill=X); self.menu_btns.append(self.btn_product)

        self.btn_sales = Button(self.LeftMenu, text="  Sales", anchor="w", font=("Segoe UI", 14), bg=self.themes["light"]["menu_bg"], fg=self.themes["light"]["menu_text"], bd=0, cursor="hand2", pady=10, command=self.sales)
        self.btn_sales.pack(side=TOP, fill=X); self.menu_btns.append(self.btn_sales)

        self.btn_exit = Button(self.LeftMenu, text="  Exit", anchor="w", font=("Segoe UI", 14), bg=self.themes["light"]["menu_bg"], fg=self.themes["light"]["menu_text"], bd=0, cursor="hand2", pady=10, command=self.root.quit)
        self.btn_exit.pack(side=TOP, fill=X); self.menu_btns.append(self.btn_exit)

        if self.user_role == "Employee":
            self.btn_employee.config(state="disabled")
            self.btn_supplier.config(state="disabled")

        # == Main Content ==
        self.Main_Frame = Frame(self.root, bg=self.themes["light"]["bg"])
        self.Main_Frame.place(x=230, y=120, relwidth=0.8, relheight=0.7)

        card_font = ("Segoe UI", 18, "bold")
        self.lbl_employee = Label(self.Main_Frame, text="Total Employee\n[ 0 ]", bd=0, bg="#3498DB", fg="white", font=card_font, cursor="hand2")
        self.lbl_employee.grid(row=0, column=0, padx=15, pady=15, sticky="nsew")
        self.lbl_employee.bind("<Button-1>", lambda e: self.employee() if self.user_role == "Admin" else None)

        self.lbl_supplier = Label(self.Main_Frame, text="Total Supplier\n[ 0 ]", bd=0, bg="#9B59B6", fg="white", font=card_font, cursor="hand2")
        self.lbl_supplier.grid(row=0, column=1, padx=15, pady=15, sticky="nsew")
        self.lbl_supplier.bind("<Button-1>", lambda e: self.supplier() if self.user_role == "Admin" else None)

        self.lbl_category = Label(self.Main_Frame, text="Total Category\n[ 0 ]", bd=0, bg="#E67E22", fg="white", font=card_font, cursor="hand2")
        self.lbl_category.grid(row=0, column=2, padx=15, pady=15, sticky="nsew")
        self.lbl_category.bind("<Button-1>", lambda e: self.category())

        self.lbl_product = Label(self.Main_Frame, text="Total Product\n[ 0 ]", bd=0, bg="#2ECC71", fg="white", font=card_font, cursor="hand2")
        self.lbl_product.grid(row=1, column=0, padx=15, pady=15, sticky="nsew")
        self.lbl_product.bind("<Button-1>", lambda e: self.product())

        self.lbl_sales = Label(self.Main_Frame, text="Total Sales\n[ 0 ]", bd=0, bg="#F1C40F", fg="white", font=card_font, cursor="hand2")
        self.lbl_sales.grid(row=1, column=1, padx=15, pady=15, sticky="nsew")
        self.lbl_sales.bind("<Button-1>", lambda e: self.sales())

        self.Main_Frame.columnconfigure((0, 1, 2), weight=1)
        self.Main_Frame.rowconfigure((0, 1), weight=1)

        # == Footer ==
        self.lbl_footer = Label(
            self.root,
            text="IMS-Inventory Management System | Developed By\nAhmed Elsayed & Gamal Esam & Shanouda Romany & Youssef Songor",
            font=("Segoe UI", 10), bg=self.primary_color, fg="white", height=2, pady=5
        )
        self.lbl_footer.pack(side=BOTTOM, fill=X)

        self.lbl_user_display = Label(
            self.lbl_footer, text="User: " + self.user_role,
            font=("Segoe UI", 10, "bold"), bg=self.primary_color, fg="#1ABC9C"
        )
        self.lbl_user_display.place(relx=0.98, rely=0.5, anchor="e")

        self.update_content()
        self.update_date_time()

    # ================== Functions ==================
    def get_connection(self):
        return pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=AMD\\SQLEXPRESS;DATABASE=ims;Trusted_Connection=yes;')

    def update_date_time(self):
        time_ = time.strftime("%I:%M:%S")
        date_ = time.strftime("%d-%m-%Y")
        self.lbl_clock.config(text=f"Welcome {self.user_role} to IMS\t\t Date: {date_}\t\t Time: {time_}")
        self.lbl_clock.after(200, self.update_date_time)

    def update_content(self):
        con = self.get_connection(); cur = con.cursor()
        try:
            cur.execute("select * from product"); self.lbl_product.config(text=f"Total Product\n[ {str(len(cur.fetchall()))} ]")
            cur.execute("select * from supplier"); self.lbl_supplier.config(text=f"Total Supplier\n[ {str(len(cur.fetchall()))} ]")
            cur.execute("select * from category"); self.lbl_category.config(text=f"Total Category\n[ {str(len(cur.fetchall()))} ]")
            cur.execute("select * from employee"); self.lbl_employee.config(text=f"Total Employee\n[ {str(len(cur.fetchall()))} ]")
            bill_count = len(os.listdir('bill')) if os.path.exists('bill') else 0
            self.lbl_sales.config(text=f"Total Sales\n[ {str(bill_count)} ]")
        except Exception as ex: messagebox.showerror("Error", str(ex))
        finally: con.close()

    def logout(self):
        if messagebox.askyesno("Confirm", "Do you really want to logout?"):
            self.root.destroy()
            # Reopen login window
            import login as login_module
            from tkinter import Tk
            login_root = Tk()
            login_module.Login_System(login_root)
            login_root.mainloop()

    def toggle_theme(self):
        self.is_dark_mode = not self.is_dark_mode
        theme = self.themes["dark"] if self.is_dark_mode else self.themes["light"]
        self.root.config(bg=theme["bg"])
        self.header.config(bg=theme["header"])
        self.title.config(bg=theme["header"])
        self.lbl_clock.config(bg=theme["clock_bg"])
        self.lbl_footer.config(bg=theme["header"])
        self.Main_Frame.config(bg=theme["bg"])
        self.LeftMenu.config(bg=theme["menu_bg"])
        self.lbl_menuLogo.config(bg=theme["menu_bg"])
        
        # أهم جزء: تحديث خلفية الـ User Admin عشان متختفيش
        self.lbl_user_display.config(bg=theme["header"])
        
        for btn in self.menu_btns:
            btn.config(bg=theme["menu_bg"], fg=theme["menu_text"])
        
        if self.is_dark_mode: self.btn_theme.config(text="☀️ Light Mode", bg="#ECF0F1", fg="black")
        else: self.btn_theme.config(text="🌙 Dark Mode", bg="#F1C40F", fg="black")

    def employee(self):
        if self.employee_win is None or not self.employee_win.winfo_exists():
            self.employee_win = Toplevel(self.root)
            self.new_obj = employeeClass(self.employee_win)
        else:
            self.employee_win.focus()

    def supplier(self):
        if self.supplier_win is None or not self.supplier_win.winfo_exists():
            self.supplier_win = Toplevel(self.root)
            self.new_obj = supplierClass(self.supplier_win)
        else:
            self.supplier_win.focus()

    def category(self):
        if self.category_win is None or not self.category_win.winfo_exists():
            self.category_win = Toplevel(self.root)
            self.new_obj = categoryClass(self.category_win)
        else:
            self.category_win.focus()

    def product(self):
        if self.product_win is None or not self.product_win.winfo_exists():
            self.product_win = Toplevel(self.root)
            self.new_obj = productClass(self.product_win)
        else:
            self.product_win.focus()

    def sales(self):
        if self.sales_win is None or not self.sales_win.winfo_exists():
            self.sales_win = Toplevel(self.root)
            self.new_obj = salesClass(self.sales_win)
        else:
            self.sales_win.focus()

if __name__ == "__main__":
    from tkinter import messagebox
    root = Tk()
    obj = IMS(root)
    root.mainloop()
