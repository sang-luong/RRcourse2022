#!/usr/bin/env python
# coding: utf-8

# In[1]:


def convert(f, target = 'c'):
    if target == 'c':
        return (f-32)/1.8
    elif tarhet == 'k':
        return ((f-32)/1.8)+273.15
    else:
        raise Exception('wrong target')


# In[15]:


import unittest
import sys


# In[21]:


class Testconvert(unittest.TestCase):
    def test_convert_Celsius(self):
        self.assertEqual(convert(50,'c'),10.0)
    def test_convert_Celsius(self):
        self.assertAlmostEqual(convert(70,'c'),21.111111111)
    def test_convert_Celsius(self):
        self.assertAlmostEqual(convert(90,'c'),32.222222222222)
if __name__ == '__main__':
    unittest.main()


# In[ ]:




