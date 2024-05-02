from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox

class Student:
    def __init__(self,root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")

        title = Label(self.root,text="Student Management System",bd=6,relief=GROOVE,font=("Algerian",30,'bold'),bg='dark blue',fg='white' )
        title.pack(side=TOP,fill=X)


        self.sl_var = StringVar()
        self.name_var = StringVar()
        self.class_var = StringVar()
        self.batch_var = StringVar()
        self.adate_var = StringVar()
        self.mob_var = StringVar()
        self.pmob_var = StringVar()

        self.jan_var = ""
        self.feb_var = ""
        self.mar_var = ""
        self.apr_var = ""
        self.may_var = ""
        self.jun_var = ""
        self.jul_var = ""
        self.aug_var = ""
        self.sep_var = ""
        self.oct_var = ""
        self.nov_var = ""
        self.dec_var = ""


        self.pay_month_var = StringVar()
        self.pay_amount_var = StringVar()


        self.search_by = StringVar()
        self.search_txt = StringVar()


        title = Label(self.root,text="Visit: CodeWithCurious.com/projects for more projects",bd=3,relief=GROOVE,font=("Brush Script MT",18),bg='blue',fg='white' )
        title.pack(side=BOTTOM,fill=X)

        manage_frame = Label(self.root,bd=4,relief=RIDGE,bg='light blue')
        manage_frame.place(x=15,y=80,width=460,height=580)

        m_title=Label(manage_frame,text="Manage Students",bg="light blue",fg="black",font=("times new roman",18,"bold"))
        m_title.grid(row=0,columnspan=2,pady=10)


        lbl_sl=Label(manage_frame,text="Serial No",bg="light blue",fg="black",font=("times new roman",14,'bold'))
        lbl_sl.grid(row=1,column=0,pady=10,padx=20,sticky='w')

        txt_sl = Entry(manage_frame,textvariable= self.sl_var, font=('times new roman',14),bd=2,relief=GROOVE)
        txt_sl.grid(row=1,column=1,pady=10,padx=20,sticky='w')


        lbl_name=Label(manage_frame,text="Name",bg="light blue",fg="black",font=("times new roman",14,'bold'))
        lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky='w')

        txt_name = Entry(manage_frame,textvariable=self.name_var,font=('times new roman',14),bd=2,relief=GROOVE)
        txt_name.grid(row=2,column=1,pady=10,padx=20,sticky='w')

        lbl_class=Label(manage_frame,text="Class",bg="light blue",fg="black",font=("times new roman",14,'bold'))
        lbl_class.grid(row=3,column=0,pady=10,padx=20,sticky='w')

        combo_class = ttk.Combobox(manage_frame,textvariable=self.class_var,font=("times new roman",12,'bold'),state='readonly')
        combo_class['values']=("Class 1","Class 2","Class 3","Class 4","Class 5","Class 6","Class 7","Class 8","Class 9","Class 10")
        combo_class.grid(row=3,column=1,pady=10,padx=20)

        lbl_batch=Label(manage_frame,text="Batch Name",bg="light blue",fg="black",font=("times new roman",14,'bold'))
        lbl_batch.grid(row=4,column=0,pady=10,padx=20,sticky='w')


        txt_batch = Entry(manage_frame,textvariable=self.batch_var,font=('times new roman',14),bd=2,relief=GROOVE)
        txt_batch.grid(row=4,column=1,pady=10,padx=20,sticky='w')

        lbl_adate=Label(manage_frame,text="Payment Date",bg="light blue",fg="black",font=("times new roman",14,'bold'))
        lbl_adate.grid(row=5,column=0,pady=10,padx=20,sticky='w')

        txt_adate = Entry(manage_frame,textvariable=self.adate_var,font=('times new roman',14),bd=2,relief=GROOVE)
        txt_adate.grid(row=5,column=1,pady=10,padx=20,sticky='w')


        lbl_mob=Label(manage_frame,text="Mobile",bg="light blue",fg="black",font=("times new roman",14,'bold'))
        lbl_mob.grid(row=6,column=0,pady=10,padx=20,sticky='w')

        txt_mob = Entry(manage_frame,textvariable=self.mob_var,font=('times new roman',14),bd=2,relief=GROOVE)
        txt_mob.grid(row=6,column=1,pady=10,padx=20,sticky='w')

        lbl_pmob=Label(manage_frame,text="Parents Mobile",bg="light blue",fg="black",font=("times new roman",14,'bold'))
        lbl_pmob.grid(row=7,column=0,pady=10,padx=20,sticky='w')

        txt_pmob = Entry(manage_frame,textvariable=self.pmob_var,font=('times new roman',14),bd=2,relief=GROOVE)
        txt_pmob.grid(row=7,column=1,pady=10,padx=20,sticky='w')


        lbl_pay=Label(manage_frame,text="Pay Amount",bg="light blue",fg="black",font=("times new roman",14,'bold'))
        lbl_pay.grid(row=8,column=0)

        combo_pay = ttk.Combobox(manage_frame,width=14,textvariable=self.pay_month_var,font=("times new roman",12,'bold'),state='readonly')
        combo_pay['values']=("jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec")
        combo_pay.grid(row=8,column=1)

        txt_pay = Entry(manage_frame,textvariable=self.pay_amount_var,width=5,font=('times new roman',14),bd=2,relief=GROOVE)
        txt_pay.grid(row=8,column=2)

        btn_frame = Frame(manage_frame,bd=4,relief=RIDGE,bg='white')
        btn_frame.place(x=10,y=470,width=425)

        addbtn = Button(btn_frame,text="Add",width=10,command=self.add_students).grid(row=0,column=0,padx=10,pady=10)
        updatebtn = Button(btn_frame,text="Update",width=10,command=self.update_data).grid(row=0,column=1,padx=10,pady=10)
        deletebtn = Button(btn_frame,text="Delete",width=10,command=self.delete_data).grid(row=0,column=2,padx=10,pady=10)
        clearbtn = Button(btn_frame,text="Clear",width=10,command=self.clear).grid(row=0,column=3,padx=10,pady=10)


        detail_frame = Frame(self.root,bd=4,relief=RIDGE,bg='light blue')
        detail_frame.place(x=500,y=80,width=820,height=580)

        lbl_search = Label(detail_frame,text="Search By",bg="light blue",fg="black",font=("times new roman",16,'bold'))
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky='w')


        combo_search = ttk.Combobox(detail_frame,width=10,textvariable=self.search_by,font=("times new roman",12,'bold'),state='readonly')
        combo_search['values']=("sl","name","class")
        combo_search.grid(row=0,column=1,pady=10,padx=20)

        txt_search = Entry(detail_frame,width=30,textvariable=self.search_txt,font=('times new roman',14),bd=2,relief=GROOVE)
        txt_search.grid(row=0,column=2,pady=10,padx=20,sticky='w')

        searchbtn = Button(detail_frame,text="Search",width=10,command=self.search_data).grid(row=0,column=3,padx=10,pady=10)
        showallbtn = Button(detail_frame,text="Show All",width=10,command=self.fetch_data).grid(row=0,column=4,padx=10,pady=10)


        table_frame = Frame(detail_frame,bd=2,relief=RIDGE,bg='light blue')
        table_frame.place(x=10,y=80,width=785,height=480)

        scroll_x = Scrollbar(table_frame,orient="horizontal")
        scroll_y = Scrollbar(table_frame,orient="vertical")
        self.student_table = ttk.Treeview(table_frame,columns=("sl","name","class","batch","adate","mob","pmob",
                                                               "jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"),
                                                              xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("sl",text="Sl.No")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("class",text="Class")
        self.student_table.heading("batch",text="Batch")
        self.student_table.heading("adate",text="Admit Date")
        self.student_table.heading("mob",text="Mobile")
        self.student_table.heading("pmob",text="Parents Mobile")

        self.student_table.heading("jan",text="January")
        self.student_table.heading("feb",text="February")
        self.student_table.heading("mar",text="March")
        self.student_table.heading("apr",text="April")
        self.student_table.heading("may",text="May")
        self.student_table.heading("jun",text="June")
        self.student_table.heading("jul",text="July")
        self.student_table.heading("aug",text="August")
        self.student_table.heading("sep",text="September")
        self.student_table.heading("oct",text="October")
        self.student_table.heading("nov",text="November")
        self.student_table.heading("dec",text="December")

        self.student_table['show']='headings'

        self.student_table.column("sl",width=80)
        self.student_table.column("name",width=200)
        self.student_table.column("class",width=140)
        self.student_table.column("batch",width=140)
        self.student_table.column("adate",width=140)
        self.student_table.column("mob",width=140)
        self.student_table.column("pmob",width=140)
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
    def add_students(self):

        if self.sl_var.get()=="" or self.name_var.get()=="" or self.class_var.get()=="":
            messagebox.showerror("Error","All fields are required!")
        else:
            conn=sqlite3.connect("student.db")
            cur=conn.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS students(sl integer,name TEXT,class TEXT,batch TEXT,adate TEXT,
                            mob TEXT,pmob TEXT,jan TEXT,feb TEXT,mar TEXT,apr TEXT,may TEXT, jun TEXT,
                            jul TEXT,aug TEXT, sep TEXT,oct TEXT,nov TEXT,dec TEXT)""")

            self.set_data()
            cur.execute("insert into students values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(
                                                                        int(self.sl_var.get()),
                                                                        self.name_var.get(),
                                                                        self.class_var.get(),
                                                                        self.batch_var.get(),
                                                                        self.adate_var.get(),
                                                                        self.mob_var.get(),
                                                                        self.pmob_var.get(),self.jan_var,self.feb_var,
                                                                        self.mar_var,self.apr_var,self.may_var,self.jun_var,
                                                                        self.jul_var,self.aug_var,self.sep_var,self.oct_var,
                                                                        self.nov_var,self.dec_var))

            conn.commit()
            self.fetch_data()
            self.clear()
            conn.close()
            messagebox.showinfo("Success","Record has been inserted successfully.")

    def fetch_data(self):
        conn=sqlite3.connect("student.db")
        cur=conn.cursor()
        cur.execute("select * from students")
        rows = cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert("",END,values=row)
            conn.commit()
        conn.close()

    def clear(self):
        self.sl_var.set("")
        self.name_var.set("")
        self.class_var.set("")
        self.batch_var.set("")
        self.adate_var.set("")
        self.mob_var.set("")
        self.pmob_var.set("")
        self.pay_month_var.set("")
        self.pay_amount_var.set("")

    def get_cursor(self,event):
        cursor_row =  self.student_table.focus()
        contents = self.student_table.item(cursor_row)
        row = contents['values']
        self.sl_var.set(row[0])
        self.name_var.set(row[1])
        self.class_var.set(row[2])
        self.batch_var.set(row[3])
        self.adate_var.set(row[4])
        self.mob_var.set(row[5])
        self.pmob_var.set(row[6])

    def update_data(self):
        conn=sqlite3.connect("student.db")
        cur=conn.cursor()
        self.set_data()
        cur.execute("""update students set name=?,class=?,batch=?,adate=?,mob=?,pmob=?,jan=?,
                       feb=?,mar=?,apr=?,may=?,jun=?,jul=?,aug=?,sep=?,oct=?,nov=?,dec=? where sl=?""",(
                                                                        self.name_var.get(),
                                                                        self.class_var.get(),
                                                                        self.batch_var.get(),
                                                                        self.adate_var.get(),
                                                                        self.mob_var.get(),
                                                                        self.pmob_var.get(),self.jan_var,self.feb_var,
                                                                        self.mar_var,self.apr_var,self.may_var,self.jun_var,
                                                                        self.jul_var,self.aug_var,self.sep_var,self.oct_var,
                                                                        self.nov_var,self.dec_var,
                                                                        int(self.sl_var.get())))

        conn.commit()
        self.fetch_data()
        self.clear()
        conn.close()
        messagebox.showinfo("Success","Record has been updated successfully.")
    def delete_data(self):
        conn=sqlite3.connect("student.db")
        cur=conn.cursor()
        cur.execute("delete from students where sl=?",(int(self.sl_var.get()),))
        conn.commit()
        self.fetch_data()
        self.clear()
        conn.close()
        messagebox.showinfo("Success","Record has been deleted successfully.")

    def search_data(self):
        #==================================for sqlite3==================
        conn=sqlite3.connect("student.db")
        cur=conn.cursor()
        cur.execute("select * from students where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows = cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert("",END,values=row)
            conn.commit()
        else:
            messagebox.showerror("Error","Record doesn't find")
        conn.close()

    def set_data(self):
        if self.pay_month_var.get()=="jan":
            self.jan_var = self.pay_amount_var.get()
        elif self.pay_month_var.get()=="feb":
            self.feb_var = self.pay_amount_var.get()
        elif self.pay_month_var.get()=="mar":
            self.mar_var = self.pay_amount_var.get()
        elif self.pay_month_var.get()=="apr":
            self.apr_var = self.pay_amount_var.get()
        elif self.pay_month_var.get()=="may":
            self.may_var = self.pay_amount_var.get()
        elif self.pay_month_var.get()=="jun":
            self.jun_var = self.pay_amount_var.get()
        elif self.pay_month_var.get()=="jul":
            self.jul_var = self.pay_amount_var.get()
        elif self.pay_month_var.get()=="aug":
            self.aug_var = self.pay_amount_var.get()
        elif self.pay_month_var.get()=="sep":
            self.sep_var = self.pay_amount_var.get()
        elif self.pay_month_var.get()=="oct":
            self.oct_var = self.pay_amount_var.get()
        elif self.pay_month_var.get()=="nov":
            self.nov_var = self.pay_amount_var.get()
        elif self.pay_month_var.get()=="dec":
            self.dec_var = self.pay_amount_var.get()

root = Tk()
ob = Student(root)
root.mainloop()