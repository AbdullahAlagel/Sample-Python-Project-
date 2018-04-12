from tkinter import *
from tkinter import ttk
from tkinter import messagebox
root=Tk()
root.title("Ticket Reservation")

root.configure(background ="#e1d8b2")
#Style
style=ttk.Style()
style.theme_use('classic')
style.configure('TLabel', background ="white")
style.configure('TButton', background ="#e1d8b2")
style.configure('TRadiobutton', background ="#e1d8b2")



#FullName Code Line 
ttk.Label(root, text="Full Name :").grid(row=0 ,column=0 , padx=10 , pady=10)
FullName=ttk.Entry(root, width=30 ,font=('Arial',16))
FullName.grid(row=0,column=1, columnspan=2 , pady=10)

#Gender Code Line 
ttk.Label(root,text="Gender").grid(row=1,column=0 )
Gender=StringVar()
ttk.Radiobutton(root,text="Male",variable=Gender, value="Male").grid(row=1,column=1)
ttk.Radiobutton(root,text="Famale", variable=Gender , value="Famale").grid(row=1,column=2)

#Comments Code Line 
ttk.Label(root, text="Comments",).grid(row=2 ,column=0 , padx=15,pady=15)
comments=Text(root, width=30, height=15, font=('Arial',16))
comments.grid(row=2 , column=1, columnspan=2)
#Button
buSubmit=ttk.Button(root,text='Submit')
buSubmit.grid(row=3 ,column=3)
buList=ttk.Button(root,text='List Res.')
buList.grid(row=3,column=2)


def BuSaveData():
    print("Full Name :{}".format(FullName.get()))
    print("Gender :{}".format(Gender.get()))
    print("Comments :{}".format(comments.get(1.0,'end')))
    FullName.delete(0,'end')
    comments.delete(1.0,'end')

def BuListData():
    #TODO SHOW ORDERS
    print("not implement yet")

buSubmit.config(command=BuSaveData)
buList.config(command=BuListData)

root.mainloop()
