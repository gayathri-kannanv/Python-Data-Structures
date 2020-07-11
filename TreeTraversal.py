#!/usr/bin/env python
# coding: utf-8

# In[11]:


class Node:
    def  __init__(self, val):
        self.leftchild=None
        self.rightchild=None
        self.nodedata=val
        
root= Node(4)
root.leftchild= Node(3)
root.rightchild= Node(5)
root.leftchild.leftchild= Node(6)
root.leftchild.rightchild= Node(7)
root.rightchild.leftchild= Node(8)


# In[12]:


def inorder(root):
    if root:
        inorder(root.leftchild)
        print(root.nodedata)
        inorder(root.rightchild)
inorder(root)


# In[13]:


def preorder(root):
    if root:
        print(root.nodedata)
        preorder(root.leftchild)
        preorder(root.rightchild)
        
preorder(root)


# In[14]:


def postorder(root):
    if root:
        
        preorder(root.leftchild)
        preorder(root.rightchild)
        print(root.nodedata)
        
postorder(root)


# In[ ]:




