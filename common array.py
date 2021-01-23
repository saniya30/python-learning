#!/usr/bin/env python
# coding: utf-8

# In[15]:


def findCommon(ar1, ar2, ar3):
    k = 0
    result = []
    final_result = []
    for item1 in ar1:
        for item2 in ar2:
            if item1 == item2:
                result.insert(k,item1)
                k = k + 1
                break
      
    k = 0 
    for item3 in ar3:
        for item4 in result:
            if item3 == item4:
                final_result.insert(k,item3)
                k = k + 1
                break
                
    print('final_result')
    print(final_result)
    


# In[17]:


ar1 = [2,3,4]
ar2 = [2,3,4,6,8,7]
ar3 = [4,6,7,2,3]
findCommon(ar1, ar2, ar3)


# In[ ]:





# In[ ]:




