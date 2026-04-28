from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import os

class salesClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x650+220+50")
        self.root.title("Inventory Management System | Sales Records")
        self.root.config(bg="#f8fafc") 
        self.root.focus_force()

        #================ Variables =================
        self.var_invoice = StringVar()
        self.bill_list = []

        #--- Header Section ---
        Header_Frame = Frame(self.root, bg="#0f172a", bd=0)
        Header_Frame.pack(side=TOP, fill=X)
        
        title = Label(Header_Frame, text="💰 SALES AND BILLING RECORDS", font=("Segoe UI", 20, "bold"), bg="#0f172a", fg="white", pady=20)
        title.pack()

        #--- Main Container ---
        Main_Frame = Frame(self.root, bg="#f8fafc")
        Main_Frame.pack(fill=BOTH, expand=1, padx=20, pady=10)

        #--- Search Bar ---
        Search_Frame = Frame(Main_Frame, bg="white", bd=1, relief=SOLID)
        Search_Frame.place(x=0, y=0, width=1060, height=70)

        lbl_invoice = Label(Search_Frame, text="Search Invoice No:", font=("Segoe UI", 12, "bold"), bg="white", fg="#475569").place(x=20, y=20)
        txt_invoice = Entry(Search_Frame, textvariable=self.var_invoice, font=("Segoe UI", 13), bg="#f1f5f9", bd=0).place(x=180, y=20, width=250, height=30)
        
        # (Flat Design)
        btn_search = Button(Search_Frame, text="Search Now", command=self.search, font=("Segoe UI", 11, "bold"), bg="#3b82f6", fg="white", cursor="hand2", bd=0).place(x=450, y=20, width=140, height=30)
        btn_clear = Button(Search_Frame, text="Refresh List", command=self.clear, font=("Segoe UI", 11, "bold"), bg="#64748b", fg="white", cursor="hand2", bd=0).place(x=600, y=20, width=140, height=30)

        #--- Content Area  ---
        
        # 1. (left)
        List_Frame = LabelFrame(Main_Frame, text=" Invoice History ", font=("Segoe UI", 12, "bold"), bd=1, bg="white", fg="#0f172a")
        List_Frame.place(x=0, y=90, width=300, height=450)

        scrolly = Scrollbar(List_Frame, orient=VERTICAL)
        self.Sales_List = Listbox(List_Frame, font=("Segoe UI", 11), bg="white", bd=0, fg="#334155", selectbackground="#3b82f6", yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT, fill=Y)
        scrolly.config(command=self.Sales_List.yview)
        self.Sales_List.pack(fill=BOTH, expand=1, padx=5, pady=5)
        self.Sales_List.bind("<ButtonRelease-1>", self.get_data)

        
        Preview_Frame = LabelFrame(Main_Frame, text=" Bill Preview Content ", font=("Segoe UI", 12, "bold"), bd=1, bg="white", fg="#0f172a")
        Preview_Frame.place(x=320, y=90, width=740, height=450)

        bill_title = Label(Preview_Frame, text="--- Customer Invoice Details ---", font=("Segoe UI", 11, "bold"), bg="#f1f5f9", fg="#64748b").pack(side=TOP, fill=X)

        scrolly2 = Scrollbar(Preview_Frame, orient=VERTICAL)
        self.bill_area = Text(Preview_Frame, font=("Consolas", 12), bg="#fffbeb", fg="#1e293b", bd=0, yscrollcommand=scrolly2.set) # استخدام خط Consolas للفواتير
        scrolly2.pack(side=RIGHT, fill=Y)
        scrolly2.config(command=self.bill_area.yview)
        self.bill_area.pack(fill=BOTH, expand=1, padx=10, pady=10)

        # Footer 
        lbl_footer = Label(self.root, text="Click on any invoice to preview its content | All files are stored in 'bill' folder", font=("Segoe UI", 9), bg="#f8fafc", fg="#94a3b8").pack(side=BOTTOM, pady=5)

        self.show()


    def show(self):
        del self.bill_list[:]
        self.Sales_List.delete(0, END)
        if not os.path.exists('bill'):
            os.mkdir('bill')
            
        for i in os.listdir('bill'):
            if i.split('.')[-1] == 'txt':
                self.Sales_List.insert(END, i)
                self.bill_list.append(i.split('.')[0])

    def get_data(self, ev):
        try:
            index_ = self.Sales_List.curselection()
            file_name = self.Sales_List.get(index_)
            self.bill_area.delete('1.0', END)
            self.bill_area.insert(END, f" FILE: {file_name}\n" + "="*50 + "\n")
            fp = open(f'bill/{file_name}', 'r')
            for i in fp:
                self.bill_area.insert(END, i)
            fp.close()
        except Exception:
            pass

    def search(self):
        if self.var_invoice.get() == "":
            messagebox.showerror("Error", "Please enter an Invoice No.", parent=self.root)
        else:
            if self.var_invoice.get() in self.bill_list:
                fp = open(f'bill/{self.var_invoice.get()}.txt', 'r')
                self.bill_area.delete('1.0', END)
                self.bill_area.insert(END, f" SEARCH RESULT: {self.var_invoice.get()}\n" + "="*50 + "\n")
                for i in fp:
                    self.bill_area.insert(END, i)
                fp.close()
            else:
                messagebox.showerror("Error", "This Invoice No. does not exist!", parent=self.root)

    def clear(self):
        self.show()
        self.bill_area.delete('1.0', END)
        self.var_invoice.set("")

if __name__=="__main__":
    root = Tk()
    obj = salesClass(root)
    root.mainloop()