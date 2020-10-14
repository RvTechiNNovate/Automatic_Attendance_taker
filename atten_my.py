# all library imported
import tkinter as tk           
import cv2,os                          
import csv
import numpy as np
from PIL import Image
import pandas as pd
import datetime as dt
import time
from tkinter import messagebox as msg

bgclr='powder blue'
#------------------------------------------------------------------------------------------------------------------------------------#
root=tk.Tk()
bgclr='powder blue'
root.title("Attendance Portal")
root.state('zoomed')
root.update()
root.configure(bg=bgclr)
root.resizable(width=False,height=False)
message = tk.Label(root, text="ATTENDANCE TAKING PORTAL" ,bg="pink"  ,fg="black"  ,width=40  ,height=1,font=('Times New Roman', 35, 'bold underline')) 
message.place(x=200, y=20)



x_marg = 75
y_marg = 20
checker=0

#---------------------------------------------------------------------------------------------------#
#                                       login window                                                #
#---------------------------------------------------------------------------------------------------#


def home():
    login_frm=tk.Frame(root,bg='pink')
    login_frm.place(x=0,y=100,width=root.winfo_width(),height=root.winfo_height())

    lbl_user=tk.Label(login_frm,bg=bgclr,font=('Time New Roman',20,''),fg='black',text='Username')
    lbl_user.place(x=300,y=100)

    lbl_pass=tk.Label(login_frm,bg=bgclr,font=('Time New Roman',20,''),fg='black',text='Password')
    lbl_pass.place(x=300,y=150)

    ent_user=tk.Entry(login_frm,bd=5,font=('Time New Roman',15,''))
    ent_user.focus()
    ent_user.place(x=490,y=105)

    ent_pass=tk.Entry(login_frm,show='*',bd=5,font=('Time New Roman',15,'bold'))
    ent_pass.place(x=490,y=155)
    
    lgn_btn=tk.Button(login_frm,text='login',command=lambda:login(login_frm,ent_user,ent_pass),bd=5,font=('Time New Roman',12,'bold'))
    lgn_btn.place(x=500,y=305)

    rst_btn=tk.Button(login_frm,command=lambda:reset(ent_user,ent_pass),text='reset',bd=5,font=('Time New Roman',12,'bold'))
    rst_btn.place(x=590,y=305)

    message = tk.Label(login_frm, text="Thanks to Aditya Sir" ,bg="white"  ,fg="black"  ,width=15 ,height=2,font=('Times New Roman', 25, 'bold')) 
    message.place(relx=0.78, rely=0.65)
    
    message = tk.Label(login_frm, text="By Ritesh" ,bg="white"  ,fg="black"  ,width=15 ,height=2,font=('Times New Roman', 25, 'bold')) 
    message.place(relx=0.78, rely=0.75)


    quitWindow =tk.Button(root, text="QUIT", command=quit_window ,fg="white"  ,bg="red"  ,width=10  ,height=2, activebackground = "pink" ,font=('Times New Roman', 15, ' bold '))
    quitWindow.place(x=700, y=735-y_marg)

# #---------------------------------------------------------------------------------------------------#
# #                                       main window                                                 #
# #---------------------------------------------------------------------------------------------------#
def welcomeAdmin():
    width_of_btn=30
    h=4

    login_frm=tk.Frame(root,bg="pink")
    login_frm.place(x=0,y=100,width=root.winfo_width(),height=root.winfo_height())

    message = tk.Label(login_frm, text="Thanks to Aditya Sir" ,bg="white"  ,fg="black"  ,width=15 ,height=2,font=('Times New Roman', 25, 'bold')) 
    message.place(relx=0.78, rely=0.65)
    
    message = tk.Label(login_frm, text="By Ritesh" ,bg="white"  ,fg="black"  ,width=15 ,height=2,font=('Times New Roman', 25, 'bold')) 
    message.place(relx=0.78, rely=0.75)
    
    lbl_user=tk.Label(login_frm,bg=bgclr,font=('Time new roman',15,'bold'),fg="Black",text='Welcome : Admin')
    lbl_user.place(x=10,y=100)

    logout_btn=tk.Button(login_frm,width=15,command=lambda:logout(login_frm),font=('Time new roman',12,'bold'),text='Logout',bd=5)
    logout_btn.place(relx=.85,y=100)


    mark_att_btn=tk.Button(login_frm,width=width_of_btn,height=h,command=lambda:mark_att(),text='MARK ATTENDANCE',fg="black"  ,bg="yellow", activebackground = "green" ,font=('Times New Roman', 15, ' bold '),bd=5)
    mark_att_btn.place(x=600,y=100)

    Add_s_btn=tk.Button(login_frm,width=width_of_btn,height=h,command=lambda:add_stu(),text='ADD STUDENT',fg="black"  ,bg="yellow", activebackground = "green" ,font=('Times New Roman', 15, ' bold '),bd=5)
    Add_s_btn.place(x=600,y=250)

    quitWindow =tk.Button(root, text="QUIT", command=quit_window ,fg="black"  ,bg="red"  ,width=10  ,height=2, activebackground = "green" ,font=('Times New Roman', 15, ' bold '))
    quitWindow.place(x=700, y=735-y_marg)


#-----------------------------------------------------------------------------------------------------------------------------------
def add_stu():
    login_frm=tk.Frame(root,bg="pink")
    login_frm.place(x=0,y=100,width=root.winfo_width(),height=root.winfo_height())


    # message =Label(login_frm, text="GBU UNIVERSITY" ,bg="white"  ,fg="black"  ,width=20  ,height=2,font=('Times New Roman', 25, 'bold')) 
    # message.place(x=1150, y=760)

    roll_lbl =tk.Label(login_frm, text="Enter Your Roll no",width=20  ,height=2  ,fg="black"  ,bg="Pink" ,font=('Times New Roman', 25, ' bold ') ) 
    roll_lbl.place(x=400-x_marg, y=200-y_marg)

    roll_entry=tk.Entry(login_frm,width=30,bg="white" ,fg="blue",font=('Times New Roman', 15, ' bold '))
    roll_entry.place(x=450-x_marg, y=300-y_marg)

    
    step1_lbl =tk.Label(login_frm, text="STEP 1",width=20  ,fg="green"  ,bg="pink"  ,height=2 ,font=('Times New Roman', 20, ' bold '))
    step1_lbl.place(x=440-x_marg, y=100)

    takeImg =tk.Button(login_frm, text="IMAGE CAPTURE ", command=lambda:TakeImages(roll_entry,name_entry)  ,fg="white"  ,bg="red"  ,width=25  ,height=2, activebackground = "pink" ,font=('Times New Roman', 15, ' bold '))
    takeImg.place(x=445-x_marg, y=425-y_marg)


    name_lbl =tk.Label(login_frm, text="Enter Your Name",width=20  ,fg="black"  ,bg="pink"    ,height=2 ,font=('Times New Roman', 25, ' bold ')) 
    name_lbl.place(x=800-x_marg, y=200-y_marg)

    name_entry =tk.Entry(login_frm,width=30  ,bg="white"  ,fg="blue",font=('Times New Roman', 15, ' bold ')  )
    name_entry.place(x=850-x_marg, y=300-y_marg)


    lbl5 =tk.Label(login_frm, text="STEP 2",width=20  ,fg="green"  ,bg="pink"  ,height=2 ,font=('Times New Roman', 20, ' bold ')) 
    lbl5.place(x=845-x_marg, y=100)


    trainImg =tk.Button(login_frm, text="TRAINING", command=lambda:TrainImages(roll_entry,name_entry)  ,fg="white"  ,bg="red"  ,width=25  ,height=2, activebackground = "pink" ,font=('Times New Roman', 15, ' bold '))
    trainImg.place(x=845-x_marg, y=425-y_marg)
    
    logout_btn=tk.Button(login_frm,width=15,command=lambda:back(login_frm),font=('Time new roman',12,'bold'),text='Back',bd=5)
    logout_btn.place(relx=.85,y=100)
   
    quitWindow =tk.Button(root, text="QUIT", command=quit_window ,fg="black"  ,bg="red"  ,width=10  ,height=2, activebackground = "green" ,font=('Times New Roman', 15, ' bold '))
    quitWindow.place(x=700, y=735-y_marg)

    message = tk.Label(login_frm, text="Thanks to Aditya Sir" ,bg="white"  ,fg="black"  ,width=15 ,height=2,font=('Times New Roman', 25, 'bold')) 
    message.place(relx=0.78, rely=0.65)
    
    message = tk.Label(login_frm, text="By Ritesh" ,bg="white"  ,fg="black"  ,width=15 ,height=2,font=('Times New Roman', 25, 'bold')) 
    message.place(relx=0.78, rely=0.75)

