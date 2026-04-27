from tkinter import * 
from PIL import Image, ImageTk 
from employee import employeeClass
import pyodbc
from supplier import supplierClass
from category import categoryClass
from product import productClass


class IMS:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1425x750+0+0")
        self.root.title("Inventory Management System")
        
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

        # == Header Buttons (Right Side) ==
        btn_logout = Button(
            self.header,
            text="Logout",
            font=("Segoe UI", 12, "bold"),
            bg=self.logout_color,
            fg="white",
            activebackground="#C0392B",
            activeforeground="white",
            cursor="hand2",
            bd=0,
            padx=15,
            pady=5
        )
        btn_logout.pack(side=RIGHT, padx=20, pady=15)

        self.btn_theme = Button(
            self.header,
            text="🌙 Dark Mode",
            font=("Segoe UI", 10, "bold"),
            bg="#F1C40F",
            fg="black",
            cursor="hand2",
            bd=0,
            padx=10,
            command=self.toggle_theme
        )
        self.btn_theme.pack(side=RIGHT, padx=5, pady=15)

        # == Clock Label ==
        self.lbl_clock = Label(
            self.root,
            text="Welcome to Inventory Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",
            font=("Segoe UI", 11),
            bg=self.themes["light"]["clock_bg"],
            fg="white",
            anchor="center"
        )
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

        self.lbl_menu_title = Label(
            self.LeftMenu,
            text="MAIN MENU",
            font=("Segoe UI", 15, "bold"),
            bg=self.secondary_color,
            fg="white"
        )
        self.lbl_menu_title.pack(side=TOP, fill=X, pady=(0, 10))

        # == Left Menu ==
        self.menu_btns = []
        menus = {
            "Employee": self.employee,
            "Supplier": self.supplier,
            "Category": self.category, 
            "Products": self.product,
            "Sales": None,
            "Exit": self.root.quit
        }

        for m_text, m_command in menus.items():
            btn = Button(
                self.LeftMenu, 
                text=f"  {m_text}", 
                anchor="w", 
                font=("Segoe UI", 14), 
                bg=self.themes["light"]["menu_bg"], 
                fg=self.themes["light"]["menu_text"],
                bd=0, 
                activebackground=self.secondary_color,
                activeforeground="white",
                cursor="hand2",
                pady=10,
                command=m_command
            )
            btn.pack(side=TOP, fill=X)
            self.menu_btns.append(btn)

        # == Main Dashboard ==
        self.Main_Frame = Frame(self.root, bg=self.themes["light"]["bg"])
        self.Main_Frame.place(x=230, y=120, relwidth=0.8, relheight=0.7)

        card_font = ("Segoe UI", 18, "bold")
        
        self.lbl_employee = Button(self.Main_Frame, text="Total Employee\n[ 0 ]", command=self.employee, bd=0, bg="#3498DB", fg="white", font=card_font, cursor="hand2")
        self.lbl_employee.grid(row=0, column=0, padx=15, pady=15, sticky="nsew")

        self.lbl_supplier = Button(self.Main_Frame, text="Total Supplier\n[ 0 ]", command=self.supplier, bd=0, bg="#9B59B6", fg="white", font=card_font, cursor="hand2")
        self.lbl_supplier.grid(row=0, column=1, padx=15, pady=15, sticky="nsew")

        self.lbl_category = Button(self.Main_Frame, text="Total Category\n[ 0 ]", command=self.category, bd=0, bg="#E67E22", fg="white", font=card_font, cursor="hand2")
        self.lbl_category.grid(row=0, column=2, padx=15, pady=15, sticky="nsew")

        self.lbl_product = Button(self.Main_Frame, text="Total Product\n[ 0 ]", command=self.product, bd=0, bg="#2ECC71", fg="white", font=card_font, cursor="hand2")
        self.lbl_product.grid(row=1, column=0, padx=15, pady=15, sticky="nsew")

        self.lbl_sales = Button(self.Main_Frame, text="Total Sales\n[ 0 ]", bd=0, bg="#F1C40F", fg="white", font=card_font, cursor="hand2")
        self.lbl_sales.grid(row=1, column=1, padx=15, pady=15, sticky="nsew")

        self.Main_Frame.columnconfigure((0, 1, 2), weight=1)
        self.Main_Frame.rowconfigure((0, 1), weight=1)

        # == Footer ==
        self.lbl_footer = Label(
            self.root,
            text="IMS-Inventory Management System | Developed By\n Ahmed Elsayed & Gamal Esam & Shanouda Romany & Youssef Songor ",
            font=("Segoe UI", 10),
            bg=self.primary_color,
            fg="white"
        )
        self.lbl_footer.pack(side=BOTTOM, fill=X)

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
        
        for btn in self.menu_btns:
            btn.config(bg=theme["menu_bg"], fg=theme["menu_text"])
        
        if self.is_dark_mode:
            self.btn_theme.config(text="☀️ Light Mode", bg="#ECF0F1", fg="black")
        else:
            self.btn_theme.config(text="🌙 Dark Mode", bg="#F1C40F", fg="black")

#=====================================================================================================================

    def employee(self):
        self.new_win = Toplevel(self.root) 
        self.new_obj = employeeClass(self.new_win) # Change this to employeeClass


    def supplier(self):
        self.new_win = Toplevel(self.root) 
        self.new_obj = supplierClass(self.new_win)  

    def category(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = categoryClass(self.new_win)    

    def product(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = productClass(self.new_win)       



if __name__ == "__main__":
    root = Tk()
    obj = IMS(root)
    root.mainloop()