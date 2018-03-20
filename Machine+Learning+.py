
# coding: utf-8

# In[1]:


print 'hello world'


# In[2]:


a=raw_input('whats your name')


# In[3]:


print 'That\'s all you have to do in Python?'


# In[4]:


print a


# In[5]:


x = 6
print x


# In[6]:


print type(x), type(a)


# In[7]:


b = 'Welcome to the course!'
print b


# In[8]:


print a + b


# In[9]:


c = a + ' ' + b
print c


# In[10]:


print x*2, x**2


# ## Flow of control
# 
# 

# In[11]:


#Conditions
len("") > 0


# In[12]:


len("Hello") > 0


# In[13]:


#if else
if (4 > 5):
    print 4
else:
    print 5


# In[15]:


#FizzBuzz
n = int(raw_input())
if n % 3 == 0 and n % 5 == 0:
    print 'FizzBuzz'
elif n % 3 == 0:
    print 'Fizz'
elif n % 5 == 0:
    print 'Buzz'
    
    


# In[16]:


#for loop
for x in range(1, 5):
    print x**2