#------------------------------------------------------------------------------------------------------------------------------------#
def clear1(e_r):
    e_r.delete(0, 'end')    
    res = ""
    message.configure(text= res)

def clear2(e_n):
    e_n.delete(0, 'end')    
    res = ""
    message.configure(text= res)    
 #------------------------------------------------------------------------------------------------------------------------------------#   
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False
 #------------------------------------------------------------------------------------------------------------------------------------#
def TakeImages(e_r,e_n):        
    Id=(e_r.get())
    name=(e_n.get())
    if not Id:
        res="Please enter Id"
        message.configure(text = res)
        MsgBox = tk.messagebox.askquestion ("Warning","Please enter roll number properly , press yes if you understood",icon = 'warning')
        if MsgBox == 'no':
            tk.messagebox.showinfo('Your need','Please go through the readme file properly')
    elif not name:
        res="Please enter Name"
        message.configure(text = res)
        MsgBox = tk.messagebox.askquestion ("Warning","Please enter your name properly , press yes if you understood",icon = 'warning')
        if MsgBox == 'no':
            tk.messagebox.showinfo('Your need','Please go through the readme file properly')
        
    elif(is_number(Id) and name.isalpha()):
            cam = cv2.VideoCapture(0)
            harcascadePath = "haarcascade_frontalface_default.xml"
            detector=cv2.CascadeClassifier(harcascadePath)
            sampleNum=0
            while(True):
                _ , img = cam.read()
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = detector.detectMultiScale(gray, 1.3, 5)
                for (x,y,w,h) in faces:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)        
                    #incrementing sample number 
                    sampleNum=sampleNum+1
                    #saving the captured face in the dataset folder TrainingImage
                    cv2.imwrite("TrainingImage/ "+name +"."+Id +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])
                    #display the frame
                    cv2.imshow('frame',img)
                #wait for 100 miliseconds 
                if cv2.waitKey(100) & 0xFF == ord('q'):
                    break
                # break if the sample number is morethan 100
                elif sampleNum>60:
                    break
            cam.release()
            cv2.destroyAllWindows() 
            res = "Images Saved for ID : " + Id +" Name : "+ name
            row = [Id , name]
            with open('StudentDetails/StudentDetails.csv','a+') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow(row)
            csvFile.close()
            message.configure(text= res)
    else:
        if(is_number(Id)):
            res = "Enter Alphabetical Name"
            message.configure(text= res)
        if(name.isalpha()):
            res = "Enter Numeric Id"
            message.configure(text= res)


#-----------------------------------------------------------------------------------------------------------------------------------------------
    
def TrainImages(e_r,e_n):
    recognizer = cv2.face_LBPHFaceRecognizer.create()
    faces,Id = getImagesAndLabels("TrainingImage")
    recognizer.train(faces, np.array(Id))
    recognizer.save("TrainingImageLabel/Trainner.yml")
    res = "Image Trained"
    clear1(e_r)
    clear2(e_n)
    message.configure(text= res)

    tk.messagebox.showinfo('Completed','Your model has been trained successfully!!')
    
