from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk 
import time
import os
import sys

# == System Modules & Database Connection ==
# Added billingClass to the imports
try:
    from employee import employeeClass
    from supplier import supplierClass
    from category import categoryClass
    from product import productClass
    from sales import salesClass
    from billing import BillClass # Import the billing module you provided
    import pyodbc
except ImportError as e:
    print(f"Error: Module missing -> {e}")

class IMS:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1425x850+0+0")
        self.root.title("Inventory Management System | Pro Dashboard")
        
        # == System State ==
        self.user_role = sys.argv[1] if len(sys.argv) > 1 else "Admin"
        self.is_dark_mode = False
        self.windows = {"emp": None, "sup": None, "cat": None, "prd": None, "sal": None, "bill": None}

        # == Professional Color Palette ==
        self.themes = {
            "light": {
                "bg": "#F8FAFC", 
                "sidebar": "#0F172A", 
                "header": "#FFFFFF", 
                "text": "#1E293B", 
                "card_bg": "#FFFFFF", 
                "sub_text": "#64748B",
                "info": "#E2E8F0"
            },
            "dark": {
                "bg": "#0B0F19",       
                "sidebar": "#161B2E",  
                "header": "#161B2E",   
                "text": "#F8FAFC",     
                "card_bg": "#1E293B",  
                "sub_text": "#94A3B8", 
                "info": "#2D3748"      
            }
        }
        
        self.active_theme = self.themes["light"]
        self.root.config(bg=self.active_theme["bg"])

        # == Sidebar Section ==
        self.sidebar = Frame(self.root, bg=self.active_theme["sidebar"], bd=0)
        self.sidebar.pack(side=LEFT, fill=Y)
        self.sidebar.config(width=260)
        self.sidebar.pack_propagate(False)

        # Brand Identity
        self.brand_frame = Frame(self.sidebar, bg=self.active_theme["sidebar"])
        self.brand_frame.pack(side=TOP, fill=X, pady=40)
        self.lbl_logo = Label(self.brand_frame, text="IMS", font=("Impact", 34), bg=self.active_theme["sidebar"], fg="#3B82F6")
        self.lbl_logo.pack()
        self.lbl_subtitle = Label(self.brand_frame, text="PRO MANAGEMENT", font=("Segoe UI", 9, "bold"), bg=self.active_theme["sidebar"], fg="#64748B")
        self.lbl_subtitle.pack()

        # == Side Navigation Menu (Dashboard removed) ==
        self.nav_btns = []
        self.btn_emp = self.create_nav_btn("Employees", "👥", self.employee)
        self.btn_sup = self.create_nav_btn("Suppliers", "🚚", self.supplier)
        self.create_nav_btn("Categories", "📂", self.category)
        self.create_nav_btn("Products", "📦", self.product)
        self.create_nav_btn("Sales Records", "📊", self.sales)
        
        # Added Billing button below Sales Records
        self.create_nav_btn("Billing System", "🧾", self.billing)
        
        self.create_nav_btn("Exit", "🚪", self.root.quit, side=BOTTOM)

        # == Top Header Bar ==
        self.header = Frame(self.root, bg=self.active_theme["header"], bd=0)
        self.header.pack(side=TOP, fill=X)
        self.lbl_panel_title = Label(self.header, text="Control Center", font=("Segoe UI", 20, "bold"), bg=self.active_theme["header"], fg=self.active_theme["text"])
        self.lbl_panel_title.pack(side=LEFT, padx=30, pady=20)
        
        # Logout & Theme Switcher
        btn_logout = Button(self.header, text="Logout", font=("Segoe UI", 10, "bold"), bg="#EF4444", fg="white", bd=0, cursor="hand2", padx=20, pady=8, command=self.logout)
        btn_logout.pack(side=RIGHT, padx=30)
        
        self.btn_theme_toggle = Button(self.header, text="🌙 Dark Mode", font=("Segoe UI", 10, "bold"), bg="#10B981", fg="white", bd=0, cursor="hand2", padx=15, command=self.toggle_ui_theme)
        self.btn_theme_toggle.pack(side=RIGHT)

        # == Status Bar (Clock & User Role) ==
        self.status_frame = Frame(self.root, bg=self.active_theme["info"])
        self.status_frame.pack(side=TOP, fill=X)
        self.lbl_clock = Label(self.status_frame, text="", font=("Segoe UI", 10), bg=self.active_theme["info"], fg="#64748B")
        self.lbl_clock.pack(side=LEFT, padx=30, pady=5)
        self.lbl_role_display = Label(self.status_frame, text=f"Role: {self.user_role}", font=("Segoe UI", 10, "bold"), bg=self.active_theme["info"], fg="#3B82F6")
        self.lbl_role_display.pack(side=RIGHT, padx=30)

        # == Main Dashboard View ==
        self.main_container = Frame(self.root, bg=self.active_theme["bg"])
        self.main_container.pack(fill=BOTH, expand=True, padx=20, pady=20)

        # == Card Data Objects ==
        self.card_elements = [] 
        self.stat_values = {}   
        
        cards_config = [
            ("Total Employees", "emp", "#3B82F6", 0, 0, self.employee),
            ("Total Suppliers", "sup", "#8B5CF6", 0, 1, self.supplier),
            ("Total Categories", "cat", "#EC4899", 0, 2, self.category),
            ("Total Products", "prd", "#10B981", 1, 0, self.product),
            ("Total Sales", "sal", "#F59E0B", 1, 1, self.sales)
        ]

        for title, key, clr, r, c, cmd in cards_config:
            labels = self.create_modern_card(self.main_container, title, clr, r, c, cmd)
            self.stat_values[key] = labels[0] 
            self.card_elements.append(labels) 

        # == Footer ==
        self.footer = Frame(self.root, bg=self.active_theme["sidebar"], height=35)
        self.footer.pack(side=BOTTOM, fill=X)
        self.lbl_footer = Label(self.footer, text="IMS-Inventory Management System | Developed By\nAhmed Elsayed & Gamal Esam & Shanouda Romany & Youssef Songor", font=("Segoe UI", 9), bg=self.active_theme["sidebar"], fg="white")
        self.lbl_footer.pack(expand=True)

        # == Security: Initial Permission Lock ==
        if self.user_role == "Employee":
            self.btn_emp.config(state="disabled")
            self.btn_sup.config(state="disabled")

        self.update_live_clock()
        self.update_content()

    # == UI Component: Modern Sidebar Button ==
    def create_nav_btn(self, text, icon, command, side=TOP):
        btn = Button(self.sidebar, text=f"  {icon}  {text}", font=("Segoe UI", 11), bg=self.active_theme["sidebar"], fg="#94A3B8", bd=0, cursor="hand2", anchor="w", padx=30, pady=15, activebackground="#1E293B", activeforeground="white", command=command)
        btn.pack(side=side, fill=X)
        btn.bind("<Enter>", lambda e: btn.config(fg="white", bg="#1E293B") if str(btn['state']) == 'normal' else None)
        btn.bind("<Leave>", lambda e: btn.config(fg="#94A3B8", bg=self.sidebar['bg']) if str(btn['state']) == 'normal' else None)
        self.nav_btns.append(btn)
        return btn

    # == UI Component: Interactive Responsive Card ==
    def create_modern_card(self, master, title, clr, r, c, cmd):
        f = Frame(master, bg=self.active_theme["card_bg"], bd=0, highlightthickness=1, highlightbackground=self.active_theme["info"], cursor="hand2")
        f.grid(row=r, column=c, padx=15, pady=15, sticky="nsew")
        
        strip = Frame(f, bg=clr, height=4)
        strip.pack(side=TOP, fill=X)
        
        cnt = Frame(f, bg=self.active_theme["card_bg"], padx=25, pady=25)
        cnt.pack(fill=BOTH, expand=True)
        
        t_lbl = Label(cnt, text=title, font=("Segoe UI", 11, "bold"), bg=self.active_theme["card_bg"], fg=self.active_theme["sub_text"])
        t_lbl.pack(anchor="w")
        v_lbl = Label(cnt, text="0", font=("Segoe UI", 32, "bold"), bg=self.active_theme["card_bg"], fg=self.active_theme["text"])
        v_lbl.pack(anchor="w", pady=10)

        def handle_click(e):
            if self.user_role == "Employee" and title in ["Total Employees", "Total Suppliers"]:
                messagebox.showwarning("Access Denied", "Your account does not have permission to view this module.")
            else: cmd()

        for widget in [f, cnt, v_lbl]:
            widget.bind("<Button-1>", handle_click)
            widget.bind("<Enter>", lambda e: f.config(highlightbackground=clr, highlightthickness=2))
            widget.bind("<Leave>", lambda e: f.config(highlightbackground=self.active_theme["info"], highlightthickness=1))

        master.columnconfigure(c, weight=1)
        master.rowconfigure(r, weight=1)
        return (v_lbl, f, t_lbl, cnt) 

    # == Theme Engine: Dark/Light Mode Switching ==
    def toggle_ui_theme(self):
        self.is_dark_mode = not self.is_dark_mode
        self.active_theme = self.themes["dark"] if self.is_dark_mode else self.themes["light"]
        
        self.root.config(bg=self.active_theme["bg"])
        self.sidebar.config(bg=self.active_theme["sidebar"])
        self.brand_frame.config(bg=self.active_theme["sidebar"])
        self.lbl_logo.config(bg=self.active_theme["sidebar"])
        self.lbl_subtitle.config(bg=self.active_theme["sidebar"])
        self.header.config(bg=self.active_theme["header"])
        self.lbl_panel_title.config(bg=self.active_theme["header"], fg=self.active_theme["text"])
        self.status_frame.config(bg=self.active_theme["info"])
        self.lbl_clock.config(bg=self.active_theme["info"])
        self.lbl_role_display.config(bg=self.active_theme["info"])
        self.main_container.config(bg=self.active_theme["bg"])
        self.footer.config(bg=self.active_theme["sidebar"])
        self.lbl_footer.config(bg=self.active_theme["sidebar"])

        for btn in self.nav_btns:
            btn.config(bg=self.active_theme["sidebar"])
        
        for v_lbl, f, t_lbl, cnt in self.card_elements:
            f.config(bg=self.active_theme["card_bg"], highlightbackground=self.active_theme["info"])
            cnt.config(bg=self.active_theme["card_bg"])
            t_lbl.config(bg=self.active_theme["card_bg"], fg=self.active_theme["sub_text"])
            v_lbl.config(bg=self.active_theme["card_bg"], fg=self.active_theme["text"])
        
        self.btn_theme_toggle.config(
            text="☀️ Light Mode" if self.is_dark_mode else "🌙 Dark Mode",
            bg="#3B82F6" if self.is_dark_mode else "#10B981"
        )

    # == Backend Logic ==
    def get_db_con(self):
        return pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=AMD\\SQLEXPRESS;DATABASE=ims;Trusted_Connection=yes;')

    def update_content(self):
        try:
            con = self.get_db_con(); cur = con.cursor()
            cur.execute("select * from product"); self.stat_values["prd"].config(text=str(len(cur.fetchall())))
            cur.execute("select * from supplier"); self.stat_values["sup"].config(text=str(len(cur.fetchall())))
            cur.execute("select * from category"); self.stat_values["cat"].config(text=str(len(cur.fetchall())))
            cur.execute("select * from employee"); self.stat_values["emp"].config(text=str(len(cur.fetchall())))
            sales = len(os.listdir('bill')) if os.path.exists('bill') else 0
            self.stat_values["sal"].config(text=str(sales))
            con.close()
        except: pass

    def update_live_clock(self):
        self.lbl_clock.config(text=time.strftime("📅 %d-%m-%Y  |  ⏰ %I:%M:%S %p"))
        self.lbl_clock.after(1000, self.update_live_clock)

    def logout(self):
        if messagebox.askyesno("Exit", "Are you sure you want to logout?"):
            self.root.destroy()
            os.system("python login.py")

    # == Window Navigation Functions ==
    def employee(self): self.open_sub_window("emp", employeeClass)
    def supplier(self): self.open_sub_window("sup", supplierClass)
    def category(self): self.open_sub_window("cat", categoryClass)
    def product(self): self.open_sub_window("prd", productClass)
    def sales(self): self.open_sub_window("sal", salesClass)
    def billing(self): self.open_sub_window("bill", BillClass) # Function to open the Billing window

    # == Helper: Sub-window Controller ==
    def open_sub_window(self, key, cls):
        if self.windows[key] is None or not self.windows[key].winfo_exists():
            self.windows[key] = Toplevel(self.root)
            cls(self.windows[key])
        else: self.windows[key].focus()

if __name__ == "__main__":
    root = Tk()
    IMS(root)
    root.mainloop()