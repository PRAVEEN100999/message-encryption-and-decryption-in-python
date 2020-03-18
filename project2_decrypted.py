#!/usr/bin/env python
# coding: utf-8

# In[6]:


alphabets = 'abcdefghijklmnopqrstuvwxyz '
key = 4
newmsg = ''
message = input('enter the encrypted message : ')
for charater in message:
    position = int(alphabets.find(charater))
    newpos = int((position - key)%27)
    newchar =alphabets[newpos]
#     print("encrypted new char is" ,newchar)
    newmsg +=newchar            
print("dencrypted message:" ,newmsg)    