#----------------------------------------------------------------------------------------------------------------------------------------------
def getImagesAndLabels(path):

    imagePaths=[os.path.join(path,f) for f in os.listdir(path)] 
    
    faces=[]

    Ids=[]

    for imagePath in imagePaths:
        #loading the image and converting it to gray scale
        pilImage=Image.open(imagePath).convert('L')
        #Now we are converting the PIL image into numpy array
        imageNp=np.array(pilImage,'uint8')
        #getting the Id from the image
        Id=int(os.path.split(imagePath)[-1].split(".")[1])
        # extract the face from the training image sample
        faces.append(imageNp)
        Ids.append(Id)        
    return faces,Ids
#-----------------------------------------------------------------------------------------------------------------------------------------------
def mark_att():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("TrainingImageLabel/Trainner.yml")
    harcascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath)    
    df=pd.read_csv("StudentDetails/StudentDetails.csv")
    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX        
    col_names =  ['Id','Name','Date','Time']
    attendance = pd.DataFrame(columns = col_names)    
    while True:
        _ , im =cam.read()
        gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        faces=faceCascade.detectMultiScale(gray, 1.2,5)    
        for(x,y,w,h) in faces:
            cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
            Id, conf = recognizer.predict(gray[y:y+h,x:x+w])                                   
            if(conf < 50):
                ts = time.time()      
                date = dt.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                timeStamp = dt.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                aa=df.loc[df['Id'] == Id]['Name'].values
                tt=str(Id)+"-"+aa
                attendance.loc[len(attendance)] = [Id,aa,date,timeStamp]
                
            else:
                Id='Unknown'                
                tt=str(Id)  
            if(conf > 75):
                noOfFile=len(os.listdir("ImagesUnknown"))+1
                cv2.imwrite("ImagesUnknown/Image"+str(noOfFile) + ".jpg", im[y:y+h,x:x+w])            
            cv2.putText(im,str(tt),(x,y+h), font, 1,(255,255,255),2) 
                   
        attendance=attendance.drop_duplicates(subset=['Id'],keep='first')
        cv2.putText(im,"press q to close and save",(20,20), font, 1,(255,255,255),2)    
        cv2.imshow('im',im) 
        if (cv2.waitKey(1)==ord('q')):
            break
    ts = time.time()      
    date = dt.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    timeStamp = dt.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    Hour,Minute,Second=timeStamp.split(":")
    fileName="Attendance/Attendance_"+date+"_"+Hour+"-"+Minute+"-"+Second+".csv"
    attendance.to_csv(fileName,index=False)
    cam.release()
    cv2.destroyAllWindows()
    res=attendance
    res = "Attendance Taken"
    message.configure(text= res)
    tk.messagebox.showinfo('Completed','Congratulations ! Your attendance has been marked successfully for the day!!')
    
def quit_window():
   MsgBox = tk.messagebox.askquestion ('Exit Application','Are you sure you want to exit',icon = 'warning')
   if MsgBox == 'yes':
       tk.messagebox.showinfo("Greetings", "Thank You very much for using our software. Have a nice day ahead!!")
       root.destroy()


#------------------------------------------------------------------------------------------------------------------------------------#

def back(frm):
    frm.destroy()
    welcomeAdmin()    

#------------------------------------------------------------------------------------------------------------------------------------#


def reset(e1,e2,e3=None,e4=None):
    u=e1.get()
    p=e2.get()
    e1.delete(0,len(u))
    e2.delete(0,len(p))
    
    if(e3!=None and e4!=None):
        e=e3.get()
        m=e4.get()
        e3.delete(0,len(e))
        e4.delete(0,len(m))
#------------------------------------------------------------------------------------------------------------------------------------#
def login(frm,e1,e2):
    u=e1.get()
    p=e2.get()
    if(len(u)==0 or len(p)==0):
        msg.showwarning('Validation Problem','Please fill all fields')
    else:
        if(u=='admin' and p=='admin'):
            msg.showinfo('Login','Welcome Admin')
            frm.destroy()
            welcomeAdmin()
        else:
            msg.showerror('Login Failed','Invalid username or password')        
 #------------------------------------------------------------------------------------------------------------------------------------#           
def logout(frm):
    frm.destroy()
    home()

#------------------------------------------------------------------------------------------------------------------------------------#

home()
root.mainloop()