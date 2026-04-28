from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import pyodbc
import os
import time

class Login_System:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System | Inventory Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#fafafa")
        self.root.state('zoomed')

        # === المتغيرات ===
        self.employee_id = StringVar()
        self.password = StringVar()

        # === إطار الصور (مع معالجة خطأ عدم وجود الصور) ===
        try:
            # تحميل صورة الموبايل الأساسية
            self.phone_image = ImageTk.PhotoImage(file="images/phone.png")
            self.lbl_phone_image = Label(self.root, image=self.phone_image, bd=0, bg="#fafafa")
            self.lbl_phone_image.place(x=200, y=50)
            
            # تحميل الصور المتحركة داخل الموبايل
            self.im1 = ImageTk.PhotoImage(file="images/im1.png")
            self.im2 = ImageTk.PhotoImage(file="images/im2.png")
            self.im3 = ImageTk.PhotoImage(file="images/im3.png")

            self.lbl_change_image = Label(self.root, bg="white")
            self.lbl_change_image.place(x=367, y=153, width=240, height=428)
            self.animate()
        except Exception as e:
            print(f"Warning: Images folder or files missing. Error: {e}")
            # في حالة عدم وجود صور، يتم وضع إطار رمادي بدلاً من الـ Crash
            Label(self.root, text="[ Image Placeholder ]", font=("Segoe UI", 20), bg="lightgray", fg="gray").place(x=200, y=50, width=410, height=550)

        # === إطار تسجيل الدخول (Login Frame) ===
        login_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        login_frame.place(x=650, y=90, width=350, height=460)

        title = Label(login_frame, text="Login System", font=("Segoe UI", 30, "bold"), bg="white", fg="#010c48")
        title.pack(side=TOP, fill=X, pady=30)

        lbl_user = Label(login_frame, text="Employee ID", font=("Segoe UI", 13), bg="white", fg="#767676")
        lbl_user.place(x=50, y=100)
        txt_employee_id = Entry(login_frame, textvariable=self.employee_id, font=("Segoe UI", 13), bg="#ECECEC", bd=1)
        txt_employee_id.place(x=50, y=130, width=250, height=35)

        lbl_pass = Label(login_frame, text="Password", font=("Segoe UI", 13), bg="white", fg="#767676")
        lbl_pass.place(x=50, y=190)
        txt_pass = Entry(login_frame, textvariable=self.password, show="*", font=("Segoe UI", 13), bg="#ECECEC", bd=1)
        txt_pass.place(x=50, y=220, width=250, height=35)

        btn_login = Button(login_frame, text="Log In", command=self.login, font=("Segoe UI", 15, "bold"), bg="#007bff", activebackground="#0056b3", fg="white", activeforeground="white", cursor="hand2", bd=0)
        btn_login.place(x=50, y=290, width=250, height=40)

        hr = Label(login_frame, bg="lightgray").place(x=50, y=370, width=250, height=2)
        or_ = Label(login_frame, text="OR", bg="white", fg="lightgray", font=("Segoe UI", 12, "bold")).place(x=158, y=358)

        btn_forget = Button(login_frame, text="Forget Password?", command=self.forget_window, font=("Segoe UI", 11), bg="white", fg="#007bff", bd=0, activebackground="white", activeforeground="#0056b3", cursor="hand2")
        btn_forget.place(x=105, y=390)

        # === إطار سفلي إضافي ===
        footer_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        footer_frame.place(x=650, y=570, width=350, height=60)
        Label(footer_frame, text="Inventory Management System", font=("Segoe UI", 12), bg="white").place(x=0, y=15, relwidth=1)

    # === دوال الأنيميشن ===
    def animate(self):
        self.img = self.im1
        self.im1, self.im2, self.im3 = self.im2, self.im3, self.im1
        self.lbl_change_image.config(image=self.img)
        self.lbl_change_image.after(2000, self.animate)

    # === وظيفة تسجيل الدخول والاتصال بالداتا بيز ===
    def get_connection(self):
        return pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=AMD\\SQLEXPRESS;DATABASE=ims;Trusted_Connection=yes;')

    def login(self):
        con = self.get_connection()
        cur = con.cursor()
        try:
            if self.employee_id.get() == "" or self.password.get() == "":
                messagebox.showerror("Error", "All fields are required", parent=self.root)
            else:
                cur.execute("select utype from employee where eid=? and pass=?", (self.employee_id.get(), self.password.get()))
                user = cur.fetchone()
                if user is None:
                    messagebox.showerror("Error", "Invalid Employee ID or Password", parent=self.root)
                else:
                    self.root.destroy()
                    # استدعاء ملف الداشبورد
                    os.system("python dashboard.py")
        except Exception as ex:
            messagebox.showerror("Error", f"Database Connection Error: {str(ex)}", parent=self.root)
        finally:
            con.close()

    # === شاشة نسيان كلمة المرور ===
    def forget_window(self):
        if self.employee_id.get() == "":
            messagebox.showerror("Error", "Please enter Employee ID to reset password", parent=self.root)
            return

        con = self.get_connection()
        cur = con.cursor()
        try:
            cur.execute("select email from employee where eid=?", (self.employee_id.get(),))
            email = cur.fetchone()
            if email is None:
                messagebox.showerror("Error", "Invalid Employee ID", parent=self.root)
            else:
                self.var_new_pass = StringVar()
                self.var_conf_pass = StringVar()
                
                self.forget_win = Toplevel(self.root)
                self.forget_win.title("RESET PASSWORD")
                self.forget_win.geometry("400x350+500+150")
                self.forget_win.focus_force()

                title = Label(self.forget_win, text="Reset Password", font=("Segoe UI", 20, "bold"), bg="#010c48", fg="white").pack(side=TOP, fill=X)
                
                Label(self.forget_win, text="New Password", font=("Segoe UI", 12)).place(x=20, y=70)
                Entry(self.forget_win, textvariable=self.var_new_pass, show="*", font=("Segoe UI", 12), bg="lightyellow").place(x=20, y=105, width=300, height=30)

                Label(self.forget_win, text="Confirm Password", font=("Segoe UI", 12)).place(x=20, y=160)
                Entry(self.forget_win, textvariable=self.var_conf_pass, show="*", font=("Segoe UI", 12), bg="lightyellow").place(x=20, y=195, width=300, height=30)

                Button(self.forget_win, text="Update Password", command=self.update_password, font=("Segoe UI", 13, "bold"), bg="#28a745", fg="white", cursor="hand2", bd=0).place(x=100, y=260, width=200, height=40)
        except Exception as ex:
            messagebox.showerror("Error", str(ex), parent=self.root)
        finally:
            con.close()

    def update_password(self):
        if self.var_new_pass.get() == "" or self.var_conf_pass.get() == "":
            messagebox.showerror("Error", "Password fields cannot be empty", parent=self.forget_win)
        elif self.var_new_pass.get() != self.var_conf_pass.get():
            messagebox.showerror("Error", "Passwords do not match", parent=self.forget_win)
        else:
            con = self.get_connection()
            cur = con.cursor()
            try:
                cur.execute("update employee set pass=? where eid=?", (self.var_new_pass.get(), self.employee_id.get()))
                con.commit()
                messagebox.showinfo("Success", "Password updated successfully", parent=self.forget_win)
                self.forget_win.destroy()
            except Exception as ex:
                messagebox.showerror("Error", str(ex), parent=self.forget_win)
            finally:
                con.close()

if __name__ == "__main__":
    root = Tk()
    obj = Login_System(root)
    root.mainloop()