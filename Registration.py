from opencv_face_detection import *
from tkinter import *
import csv
from tkinter import messagebox
from tkinter import font

import MySQLdb

from face_detection import *

import datetime
from tkinter import ttk
from tkcalendar import DateEntry
import random


####################################################################################################
####################################################################################################
db = MySQLdb.connect("localhost", "root", "", "faceattendancesystem")
cursor = db.cursor()


top = Tk()
top.geometry("350x350")
top.title("LOGIN FORM")
top.minsize(860, 400)
top.maxsize(860, 400)
top.config(bg="blue")
img = PhotoImage(file="13.png")
label = Label(
    top,
    image=img
)
label.place(x=0, y=0, relwidth=1, relheight=1)

labelFont3 = font.Font(family="Helvetica", size=18, weight=font.BOLD,)


# -------------------------------------------------------------------------------
teacher_id = 0
# -------------------------------------------------------------------------------


def clea():
    txx.delete(0, END)
    tx1.delete(0, END)
    tx2.delete(0, END)
    tx3.delete(0, END)
    tx4.delete(0, END)
    tx5.delete(0, END)
    tx6.delete(0, END)
    tx8.delete(0, END)
    tx9.delete(0, END)


def ext():
    window.destroy()

# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------


def register():
    USER = tx1.get()
    register_face(USER)
    return "file created"
# -------------------------------------------------------------------------------


def train_to_xml():
    print("training")
    cascadeClassifier = cv2.CascadeClassifier(
        'haarcascade_frontalface_alt.xml')
    faceRecognizer = cv2.face.LBPHFaceRecognizer_create()
# con = sqlite3.connect('FACEATTENDANCESYSTEM.db')
# cur = con.cursor()
    cur = db.cursor()
    if faceRecognizer:
        images = []
        labels = []
        for users in os.listdir('DATABASE/'):
            name = users
            print("name :", name)
            sql = "SELECT StudentID FROM studentreg WHERE StudentName='%s'" % (
                name)
            cur.execute(sql)
            idd = cur.fetchone()
            if idd:
                print("USER ID  :", idd[0])
                lbl_id = int(idd[0])
                for filee in os.listdir('DATABASE/' + users + "/"):
                    print("File :", filee)
                   # time.sleep(2)
                    image = cv2.imread('DATABASE/' + users + "/" + filee, 0)
                    images.append(image)
                    labels.append(lbl_id)

        faceRecognizer.train(images, np.array(labels))
        faceRecognizer.write('faceRecognizer1.yml')
    print("Training Completed")

# -------------------------------------------------------------------------------


def signin():
            USER = tx1.get()
            print(USER)
# con = sqlite3.connect('FACEATTENDANCESYSTEM.db')
            cur = db.cursor()
            try:
                cur.execute(
                    "create table StudentReg(StudentID TEXT, StudentName TEXT,Department TEXT,ADDRESS TEXT,DOB TEXT,Age TEXT,DOJ TEXT, PHNO TEXT,Email TEXT)")
                print("Table Created")
            except:
                print(" table already exit ")
            finally:
               val = validation()
               print("VAL=", val)
               if val == 1:
                rtn = register()
               else:
                 messagebox.showinfo("Registration info", "Validation Faild")
               if rtn == "file created":
                 try:
                    a = txx.get(); b = tx1.get(); c = tx2.get(); d = tx3.get(); f = tx4.get(
                    ); g = tx5.get(); h = tx6.get(); k = tx8.get(); l = tx9.get()
                    sql = "INSERT INTO StudentReg values('%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
                        a, b, c, d, f, g, h, k, l)
                    print(sql)
                    cur.execute(sql)
                    db.commit()
                    # sql="INSERT INTO StudentDBid (DBid,StudentName) values('%s','%s')"%(a,b)
                    # cur.execute(sql)
                    # db.commit()
                    # print ("commit")
                    print('record inserted in DB')
                    train_to_xml()
                    messagebox.showinfo("Registration info",
                                        "successfully Registered")
                 except Exception as e:
                      print("sigin in finally", e)
                      messagebox.showinfo(
                          "Registration info", "Error occured while Registration")
# ---------------------------------------------------------------------------------------------------


def validation():
     val = 1
     print(val)
     a = txx.get(); b = tx1.get(); c = tx2.get(); d = tx3.get(); f = tx4.get(
     ); g = tx5.get(); h = tx6.get(); k = tx8.get(); l = tx9.get()
     print(a, b, c, d, f, g, h, k, l)
     if a == "":
         print("required")
         val = 0
         messagebox.showinfo("Rgistration Error", "StudentId required")
     else:
         pass
     if b == "":
         val = 0
         messagebox.showinfo("Rgistration Error", "Student Name required")
     else:
         pass
     if c == "":
         print("required")
         val = 0
         messagebox.showinfo("Registration Error", "Department required")
     else:
         pass
     # if d=="" :
         # val=0
         # messagebox.showinfo( "Rgistration Error", "DOB required" )
     # else:
         # pass
     if f == "":
         print("required")
         val = 0
         messagebox.showinfo("Rgistration Error", "DOB required")
     else:
         pass
     if g == "":
         val = 0
         messagebox.showinfo("Rgistration Error", "Age required")
     else:
         pass
     if h == "":
         val = 0
         print("required")
         messagebox.showinfo("Rgistration Error", "DOJ required")
     else:
         pass
     if k == "":
         val = 0
         messagebox.showinfo("Rgistration Error", "Ph No required")
     else:
         pass
     if l == "":
         val = 0
         messagebox.showinfo("Rgistration Error", "Email required")
     else:
         print("validation successfull")
         messagebox.showinfo("Rgistration Info", "validation successfull")
         val = 1
     return val
# ------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------
# ________________________________________________ add_student()_______________________________________________________


def add_student():
# messagebox.showinfo("ADD STUDENT","ongoing...")

    global txx, tx1, tx2, tx3, tx4, tx5, tx6, tx8, tx9, window
    window = Tk()
    window.title("REGISTRATION")
    Studentid = Label(window, text="Student ID", width=12,
                      bg='white', anchor=W, justify=LEFT)
    Studentid.grid(row=0, column=0)
    txx = Entry(window, width=30)
    txx.grid(row=0, column=4)
    Studentname = Label(window, text="Student Name",
                        bg='white', width=12, anchor=W, justify=LEFT)
    Studentname.grid(row=1, column=0)
    tx1 = Entry(window, width=30)
    tx1.grid(row=1, column=4)
    dept = Label(window, text="Department", bg='white',
                 width=12, anchor=W, justify=LEFT)
    dept.grid(row=2, column=0)
    tx2 = Entry(window, width=30)
    tx2.grid(row=2, column=4)
    add = Label(window, text="Address", width=12,
                bg='white', anchor=W, justify=LEFT)
    add.grid(row=3, column=0)
    tx3 = Entry(window, width=30)
    tx3.grid(row=3, column=4)
    dob = Label(window, text="Date Of Birth", width=12,
                bg='white', anchor=W, justify=LEFT)
    dob.grid(row=4, column=0)
    tx4 = Entry(window, width=30)
    tx4.grid(row=4, column=4)
    age = Label(window, text="Age", width=12,
                anchor=W, bg='white', justify=LEFT)
    age.grid(row=5, column=0)
    tx5 = Entry(window, width=30)
    tx5.grid(row=5, column=4)
    doj = Label(window, text="Date of Join", width=12,
                bg='white', anchor=W, justify=LEFT)
    doj.grid(row=6, column=0)
    tx6 = Entry(window, width=30)
    tx6.grid(row=6, column=4)
    phno = Label(window, text="PH:NO", width=12,
                 anchor=W, bg='white', justify=LEFT)
    phno.grid(row=7, column=0)
    tx8 = Entry(window, width=30)
    tx8.grid(row=7, column=4)
    email = Label(window, text="Email", width=12,
                  bg='white', anchor=W, justify=LEFT)
    email.grid(row=9, column=0)
    tx9 = Entry(window, width=30)
    tx9.grid(row=9, column=4)
    reg = Button(window, text="REGISTER", command=signin)
    reg.grid(row=11, column=0)
    clear = Button(window, text="CLEAR", command=clea)
    clear.grid(row=11, column=3)
    exi = Button(window, text="EXIT", command=ext)
    exi.grid(row=11, column=4)
    window.mainloop()

# ________________________________________________ add_teacher()_______________________________________________________


def add_teacher():
    add_tech = Toplevel()
    add_tech.config(bg="powderblue")
    add_tech.minsize(350, 400)
    log_name = StringVar()
    log_pass = StringVar()
    un = log_name.get()
    ps = log_pass.get()
    print("un", un, "ps", ps)
    print("..*..")

    l1 = Label(add_tech, text="Register Teacher", font="Verdana 12 bold")
    l1.place(x=150, y=50)

    usr_nm = Label(add_tech, text="USER NAME", font="Verdana 12 bold")
    usr_nm.place(x=15, y=100)
    usr_nm_ent = Entry(add_tech, textvariable=log_name,
                       bg="powderblue", width=15, font="Verdana 12 bold")
    usr_nm_ent.place(x=150, y=100)

    usr_pass = Label(add_tech, text="PASSWORD", font="Verdana 12 bold")
    usr_pass.place(x=15, y=140)
    usr_pass_ent = Entry(add_tech, textvariable=log_pass,
                         bg="powderblue", width=15, font="Verdana 12 bold")
    usr_pass_ent.place(x=150, y=140)

    btn_login = Button(add_tech, text="Register", font="Verdana 14 bold",
                       relief=RIDGE, command=lambda: reg_tech(log_name.get(), log_pass.get()))
    btn_login.place(x=150, y=200)

    add_tech.mainloop()
# messagebox.showinfo("ADD TEACHER","ongoing...")
# ----------------------------------register teacher-------------------


def reg_tech(u, p):
    try:
        print("teacher new:", u, p)
        db = MySQLdb.connect("localhost", "root", "", "faceattendancesystem")
        sql = "select username,password from admin where username='%s' and password='%s'" % (
            u, p)
        print(sql)
        cursor = db.cursor()
        cursor.execute(sql)
        res = cursor.fetchall()
        print("res", res)
        print(type(res))
        print("length:", len(res))
        if len(res) == 0:
            sql1 = """insert into admin(username,password)values('%s','%s')""" % (
                u, p)
            print(sql1)
            try:
                cursor.execute(sql1)
                db.commit()
                print("inserted")
                messagebox.showinfo("SUBMIT", "Registration Successful")
            except Exception as e:
                db.rollback()
                print("error", e)
                messagebox.showinfo("Register TEACHER",
                                    "Registration Unsuccessful")
        else:
            messagebox.showinfo("Register TEACHER",
                                "Registration Unsuccessful")
# db.close()
    except Exception as e:
        print("error", e)


# _________________________________________________function_login_______________________________________________________
def check_tb(un, ps):
    global teacher_id
    print(":", un, ":", ps)
    try:
        if un == '' or ps == '':
            print("please fill all fields")
            messagebox.showinfo("login", "please fill all fields")
        elif un == 'admin' and ps == 'admin':  # admin home
            messagebox.showinfo("login", "Welcome Admin")
            admin_home = Toplevel()
            admin_home.config(bg="powderblue")
            admin_home.minsize(420, 400)
            admin_home.maxsize(420, 400)
            l1 = Label(admin_home, text="ADMIN HOME",
                       font=labelFont3)
            l1.place(x=110, y=40)

            add_stud = Button(admin_home, text="ADD STUDENT",
                              font="Verdana 12 bold", relief=RIDGE, command=lambda: add_student())
            add_stud.place(x=125, y=150)

            add_tech = Button(admin_home, text="ADD TEACHER",
                              font="Verdana 12 bold", relief=RIDGE, command=lambda: add_teacher())
            add_tech.place(x=125, y=200)

            generate = Button(admin_home, text="GENERATE REPORT",
                              font="Verdana 12 bold", relief=RIDGE, command=generatecsv)
            generate.place(x=125, y=250)

            admin_home.mainloop()
        else:
            sql = "select username,password,id from admin where username='%s'" % (
                un)
            print(sql)
        try:
            cursor.execute(sql)
            res = cursor.fetchall()
            print("res", res)
            print(type(res))
            print("length:", len(res))
            if len(res) == 0:
                print("invalid username/password")
                messagebox.showinfo("login", "invalid username/password")
            else:
                for i in res:
                    fname = i[0]
                    fpass = i[1]
                    teacher_id = i[2]
                    teacher_id = str(teacher_id)  # [:-1]
                    print("username", fname, "\npassword",
                          fpass, "\nteacher_id", teacher_id)
                    if fname == un and ps == fpass:
                        print("sucessfull")
                        messagebox.showinfo("login", "Successful")

                        messagebox.showinfo("login", "Welcome Teacher")

                        teacher_home = Toplevel()
                        teacher_home.config(bg="powderblue")
                        teacher_home.minsize(500, 450)
                        teacher_home.maxsize(500, 450)
                        var = StringVar(teacher_home)
                        
                        peroid_no = [1, 2, 3, 4, 5, 6, 7]


                        l1 = Label(teacher_home, text="TEACHER HOME",
                                   font="Verdana 14 bold")
                        l1.place(x=150, y=50)

                        peroid_lbl = Label(
                            teacher_home, text="PEROID NO", font="Verdana 14 bold")
                        peroid_lbl.place(x=15, y=100)
                        # ,command = onselect1)
                        option = OptionMenu(teacher_home, var, *(peroid_no))
                        option.pack()
                        option.place(x=150, y=100)

                        btn_login = Button(teacher_home, text="TAKE ATTENDENCE",  font="Verdana 14 bold",
                                           relief=RIDGE, command=lambda: log_face(teacher_id, var.get()))  # taking attendence
                        btn_login.place(x=250, y=100)

                        btn_login = Button(teacher_home, text="VIEW ATTENDENCE", 
                                           font="Verdana 14 bold", relief=RIDGE, command=lambda: view_att())
                        btn_login.place(x=250, y=180)

                        btn_login = Button(teacher_home, text="EDIT ATTENDENCE", 
                                           font="Verdana 14 bold", relief=RIDGE, command=vw_ABSCENT)  # taking attendence
                        btn_login.place(x=250, y=260)
                        teacher_home.mainloop()


                    else:
                        print ("invalid username/password")
                        messagebox.showinfo("login","invalid username/password")

        except Exception as e:
            print ("Error",e)
            
# else:
# print ("invalid username/password")
# messagebox.showinfo("login","invalid username/password")

    except Exception as e:
        print ("Error",e)
##################################################################################################################
# -------------------------------------------View Attendance-----------------------------------------------------
def view_att():
    print("view")
    
    attendance_vw_home=Toplevel()
    attendance_vw_home.config(bg="powderblue")
    attendance_vw_home.minsize(500,500)
    attendance_vw_home.maxsize(500,500)
    l1=Label(attendance_vw_home,text="VIEW ATTENDANCE",font=labelFont3)
    l1.place(x=110,y=40)

    blblb=ttk.Label(attendance_vw_home, text='Choose date')
    blblb.place(x=50,y=150)

    cal = DateEntry(attendance_vw_home, width=12, background='darkblue',foreground='white', borderwidth=2)
    cal.place(x=125,y=150)
    ent=Button(attendance_vw_home,text="VIEW",font="Verdana 12 bold",relief=RIDGE,command=lambda:print_sel(cal.get()))
    ent.place(x=125,y=180)

    # add_tech=Button(attendance_vw_home,text="ADD TEACHER",bg="orange",font="Verdana 14 bold",relief=RIDGE,command=lambda:add_teacher())
    # add_tech.place(x=125,y=200)


    s = ttk.Style(attendance_vw_home)
    s.theme_use('clam')

    attendance_vw_home.mainloop()

def print_sel(dtt):
        print(dtt)
        d=dtt.split('/')
        print(d)
        if len(d[0])!=2:
            d[0]='0'+d[0]
        if len(d[1])!=2:
            d[1]='0'+d[1]

        c=d[1]+'-'+d[0]+'-'+d[2]
        print(c)

        cursor=db.cursor()
        sql="select StudentName,teacher_id,period_no,LogDate from studentattendance where LogDate='%s'"%(c)
        print (sql)
        try:
            cursor.execute(sql)
            res=cursor.fetchall()
            viewtop=Toplevel()
            h1=Label(viewtop, text='Name').grid(row=0,column=0)
            h2=Label(viewtop, text='Teacher ID').grid(row=0,column=1)
            h3=Label(viewtop, text='Hour').grid(row=0,column=2)
            h4=Label(viewtop, text='Date').grid(row=0,column=3)
            r=1
            for i in res:
                c=0
                for j in i:
                    e=Label(viewtop,text=j)
# e.insert(0,j)
                    e.grid(row=r,column=c)
                    c+=1
                r+=1
        except Exception as e:
            print ("unable to fetch category",e)
# pass
# -------------------------------------------End View Attendance-------------------------------------------------

##################################################################################################################
            # ABSENT
##################################################################################################################
def vw_ABSCENT():
    print("vw_ABSCENT")
    
    ab_vw_home=Toplevel()
    ab_vw_home.config(bg="powderblue")
    ab_vw_home.minsize(400,400)
    ab_vw_home.maxsize(400,400)
    l1=Label(ab_vw_home,text="VIEW ABSENT",font=labelFont3)
    l1.place(x=110,y=40)

    blbblb=ttk.Label(ab_vw_home, text='Choose Hour')
    blbblb.place(x=50,y=130)
    peroid_no=[1,2,3,4,5,6,7]
    global varr
    varr = StringVar(ab_vw_home)
    option = OptionMenu(ab_vw_home, varr,*(peroid_no))#,command = onselect1)
    option.place(x=125,y=130)

    blblb=ttk.Label(ab_vw_home, text='Choose date')
    blblb.place(x=50,y=150)

    cal1 = DateEntry(ab_vw_home, width=12, background='darkblue',foreground='white', borderwidth=2)
    cal1.place(x=125,y=150)
    ent=Button(ab_vw_home,text="VIEW",font="Verdana 12 bold",relief=RIDGE,command=lambda:ABSCENT(cal1.get(),varr.get()))
    ent.place(x=125,y=180)

    # add_tech=Button(ab_vw_home,text="ADD TEACHER",bg="orange",font="Verdana 14 bold",relief=RIDGE,command=lambda:add_teacher())
    # add_tech.place(x=125,y=200)


    s = ttk.Style(ab_vw_home)
    s.theme_use('clam')

    ab_vw_home.mainloop()

def edt(event):
    global teacher_id
    global varr
    cursor=db.cursor()
    stud_name=variable.get()
    hr_no=varr.get()
    print("stud_name",stud_name)
    print("hr_no",hr_no)
    print("selted date",dt)
    print("teacher_id logged in",teacher_id)
    cur = db.cursor()
    sql="SELECT teacher_id,period_no FROM StudentAttendance WHERE LogDate='%s' and period_no='%s'" %(str(dt),hr_no)
    cur.execute(sql)
    print("----",sql)
    view_att=cur.fetchone()
    if view_att and hr_no:
        print(" fetched teacher_id:",view_att[0])
        print("TID=",teacher_id)
        if int(view_att[0])==int(teacher_id):


            sql="INSERT INTO StudentAttendance  (StudentName,teacher_id,period_no,LogDate,LogTime) values('%s','%s','%s','%s','%s')"%(stud_name,teacher_id,hr_no,str(dt),'edited')
            cur.execute(sql)
            db.commit()
            print('Attendance Marked\n',sql)
            messagebox.showinfo("Attendance Edit", "Attendance marked successfully..")
        else:
            messagebox.showinfo("Attendance Edit", "Sorry, you have no permission to edit it..")
    else:
        messagebox.showinfo("Attendance Edit", "Sorry, you have no permission to edit it..")
    wndw.destroy()
def ABSCENT(dtt,hr):
    global teacher_id
    global dt
    global wndw
    print("hour::",hr)
    print(dtt)
    d=dtt.split('/')
    print(d)
    if len(d[0])!=2:
        d[0]='0'+d[0]
    if len(d[1])!=2:
        d[1]='0'+d[1]

    att_date=d[1]+'-'+d[0]+'-'+d[2]
    print (att_date)
    if att_date and hr:
        dt=att_date
# con = sqlite3.connect('FACEATTENDANCESYSTEM.db')
        cur = db.cursor()
        sql="SELECT StudentName FROM StudentAttendance WHERE LogDate='%s' and period_no='%s'" %(str(dt),hr)
        cur.execute(sql)
        print(sql)
        view_att=cur.fetchall()
        view_att=[str(i[0]) for i in view_att]
        print (view_att,"Present")
        sql1="SELECT StudentName FROM StudentReg"
        cur.execute(sql1)
        view_att1=cur.fetchall()
        view_att1=[str(i[0]) for i in view_att1]
        print (view_att1,"All")
        name_list=[]
        for emp_att in view_att1:
            if emp_att not in view_att:
                name_list.append(emp_att)
        print (name_list,"ABS")
        try:
            wndw = Toplevel()
            w=600;h=600
            x=(wndw.winfo_screenwidth()- w)/2
            y=(wndw.winfo_screenheight()-h)/2
            wndw.geometry("%dx%d+%d+%d" % (w,h,x,y))
            wndw.configure(bg="AliceBlue")
            wndw.title("Attendance")
