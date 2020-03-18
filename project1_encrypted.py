#!/usr/bin/env python
# coding: utf-8

# In[9]:


alphabets = 'abcdefghijklmnopqrstuvwxyz '
key = 4
newmsg = ''
message = input('enter the messsge ')
for charater in message:
    position = int(alphabets.find(charater))
    newpos = int((position + key)%26)
    newchar =alphabets[newpos]
#     print("encrypted new char is" ,newchar)
    newmsg +=newchar            
print("encrypted message:" ,newmsg)           
                


# In[ ]:




