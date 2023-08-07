from tkinter import *
import smtplib, ssl

top = Tk()
top.geometry('500x500')

def send():
    port = 465  
    smtp_server = "smtp.gmail.com"
    sender_email = t1.get()  
    receiver_email = t2.get()
    subject = t3.get
    password = input("Type your password and press enter: ")
    message = t4.get()

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email,subject,message)


l1=Label(top,text="From : ")
l1.grid(row=0,column=0)

t1=Text(top,width=20,height=1)
t1.grid(row=0,column=1)

l2=Label(top,text="To : ")
l2.grid(row=1,column=0)

t2=Text(top,width=20,height=2)
t2.grid(row=1,column=1)

l3=Label(top,text="Subject : ")
l3.grid(row=2,column=0)

t3=Text(top,width=20,height=1)
t3.grid(row=2,column=1)

l4=Label(top,text="Msg : ")
l4.grid(row=3,column=0)

t4=Text(top,width=20,height=5)
t4.grid(row=3,column=1)

l5=Label(top,text="Attachment : ")
l5.grid(row=4,column=0)

t5=Text(top,width=10,height=1)
t5.grid(row=4,column=1)

b1=Button(top,text="Send",command=send)
b1.grid(row=5,column=1)




top.mainloop()
