#!/usr/bin/env python
# coding: utf-8

# In[1]:


example=[{
        "question": "The variable mylist is a Python list. Choose which code snippet will append the item 3 to mylist.",
        "type": "multiple_choice",
        "answers": [
            {
                "code": "mylist+=3",
                "correct": False
            },
            {
                "code": "mylist+=[3]",
                "correct": True
            },
            {
                "code": "mylist+={3}",
                "correct": False
            }
        ]
    }]


# In[2]:


from jupyterquiz import display_quiz
display_quiz(example)


# In[ ]:




