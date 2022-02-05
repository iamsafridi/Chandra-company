import os
import sqlite3
from tkinter import *
from tkinter import messagebox


class Login_System:
    def __init__(self,root):
        self.root=root
        self.root.title('Login System | Developed by Shahid Afridi')
        self.root.geometry('1650x800+0+0')
        # self.root.config('fafafa')clear

        # ===Login Frame===
        self.employee_id=StringVar()
        self.password=StringVar()
        login_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        login_frame.place(x=650,y=90,width=350,height=460)

        title=Label(login_frame,text='Login System',font=('Elephant',30,'bold'),bg='white').place(x=0,y=30,relwidth=1)

        lbl_user=Label(login_frame,text='Employee ID',font=('Andulas',15),bg='white',fg='#767171').place(x=50,y=100)
        txt_employee_id=Entry(login_frame,textvariable=self.employee_id,font=("times new roman",15),bg="#ECECEC").place(x=50,y=140,width=250)

        lbl_pass=Label(login_frame,text='Password',font=('Andulas',15),bg='white',fg='#767171').place(x=50,y=200)
        txt_password=Entry(login_frame,textvariable=self.password,show="*",font=("times new roman",15),bg="#ECECEC").place(x=50,y=240,width=250)

        btn_login=Button(login_frame,text="Login",command=self.login,font=("Arial Rounded MT Bold",15),bg="#00B0F0").place(x=50,y=300,height=35,width=250)

        hr=Label(login_frame,bg="lightgray").place(x=50,y=370,width=250,height=2)

        btn_forget=Button(login_frame,text='Forget Password?',font=("times new roman",13),bg='white',fg='#00759E',bd=0).place(x=100,y=390)


        # ===Frame2===
        # reg_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        # reg_frame.place(x=650,y=570,width=350,height=60)

        # lbl_reg=Label(reg_frame,text="Don't have an account ?",font=("times new roman",13),bg='white').place(x=40,y=20)

        # btn_signup=Button(reg_frame,text='Signup?',font=("times new roman",13,'bold'),bg='white',fg='#00759E',bd=0).place(x=200,y=17)



    def login(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.employee_id.get()=="" or self.password.get()=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)
            else:
                cur.execute('select utype from employee where eid=? AND pass=?',(self.employee_id.get(),self.password.get()))
                user=cur.fetchone()
                if user==None:
                    messagebox.showerror("Error","invalid",parent=self.root)
                else:
                    if user[0]=="Admin":
                        self.root.destroy()
                        os.system("python dashboard.py")
                    else:
                        self.root.destroy()
                        os.system("python billing.py")



        except Exception as ex:
            messagebox.showerror('Error',f'Error due to : {str(ex)}',parent=self.root)


root=Tk()
obj=Login_System(root)
root.mainloop()
