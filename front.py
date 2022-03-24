from cProfile import label
from email import message
from encodings import utf_8
from fileinput import filename
from tkinter import *
import cv2

from PIL import Image
from matplotlib.pyplot import text
import stepic
import dc
import dc1
def stegnot(source,message,):
    im = Image.open(source)

#Encode some text into your Image file and save it in another file#
    sm = bytes(message,"utf_8")
    s = stepic.Steganographer(im)
    img = s.encode(sm)
    img.save("urname.png","PNG")


def full():
    face_cascade = cv2.CascadeClassifier(cv2.haarcascades+"haarcascade_frontalface_default.xml")
    source = Iname.get()
    img = cv2.imread(source,0)
    message = opname.get()
    dc.insertBLOB(message,source)
   
    
    faces = face_cascade.detectMultiScale(img,scaleFactor=1.05,minNeighbors=5)
    
   
    gauss = cv2.GaussianBlur(img,(151,151),100)
    gauss = cv2.cvtColor(gauss,cv2.COLOR_BGR2RGB)
    
  
  
    
    
    s = filename.get()
    urfile = cv2.imwrite(s,gauss)
    t1.delete("1.0",END)
    t1.insert(END,"Image has beeen ecrypted")

    stegnot(s,message)
def face():
    face_cascade = cv2.CascadeClassifier(cv2.haarcascades+"haarcascade_frontalface_default.xml")
    source = Iname.get()
    img = cv2.imread(source,1)
   
    
    faces = face_cascade.detectMultiScale(img,scaleFactor=1.05,minNeighbors=5)
    message = opname.get()
    dc.insertBLOB(message,source)
  
    for x1,y1,m,n in faces:
                
            top = (x1,y1)
            bott = (x1+m,y1+n)
            x,y = top[0],top[1]
            w,h = bott[0]-top[0],bott[1]-top[1]
            ROI = img[y:y+h,x:x+w]
                
            gauss = cv2.GaussianBlur(ROI,(151,151),100)
            img[y:y+h,x:x+w]=gauss
    
    s = filename.get() 
    cv2.imwrite(s,img)
    t1.delete("1.0",END)
    t1.insert(END,"Image has beeen ecrypted")
    stegnot(s,message)   

def aadhar():
    source = Iname.get()
    img = cv2.imread(source,1)
    wd,ht,ch = img.shape
    start = (10,1400)
    end_point = (1250,3000)
    x,y = start[0],start[1]
    w,h = end_point[0]-start[0],end_point[1]-start[1]
    ROI= img[y:y+h,x:x+w]
    gauss = cv2.GaussianBlur(ROI,(151,151),100)
    img[y:y+h,x:x+w]=gauss
   
    s= filename.get()
    message = opname.get()
    dc.insertBLOB(message,source)
    cv2.imwrite(s,img)
    cv2.waitKey(0)
    t1.delete("1.0",END)
    t1.insert(END,"Image has beeen ecrypted") 
    stegnot(s,message)  
def cbsc():
    source = Iname.get()

    img = cv2.imread(source,0)
    start = (10,200)
    end = (700,528)
    x,y = start[0],start[1]
    w,h = end[0]-start[0],end[1]-start[1]
    ROI= img[y:y+h,x:x+w]
    gauss = cv2.GaussianBlur(ROI,(151,151),100)
    
    img[y:y+h,x:x+w]=gauss
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    s = filename.get()
    message = opname.get()
    dc.insertBLOB(message,source)
    cv2.imwrite(s,img)
    t1.delete("1.0",END)
    t1.insert(END,"Image has beeen ecrypted") 
    stegnot(s,message)         
            
def check():
    s = Iid.get()
    passk = passkey.get()
    im2 = Image.open(s)
    stegoImage = stepic.decode(im2)
    if passk==stegoImage:
        dc1.readBlobData(passk)
        t2.delete("1.0",END)
        t2.insert(END,"Image has been decrypted")
    else:
        t2.delete("1.0",END)
        t2.insert(END,"Incorrect password re-enter")


    



window = Tk()
window.wm_title("Image encryption system")
l1 = Label(window,text="Imagepath")
l1.grid(row=1,column=0)

l2 = Label(window,text="Password")
l2.grid(row=2,column=0)

l3 = Label(window,text="Output file name")
l3.grid(row=3,column=0)
l4 = Label(window,text="Encryption")
l4.grid(row=0,column=1)
l5 = Label(window,text="Decryption")
l5.grid(row=5,column=1)
l6 = Label(window,text="Imagepath")
l6.grid(row=6,column=0)
l7=Label(window,text="Password")
l7.grid(row=7,column=0)
Iname = StringVar()
e1 = Entry(window,textvariable=Iname)
e1.grid(row=1,column=1)
b1 = Button(window,text="Blur",width=10,height=1,command=full)
b1.grid(row=0,column=2)
b2 = Button(window,text="Face",width=10,height=1,command=face)
b2.grid(row=1,column=2)
b3 = Button(window,text="Aadhar",width=10,height=1,command=aadhar)
b3.grid(row=2,column=2)
b4 = Button(window,text="Marksheets",width=10,height=1,command=cbsc)
b4.grid(row=3,column=2)
b5 = Button(window,text="Encrypt",width=10,height=1)
b5.grid(row=4,column=2)
opname = StringVar()
e2 = Entry(window,textvariable=opname)
e2.grid(row=2,column=1)
filename = StringVar()
e3 = Entry(window,textvariable=filename)
e3.grid(row=3,column=1)

t1 = Text(window,height=1,width=25)
t1.grid(row=4,column=1)
Iid = StringVar()
e4 = Entry(window,textvariable= Iid)
e4.grid(row=6,column=1)
passkey = StringVar()
e5 = Entry(window,textvariable=passkey)
e5.grid(row=7,column=1)
b4 = Button(window,text="Check",width=10,height=1,command=check)
b4.grid(row=6,column=2)
t2 = Text(window,width=25,height=1)
t2.grid(row=8,column=1)

window.mainloop()