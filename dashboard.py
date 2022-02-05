import os
import sqlite3
import time
from tkinter import *
from tkinter import messagebox

from category import categoryClass
from employee import employeeClass
from product import productClass
from sales import salesClass
from supplier import supplierClass


class IMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1650x800+0+0")
        self.root.title("চন্দ্রা কোম্পানি | Developed By Shahid Afridi")
        self.root.config(bg='white')

        #===title===
        title=Label(self.root,text='চন্দ্রা কোম্পানি',font=("times new roman",40,"bold"),bg='#010c48',fg='white').place(x=0,y=0,relwidth=1,height=70)

        # ===Button===
        btn_logout=Button(self.root,command=self.logout,text='logout',font=("times new roman",15,"bold"),bg='yellow',cursor='hand2').place(x=1300,y=10,height=50,width=150)

        # ===clock===
        self.lbl_clock=Label(self.root,text='Welcome to চন্দ্রা কোম্পানি\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS',font=("times new roman",20),bg='#4d636d',fg='white')
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)    

        # ===Left Menu===
        leftMenu=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        leftMenu.place(x=0,y=102,width=220,height=650)

        lbl_menu=Label(leftMenu,text='Menu',font=("times new roman",20),bg='#009688').pack(side=TOP,fill=X)
        
        btn_employee=Button(leftMenu,text='Employee',command=self.employee,font=("times new roman",20,'bold'),bg='white',bd=3,cursor='hand2').pack(side=TOP,fill=X)
        btn_supplier=Button(leftMenu,text='Supplier',command=self.supplier,font=("times new roman",20,'bold'),bg='white',bd=3,cursor='hand2').pack(side=TOP,fill=X)
        btn_category=Button(leftMenu,text='Category',command=self.category,font=("times new roman",20,'bold'),bg='white',bd=3,cursor='hand2').pack(side=TOP,fill=X)
        btn_product=Button(leftMenu,text='Product',command=self.product,font=("times new roman",20,'bold'),bg='white',bd=3,cursor='hand2').pack(side=TOP,fill=X)
        btn_sales=Button(leftMenu,text='Sales',command=self.sales,font=("times new roman",20,'bold'),bg='white',bd=3,cursor='hand2').pack(side=TOP,fill=X)
        btn_exit=Button(leftMenu,text='Exit',font=("times new roman",20,'bold'),bg='white',bd=3,cursor='hand2').pack(side=TOP,fill=X)

        # ===content===
        self.lbl_employee=Label(self.root,text='Total Employee\n[ 0 ]',bd=5,relief=RIDGE,bg='#33bbf9',fg='white',font=('goudy old sytyle',20,'bold'))
        self.lbl_employee.place(x=300,y=120,height=150,width=300)

        self.lbl_supplier=Label(self.root,text='Total Supplier\n[ 0 ]',bd=5,relief=RIDGE,bg='#ff5722',fg='white',font=('goudy old sytyle',20,'bold'))
        self.lbl_supplier.place(x=650,y=120,height=150,width=300)

        self.lbl_category=Label(self.root,text='Total Category\n[ 0 ]',bd=5,relief=RIDGE,bg='#009688',fg='white',font=('goudy old sytyle',20,'bold'))
        self.lbl_category.place(x=1000,y=120,height=150,width=300)

        self.lbl_product=Label(self.root,text='Total Product\n[ 0 ]',bd=5,relief=RIDGE,bg='#607d8b',fg='white',font=('goudy old sytyle',20,'bold'))
        self.lbl_product.place(x=300,y=300,height=150,width=300)
        
        self.lbl_sales=Label(self.root,text='Total Sales\n[ 0 ]',bd=5,relief=RIDGE,bg='#ffc107',fg='white',font=('goudy old sytyle',20,'bold'))
        self.lbl_sales.place(x=650,y=300,height=150,width=300)

        # ===footer===
        lbl_footer=Label(self.root,text='চন্দ্রা কোম্পানি | Developed By Shahid Afridi',font=("times new roman",30),bg='#4d636d',fg='white').pack(side=BOTTOM,fill=X)

        self.update_content()
        self.update_date_time()


    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeClass(self.new_win)

    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=supplierClass(self.new_win)

    def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=categoryClass(self.new_win)

    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=productClass(self.new_win)

    def sales(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=salesClass(self.new_win)

    def update_content(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute('select * from product')
            product=cur.fetchall()
            self.lbl_product.config(text=f'Total Product\n[ {str(len(product))} ]')

            cur.execute('select * from supplier')
            supplier=cur.fetchall()
            self.lbl_supplier.config(text=f'Total Supplier\n[ {str(len(supplier))} ]')

            cur.execute('select * from category')
            category=cur.fetchall()
            self.lbl_category.config(text=f'Total Category\n[ {str(len(category))} ]')

            cur.execute('select * from employee')
            employee=cur.fetchall()
            self.lbl_employee.config(text=f'Total Category\n[ {str(len(employee))} ]')
            bill=len(os.listdir('bill'))
            self.lbl_sales.config(text=f'Total Sales\n[{str(bill)}]')
        
        except Exception as ex:
            messagebox.showerror('Error',f'Error due to : {str(ex)}',parent=self.root)

    def update_date_time(self):
        time_=time.strftime("%I:%M:%S")
        date_=time.strftime("%d-:%m-:%Y")
        self.lbl_clock.config(text=f'Welcome to চন্দ্রা কোম্পানি\t\t Date: {str(date_)}\t\t Time: {str(time_)}')
        self.lbl_clock.after(200,self.update_date_time)

    def logout(self):
        self.root.destroy()
        os.system("python login.py")

if __name__ == '__main__':
    root=Tk()
    obj=IMS(root)
    root.mainloop()
