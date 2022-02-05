from tkinter import*
from tkinter import ttk,messagebox
import sqlite3

class productClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1200x600+220+150")
        self.root.title("Chandra Company | Developed By Shahid Afridi")
        self.root.config(bg='white')
        self.root.focus_force()

        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()

        self.var_pid=StringVar()
        self.var_cat=StringVar()
        self.var_sup=StringVar()
        self.cat_list=[]
        self.sup_list=[]
        self.fetch_cat_sup()
        self.var_name=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_status=StringVar()

        product_Frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        product_Frame.place(x=10,y=10,width=450,height=500)

        title=Label(product_Frame,text='Manage Products Details',font=('goudy old style',18),bg='#0f4d7d',fg='white').pack(side=TOP,fill=X)

        lbl_category=Label(product_Frame,text='Category',font=('goudy old style',18),bg='white').place(x=30,y=60)
        lbl_supplier=Label(product_Frame,text='Spplier',font=('goudy old style',18),bg='white').place(x=30,y=110)
        lbl_product_name=Label(product_Frame,text='Name',font=('goudy old style',18),bg='white').place(x=30,y=160)
        lbl_price=Label(product_Frame,text='Price',font=('goudy old style',18),bg='white').place(x=30,y=210)
        lbl_quantity=Label(product_Frame,text='Quantity',font=('goudy old style',18),bg='white').place(x=30,y=260)
        lbl_status=Label(product_Frame,text='Status',font=('goudy old style',18),bg='white').place(x=30,y=310)

        # col 2
        cmb_cat=ttk.Combobox(product_Frame,textvariable=self.var_cat,values=self.cat_list,state='readonly',justify=CENTER,font=('goudy old style',15))
        cmb_cat.place(x=150,y=60,width=200)
        cmb_cat.current(0)

        cmb_sup=ttk.Combobox(product_Frame,textvariable=self.var_sup,values=self.sup_list,state='readonly',justify=CENTER,font=('goudy old style',15))
        cmb_sup.place(x=150,y=110,width=200)
        cmb_sup.current(0)

        txt_name=Entry(product_Frame,textvariable=self.var_name,font=('goudy old style',15),bg='lightyellow').place(x=150,y=160,width=200)

        txt_price=Entry(product_Frame,textvariable=self.var_price,font=('goudy old style',15),bg='lightyellow').place(x=150,y=210,width=200)

        txt_qty=Entry(product_Frame,textvariable=self.var_qty,font=('goudy old style',15),bg='lightyellow').place(x=150,y=260,width=200)

        cmb_status=ttk.Combobox(product_Frame,textvariable=self.var_status,values=('Active','Inactive'),state='readonly',justify=CENTER,font=('goudy old style',15))
        cmb_status.place(x=150,y=310,width=200)
        cmb_status.current(0)
        
        # ===button==
        btn_add=Button(product_Frame,text='Save',command=self.add,font=('goudy old style',15),bg='#2196f3',fg='white',cursor='hand2').place(x=10,y=400,width=100,height=40)
        btn_update=Button(product_Frame,text='Update',command=self.update,font=('goudy old style',15),bg='#4caf50',fg='white',cursor='hand2').place(x=120,y=400,width=100,height=40)
        btn_delete=Button(product_Frame,text='Delete',command=self.delete,font=('goudy old style',15),bg='#f44336',fg='white',cursor='hand2').place(x=230,y=400,width=100,height=40)
        btn_clear=Button(product_Frame,text='Clear',command=self.clear,font=('goudy old style',15),bg='#607d8b',fg='white',cursor='hand2').place(x=340,y=400,width=100,height=40)

        # ===searchFrame===
        searchFrame=LabelFrame(self.root,text='Search product',font=('goudy old style',12,'bold'),bd=2,relief=RIDGE,bg='white')
        searchFrame.place(x=480,y=10,width=600,height=80)

        # ===option====
        cmd_search=ttk.Combobox(searchFrame,textvariable=self.var_searchby,values=('Select','Category','Name','Supplier'),state='readonly',justify=CENTER,font=('goudy old style',15))
        cmd_search.place(x=10,y=10,width=180)
        cmd_search.current(0)

        txt_serach=Entry(searchFrame,textvariable=self.var_searchtxt,font=('goudy old style',15),bg='lightyellow').place(x=200,y=10)

        btn_serach=Button(searchFrame,text='Search',font=('goudy old style',15),bg='#4caf50',fg='white',cursor='hand2').place(x=420,y=9,width=150,height=28)

        # ===Product Details===
        p_frame=Frame(self.root,bd=3,relief=RIDGE)
        p_frame.place(x=480,y=100,width=600,height=390)

        scrolly=Scrollbar(p_frame,orient=VERTICAL) 
        scrollx=Scrollbar(p_frame,orient=HORIZONTAL) 

        self.productTable=ttk.Treeview(p_frame,columns=('pid','Category','Supplier','name','price','qty','status'),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.productTable.xview)
        scrolly.config(command=self.productTable.yview)
        self.productTable.heading('pid',text='PID')
        self.productTable.heading('Category',text='Category')
        self.productTable.heading('Supplier',text='Supplier')
        self.productTable.heading('name',text='Name')
        self.productTable.heading('price',text='Price')
        self.productTable.heading('qty',text='Qty')
        self.productTable.heading('status',text='Status')

        self.productTable['show']='headings'

        self.productTable.column('pid',width=100)
        self.productTable.column('Category',width=100)
        self.productTable.column('Supplier',width=100)
        self.productTable.column('name',width=100)
        self.productTable.column('price',width=100)
        self.productTable.column('qty',width=100)
        self.productTable.column('status',width=100)

        self.productTable.pack(fill=BOTH,expand=1)
        self.productTable.bind("<ButtonRelease-1>",self.get_data)

        self.show()
        

        # ============================
    def fetch_cat_sup(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("Select name from category")
            cat=cur.fetchall()
            self.cat_list.append('Empty')
            self.sup_list.append('Empty')
            if len(cat)>0:
                del self.cat_list[:]
                self.cat_list.append('Select')
                for i in cat:
                    self.cat_list.append(i[0])

            cur.execute("Select name from supplier")
            sup=cur.fetchall()
            if len(sup)>0:
                del self.sup_list[:]
                self.cat_list.append('Select')
                for i in sup:
                    self.sup_list.append(i[0])


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


    def add(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:    
            if self.var_cat.get()=="Select" or self.var_cat.get()=="Empty" or self.var_sup.get()=="Select" or self.var_name.get()=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)
            else:
                cur.execute("Select * from product where name=? ",(self.var_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This product already added, try different",parent=self.root)
                else:
                    cur.execute("Insert into product (Category,Supplier,name,price,qty,status) values(?,?,?,?,?,?)",(
                        self.var_cat.get(),
                        self.var_sup.get(),
                        self.var_name.get(),
                        self.var_price.get(),
                        self.var_qty.get(),
                        self.var_status.get(),

                    ))
                    con.commit()
                    messagebox.showinfo("Success","product Added successfully",parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


    def show(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            cur.execute("Select * from product")
            rows=cur.fetchall()
            self.productTable.delete(*self.productTable.get_children())
            for row in rows:
                self.productTable.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


    def get_data(self,ev):
        f=self.productTable.focus()
        content=(self.productTable.item(f))
        row=content['values']
        self.var_pid.set(row[0])
        self.var_cat.set(row[1])
        self.var_sup.set(row[2])
        self.var_name.set(row[3])
        self.var_price.set(row[4])
        self.var_qty.set(row[5])
        self.var_status.set(row[6])


    def update(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            if self.var_pid.get()=="":
                messagebox.showerror("Error","Please select product",parent=self.root)
            else:
                cur.execute("Select * from product where pid=?",(self.var_pid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid product ID",parent=self.root)
                else:
                    cur.execute("Update product set Category=?,Supplier=?,name=?,price=?,qty=?,status=? where pid=?",(
                        self.var_cat.get(),
                        self.var_sup.get(),
                        self.var_name.get(),
                        self.var_price.get(),
                        self.var_qty.get(),
                        self.var_status.get(),
                        self.var_pid.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","product Updated successfully",parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


    def delete(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            if self.var_pid.get()=="":
                messagebox.showerror("Error","Select product",parent=self.root)
            else:
                cur.execute("Select * from product where pid=?",(self.var_pid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid product",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from product where pid=?",(self.var_pid.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","product Deleted successfully",parent=self.root)
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def clear(self):
        self.var_cat.set("Select")
        self.var_sup.set("Select")
        self.var_name.set("")
        self.var_price.set("")
        self.var_qty.set("")
        self.var_status.set("Active")
        self.var_pid.set("")
        self.var_searchby.set("")
        self.var_searchtxt.set("")
        self.show()
    

    def search(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            if self.var_searchby.get()=='Select':
                messagebox.showerror('Error',"Select Search by Option",parent=self.root)
            elif self.var_searchtxt.get()=='':
                messagebox.showerror('Error',"Search Input should be required",parent=self.root)
            else:
                cur.execute("Select * from product where "+self.var_searchby.get()+" Like '%"+self.var_searchtxt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.productTable.delete(*self.productTable.get_children())
                    for row in rows:
                        self.productTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No Record found",parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


if __name__ == '__main__':
    root=Tk()
    obj=productClass(root)
    root.mainloop()