# peroid_no=[1,2,3,4,5,6,7]
# global varr
# varr = StringVar(wndw)
# option = OptionMenu(wndw, varr,*(peroid_no))#,command = onselect1)
# option.place(x=150,y=100)


            global variable
            variable = StringVar(wndw)
            variable.set("Attendance") 

    # select_option = apply(OptionMenu, [wndw, variable] + name_list,command=edt)
            select_option=OptionMenu(wndw,variable,*name_list,command=edt)
            select_option.configure(width=20)
            select_option.place(x=150,y=130)
            wndw.mainloop()
        except Exception as e:
            print("no absences on "+dt)
            wndw.destroy()
            messagebox.showinfo("Info","no absences on "+dt+" or Holiday. Please contanct to system administrator ")
    else:
        
        messagebox.showinfo("Info","Please Select Date and Hour")
# ----------------------------------------Absent----------------------------------------------------
##################################################################################################################
# -------------------------------------------------------------------------------
def log_face(t_id,p_no):


    print("teacher id: ",t_id)
    print("period no: ",p_no)
    l=['1.m4v','2.m4v','3.m4v']
    vdnm=random.choice(l)
    print("selected video:-",vdnm)
# train_to_xml()
    cur = db.cursor()
    date_time=get_date_time()
    if date_time:
        date_time_list=date_time.split(" ")

        sql="SELECT StudentName FROM StudentAttendance WHERE period_no='%s' and teacher_id='%s' AND LogDate='%s'"%(p_no,t_id,str(date_time_list[0]))
        print(sql)
        print("---------------------")

        cur.execute(sql)
        db.commit()
        db_id=cur.fetchone()
        print (db_id,"db_id")
        ck="SELECT * FROM StudentAttendance WHERE period_no='%s'  AND LogDate='%s'"%(p_no,str(date_time_list[0]))
        print(ck)
        cur.execute(ck)
        db.commit()
        rs=cur.fetchone()
        print("---------------------",rs)
        if rs:
            print ("Attendance already marked for this day and this hour")
            messagebox.showinfo("Attendance info", "Attendance already marked for this day and this hour")
        else:
            if p_no:

                train_to_xml()

                size = 4
                webcam = cv2.VideoCapture(vdnm) #Use camera 0
                # We load the xml file
                classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
                faceRecognizer = cv2.face.LBPHFaceRecognizer_create()
                faceRecognizer.read('faceRecognizer1.yml')
                print ("hai")
                while True:
                        try:

                            (rval, mini) = webcam.read()
                            mini = cv2.cvtColor(mini, cv2.COLOR_BGR2GRAY)

                        except:
                            break
                        # cv2.imshow('Video1', mini)
                        # detect MultiScale / faces
                        faces = classifier.detectMultiScale(mini, scaleFactor=1.3,minNeighbors=5)
                        print("Number of face detected=",len(faces))
                        for (x, y, w, h) in faces:
                            print ("face detected")
                            cv2.rectangle(mini, (x, y), (x + w, y + h),(0,255,0),thickness=3)

                            # cv2.imshow('Video2', mini)

                            sub_face = mini[y:y + h, x:x + w]
                            # cv2.imshow('sub11', sub_face)
                            FaceFileName = "/detected_face" + ".jpg"
                            # FaceFileName="/Face_"+str(y) + ".jpg"
                            handle_file(sub_face, FaceFileName, "LOGIN")
                            path = "LOGIN/" + FaceFileName
                            print(path)
                            for file in os.listdir('LOGIN/'):
                                if file:
                                    print("in file")
                                    image1 = cv2.imread(path, 0)
                                    # cv2.imshow('predict_img', image1)
                                    user, confidence = faceRecognizer.predict(image1)

                                    print(user, "--------------------------------------------------------", confidence)
                                    if confidence > 80:
                                        print(user, confidence)
                                        if user:
                                            print("teacher id", t_id)
                                            mark_attendance(user, t_id, p_no)


                        im=mini
                        scale_percent = 50 # percent of original size
                        width = int(im.shape[1] * scale_percent / 100)
                        height = int(im.shape[0] * scale_percent / 100)
                        dim = (width, height)
                        if height>750 or width>750:
                            im = cv2.resize(im, dim, interpolation = cv2.INTER_AREA)
                            cv2.putText(im,str(user)+"--"+str(confidence),(x+width,y+height),cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)
                        # Show the image
                        cv2.imshow('Face Detection',   im)
                        



                        key = cv2.waitKey(10)
                        # if Esc key is press then break out of the loop
                        if key == 27: #The Esc key
                            print ("face recognized")
                            break
                print("Ended")
                cv2.destroyAllWindows()

            else:
                messagebox.showinfo("Attendance info", "Can't take attendance, please select your Hour")
                pass
# -----------------------------------------------------------------------------------------------------------------
def mark_attendance(user_id,tid,pno):
    print("user_id,tid,pno : ",user_id," : ",tid," : ",pno)



    cur = db.cursor()
    try:
        sql="create table StudentAttendance( StudentName TEXT, teacher_id TEXT, period_no TEXT, LogDate TEXT, LogTime TEXT )"
        cur.execute(sql)
#                 co.commit()
        print ("Table Created")
    except:
        print ("table already exit ")
    finally: 
        date_time=get_date_time()
        if date_time:
            date_time_list=date_time.split(" ")
            print("User id====",user_id)
            sql="SELECT StudentName FROM studentreg WHERE StudentID='%d'"%(int(user_id))
            cur.execute(sql)
            db.commit()
            USERS=cur.fetchone()
            print (USERS)
            USER=USERS[0]
            print (USER)
            sql="SELECT StudentName FROM StudentAttendance WHERE period_no='%s' and StudentName='%s' AND LogDate='%s'"%(pno,USER,str(date_time_list[0]))
            print(sql)
            print("---------------------")

            cur.execute(sql)
            db.commit()
            db_id=cur.fetchone()
            print (db_id,"db_id")
            if  db_id:
                print ("in iff")
# messagebox.showinfo("Attendance info", "Attendance already marked for this day and this hour")
                pass
            else:
                sql="INSERT INTO StudentAttendance (StudentName,teacher_id,period_no,LogDate,LogTime) values('%s','%s','%s','%s','%s')"%(USER,tid,pno,str(date_time_list[0]),str(date_time_list[1]))


                # sql="INSERT INTO StudentAttendance(StudentName,teacher_id,period_no,LogDate,LogTime)values('%s','%s','%s','%s','%s')",(USER,tid,pno,str(date_time_list[0]),str(date_time_list[1]))
                cur.execute(sql)
                db.commit()
                print('Attendance Marked',sql)
            # messagebox.showinfo("Login info", "Attendance Marked")
        else:
            messagebox.showinfo("Login info", "Error occur while Login")
########################################################################################
def generatecsv():
    from csv import writer
    cur = db.cursor()
    sql="select StudentReg.StudentID,StudentReg.StudentName, StudentAttendance.LogDate,StudentAttendance.period_no from StudentReg join StudentAttendance on StudentReg.StudentName=StudentAttendance.StudentName"
    print(sql)
    cur.execute(sql)
    result=cur.fetchall()
    print (result)
    with open("out.csv", 'a') as f_object:              # Python 2 version
        writer_object = writer(f_object)
        writer_object.writerow(["Id","Name",'Login Date','Hour'])

        writer_object.writerows(result)
        messagebox.showinfo("Report", "Report generated please check your folder")
##############################################################################################
def get_date_time():
    login_time=datetime.datetime.now()
    login_time=login_time.strftime("%d-%m-%y %H:%M:%S")
    s_login_time=str(login_time)
    print (s_login_time)
    return s_login_time
# ------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------
l1=Label(top,text="LOGIN",font="Verdana 20 bold",fg='black')
l1.place(x=380,y=40)

usr_nm=Label(top,text="USER NAME",font="Verdana 12 bold",bg='powderblue',fg='black')
usr_nm.place(x=280,y=103)
usr_nm_ent=Entry(top,bg="powderblue",width=20,font="Verdana 12 bold")
usr_nm_ent.place(x=400,y=100,height=30)

usr_pass=Label(top,text="PASSWORD",font="Verdana 12 bold",bg='powderblue',fg='black')
usr_pass.place(x=280,y=143)
usr_pass_ent=Entry(top,bg="powderblue",width=20,font="Verdana 12 bold",show="*")
usr_pass_ent.place(x=400,y=140,height=30)

btn_login=Button(top,text="LOGIN",bg="powderblue",font="Verdana 14 bold",relief=RIDGE,command=lambda: check_tb(usr_nm_ent.get(),usr_pass_ent.get()))
btn_login.place(x=400,y=200)
top.mainloop()


