

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from PIL import ImageTk, Image
import ctypes

# helping modules
from support import *
from information import *


filename=""
username=""
root=Tk()
root.title("Coin Currency Detector")
root.geometry("925x500+300+200")
root.configure(bg="#fff")
root.resizable(False,False)

img=PhotoImage(file="images/login.png")
Label(root,image=img,bg="white").place(x=50,y=50)

frame=Frame(root,width=350,height=350,bg="white") #white
frame.place(x=480,y=70)

heading=Label(frame,text='Sign in', fg="#57a1f8",bg="white",font=("Microsft YaHei UI Light",23,'bold'))
heading.place(x=100,y=5)


#----------------user profile info-----------------------
def show_profile():
    win=Toplevel(root)
    win.title("Profile")
    win.geometry("650x300+300+200")
    win.configure(bg="#fff")
    win.resizable(False,False)

    frame=Frame(win,width=230,height=250,bg="white",highlightbackground="black", highlightthickness=3) 
    frame.place(x=20,y=20)

    info_frame = LabelFrame(win,text="Profile",font=("times new roman",15,"bold"),bg="white",fg="#cdc0b0",bd=5,relief=GROOVE)
    info_frame.place(x=280,y=10,width=350,height=270)
    profile(username,frame,info_frame)

#-------------------------show ouput-------------------------------------------------------------------------
def prediction():
    result=get_prediction(filename)
    temp=result.split(",")
    present="Currency value: {}\nCurrency: {}\nCountry: {}".format(temp[0],temp[1],temp[2].capitalize())
    ctypes.windll.user32.MessageBoxW(0,present,"Prediction",1)

#----------------------------after login page design-----------------------------------------------------------------------
def internal_page_design(username):
    info_frame=Frame(root,width=250,height=40,bg="white")
    info_frame.place(relx=1, rely=0, anchor='ne')

    user_info=Button(info_frame,text=username, fg="#57a1f8",bg="white",font=("Sans-serif",16,'bold'),border=0,cursor="hand2",command=show_profile)
    user_info.place(x=110,y=5)

    logout=Button(info_frame,text='Logout', fg="#57a1f8",bg="white",font=("Sans-serif",16,'bold'),border=0,cursor="hand2",command=root.destroy)
    logout.place(x=0,y=5)

    file_frame = LabelFrame(root,text="File Preview",font=("times new roman",15,"bold"),bg="white",fg="#cdc0b0",bd=5,relief=GROOVE)
    file_frame.place(x=510,y=50,width=370,height=400)

    filetypes = (('image files', '*.jpg'),('image files', '*.jpeg'))
    globals()['filename']=fd.askopenfilename(title='Open a file',initialdir='/',filetypes=filetypes)
    

    Button(file_frame,width=39,pady=7,text="Predict",bg="#57a1f8",fg="white",border=0,command=prediction).place(x=38,y=300)

    image=Image.open(filename)
    resize_image = image.resize((300,230))
    imgg = ImageTk.PhotoImage(resize_image)
    lbl=Label(file_frame,image=imgg,bg="white").place(x=25,y=25)
    lbl.image=imgg
    lbl.pack()
    

#----------------------------------Sign in-----------------------------------------------------------------------------
def signin():
    globals()['username']=user.get()
    password=pswd.get()

    if (username=='deepika123' and password=='123') or (username=='saurabh123' and password=="123"):
        frame.destroy()
        internal_page_design(username)    
        
    elif (username!='deepika123' and password!='123') or (username!='saurabh123' and password!="123"):
        messagebox.showerror("Invalid","Inavlid username and password")
    elif (password!='123') or (password!="123"):
        messagebox.showerror("Invalid","Inavlid password")
    elif (username!='deepika123') or (username!='saurabh123'):
        messagebox.showerror("Invalid","Inavlid username")

#-----------------------------------------Sign up------------------------------------------------
def signup():
    ctypes.windll.user32.MessageBoxW(0,"Please contact owner of Application","Sign up",1)

#--------------------------------------------------------------------------------------------

def on_enter(e):
    user.delete(0,"end")
def on_leave(e):
    name=user.get()
    if name=="":
        user.insert(0,"Username")

user=Entry(frame,width=25,fg="black",border=0,bg="white",font=("Microsft YaHei UI Light",12))
user.place(x=30,y=80)
user.insert(0,'username')
user.bind("<FocusIn>",on_enter)
user.bind("<FocusOut>",on_leave)

Frame(frame,width=295,height=2,bg="black").place(x=25,y=107)

#--------------------------------------------------------------------------------------------
def on_enter(e):
    pswd.delete(0,"end")
def on_leave(e):
    name=pswd.get()
    if name=="":
        pswd.insert(0,"Password")

pswd=Entry(frame,width=25,fg="black",border=0,bg="white",font=("Microsft YaHei UI Light",12))
pswd.place(x=30,y=150)
pswd.insert(0,'Password')
pswd.bind("<FocusIn>",on_enter)
pswd.bind("<FocusOut>",on_leave)

Frame(frame,width=295,height=2,bg="black").place(x=25,y=177)

#---------------------------------------------------------------------------------------------
Button(frame,width=39,pady=7,text="Sign in",bg="#57a1f8",fg="white",border=0,command=signin).place(x=35,y=204)
label=Label(frame,text="Don't have account ?",fg="black",bg="white",font=("Microsft YaHei UI Light",9))
label.place(x=75,y=270)

sign_up=Button(frame,width=6,text="Sign up",border=0,bg="white",cursor="hand2",fg="#57a1f8",command=signup)
sign_up.place(x=215,y=270)



root.mainloop()