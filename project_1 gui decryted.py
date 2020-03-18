#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:





# In[27]:


from tkinter import *
from tkinter import messagebox
top = Tk()

L1 = Label(top,text='user name')
L1.grid(column = 0,row = 0)
e1 = Entry(top,bd = 5)
e1.grid(column = 1,row = 0)
e2 = Entry(top,bd = 5)
e2.grid(column = 2,row = 0)
alphabets = 'abcdefghijklmnopqrstuvwxyz '
key = 4
newmsg = ''

def submit():
    messagebox.showinfo("mes",e1.get() +  "-your data")
    global newmsg
    for charater in e1.get():
        position = int(alphabets.find(charater))
        newpos = int((position - key)%27)
        newchar =alphabets[newpos]
#     print("encrypted new char is" ,newchar)
        newmsg +=newchar
    print(newmsg)
    e2.insert(0,newmsg)
    
    

bt1 = Button(top,text = "praveen",fg = "red",command = submit)
bt1.grid(column = 1,row = 1)
top.mainloop()

