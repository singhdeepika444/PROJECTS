from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from PIL import ImageTk, Image

def profile(username,frame,info_frame):
    # win=Tk()
    # win.title("Profile")
    # win.geometry("650x300+300+200")
    # win.configure(bg="#fff")
    # win.resizable(False,False)

    # frame=Frame(win,width=230,height=250,bg="white",highlightbackground="black", highlightthickness=3) 
    # frame.place(x=20,y=20)

    # info_frame = LabelFrame(win,text="Profile",font=("times new roman",15,"bold"),bg="white",fg="#cdc0b0",bd=5,relief=GROOVE)
    # info_frame.place(x=280,y=10,width=350,height=270)
    
    
    if username=="deepika123":
        user=Label(info_frame,text='Username:\tdeepika123', fg="#57a1f8",bg="white",font=("Microsft YaHei UI Light",13,'bold'))
        user.place(x=10,y=5)
        name=Label(info_frame,text='Name:\t\tDeepika Singh', fg="#57a1f8",bg="white",font=("Microsft YaHei UI Light",13,'bold'))
        name.place(x=10,y=40)#+35
        gender=Label(info_frame,text='Gender:\t\tFemale', fg="#57a1f8",bg="white",font=("Microsft YaHei UI Light",13,'bold'))
        gender.place(x=10,y=75)#+35
        email=Label(info_frame,text='Email:\t\tdeepika@demo.com', fg="#57a1f8",bg="white",font=("Microsft YaHei UI Light",13,'bold'))
        email.place(x=10,y=110)#+35

        path="images/dp.jpg"
        image = Image.open(path)
        resize_image = image.resize((230, 250))
        img = ImageTk.PhotoImage(resize_image)
        label1 = Label(frame,image=img,bg="white")
        label1.place(x=10,y=10)
        label1.image = img
        label1.pack()
    else:
        user=Label(info_frame,text='Username:\tsaurabh123', fg="#57a1f8",bg="white",font=("Microsft YaHei UI Light",13,'bold'))
        user.place(x=10,y=5)
        name=Label(info_frame,text='Name:\t\tSaurabh Prakash', fg="#57a1f8",bg="white",font=("Microsft YaHei UI Light",13,'bold'))
        name.place(x=10,y=40)#+35
        gender=Label(info_frame,text='Gender:\t\tMale', fg="#57a1f8",bg="white",font=("Microsft YaHei UI Light",13,'bold'))
        gender.place(x=10,y=75)#+35
        email=Label(info_frame,text='Email:\t\tsaurabh@demo.com', fg="#57a1f8",bg="white",font=("Microsft YaHei UI Light",13,'bold'))
        email.place(x=10,y=110)#+35

        path="images/sp.jpg"
        image = Image.open(path)
        resize_image = image.resize((230, 250))
        img = ImageTk.PhotoImage(resize_image)
        label1 = Label(frame,image=img,bg="white")
        label1.place(x=10,y=10)
        label1.image = img
        label1.pack()