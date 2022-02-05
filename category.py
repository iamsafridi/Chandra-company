import sqlite3
from tkinter import *
from tkinter import messagebox, ttk


class categoryClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1200x600+220+150")
        self.root.title("NS Traders | Developed By Shahid Afridi")
        self.root.config(bg='white')
        self.root.focus_force()

        # variables
        self.var_cat_id=StringVar()
        self.var_name=StringVar()

        # ===title===
        lbl_title=Label(self.root,text='Manage Product Category',font=('goudy old style',30),bg='#184a45',fg='white',bd=2,relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=20)

        lbl_name=Label(self.root,text='Enter Category Name',font=('goudy old style',30),bg='white').place(x=50,y=100)

        txt_name=Entry(self.root,textvariable=self.var_name,font=('goudy old style',18),bg='lightyellow').place(x=50,y=170,width=300)

        # ===Button===

        btn_add=Button(self.root,text='ADD',command=self.add,font=('goudy old style',15,"bold"),bg='#4caf50',fg='white',cursor='hand2').place(x=360,y=170,width=150,height=30)
        btn_delete=Button(self.root,text='Delete',command=self.delete,font=('goudy old style',15,"bold"),bg='red',fg='white',cursor='hand2').place(x=520,y=170,width=150,height=30)


        # ===category Details===
        cat_frame=Frame(self.root,bd=3,relief=RIDGE)
        cat_frame.place(x=700,y=120,width=400,height=350)

        scrolly=Scrollbar(cat_frame,orient=VERTICAL) 
        scrollx=Scrollbar(cat_frame,orient=HORIZONTAL) 

        self.categoryTable=ttk.Treeview(cat_frame,columns=('cid','name'),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.categoryTable.xview)
        scrolly.config(command=self.categoryTable.yview)

        self.categoryTable.heading('cid',text='C ID')
        self.categoryTable.heading('name',text='Name')

        self.categoryTable['show']='headings'

        self.categoryTable.column('cid',width=100)
        self.categoryTable.column('name',width=100)

        self.categoryTable.pack(fill=BOTH,expand=1)
        self.categoryTable.bind("<ButtonRelease-1>",self.get_data)

        self.show()



    def add(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            if self.var_name.get()=="":
                messagebox.showerror("Error","Category Name should be required",parent=self.root)
            else:
                cur.execute("Select * from category where name=?",(self.var_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Category already assigned, try different",parent=self.root)
                else:
                    cur.execute("Insert into category (name) values(?)",(
                        self.var_name.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Category Added successfully",parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def show(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            cur.execute("Select * from category")
            rows=cur.fetchall()
            self.categoryTable.delete(*self.categoryTable.get_children())
            for row in rows:
                self.categoryTable.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


    def get_data(self,ev):
        f=self.categoryTable.focus()
        content=(self.categoryTable.item(f))
        row=content['values']
        self.var_cat_id.set(row[0])
        self.var_name.set(row[1])

    def delete(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            if self.var_cat_id.get()=="":
                messagebox.showerror("Error","Please select category from the lsit",parent=self.root)
            else:
                cur.execute("Select * from category where cid=?",(self.var_cat_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Try again",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from category where cid=?",(self.var_cat_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","category Deleted successfully",parent=self.root)
                        self.show()
                        self.var_cat_id.set("")
                        self.var_name.set("")

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


if __name__ == '__main__':
    root=Tk()
    obj=categoryClass(root)
    root.mainloop()
