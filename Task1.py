#!/usr/bin/env python
# coding: utf-8

# In[1]:


from collections import deque
lst = '12345'
step = 4
arr = deque(lst)
res = list(arr[0])
arr.rotate(-(step-1))
while arr[0] != lst[0]:
    res.append(arr[0])
    arr.rotate(-(step-1))
    print(res)


# In[ ]:




