#!/usr/bin/env python
# coding: utf-8

# In[1]:


a = [1, 10, 2, 9]
m = sorted(a)[len(a) // 2]
print(sum(abs(v - m) for v in a))


# In[ ]:




