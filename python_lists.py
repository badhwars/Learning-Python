#!/usr/bin/env python
# coding: utf-8

# In[1]:


print ('Hello World')


# In[8]:


a='474'

print(a+'22')


# In[9]:


py_list =['dave','sid','amanda']


# In[11]:


for i in range(3):
    print(py_list[i])


# #the following method appends to the list

# In[12]:


py_list.append("April Duck")


# In[13]:


print(py_list)


# In[14]:


#concatenate the list 
# use + sign or concat method
py_extend=['sami','ahmed','savvy']
py_ans=py_list+py_extend
print(py_ans)


# In[15]:


#inserting elements at any index in list

py_extend.insert(0,'McdOnalds')


# In[16]:


print(py_extend)


# In[18]:


#delete elements by index or by value

del py_extend[0]
print (py_extend)


# In[19]:


py_extend.remove('savvy')
print(py_extend)


# In[23]:


# slicing 
squares=['0','1','4','9','16','25','36','49']

squares[0:3]


# In[22]:


print(squares)


# In[25]:


# get the last element in the list 
squares[-1]
# print entire list
squares[:]


# In[26]:


squares[-1]


# In[27]:


print("ag")
print("dsjsh")


# In[29]:


print (squares)


# In[30]:


del squares[-2:]


# In[32]:


print(squares)


# In[33]:


for value in squares:
    print("element", value)


# In[ ]:




