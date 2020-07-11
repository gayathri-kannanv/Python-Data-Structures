#!/usr/bin/env python
# coding: utf-8

# In[2]:


def bubbsort(list1):
    n=len(list1)-1
    for i in range(n):
        for j in range(n-i):
            if(list1[j]>list1[j+1]):
                list1[j+1], list1[j]=list1[j],list1[j+1]
                
    return list1

list1= list(map(int, input("Enter a list: ").split()))
bubbsort(list1)


# In[ ]:




