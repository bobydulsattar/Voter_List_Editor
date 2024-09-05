from tkinter import *
import sqlite3
from tkinter import ttk,messagebox
from PIL import Image, ImageTk
from io import BytesIO

class Voter:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1540x790+0+0")
        self.root.title("Voter List")

        # Color palette
        self.Titlebg_color="#987899" #
        self.bg_color = "#ecd6ed"  #background
        self.Titlefg_color = 'white' #  Title text color
        self.fg_color ="#FF4500" #headings text color 
        self.button_bg = "#1E2167" # button color
        self.button_fg = "white"  # buttons text color
        self.notefg_color ="black" # note heading text color
        self.entryfg_color ="black"

        # Retrieve image from database with ID 1
        img = self.get_image_from_db(image_id=1)
        if img:
            img = ImageTk.PhotoImage(img)  # Convert PIL.Image to PhotoImage
            self.root.iconphoto(False, img)
            self.photo_icon = img  # Keep a reference to avoid garbage collection
        else:
            print("Image with ID 1 could not be loaded from the database.")
        
        self.root.title("Voter List")

        self.fName=StringVar()#dataBase variables
        self.lName=StringVar()
        self.id=StringVar()
        self.fatherN=StringVar()
        self.gender=StringVar()
        self.DOB=StringVar()
        self.add=StringVar()

        self.searchBy=StringVar()#search variables
        self.searchText=StringVar()
        
        self.table=""
        self.table_name=StringVar()
        self.table_name2=StringVar()

        self.adminId=""
        self.id_name=StringVar()
        self.adminPass=""
        self.pass_name=StringVar()

        self.home_page()

        #home page
    def home_page(self):
        self.home_frame = Frame(self.root, bg=self.bg_color)
        self.home_frame.place(x=0, y=0, width=1550, height=790)

        # Container frame to hold the logos and title
        Top_frame = Frame(self.home_frame, bg=self.Titlebg_color)
        Top_frame.place(x=0,y=0,height=60,width=1550 ) 

        #reset fields
        self.table_name.set("")
        self.id_name.set("")
        self.pass_name.set("")
        
        # To load image frome db
        img_logo1 = self.get_image_from_db(image_id=2)
        if img_logo1:
            img_logo1 = img_logo1.resize((40, 50))
            self.photo_logo1 = ImageTk.PhotoImage(img_logo1)
            self.logo = Label(self.home_frame, image=self.photo_logo1, bg=self.Titlebg_color)
            self.logo.place(x=500, y=3, width=50, height=50)
        else:
            print("Image with ID 2 could not be loaded from the database.")

        title = Label(Top_frame, text="VOTER LIST",
                      font=('times new roman', 37, 'bold'), fg=self.Titlefg_color, bg=self.Titlebg_color)
        title.place(x=0, y=0, width=1550, height=60)

        img_logo2 = self.get_image_from_db(image_id=2)
        if img_logo2:
            img_logo2 = img_logo2.resize((40, 50))
            self.photo_logo2 = ImageTk.PhotoImage(img_logo2)
            self.logo = Label(Top_frame, image=self.photo_logo2, bg=self.Titlebg_color)
            self.logo.place(x=1000, y=3, width=50, height=50)
        else:
            print("Image with ID 2 could not be loaded from the database.")

        #Main frame
        Main_frame = Frame(self.home_frame, bd=2, relief='flat', bg=self.bg_color)
        Main_frame.place(x=0, y=230, width=1540, height=560)

        #Login Section
        upper_frame = LabelFrame(Main_frame, bd=5, relief="solid", bg=self.bg_color,
                                 text='Login Section',
                                 font=('arial', 20, 'bold'), fg=self.fg_color)
        upper_frame.place(x=10, y=10, width=1510, height=360)

        #User Login 
        user_frame = LabelFrame(Main_frame, bd=5, relief='solid',bg=self.bg_color,
                                text='User Login',
                                font=('arial', 13, 'underline bold'), fg=self.fg_color)
        user_frame.place(x=110, y=60, width=400, height=250)

        lb_code = Label(user_frame, text="VILLAGE CODE:", font=('arial', 11, 'bold'), bg=self.bg_color, fg=self.fg_color)
        lb_code.place(x=30, y=60)

        entry_code = Entry(user_frame, font=('arial', 11, 'bold'),textvariable=self.table_name, width=20, bg=self.button_fg, fg=self.entryfg_color)
        entry_code.place(x=150, y=60)

        btn_code = Button(user_frame, text="Show List",command=self.check1,
                          font=('arial', 12, 'bold'), fg=self.button_fg, bg=self.button_bg, width=12)
        btn_code.place(x=100, y=90, height=25)
        
        #Admin Login
        admin_frame = LabelFrame(Main_frame, bd=5, relief="solid",bg=self.bg_color,
                                 text='Admin Login',
                                 font=('arial', 13, 'underline bold'), fg=self.fg_color)
        admin_frame.place(x=580, y=60, width=400, height=250)

        lb_Id = Label(admin_frame, text="ID:", font=('arial', 11, 'bold'), bg=self.bg_color, fg=self.fg_color)
        lb_Id.place(x=70, y=40)

        entry_Id = Entry(admin_frame, font=('arial', 11, 'bold'), width=20,textvariable=self.id_name, bg=self.button_fg, fg=self.entryfg_color)
        entry_Id.place(x=100, y=40)

        lb_Pass = Label(admin_frame, text="Password:", font=('arial', 11, 'bold'), bg=self.bg_color, fg=self.fg_color)
        lb_Pass.place(x=20, y=80)

        entry_Pass = Entry(admin_frame, font=('arial', 11, 'bold'), width=20,textvariable=self.pass_name, bg=self.button_fg, fg=self.entryfg_color, show='*')
        entry_Pass.place(x=100, y=80)

        btn_login = Button(admin_frame, text="Login",command=self.Pass_check, font=('arial', 12, 'bold'), fg=self.button_fg, bg=self.button_bg, width=12)
        btn_login.place(x=110, y=115, height=25)

        #Note frame
        note_frame = LabelFrame(Main_frame, bd=2, relief="solid", bg=self.bg_color,text='Notes',
                                font=('arial', 11, 'underline bold'), fg=self.notefg_color)
        note_frame.place(x=1010, y=45, width=490, height=300)

        note_txt1=Label(note_frame,text=""" I) In User Login Enter Your Village Code to see your Village list of Voters.""",bg=self.bg_color,font=('verdana', 9),justify='left')
        note_txt1.place(x=10,y=10)

        note_txt2=Label(note_frame,text="""II) In Admin Login Enter Your ID and Password to edit Village list of Voters.""",bg=self.bg_color,font=('verdana', 9),justify='left')
        note_txt2.place(x=10,y=40)

        note_txt3=Label(note_frame,text="""    Here is List of Admins.
        Name                  ID
    1. Akshat               36621        
    2. Chandrabhan    39625   
    3. Bobydul             12345""",bg=self.bg_color,font=('Verdana', 9 ,'bold'),justify="left")
        note_txt3.place(x=0,y=65)

    #image retrieval from database

    #List page
    def list_page(self):
        
        self.home_frame.destroy()
        self.list_frame = Frame(self.root, bg=self.bg_color)
        self.list_frame.place(x=0, y=0, width=1550, height=790)

        title = Label(self.list_frame, text=f"LIST PAGE- `{self.table}`",
                      font=('times new roman', 37, 'bold'), fg=self.Titlefg_color, bg=self.Titlebg_color)
        title.place(x=0, y=0, width=1550, height=60)

        back_button = Button(self.list_frame, text="<", command=self.back_list,
                             font=('arial', 12, 'bold'), fg=self.button_fg, bg=self.button_bg, width=5)
        back_button.place(x=25, y=65, height=25)

        #Main frame
        A_frame = Frame(self.list_frame, bd=2, relief='solid', bg=self.bg_color)
        A_frame.place(x=10, y=100, width=1500, height=560)

        #List Management
        upper_frame = LabelFrame(A_frame, bd=3, relief="solid", bg=self.bg_color,
                                 text='Search Section',
                                 font=('arial', 15, 'bold'), fg=self.fg_color)
        upper_frame.place(x=50, y=20, width=620, height=500)

        search_lbl = Label(upper_frame,text="Search By:",font=('arial',11,'bold'),bg=self.bg_color)
        search_lbl.grid(row=0,column=1,padx=4,pady=2,sticky=W)

        lbl_combo2 = ttk.Combobox(upper_frame,textvariable=self.searchBy,
                                  font=('arial',11,'bold'),width=20,state='readonly')
        lbl_combo2['value'] =("ID","FirstName")
        lbl_combo2.current(0)
        lbl_combo2.grid(row=0,column=2,padx=4,pady=2,sticky=W)

        search_entry = Entry(upper_frame,textvariable=self.searchText,bg='white',font=('arial',12,'bold'),bd=2,width=30)
        search_entry.grid(row=0,column=3,padx=4,pady=2,sticky=W)

        btn_search = Button(upper_frame,command=self.searchInfo,text="Search",font=('arial',12,'bold'),fg='white',bg=self.button_bg,width=12)
        btn_search.grid(row=1,column=2,padx=4,pady=4,sticky=W)
        
        btn_search = Button(upper_frame,command=self.ShowAll,text="Show All",font=('arial',12,'bold'),fg='white',bg=self.button_bg,width=12)
        btn_search.grid(row=1,column=3,padx=4,pady=4,sticky=W)

        #List View
        table_frame=LabelFrame(A_frame,bd=3,relief='solid',bg=self.bg_color,
                               text='Voter List',
                               font=('arial',15,'bold'),fg=self.fg_color)
        table_frame.place(x=700, y=20, width=750, height=500)

        scroll_x= ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y= ttk.Scrollbar(table_frame,orient=VERTICAL)
    
        self.List_table = ttk.Treeview(table_frame,column=("fname","lname","id","fatherN","gender","dob","address",),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.List_table.xview)
        scroll_y.config(command=self.List_table.yview)

        self.List_table.heading('fname',text='First Name')
        self.List_table.heading('lname',text='Last Name')
        self.List_table.heading('id',text='ID')
        self.List_table.heading('fatherN',text='Father\'s Name')
        self.List_table.heading('gender',text='Gender')
        self.List_table.heading('dob',text='DOB')
        self.List_table.heading('address',text='Address')
        
        self.List_table['show'] ='headings'
        self.List_table.pack(fill=BOTH,expand=1)

        self.List_table.column('fname',width=85)
        self.List_table.column('lname',width=85)
        self.List_table.column('id',width=85)
        self.List_table.column('fatherN',width=85)
        self.List_table.column('gender',width=85)
        self.List_table.column('dob',width=85)
        self.List_table.column('address',width=85)

        self.List_table.bind("<ButtonRelease>",self.setDataIntoUpperFrame)
    
        self.ShowAll()

        #admin page
    def admin_page(self):
        self.home_frame.destroy()
        self.admin_frame = Frame(self.root, bg=self.bg_color)
        self.admin_frame.place(x=0, y=0, width=1550, height=790)

        self.table_name.set("")

        title = Label(self.admin_frame, text="ADMIN PAGE",
                      font=('times new roman', 37, 'bold'), fg=self.Titlefg_color, bg=self.Titlebg_color)
        title.place(x=0, y=0, width=1550, height=60)

        back_button = Button(self.admin_frame, text="<", command=self.back_admin,
                             font=('arial', 12, 'bold'), fg=self.button_fg, bg=self.button_bg, width=5)
        back_button.place(x=25, y=65, height=25)

        #Main frame
        A_frame = Frame(self.admin_frame, bd=2, relief='solid', bg=self.bg_color)
        A_frame.place(x=10, y=100, width=1500, height=560)

        #List Management
        upper_frame = LabelFrame(A_frame, bd=3, relief="solid", bg=self.bg_color,
                                 text='List Management',
                                 font=('arial', 15, 'bold'), fg=self.fg_color)
        upper_frame.place(x=50, y=20, width=620, height=500)

        upper_frame.grid_rowconfigure(0, weight=0)
        upper_frame.grid_rowconfigure(1, weight=0)
        upper_frame.grid_rowconfigure(2, weight=0)
        upper_frame.grid_rowconfigure(3, weight=0)
        upper_frame.grid_rowconfigure(4, weight=0)
        upper_frame.grid_rowconfigure(5, weight=0)
        upper_frame.grid_rowconfigure(6, weight=0)
        upper_frame.grid_columnconfigure(0, weight=0)
        upper_frame.grid_columnconfigure(1, weight=0)
        upper_frame.grid_columnconfigure(2, weight=0)
        upper_frame.grid_columnconfigure(3, weight=0)

        lb_code = Label(upper_frame, text="Village Code:", font=('arial', 11, 'bold'), bg=self.bg_color, fg=self.fg_color)
        lb_code.grid(row=0,column=0,padx=3,pady=10,sticky=W)

        entry_code = Entry(upper_frame, font=('arial', 11, 'bold'),textvariable=self.table_name2,
                            width=20,bd=1,relief='solid')
        entry_code.grid(row=0,column=1,padx=3,pady=10,sticky=W)

        btn_code = Button(upper_frame, text="Show List",command=self.check2,
                          font=('arial', 12, 'bold'), fg=self.button_fg, bg=self.button_bg, width=13)
        btn_code.grid(row=0,column=2,padx=3,pady=10,sticky=W)
        
        lbl_fname = Label(upper_frame,text="First Name:",font=('arial',11,'bold'),bg=self.bg_color)
        lbl_fname.grid(row=1,column=0,padx=3,pady=10,sticky=W)

        entry_fname = Entry(upper_frame,font=('arial',11,'bold'),textvariable=self.fName,
                            width=20,bd=1,relief='solid')
        entry_fname.grid(row=1,column=1,padx=3,pady=10,sticky=W)

        lbl_lname = Label(upper_frame,text="Last Name:",font=('arial',11,'bold'),bg=self.bg_color)
        lbl_lname.grid(row=1,column=2,padx=3,pady=10,sticky=W)

        entry_lname = Entry(upper_frame,font=('arial',11,'bold'),textvariable=self.lName,
                            width=20,bd=1,relief='solid')
        entry_lname.grid(row=1,column=3,padx=3,pady=10,sticky=W)

        lbl_id = Label(upper_frame,text="ID:",font=('arial',11,'bold'),bg=self.bg_color)
        lbl_id.grid(row=2,column=0,padx=3,pady=10,sticky=W)

        entry_id = Entry(upper_frame,font=('arial',11,'bold'),textvariable=self.id,
                         width=20,bd=1,relief='solid')
        entry_id.grid(row=2,column=1,padx=3,pady=10,sticky=W)

        lbl_father = Label(upper_frame,text="Father's name:",font=('arial',11,'bold'),bg=self.bg_color)
        lbl_father.grid(row=2,column=2,padx=3,pady=10,sticky=W)

        entry_father = Entry(upper_frame,font=('arial',11,'bold'),textvariable=self.fatherN,
                             width=20,bd=1,relief='solid')
        entry_father.grid(row=2,column=3,padx=3,pady=10,sticky=W)

        lbl_gender = Label(upper_frame,text="Gender:",font=('arial',11,'bold'),bg=self.bg_color)
        lbl_gender.grid(row=3,column=0,padx=3,pady=10,sticky=W)

        lbl_combo = ttk.Combobox(upper_frame,font=('arial',11,'bold'),textvariable=self.gender,
                                 width=18,state='readonly')
        lbl_combo['value'] =("Male","Female","Other")
        lbl_combo.current(0)
        lbl_combo.grid(row=3,column=1,padx=3,pady=10,sticky=W)

        lbl_dob = Label(upper_frame,text="DOB:",font=('arial',11,'bold'),bg=self.bg_color)
        lbl_dob.grid(row=3,column=2,padx=3,pady=10,sticky=W)

        entry_dob = Entry(upper_frame,font=('arial',11,'bold'),textvariable=self.DOB,
                          width=20,bd=1,relief='solid')
        entry_dob.grid(row=3,column=3,padx=3,pady=10,sticky=W)

        lbl_add = Label(upper_frame,text="Address:",font=('arial',11,'bold'),bg=self.bg_color)
        lbl_add.grid(row=4,column=0,padx=3,pady=10,sticky=W)

        entry_add = Entry(upper_frame,font=('arial',11,'bold'),textvariable=self.add,
                          width=20,bd=1,relief='solid')
        entry_add.grid(row=4,column=1,padx=3,pady=10,sticky=W)

        search_lbl = Label(upper_frame,text="Search By:",font=('arial',11,'bold'),bg=self.bg_color)
        search_lbl.grid(row=5,column=0,padx=3,pady=10,sticky=W)

        lbl_combo2 = ttk.Combobox(upper_frame,textvariable=self.searchBy,
                                  font=('arial',11,'bold'),width=17,state='readonly')
        lbl_combo2['value'] =("ID","FirstName")
        lbl_combo2.current(0)
        lbl_combo2.grid(row=5,column=1,padx=3,pady=10,sticky=W)

        search_entry = Entry(upper_frame,font=('arial',11,'bold'),textvariable=self.searchText,
                             width=17,bd=1,relief='solid')
        search_entry.grid(row=5,column=2,padx=3,pady=10,sticky=W)

        btn_search = Button(upper_frame,command=self.searchInfo,text="Search",font=('arial',12,'bold'),fg='white',bg=self.button_bg,width=14)
        btn_search.grid(row=5,column=3,padx=3,pady=10,sticky=W)
        
        #button Labels
        button_frame = Frame(upper_frame,bd=2,relief='ridge',bg=self.bg_color)
        button_frame.grid(row=6,column=0,columnspan=4,padx=0,pady=15,sticky=NSEW)

        button_frame.grid_rowconfigure(0, weight=0)
        button_frame.grid_rowconfigure(1, weight=0)
        button_frame.grid_rowconfigure(2, weight=0)
        button_frame.grid_rowconfigure(3, weight=0)
        button_frame.grid_columnconfigure(0, weight=0)
        button_frame.grid_columnconfigure(1, weight=0)
        button_frame.grid_columnconfigure(2, weight=0)
        button_frame.grid_columnconfigure(3, weight=0)

        btn_save = Button(button_frame,text="Save",font=('arial',12,'bold'),fg=self.button_fg,
                          command=self.AddData,bg=self.button_bg,width=12)
        btn_save.grid(row=1,column=0,pady=8,padx=8,sticky=NSEW)

        btn_update = Button(button_frame,text="Update",font=('arial',12,'bold'),fg=self.button_fg,
                            command=self.UpdateData,bg=self.button_bg,width=12)
        btn_update.grid(row=1,column=1,pady=8,padx=8,sticky=NSEW)

        btn_delete = Button(button_frame,text="Delete",font=('arial',12,'bold'),fg=self.button_fg,
                            command=self.DeleteData,bg=self.button_bg,width=12)
        btn_delete.grid(row=1,column=2,pady=8,padx=8,sticky=NSEW)

        btn_reset = Button(button_frame,text="Reset",font=('arial',12,'bold'),fg=self.button_fg,
                           command=self.resetFields,bg=self.button_bg,width=12)
        btn_reset.grid(row=1,column=3,pady=8,padx=8,sticky=NSEW)

        #List View
        table_frame=LabelFrame(A_frame,bd=3,relief='solid',bg=self.bg_color,
                               text='Voter List',
                               font=('arial',15,'bold'),fg=self.fg_color)
        table_frame.place(x=700, y=20, width=750, height=500)

        scroll_x= ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y= ttk.Scrollbar(table_frame,orient=VERTICAL)
    
        self.List_table = ttk.Treeview(table_frame,column=("fname","lname","id","fatherN","gender","dob","address",),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.List_table.xview)
        scroll_y.config(command=self.List_table.yview)

        self.List_table.heading('fname',text='First Name')
        self.List_table.heading('lname',text='Last Name')
        self.List_table.heading('id',text='ID')
        self.List_table.heading('fatherN',text='Father\'s Name')
        self.List_table.heading('gender',text='Gender')
        self.List_table.heading('dob',text='DOB')
        self.List_table.heading('address',text='Address')
        
        self.List_table['show'] ='headings'
        self.List_table.pack(fill=BOTH,expand=1)

        self.List_table.column('fname',width=85)
        self.List_table.column('lname',width=85)
        self.List_table.column('id',width=85)
        self.List_table.column('fatherN',width=85)
        self.List_table.column('gender',width=85)
        self.List_table.column('dob',width=85)
        self.List_table.column('address',width=85)

        self.List_table.bind("<ButtonRelease>",self.setDataIntoUpperFrame)

        self.ShowAll()

    def get_image_from_db(self, image_id):
        conn = None
        try:
            # Connect to the database
            conn = sqlite3.connect('voter_list.db')

            cursor = conn.cursor()

            # Retrieve the image from the database
            sql = "SELECT imagedata FROM Images WHERE id = ?"
            cursor.execute(sql, (image_id,))

            result = cursor.fetchone()

            if result:
                # Convert the binary data to an image
                image_data = BytesIO(result[0])
                pil_image = Image.open(image_data)
                return pil_image
            else:
                print(f"Image with ID {image_id} not found in the database.")
                return None
            
        except sqlite3.Error as e:
            print(f"MySQL Error: {e}")
            return None

        finally:
            if conn:
                cursor.close()
                conn.close()
                
    def check1(self):
        self.table = self.table_name.get()
        conn = None  # Initialize connection variable
        try:
            # Establish the connection to the MySQL database
            conn = sqlite3.connect('voter_list.db')

            cursor = conn.cursor()
            # Query to check if the table exists
            cursor.execute(f"""
            SELECT COUNT(*)
            FROM sqlite_master
            WHERE type='table'
            AND name='{self.table}';
            """)
            result = cursor.fetchone()

            # Check if the table exists
            if result[0] == 1:
                self.list_page()  # Table exists, proceed to list_page
            else:
                    messagebox.showerror("Error", "Table Does Not Exist", parent=self.root)  # Table doesn't exist
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error :{e}", parent=self.root)

        finally:
            if conn:
                cursor.close()
                conn.close()
        
    def check2(self):
        self.table = self.table_name2.get()
        conn = None  # Initialize connection variable
        try:
            # Establish the connection to the MySQL database
            conn = sqlite3.connect('voter_list.db')
            cursor = conn.cursor()
            # Query to check if the table exists
            cursor.execute(f"""
            SELECT COUNT(*)
            FROM sqlite_master
            WHERE type='table' AND name='{self.table}';
            """)
            result = cursor.fetchone()

            # Check if the table exists
            if result[0] == 1:
                self.admin_page()  # Table exists, proceed to admin_page
            else:
                messagebox.showerror("Error", f"'{self.table}' Table Does Not Exist.", parent=self.root)  # Table doesn't exist

        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error: {e}", parent=self.root)

        finally:
            if conn:
                cursor.close()
                conn.close()

    def Pass_check(self):
        self.adminPass=self.pass_name.get()
        self.adminId=self.id_name.get()
        conn = None
        try:
            # Connect to the database
            conn = sqlite3.connect('voter_list.db')
            cursor = conn.cursor()

            # Query to check if adminId and adminPass match a record in adminlist table
            query = "SELECT COUNT(*) FROM adminlist WHERE ID = ? AND Pass = ?"
            cursor.execute(query, (self.adminId, self.adminPass))
            result = cursor.fetchone()

            if result[0] > 0:
                # Credentials are correct, proceed to the admin page
                self.admin_page()
            else:
                # Credentials are incorrect, show error message
                messagebox.showerror("Error", "Invalid Input", parent=self.root)

        except sqlite3.Error as err:
            # Handle any database connection or query errors
            messagebox.showerror("Database Error", f"Error: {err}", parent=self.root)

        finally:
            # Close the database connection
            if conn:
                cursor.close()
                conn.close()
         
    def AddData(self):
        if self.id.get() == "":
            messagebox.showerror("Error", "ID is required", parent=self.root)
            return
        conn = None
        try:
            conn = sqlite3.connect('voter_list.db')
            cursor = conn.cursor()

            cursor.execute(
                f"INSERT INTO `{self.table}` (FirstName, LastName, ID, FatherName, Gender, DOB , Address) VALUES (?,?,?,?,?,?,?)",
                (
                    self.fName.get(),
                    self.lName.get(),
                    self.id.get(),
                    self.fatherN.get(),
                    self.gender.get(),
                    self.DOB.get(),
                    self.add.get(),
                )
            )
            conn.commit()
            messagebox.showinfo("Success", "Data Added Successfully", parent=self.root)
            self.resetFields()
            self.ShowAll()

        except sqlite3.Error as err:
            messagebox.showerror("Database Error", f"Error: {str(err)}", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error: {str(ex)}", parent=self.root)
        finally:
            if conn:
               cursor.close()
               conn.close()
    def ShowAll(self):
        if self.table=='':
            self.table_name2.set("")
        else:
            conn = None
            try:
                conn = sqlite3.connect('voter_list.db')
                cursor = conn.cursor()
                # Check if the table exists before executing the query
                cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{self.table}'")
                result = cursor.fetchone()
                if result:
                    cursor.execute(f"SELECT * FROM `{self.table}`")
                    data = cursor.fetchall()
                    if len(data) != 0:
                        self.List_table.delete(*self.List_table.get_children())
                        for i in data:
                            self.List_table.insert("", END, values=i)
                else:
                    messagebox.showerror("Error", f"Table '{self.table}' doesn't exist.", parent=self.root)

            except sqlite3.Error as ex:
                messagebox.showerror("Error", str(ex), parent=self.root)
            finally:
                if conn:
                    cursor.close()
                    conn.close() 

    def setDataIntoUpperFrame(self,event = ""):
        curr_row =self.List_table.focus()
        data = self.List_table.item(curr_row)['values']
        self.fName.set(data[0])
        self.lName.set(data[1])
        self.id.set(data[2])
        self.fatherN.set(data[3])
        self.gender.set(data[4])
        self.DOB.set(data[5])      
        self.add.set(data[6])
        
    #search Emoloyeeinfo
    def searchInfo(self):
        conn = None
        conn = sqlite3.connect('voter_list.db')
        cursor = conn.cursor()
        try:
            query=f"select * FROM `{self.table}` where {self.searchBy.get()} LIKE ?"
            cursor.execute(query,('%'+self.searchText.get()+'%',))
            data= cursor.fetchall()
            print(data,self.searchBy.get(),self.searchText.get())
            
            self.List_table.delete(*self.List_table.get_children())
            if(len(data) != 0):
                for row in data:
                    self.List_table.insert("",END,values=row)
            conn.commit()
        except sqlite3.Error as ex:
            messagebox.showerror("Error",str(ex),parent= self.root)
        finally:
            if conn:
                cursor.close()
                conn.close()

    #Update Function
    def UpdateData(self):
        if self.id.get() == "":
            messagebox.showerror("Error", "ID is required to update", parent=self.root)
            return
        conn = None
        try:
            conn = sqlite3.connect('voter_list.db')
            cursor = conn.cursor()

            query=f"""
            UPDATE `{self.table}` 
            SET FirstName=?, LastName=?, FatherName=?, Gender=?, DOB=?, Address=? 
            WHERE ID=?
            """
            cursor.execute(
                query,
            (
                self.fName.get(),
                self.lName.get(),
                self.fatherN.get(),
                self.gender.get(),
                self.DOB.get(),
                self.add.get(),
                self.id.get()
            )
            )
            conn.commit()
            messagebox.showinfo("Success", "Data Updated Successfully", parent=self.root)
            self.resetFields()
            self.ShowAll()

        except sqlite3.Error as err:
            messagebox.showerror("Database Error", f"Error: {str(err)}", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error: {str(ex)}", parent=self.root)
        finally:
            if conn:
                cursor.close()
                conn.close()

    def DeleteData(self):
        if self.id.get() == "":
            messagebox.showerror("Error", "ID is required to delete", parent=self.root)
            return
        conn = None
        try:
            conn = sqlite3.connect('voter_list.db')
            cursor = conn.cursor()

            cursor.execute(f"DELETE FROM `{self.table}` WHERE id=?", (self.id.get(),))

            conn.commit()
            messagebox.showinfo("Success", "Data Deleted Successfully", parent=self.root)
            self.resetFields()
            self.ShowAll()

        except sqlite3.Error as err:
            messagebox.showerror("Database Error", f"Error: {str(err)}", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error: {str(ex)}", parent=self.root)
        finally:
            if conn:
                cursor.close()
                conn.close()

    def resetFields(self):
        self.fName.set("")
        self.lName.set("")
        self.id.set("")
        self.fatherN.set("")
        self.DOB.set("")
        self.gender.set("Male")
        self.add.set("")
        self.table_name.set("")
        self.table_name2.set("")

        #back button def
    def back_list(self):
        self.list_frame.destroy()
        self.home_page()

    def back_admin(self):
        self.admin_frame.destroy()
        self.home_page()
        
if __name__ == "__main__":
    root = Tk()
    obj = Voter(root)
    root.mainloop()