from tkinter import *
from PIL import Image, ImageTk 
from tkinter import messagebox
import pyodbc
import os
import time

class Login_System:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System | Inventory Management")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#0b1220") 
        self.root.state('zoomed')

        # المتغيرات
        self.employee_id = StringVar()
        self.password = StringVar()
        self.otp = StringVar() 
        self.new_pass = StringVar()
        self.conf_pass = StringVar()
        self.actual_eid = "" # متغير لحفظ الـ ID الحقيقي بعد العثور عليه بالإيميل

        # === Glass Card (إطار تسجيل الدخول) ===
        login_frame = Frame(self.root, bg="#111827", highlightbackground="#1f2937", highlightthickness=1)
        login_frame.place(relx=0.5, rely=0.45, anchor=CENTER, width=420, height=520)

        # === Title ===
        Label(login_frame, text="Login System", font=("Segoe UI", 28, "bold"), bg="#111827", fg="#e5e7eb").pack(pady=(30, 20))

        # === Username Input ===
        Label(login_frame, text="Username / ID / Email", font=("Segoe UI", 10), bg="#111827", fg="#9ca3af").pack(anchor="w", padx=40)
        self.user_entry = Entry(login_frame, textvariable=self.employee_id, font=("Segoe UI", 12), bg="#1f2937", fg="white", insertbackground="white", bd=0)
        self.user_entry.pack(padx=40, pady=8, ipady=10, fill=X)

        # === Password Input ===
        Label(login_frame, text="Password", font=("Segoe UI", 10), bg="#111827", fg="#9ca3af").pack(anchor="w", padx=40, pady=(10, 0))
        self.pass_entry = Entry(login_frame, textvariable=self.password, show="*", font=("Segoe UI", 12), bg="#1f2937", fg="white", insertbackground="white", bd=0)
        self.pass_entry.pack(padx=40, pady=8, ipady=10, fill=X)

        # === Login Button ===
        self.login_btn = Button(login_frame, text="Log In", command=self.login, font=("Segoe UI", 13, "bold"), bg="#2563eb", fg="white", activebackground="#1d4ed8", activeforeground="white", bd=0, cursor="hand2")
        self.login_btn.pack(padx=40, pady=25, fill=X, ipady=10)

        # === Forget Password ===
        Button(login_frame, text="Forget Password?", command=self.forget_window, font=("Segoe UI", 10), bg="#111827", fg="#60a5fa", bd=0, cursor="hand2", activebackground="#111827", activeforeground="#2563eb").pack()

    def get_connection(self):
        return pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=AMD\\SQLEXPRESS;DATABASE=ims;Trusted_Connection=yes;')

    def login(self):
        con = self.get_connection()
        cur = con.cursor()
        try:
            if self.employee_id.get() == "" or self.password.get() == "":
                messagebox.showerror("Error", "All fields are required", parent=self.root)
            else:
                input_val = str(self.employee_id.get())
                pas_val = str(self.password.get())
                # تسجيل الدخول يدعم (ID أو الاسم أو الإيميل)
                query = "select utype from employee where (CAST(eid AS VARCHAR) = ? OR name = ? OR email = ?) and pass = ?"
                cur.execute(query, (input_val, input_val, input_val, pas_val))
                user = cur.fetchone()
                
                if user is None:
                    messagebox.showerror("Error", "Invalid Credentials", parent=self.root)
                else:
                    user_type = user[0]
                    self.root.destroy()
                    os.system(f"python dashboard.py {user_type}")
        except Exception as ex:
            messagebox.showerror("Error", f"Database Error: {str(ex)}", parent=self.root)
        finally: con.close()

    # ================= وظيفة استعادة كلمة المرور المحدثة =================
    def forget_window(self):
        con = self.get_connection()
        cur = con.cursor()
        try:
            input_user = self.employee_id.get()
            if input_user == "":
                messagebox.showerror("Error", "Please enter User ID or Email to reset password", parent=self.root)
                return
            
            # البحث عن الموظف باستخدام (ID أو الإيميل أو الاسم)
            query = "select email, eid from employee where (CAST(eid AS VARCHAR) = ? OR email = ? OR name = ?)"
            cur.execute(query, (input_user, input_user, input_user))
            row = cur.fetchone()
            
            if row is None:
                messagebox.showerror("Error", "Invalid User ID / Email", parent=self.root)
            else:
                # حفظ الـ ID الحقيقي لاستخدامه في عملية التحديث لاحقاً
                self.actual_eid = str(row[1])
                user_email = row[0]

                # --- تصميم نافذة Reset Password ---
                self.forget_win = Toplevel(self.root)
                self.forget_win.title("RESET PASSWORD")
                self.forget_win.geometry("400x480+500+150")
                self.forget_win.config(bg="#111827")
                self.forget_win.focus_force()

                title = Label(self.forget_win, text="Reset Password", font=("Segoe UI", 20, "bold"), bg="#1f2937", fg="white").pack(side=TOP, fill=X)
                
                # جزء الـ OTP
                lbl_otp = Label(self.forget_win, text=f"OTP sent to: {user_email[:3]}***{user_email[-10:]}", font=("Segoe UI", 10), bg="#111827", fg="#9ca3af").place(x=20, y=60)
                txt_otp = Entry(self.forget_win, textvariable=self.otp, font=("Segoe UI", 12), bg="#1f2937", fg="white", bd=0).place(x=20, y=90, width=250, height=35)
                
                btn_verify = Button(self.forget_win, text="VERIFY", font=("Segoe UI", 10, "bold"), bg="#3b82f6", fg="white", bd=0, cursor="hand2").place(x=280, y=90, width=80, height=35)

                # حقول كلمة المرور الجديدة
                lbl_new_pass = Label(self.forget_win, text="New Password", font=("Segoe UI", 11), bg="#111827", fg="#9ca3af").place(x=20, y=160)
                txt_new_pass = Entry(self.forget_win, textvariable=self.new_pass, show="*", font=("Segoe UI", 12), bg="#1f2937", fg="white", bd=0).place(x=20, y=190, width=340, height=35)

                lbl_conf_pass = Label(self.forget_win, text="Confirm Password", font=("Segoe UI", 11), bg="#111827", fg="#9ca3af").place(x=20, y=260)
                txt_conf_pass = Entry(self.forget_win, textvariable=self.conf_pass, show="*", font=("Segoe UI", 12), bg="#1f2937", fg="white", bd=0).place(x=20, y=290, width=340, height=35)

                btn_update = Button(self.forget_win, text="UPDATE PASSWORD", command=self.update_password, font=("Segoe UI", 13, "bold"), bg="#10b981", fg="white", bd=0, cursor="hand2").place(x=20, y=380, width=340, height=45)

        except Exception as ex:
            messagebox.showerror("Error", str(ex), parent=self.root)
        finally: con.close()

    def update_password(self):
        if self.new_pass.get() == "" or self.conf_pass.get() == "":
            messagebox.showerror("Error", "Password is required", parent=self.forget_win)
        elif self.new_pass.get() != self.conf_pass.get():
            messagebox.showerror("Error", "New Password & Confirm Password must be same", parent=self.forget_win)
        else:
            con = self.get_connection()
            cur = con.cursor()
            try:
                # نستخدم self.actual_eid الذي جلبناه في الخطوة السابقة
                cur.execute("update employee set pass=? where eid=?", (self.new_pass.get(), self.actual_eid))
                con.commit()
                messagebox.showinfo("Success", "Password updated successfully", parent=self.forget_win)
                self.forget_win.destroy()
            except Exception as ex:
                messagebox.showerror("Error", str(ex), parent=self.forget_win)
            finally: con.close()

if __name__ == "__main__":
    root = Tk()
    obj = Login_System(root)
    root.mainloop()