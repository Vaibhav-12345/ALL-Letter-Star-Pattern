#!/usr/bin/env python
# coding: utf-8

# In[4]:


n=int(input())
for i in range(0,n):
    for j in range(0,i+1):
        print("*",end="")
    print()    
    


# In[29]:


n=int(input())
for i in range(n,0,-1):
    for j in range(0,i):
        print("*",end="")
    print() 


# In[31]:


n=int(input())
for i in range(n,0,-1):
    for k in range(0,n-i):
        print(" ",end="")
    for j in range(0,i):
        print("*",end="")
    print() 


# In[16]:


n=int(input())
for i in range(0,n):
    for k in range(0,n-i):
        print(" ",end="")
    for j in range(0,i+1):
        print("*",end="")
    print()


# In[35]:


n=int(input())
for i in range(0,n):
    for k in range(0,n-i):
        print(" ",end="")
    for j in range(0,2*i+1):
        print("*",end="")
    print()


# In[18]:


n=int(input())
for i in range(n,0,-1):
    for k in range(0,n-i):
        print(" ",end="")
    for j in range(0,i*2-1):
        print("*",end=" ")
    print()


# In[21]:


n=int(input())
for i in range(n,0,-1):
    for k in range(0,n-i):
        print(" ",end="")
    for j in range(0,i):
        print("*",end=" ")
    print()


# In[33]:


n=int(input())
for i in range(0,n):
    for k in range(0,n-i):
        print(" ",end=" ")
    for j in range(1,2*i):
        print("*",end=" ")
    print()
for i in range(n,0,-1):
    for k in range(0,n-i):
        print(" ",end=" ")
    for j in range(1,2*i):
        print("*",end=" ")
    print()   


# In[49]:


for i in range(7):
    for j in range(5):
        if ((j==0 or j==4) and i!=0) or ((i==0 or i==3) and (j>0 and j<4)):
            print("*",end="")
        else:
            print(" ",end="")
    print()        
        


# In[5]:


for i in range(7):
    for j in range(5):
        if(j==0) or (j==4 and (i!=0 and i!=3 and i!=6)) or ((i==0 or i==3 or i==6)and j>0 and j<4):
            print("*",end="")
        else:
            print(" ",end="")
    print()        
            


# In[2]:


for i in range(7):
    for j in range(5):
        if (j==0 and (i!=0 and i!=6)) or ((i==0 or i==6) and (j>0)):
            print("*",end="")
        else:
            print(" ",end="")
    print()        


# In[10]:


for i in range(5):
    for j in range(4):
        if (j==0) or (j==3  and (i!=0 and i!=4 )) or ((i==0 or i==4) and (j>0 and j<3)):
            print("*",end="")
        else:
            print(" ",end="")
    print() 
print()    
        


# In[17]:


for i in range(5):
    for j in range(5):
        if (j==0) or ((i==0 or i==4 or i==2) and (j>0 and j<5)): 
            print("*",end="")
        else:
            print(" ",end="")
    print() 
print()


# In[18]:


for i in range(5):
    for j in range(5):
        if (j==0) or ((i==0 or i==2) and (j>0 and j<5)): 
            print("*",end="")
        else:
            print(" ",end="")
    print() 
print()


# In[44]:


for i in range(5):
    for j in range(5):
        if (j==0) or (j==1 and i!=1 and i!=2 and i!=3) or (j==2 and i!=1) or (j==3 and i!=1 and i!=3 and i!=4) or (j==4 and i!=1): 
            print("*",end="")
        else:
            print(" ",end="")
    print() 
print()


# In[62]:


for i in range(5):
    for j in range(4):
        if(j==0 or j==3 or i==2):
            print("*",end="")
        else:
            print(" ",end="")
    print()


# In[63]:


for i in range(4):
    for j in range(5):
        if(i==0 or j==2 or i==3):
            print("*",end="")
        else:
            print(" ",end="")
    print()


# In[27]:


for i in range(5):
    for j in range(6):
        if (j==1 and (i!=1 and i!=2)) or (j==2 and (i!=1 and i!=2 and i!=3)) or j==3 or i==0 and j>0 and j<6: 
            print(" *",end="")
        else:
            print("  ",end="")
    print() 
print()


# In[81]:


for i in range(7):
    for j in range(4):
        if j==0 or i+j==3 or i-j==3 : 
            print("* ",end="")
        else:
            print(" ",end="")
    print() 
print()


# In[95]:


for i in range(5):
    for j in range(4):
        if j==0 or i==4 : 
            print("* ",end="")
        else:
            print(" ",end="")
    print() 
print()


# In[159]:


for i in range(5):
    for j in range(5):
        if (j==0 or j==4 )or (i==1 and j==1) or (i==1 and j==3 ) or (i==2 and j==2): 
            print("* ",end="")
        else:
            print("  ",end="")
    print() 
print()


# In[163]:


for i in range(5):
    for j in range(5):
        if (j==0 or j==4 ) or i==j : 
            print("* ",end="")
        else:
            print("  ",end="")
    print() 
print()


# In[164]:


for i in range(5):
    for j in range(5):
        if (j==): 
            print("*",end="")
        else:
            print(" ",end="")
    print() 
print()


# In[13]:


for i in range(5):
    for j in range(5):
        if (j==0 or j==4 and i!=0 and i!=4) or (i==0 or i==4) and (j>0 and j<5): 
            print("*",end="")
        else:
            print(" ",end="")
    print() 
print()


# In[17]:


for i in range(5):
    for j in range(5):
        if j==0 or (j==4 and i!=3 and i!=4 )or i==0 or i==2 : 
            print("*",end="")
        else:
            print(" ",end="")
    print() 
print()


# In[24]:


for i in range(5):
    for j in range(5):
        if j==0 or (j==4 and i!=3) or i==0 or (i==2 and j!=1) or (i+j==5 and j!=1): 
            print("*",end="")
        else:
            print(" ",end="")
    print() 
print()


# In[37]:


for i in range(5):
    for j in range(5):
        if (j==0 and  i!=3) or (j==4 and i!=1) or i==0 or i==2 or i==4: 
            print(" *",end="")
        else:
            print("  ",end="")
    print() 
print()


# In[47]:


for i in range(5):
    for j in range(5):
        if (j==2 or i==0):
            print("*",end="")
        else:
            print(" ",end="")
    print()        


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[48]:


for i in range(4):
    for j in range(7):
        if (i==j or j+i==6):
            print("*",end="")
        else:
            print(" ",end="")
    print() 
print()    
for i in range(7):
    for j in range(5):
        if ((j==0 or j==4) and i!=0) or ((i==0 or i==3) and (j>0 and j<4)):
            print("*",end="")
        else:
            print(" ",end="")
    print()
print()    
for i in range(4):
    for j in range(5):
        if(i==0 or j==2 or i==3):
            print("*",end="")
        else:
            print(" ",end="")
    print()  
print(end="")    
for i in range(7):
    for j in range(5):
        if(j==0) or (j==4 and (i!=0 and i!=3 and i!=6)) or ((i==0 or i==3 or i==6)and j>0 and j<4):
            print("*",end="")
        else:
            print(" ",end="")
    print()
print()
for i in range(5):
    for j in range(4):
        if(j==0 or j==3 or i==2):
            print("*",end="")
        else:
            print(" ",end="")
    print() 
    
for i in range(6):
    for j in range(5):
        if((j==0 or j==4) and i!=0)  or (i==0 or i==2) and (j>0 and j<4):
                  print("*",end="")
        else:
            print(" ",end="")
    print() 
    
print()
for i in range(4):
    for j in range(7):
        if i==j or j+i==6:
             print("*",end="")
        else:
            print(" ",end="")
    print() 
    
print()

for i in range(5):
    for j in range(5):
        if j==0 or (j==4 and i!=3) or i==0 or (i==2 and j!=1) or (i+j==5 and j!=1): 
            print("*",end="")
        else:
            print(" ",end="")
    print() 
print()
for i in range(7):
    for j in range(5):
        if ((j==0 or j==4) and i!=0) or ((i==0 or i==3) and (j>0 and j<4)):
            print("*",end="")
        else:
            print(" ",end="")
    print()
print() 
for i in range(5):
    for j in range(6):
        if (j==1 and (i!=1 and i!=2)) or (j==2 and (i!=1 and i!=2 and i!=3)) or j==3 or i==0 and j>0 and j<6: 
            print("*",end="")
        else:
            print(" ",end="")
    print() 
print()
for i in range(5):
    for j in range(5):
        if (j==0 and  i!=3) or (j==4 and i!=1) or i==0 or i==2 or i==4: 
            print("*",end="")
        else:
            print(" ",end="")
    print() 
print()
for i in range(4):
    for j in range(5):
        if(i==0 or j==2 or i==3):
            print("*",end="")
        else:
            print(" ",end="")
    print()
for i in range(5):
    for j in range(5):
        if (j==0 or j==4 ) or i==j : 
            print("*",end="")
        else:
            print(" ",end="")
    print() 
print() 
for i in range(5):
    for j in range(5):
        if (j==0) or (j==1 and i!=1 and i!=2 and i!=3) or (j==2 and i!=1) or (j==3 and i!=1 and i!=3 and i!=4) or (j==4 and i!=1): 
            print("*",end="")
        else:
            print(" ",end="")
    print() 

for i in range(5):
    for j in range(4):
        if(j==0 or j==3 or i==2):
            print("*",end="")
        else:
            print(" ",end="")
    print() 
print()    


# In[108]:


for i in range(8):
    for j in range(9):
        if(j==0 and i!=0 and i!=4 and i!=4 and i!=5 and i!=6 and i!=7) or (j==8 and i!=0 and i!=4 and i!=4 and i!=5 and i!=6 and i!=7) or (i-j==3 or i+j==11) or (i==0 and j!=0 and j!=3 and j!=4 and j!=5 and j!=8 ) or (j-i==2 and j!=5 and j!=6 and i!=5 and i!=6 and i!=7) or (i+j==6 and j!=2 and j!=3 and j!=4 and i!=5 and i!=6 ):
            print(" *",end="")
        else:
            print("  ",end="")
    print()        


# In[118]:


for i in range(5):
    for j in range(5):
        if i==0 or i==4 or i+j==4:
            print("*",end="")
        else:
            print(" ",end="")
    print()        


# In[21]:


# ******
# *****
# ****
# ***
# *



# n=int(input())
# for i in range(0,n):
#     for k in range(i):
#         print("1",end="")
#     for j in range(i+1,0,-1):
#         print("*",end="")
#     print()
    
    
    


# In[119]:


for i in range(5):
    for j in range(4):
        if (j==0 and (i==0 or i==5):
            print("*",end="")
        else:
            print(" ",end="")
    print()


# In[ ]:





# In[ ]:





# In[ ]:




