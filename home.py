from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import numpy as np
import face_recognition
from tensorflow.keras.models import load_model

def open_reg():

    path=""
    #---REGISTER---
    def save():
        def clear():
            txt_name.delete(0,END)
            txt_dept.delete(0,END)
            txt_email.delete(0,END)
            txt_pswd.delete(0,END)
            
        global path
        d1=txt_name.get()
        d2=txt_dept.get()
        d3=txt_email.get()
        d4=txt_pswd.get()
        d5=str(0)

        if d1=="" or d2=="" or d3=="" or d4=="" or d5=="" or str=="":
            messagebox.showerror("ERROR!","All Fields Are Required!")
        else:
            try:
                conn = mysql.connector.connect(host='127.0.0.1',user='root',password='')
                cur = conn.cursor()
                cur.execute("use face")
                cur.execute("insert into info values("+"'"+d1+"'"+","+"'"+d2+"'"+","+"'"+d3+"'"+","+"'"+d4+"'"+","+"'"+path+"'"+","+"'"+d5+"'"+")")
                conn.commit()
                conn.close()
                messagebox.showinfo("SUCCESS","Data Saved Successfully! Please Login!")
                clear()
                open_log()
            except:
                messagebox.showerror("ERROR!","Error Occured!Try Again!")
        
    #---UPLOAD_IMAGE---
    def cam():
        global path
        cap=cv2.VideoCapture(0)
        conn=mysql.connector.connect(host="127.0.0.1",user="root",password="")
        my=conn.cursor()
        my.execute("use face")
        res=my.execute("select count(*) from info")
        rows=my.fetchall()
        for i in rows:
            x=i[0]
            break
        x=x+1
        while True:
            rect,frame=cap.read()
            cv2.imshow("CAPTURE FACE",frame)
            cv2.imwrite(r"C:/Face/user_image/pic"+str(x)+".jpg",frame)
            if cv2.waitKey(1)& 0xff==ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()

        img_lb=Label(img_fr)
        img_lb.place(x=0,y=0)
        path="C:/Face/user_image/pic"+str(x)+".jpg"
        img=Image.open(r"C:/Face/user_image/pic"+str(x)+".jpg")
        img=img.resize((280,170),Image.ANTIALIAS)
        img=ImageTk.PhotoImage(img)
        img_lb.config(image=img)
        img_lb.image=img
        
    #---Register_Toplevel---    
    root.title("REGISTER!")
    root.geometry("1366x768+0+0")
    root.config(bg="white")
    

    #---BG_IMAGE---
    bg=Label(root)
    img=Image.open(r"C:\Face\images\bg.jpg")
    img=ImageTk.PhotoImage(img)
    bg.config(image=img)
    bg.image=img
    bg.place(x=0,y=0,relheight=1,relwidth=1)

    #---ICON_IMAGE---
    icon=Label(root)
    img=Image.open(r"C:\Face\images\x1.png")
    img=ImageTk.PhotoImage(img)
    icon.config(image=img)
    icon.image=img
    icon.place(x=80,y=100)

    
    #---REGISTER_FRAME---
    frame1=Frame(root,bg="white")
    frame1.place(x=585,y=100,width=700,height=586)

    title=Label(frame1,text="REGISTER HERE",font=("Californian FB",20,"bold"),bg="white",fg="red").place(x=50,y=30)

    img_lbl=Label(frame1,text="Image",font=("Californian FB",15,"bold"),bg="white",fg="gray").place(x=380,y=100)

    name=Label(frame1,text="Username",font=("Californian FB",15,"bold"),bg="white",fg="gray").place(x=50,y=100)
    txt_name=Entry(frame1,font=("Californian FB",15),bg="lightgray")
    txt_name.place(x=50,y=130,width=300)

    email=Label(frame1,text="Email",font=("Californian FB",15,"bold"),bg="white",fg="gray").place(x=50,y=180)
    txt_email=Entry(frame1,font=("Californian FB",15),bg="lightgray")
    txt_email.place(x=50,y=210,width=300)

    dept=Label(frame1,text="Department",font=("Californian FB",15,"bold"),bg="white",fg="gray").place(x=50,y=260)
    txt_dept=Entry(frame1,font=("Californian FB",15),bg="lightgray")
    txt_dept.place(x=50,y=290,width=300)

    pswd=Label(frame1,text="Password",font=("Californian FB",15,"bold"),bg="white",fg="gray").place(x=50,y=340)
    txt_pswd=Entry(frame1,show="*",font=("Californian FB",15),bg="lightgray")
    txt_pswd.place(x=50,y=370,width=300)
    
    #---HOME_BUTTON---
    h_btn=Button(frame1)
    img=Image.open(r"C:\Face\images\home.jpg")
    img=ImageTk.PhotoImage(img)
    h_btn.config(image=img,bd=0,cursor="hand2",command=start)
    h_btn.image=img
    h_btn.place(x=600,y=30,height=50,width=50)
    
    #---IMAGE_FRAME---
    img_fr=Frame(frame1,highlightthickness=2,highlightbackground = "black", highlightcolor= "black")
    img_fr.place(x=380,y=130,height=180,width=290)

    #---REGISTER_BUTTON---
    reg_btn=Button(frame1)
    img=Image.open(r"C:\Face\images\reg.jpg")
    img=ImageTk.PhotoImage(img)
    reg_btn.config(image=img,bd=0,cursor="hand2",command=save)
    reg_btn.image=img
    reg_btn.place(x=230,y=450,height=50,width=240)

    #---UPLOAD_IMAGE_BUTTON---
    upl_btn=Button(frame1)
    img=Image.open(r"C:\Face\images\upload.jpg")
    img=ImageTk.PhotoImage(img)
    upl_btn.config(image=img,bd=0,cursor="hand2",command=cam)
    upl_btn.image=img
    upl_btn.place(x=453,y=370,height=30,width=144)

    root.mainloop()


def open_log():  
    
    def auth():

        #---DETECT_MASK---
        def mask():
            from detect_mask_video import detect_and_predict_mask
            
        #---DETECT_SOCIAL_DISTANCING---
        def dist():
            import social_distance_detector

        #---HOME---
        def home():
            dash.destroy()
            txt_pswd.delete(0,END)
            txt_email.delete(0,END)

        def loglog(em,pd,atno):
            global c,path1
            conn=mysql.connector.connect(host="127.0.0.1",user="root",password="")
            cur=conn.cursor()
            cur.execute("use face")
            cur.execute("select * from info where email="+"'"+em+"'"+" and pswd="+"'"+pd+"'"+"")
            res=cur.fetchall()
            if atno == 1:
                for row in res:
                    no = row[5]
                no = no+1
                cur.execute("update info set att="+"'"+str(no)+"'"+" where email="+"'"+em+"'"+"")
            cur.execute("select * from info where email="+"'"+em+"'"+" and pswd="+"'"+pd+"'"+"")
            res=cur.fetchall()
            for data in res:
                c=c+1
                path1=data[4]
                
                #---DEATIL_SECTION---
                det=Frame(frame1,bg="white",highlightthickness=2,highlightbackground = "black", highlightcolor= "black")
                det.place(x=0,y=150,height=200,width=700)
                    
                det1=Label(det,text="Username : "+data[0],font=("Californian FB",20,"bold"),bg="white",fg="blue").place(x=50,y=20)
                det2=Label(det,text="Department : "+data[1],font=("Californian FB",20,"bold"),bg="white",fg="blue").place(x=50,y=60)
                det3=Label(det,text="Email : "+data[2],font=("Californian FB",20,"bold"),bg="white",fg="blue").place(x=50,y=100)
                det3=Label(det,text="Attendance : "+str(data[5]),font=("Californian FB",20,"bold"),bg="white",fg="blue").place(x=50,y=140)
                det4=Label(det)
                img1=Image.open(r""+data[4]+"")
                img1=img1.resize((250,160),Image.ANTIALIAS)
                img1=ImageTk.PhotoImage(img1)
                det4.config(image=img1)
                det4.image=img1
                det4.place(x=400,y=20)
                
                #---MARK_ATTENDANCE---
                att_btn=Button(frame1)
                img=Image.open(r"C:\Face\images\tick.jpg")
                img=ImageTk.PhotoImage(img)
                att_btn.config(image=img,bd=0,cursor="hand2",command=att)
                att_btn.image=img
                att_btn.place(x=25,y=390,height=50,width=200)
                        
                #---DETECT_MASK---
                mask_btn=Button(frame1)
                img=Image.open(r"C:\Face\images\mask.jpg")
                img=ImageTk.PhotoImage(img)
                mask_btn.config(image=img,bd=0,cursor="hand2",command=mask)
                mask_btn.image=img
                mask_btn.place(x=250,y=390,height=50,width=200)
                        
                #---SOCIAL_DISTANCING---
                dist_btn=Button(frame1)
                img=Image.open(r"C:\Face\images\dist.jpg")
                img=ImageTk.PhotoImage(img)
                dist_btn.config(image=img,bd=0,cursor="hand2",command=dist)
                dist_btn.image=img
                dist_btn.place(x=475,y=390,height=50,width=200)

                #---LOGOUT_BUTTON---
                out_btn=Button(frame1)
                img=Image.open(r"C:\Face\images\logout.jpg")
                img=ImageTk.PhotoImage(img)
                out_btn.config(image=img,bd=0,cursor="hand2",command=home)
                out_btn.image=img
                out_btn.place(x=250,y=480,height=50,width=200)

                #---CLOSE_CONNECTION---
                conn.commit()
                conn.close()

        #---ATTENDANCE_MARKER---
        def att():

            #---CAPTURE_IMAGE---
            def click():
                global cam
                cap=cv2.VideoCapture(0)
                while True:
                    rect,frame=cap.read()
                    #gray=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
                    cv2.imshow("CAPTURE - Press 'q' key!",frame)
                    cv2.imwrite(r"C:/Face/user_image/att.jpg",frame)
                    cam=(r"C:/Face/user_image/att.jpg")
                    imgc=Image.open(cam)
                    imgc=imgc.resize((480,330),Image.ANTIALIAS)
                    imgc=ImageTk.PhotoImage(imgc)
                    c_img.config(image=imgc)
                    c_img.image=imgc
                    if cv2.waitKey(1)& 0xff==ord('q'):
                        break
                cap.release()
                cv2.destroyAllWindows()
                
            #---MATCH_FACES---    
            def match():
                def mess():
                    mes.destroy()
                    at.destroy()
                global path1
                x=0
                img1=face_recognition.load_image_file(path1)
                img1=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
                faceloc=face_recognition.face_locations(img1)[0]
                encode1=face_recognition.face_encodings(img1)[0]
                cv2.rectangle(img1,(faceloc[3],faceloc[0]),(faceloc[1],faceloc[2]),(255,0,0),2)

                img2=face_recognition.load_image_file("C:/Face/user_image/att.jpg")
                img2=cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
                faceloc1=face_recognition.face_locations(img2)[0]
                encode2=face_recognition.face_encodings(img2)[0]
                cv2.rectangle(img2,(faceloc1[3],faceloc1[0]),(faceloc1[1],faceloc1[2]),(255,0,0),2)
                
                res=face_recognition.compare_faces([encode1],encode2)
                if res[0] == True :
                    loglog(d1,d2,1)
                    mes = Toplevel()
                    mes.geometry("250x80+602+200")
                    mes.title("SUCCESS")
                    er=Label(mes,text="Marked Successfully!",font=("bold")).place(x=15,y=15)
                    bt=Button(mes,text="Close",command=mess).place(x=105,y=45)
                    mes.lift()
                    
                else:
                    mes = Toplevel()
                    mes.geometry("250x80+602+200")
                    mes.title("ERROR")
                    er=Label(mes,text="Marking Failed!",font=("bold")).place(x=15,y=15)
                    bt=Button(mes,text="Close",command=mess).place(x=105,y=45)
                    
                
            #---ATTENDANCE_TOPLEVEL---    
            global path1
            at=Toplevel()
            at.title("ATTENDANCE!")
            at.geometry("1205x550+80+100")
            at.config(bg="white")
            c=0
            #---BG_IMAGE---
            
            bg=Label(at)
            img=Image.open(r"C:\Face\images\bg.jpg")
            img=img.resize((1205,550),Image.ANTIALIAS)
            img=ImageTk.PhotoImage(img)
            bg.config(image=img)
            bg.image=img
            bg.place(x=0,y=0,relheight=1,relwidth=1)

            #---Frame_Image---
            fr1=Frame(at,bg="white")
            fr1.place(x=66,y=50,width=500,height=400)

            fi = Frame(fr1,bg="red")
            fi.place(x=0,y=0,width=500,height=350)

            u_img=Label(fi)
            img=Image.open(r""+path1+"")
            img=img.resize((480,330),Image.ANTIALIAS)
            img=ImageTk.PhotoImage(img)
            u_img.config(image=img)
            u_img.image=img
            u_img.place(x=8,y=8)
            
            lb=Label(fr1,text="Your Profile Image",font=("Californian FB",15,"bold"),bg="white",fg="red").place(x=170,y=360)

            #---Frame_Camera---
            fr2=Frame(at,bg="white")
            fr2.place(x=632,y=50,width=500,height=400)

            fc = Frame(fr2,bg="skyblue")
            fc.place(x=0,y=0,width=500,height=350)

            c_img=Label(fc)
            imgc=Image.open(r"C:\Face\images\cam.jpg")
            imgc=imgc.resize((480,330),Image.ANTIALIAS)
            imgc=ImageTk.PhotoImage(imgc)
            c_img.config(image=imgc)
            c_img.image=imgc
            c_img.place(x=8,y=8)
            
            #---UPLOAD_IMAGE_BUTTON---
            upl_btn=Button(fr2)
            img=Image.open(r"C:\Face\images\upload.jpg")
            img=ImageTk.PhotoImage(img)
            upl_btn.config(image=img,bd=0,cursor="hand2",command=click)
            upl_btn.image=img
            upl_btn.place(x=178,y=360,height=30,width=144)

            #---MARK_ATTENDANCE---
            att_btn=Button(at)
            img=Image.open(r"C:\Face\images\mark.jpg")
            img=ImageTk.PhotoImage(img)
            att_btn.config(image=img,bd=0,cursor="hand2",command=match)
            att_btn.image=img
            att_btn.place(x=502,y=475,height=50,width=200)
            
        #---LOGIN---
        global path1,c
        c=0
        d1=txt_email.get()
        d2=txt_pswd.get()


        txt_pswd.delete(0,END)
        txt_email.delete(0,END)
        
        dash=Toplevel()
        dash.title("DASHBOARD!")
        dash.geometry("1366x768+0+0")
        dash.config(bg="white")
                
        #---BG_IMAGE---
        bg=Label(dash)
        img=Image.open(r"C:\Face\images\bg.jpg")
        img=ImageTk.PhotoImage(img)
        bg.config(image=img)
        bg.image=img
        bg.place(x=0,y=0,relheight=1,relwidth=1)

        #---ICON_IMAGE---
        icon=Label(dash)
        img=Image.open(r"C:\Face\images\x1.png")
        img=ImageTk.PhotoImage(img)
        icon.config(image=img)
        icon.image=img
        icon.place(x=80,y=100)
            
        #---DASHBOARD_FRAME---
        frame1=Frame(dash,bg="white")
        frame1.place(x=585,y=100,width=700,height=586)

        #---HOME_BUTTON---
        h_btn=Button(frame1)
        img=Image.open(r"C:\Face\images\home.jpg")
        img=ImageTk.PhotoImage(img)
        h_btn.config(image=img,bd=0,cursor="hand2",command=home)
        h_btn.image=img
        h_btn.place(x=600,y=30,height=50,width=50)

        title=Label(frame1,text="Student Dashboard",font=("Californian FB",30,"bold"),bg="white",fg="red").place(x=50,y=30)
        loglog(d1,d2,0)

        if c==0:
            out()
            mes = Toplevel()
            mes.geometry("250x80+785+200")
            mes.title("ERROR")
            er=Label(mes,text="Invalid Login Credentials!",font=("bold")).place(x=15,y=15)
            bt=Button(mes,text="Close",command=mes.destroy).place(x=105,y=45)
        
    #---LOGIN_TOPLEVEL---
    root.title("LOGIN!")
    root.geometry("1366x768+0+0")
    root.config(bg="white")
    

    #---BG_IMAGE---
    bg=Label(root)
    img=Image.open(r"C:\Face\images\bg.jpg")
    img=ImageTk.PhotoImage(img)
    bg.config(image=img)
    bg.image=img
    bg.place(x=0,y=0,relheight=1,relwidth=1)

    #---ICON_IMAGE---
    icon=Label(root)
    img=Image.open(r"C:\Face\images\x2.png")
    img=ImageTk.PhotoImage(img)
    icon.config(image=img)
    icon.image=img
    icon.place(x=80,y=100)

    
    #---LOGIN_FRAME---
    frame1=Frame(root,bg="white")
    frame1.place(x=585,y=100,width=700,height=586)

    title=Label(frame1,text="LOGIN HERE",font=("Californian FB",20,"bold"),bg="white",fg="red").place(x=50,y=30)

    email=Label(frame1,text="Email",font=("Californian FB",15,"bold"),bg="white",fg="gray").place(x=200,y=210)
    txt_email=Entry(frame1,font=("Californian FB",15),bg="lightgray")
    txt_email.place(x=200,y=240,width=300)

    pswd=Label(frame1,text="Password",font=("Californian FB",15,"bold"),bg="white",fg="gray").place(x=200,y=290)
    txt_pswd=Entry(frame1,show="*",font=("Californian FB",15),bg="lightgray")
    txt_pswd.place(x=200,y=320,width=300)
    
    #---HOME_BUTTON---
    h_btn=Button(frame1)
    img=Image.open(r"C:\Face\images\home.jpg")
    img=ImageTk.PhotoImage(img)
    h_btn.config(image=img,bd=0,cursor="hand2",command=start)
    h_btn.image=img
    h_btn.place(x=600,y=30,height=50,width=50)

    #---LOGIN_BUTTON---
    log_btn=Button(frame1)
    img=Image.open(r"C:\Face\images\log.jpg")
    img=ImageTk.PhotoImage(img)
    log_btn.config(image=img,bd=0,cursor="hand2",command=auth)
    log_btn.image=img
    log_btn.place(x=230,y=400,height=50,width=240)


    root.mainloop()

x=1

root=Tk()
def start():
    root.title("HOME!")
    root.geometry("1366x768+0+0")
    root.config(bg="white")
        

    #---BG_IMAGE---
    bg=Label(root)
    img=Image.open(r"C:\Face\images\bg.jpg")
    img=ImageTk.PhotoImage(img)
    bg.config(image=img)
    bg.image=img
    bg.place(x=0,y=0,relheight=1,relwidth=1)

    #---ICON_IMAGE---
    icon=Label(root)
    icon.place(x=80,y=100)


    frame1=Frame(root,bg="white")
    frame1.place(x=585,y=100,width=700,height=586)

    #---INTRODUCTION---

    title=Label(frame1,text="FACIAL RECOGNITION SYSTEM",font=("Californian FB",30,"bold"),bg="white",fg="red").place(x=50,y=30)

    desc1=Label(frame1,text="This is a Facial Recognition System for students. Here",font=("Californian FB",18),bg="white").place(x=80,y=100)
    desc2=Label(frame1,text="students can mark attendance and detect mask by recognising",font=("Californian FB",18),bg="white").place(x=55,y=150)
    desc3=Label(frame1,text="recognising individual faces.",font=("Californian FB",18),bg="white").place(x=210,y=200)

    desc4=Label(frame1,text="New User!",font=("Californian FB",18),bg="white").place(x=120,y=350)
    desc5=Label(frame1,text="Existing User!",font=("Californian FB",18),bg="white").place(x=450,y=350)

    #---REGISTER_BUTTON---
    reg_btn=Button(frame1)
    img=Image.open(r"C:\Face\images\reg.jpg")
    img=ImageTk.PhotoImage(img)
    reg_btn.config(image=img,bd=0,cursor="hand2",command=open_reg)
    reg_btn.image=img
    reg_btn.place(x=80,y=400,height=50,width=240)

    #---LOGIN_BUTTON---
    log_btn=Button(frame1)
    img=Image.open(r"C:\Face\images\log.jpg")
    img=ImageTk.PhotoImage(img)
    log_btn.config(image=img,bd=0,cursor="hand2",command=open_log)
    log_btn.image=img
    log_btn.place(x=400,y=400,height=50,width=240)

    #---QUIT_BUTTON---
    q_btn=Button(frame1)
    img=Image.open(r"C:\Face\images\quit.jpg")
    img=ImageTk.PhotoImage(img)
    q_btn.config(image=img,bd=0,cursor="hand2",command=root.destroy)
    q_btn.image=img
    q_btn.place(x=230,y=500,height=50,width=240)

    
    def a():
        global x
        img=Image.open(r"C:\Face\images\x"+str(x)+".png")
        img=ImageTk.PhotoImage(img)
        icon.config(image=img)
        icon.image=img
        x=x+1
        root.after(2000,a)
        if x==3:
            x=1
    a()
start()
root.mainloop()
