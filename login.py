from tkinter import *
from PIL import Image, ImageTk 
from tkinter import messagebox
import pyodbc
import os
import time
import email_pass
import smtplib


class Login_System:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System | Inventory Management")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#0b1220") 
        self.root.state('zoomed')

        self.otp=''

        self.employee_id = StringVar()
        self.password = StringVar()
        self.var_otp = StringVar() 
        self.new_pass = StringVar()
        self.conf_pass = StringVar()

        # === Login Frame ===
        login_frame = Frame(self.root, bg="#111827", highlightbackground="#1f2937", highlightthickness=1)
        login_frame.place(relx=0.5, rely=0.45, anchor=CENTER, width=420, height=520)

        Label(login_frame, text="Login System", font=("Segoe UI", 28, "bold"), bg="#111827", fg="#e5e7eb").pack(pady=(30, 20))

        Label(login_frame, text="Username / ID / Email", font=("Segoe UI", 10), bg="#111827", fg="#9ca3af").pack(anchor="w", padx=40)
        self.user_entry = Entry(login_frame, textvariable=self.employee_id, font=("Segoe UI", 12), bg="#1f2937", fg="white", insertbackground="white", bd=0)
        self.user_entry.pack(padx=40, pady=8, ipady=10, fill=X)

        Label(login_frame, text="Password", font=("Segoe UI", 10), bg="#111827", fg="#9ca3af").pack(anchor="w", padx=40, pady=(10, 0))
        self.pass_entry = Entry(login_frame, textvariable=self.password, show="*", font=("Segoe UI", 12), bg="#1f2937", fg="white", insertbackground="white", bd=0)
        self.pass_entry.pack(padx=40, pady=8, ipady=10, fill=X)

        self.login_btn = Button(login_frame, text="Log In", command=self.login, font=("Segoe UI", 13, "bold"), bg="#2563eb", fg="white", activebackground="#1d4ed8", activeforeground="white", bd=0, cursor="hand2")
        self.login_btn.pack(padx=40, pady=25, fill=X, ipady=10)

        Button(login_frame, text="Forget Password?", command=self.forget_window, font=("Segoe UI", 10), bg="#111827", fg="#60a5fa", bd=0, cursor="hand2", activebackground="#111827", activeforeground="#2563eb").pack()

    def get_connection(self):
        return pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=***\\SQLEXPRESS;DATABASE=ims;Trusted_Connection=yes;')

    def login(self):
        con = self.get_connection()
        cur = con.cursor()
        try:
            user_input = self.employee_id.get().strip()
            pass_input = self.password.get().strip()
            
            if user_input == "" or pass_input == "":
                messagebox.showerror("Error", "All fields are required", parent=self.root)
            else:
                cur.execute("select utype from employee where (CAST(eid AS VARCHAR) = ? OR name = ? OR email = ?) and pass = ?", 
                            (user_input, user_input, user_input, pass_input))
                user = cur.fetchone()
                if user is None:
                    messagebox.showerror("Error", "Invalid Credentials", parent=self.root)
                else:
                    user_type = user[0]
                    self.root.destroy()
                    os.system(f"python dashboard.py {user_type}")
        except Exception as ex:
            messagebox.showerror("Error", f"Database Error: {str(ex)}", parent=self.root)
        finally: 
            con.close()

    def send_email(self, to_):
        try:
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            email_ = email_pass.email_
            pass_ = email_pass.pass_ # App Password (16 chars)
            s.login(email_, pass_)

            # توليد OTP رقمي
            self.otp = int(time.strftime("%H%M%S")) + int(time.strftime("%S"))
            
            subj = "IMS-Reset Password OTP"
            msg = f"Subject: {subj}\n\nDear Sir/Madam,\n\nYour Reset OTP is {str(self.otp)}.\n\nWith Regards,\nIMS Team"
            
            s.sendmail(email_, to_, msg)
            s.quit()
            return 's'
        except Exception as ex:
            print(f"Mail Error: {str(ex)}") 
            return 'f'

    def forget_window(self):
        con = self.get_connection()
        cur = con.cursor()
        try:
            input_val = self.employee_id.get().strip()
            if input_val == "":
                messagebox.showerror("Error", "Employee ID or Email is required", parent=self.root)
            else:
                cur.execute("select email from employee where CAST(eid AS VARCHAR) = ? OR email = ?", (input_val, input_val))
                email = cur.fetchone()
                
                if email is None:
                    messagebox.showerror("Error", "Invalid Employee ID / Email", parent=self.root)
                else:
                    chk = self.send_email(email[0])
                    if chk == 'f':
                        messagebox.showerror("Error", "Connection Error or Google Security Issue. Use App Password.", parent=self.root)
                    else:
                        self.forget_win = Toplevel(self.root)
                        self.forget_win.title("RESET PASSWORD")
                        self.forget_win.geometry("400x440+500+150")
                        self.forget_win.config(bg="#111827")
                        self.forget_win.focus_force()

                        Label(self.forget_win, text="Reset Password", font=("Segoe UI", 20, "bold"), bg="#1f2937", fg="white").pack(side=TOP, fill=X)
                        
                        Label(self.forget_win, text="Enter OTP Sent on Email", font=("Segoe UI", 11), bg="#111827", fg="#9ca3af").place(x=20, y=60)
                        txt_otp = Entry(self.forget_win, textvariable=self.var_otp, font=("Segoe UI", 12), bg="#1f2937", fg="white", bd=0).place(x=20, y=90, width=250, height=35)
                        
                        btn_verify = Button(self.forget_win, text="VERIFY", command=self.validate_otp, font=("Segoe UI", 10, "bold"), bg="#3b82f6", fg="white", bd=0, cursor="hand2").place(x=280, y=90, width=80, height=35)

                        Label(self.forget_win, text="New Password", font=("Segoe UI", 11), bg="#111827", fg="#9ca3af").place(x=20, y=150)
                        txt_new_pass = Entry(self.forget_win, textvariable=self.new_pass, show="*", font=("Segoe UI", 12), bg="#1f2937", fg="white", bd=0).place(x=20, y=180, width=340, height=35)

                        Label(self.forget_win, text="Confirm Password", font=("Segoe UI", 11), bg="#111827", fg="#9ca3af").place(x=20, y=240)
                        txt_conf_pass = Entry(self.forget_win, textvariable=self.conf_pass, show="*", font=("Segoe UI", 12), bg="#1f2937", fg="white", bd=0).place(x=20, y=270, width=340, height=35)

                        self.btn_update = Button(self.forget_win, text="UPDATE", command=self.update_password, state=DISABLED, font=("Segoe UI", 13, "bold"), bg="#10b981", fg="white", bd=0, cursor="hand2")
                        self.btn_update.place(x=20, y=340, width=340, height=45)

        except Exception as ex:
            messagebox.showerror("Error", str(ex), parent=self.root)
        finally: 
            con.close()

    def validate_otp(self):
        if str(self.otp) == str(self.var_otp.get().strip()):
            self.btn_update.config(state=NORMAL)
            messagebox.showinfo("Success", "OTP Verified, Please enter new password", parent=self.forget_win)
        else:
            messagebox.showerror("Error", "Invalid OTP", parent=self.forget_win)

    def update_password(self):
        new_p = self.new_pass.get().strip()
        conf_p = self.conf_pass.get().strip()
        user_ref = self.employee_id.get().strip()

        if new_p == "" or conf_p == "":
            messagebox.showerror("Error", "Password is required", parent=self.forget_win)
        elif new_p != conf_p:
            messagebox.showerror("Error", "Passwords do not match", parent=self.forget_win)
        else:
            con = self.get_connection()
            cur = con.cursor()
            try:
                # التعديل الهام: التحديث بناءً على الـ ID أو الإيميل المدخل في شاشة الدخول
                cur.execute("update employee set pass=? where (CAST(eid AS VARCHAR)=? OR email=?)", 
                            (new_p, user_ref, user_ref))
                con.commit()
                
                if cur.rowcount > 0:
                    messagebox.showinfo("Success", "Password updated successfully", parent=self.forget_win)
                    self.forget_win.destroy()
                else:
                    messagebox.showerror("Error", "Update failed: User reference lost.", parent=self.forget_win)
            except Exception as ex:
                messagebox.showerror("Error", str(ex), parent=self.forget_win)
            finally: 
                con.close()

if __name__ == "__main__":
    root = Tk()
    obj = Login_System(root)
    root.mainloop()
