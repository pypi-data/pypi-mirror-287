'''
Test Module: test_stack.py
Test Module Name: test_stack
Author: A K M Aminul Islam
Author Email: aminul71bd@gmail.com
Last Modified: Friday July 19 2024 10:30 PM
Version:1.0.0
Python Version:3.12.4
'''

version="1.0.0"


import unittest
import os
from pcds import stack as stk


class TestStack(unittest.TestCase):

    # testing the constructor function
    def test___init__(self):
        s1=stk.Stack()
        s2=stk.Stack()
        self.assertIsInstance(s1,stk.Stack)
        self.assertIsInstance(s2,stk.Stack)



    # testing push(), __str__(), __len__(), getSize() functions   
    def test_push(self):
        s1=stk.Stack()        
        s1.push(10)
        s1.push(14.78)
        s1.push('hello')
        s1.push('abc')
        s1.push(True)
        s1.push(False)
        s1.push(None)
        s1.push([4,1,8,9.5,('xy','ab','mn','pr',{1:'a',2:'b',3:{'name':'ali'}})])
        s="<Stack[size=8] Bottom:(10, 14.78, 'hello', 'abc', True, False, None, [4, 1, 8, 9.5, ('xy', 'ab', 'mn', 'pr', {1: 'a', 2: 'b', 3: {'name': 'ali'}})]):Top>"
        self.assertEqual(s,str(s1))
        self.assertEqual(8,len(s1))
        self.assertEqual(8,s1.getSize())

        s2=stk.Stack()
        s2.push(-100)
        s2.push(-0.00145)
        s2.push('john')
        s2.push('bob')
        s2.push(True)        
        s="<Stack[size=5] Bottom:(-100, -0.00145, 'john', 'bob', True):Top>"
        self.assertEqual(s,str(s2))
        self.assertEqual(5,len(s2))
        self.assertEqual(5,s2.getSize())



    # testing __len__(), pop(), __repr__(), getSize() functions
    def test_pop(self):
        s2=stk.Stack()
        s2.push(-100)
        s2.push(-0.00145)
        s2.push('john')
        s2.push('bob')
        s2.push(True)
        self.assertEqual(5,len(s2))
        self.assertEqual(True,s2.pop())
        s="<Stack[size=4] Bottom:(-100, -0.00145, 'john', 'bob'):Top>"
        self.assertEqual(s,repr(s2))
        self.assertEqual(4,len(s2))
        self.assertEqual('bob',s2.pop())
        self.assertEqual('john',s2.pop())
        self.assertEqual(-0.00145,s2.pop())
        s="<Stack[size=1] Bottom:(-100):Top>"
        self.assertEqual(s,repr(s2))
        self.assertEqual(-100,s2.pop())
        self.assertEqual(0,len(s2))
        self.assertEqual(0,s2.getSize())
        self.assertEqual(None,s2.pop())
        self.assertEqual(None,s2.pop())



    # testing clear() function
    def test_clear(self):
        s2=stk.Stack()
        s2.push(-100)
        s2.push(-0.00145)
        s2.push('john')
        s2.push('bob')
        s2.push(True)
        self.assertEqual(5,len(s2))
        s2.clear()
        self.assertEqual(0,len(s2))



    # testing setFileAddress(self, directory=datadir, filename="stack", enc=True)
    # and getFileAddress() functions. It creates a blank data file.
    def test_setFileAddress(self):
        s2=stk.Stack()
        self.assertEqual(None,s2.getFileAddress())
        filedir=os.path.expanduser('~')+os.sep+"pcds_data"
        if os.path.isdir(filedir):
            s2.setFileAddress()
            s=os.path.expanduser('~')+os.sep+"pcds_data"+os.sep+"stack.pcds"
            if os.path.isfile(s):            
                self.assertEqual(s,s2.getFileAddress())
        filedir="D:"+os.sep+"TEMP"
        if os.path.isdir(filedir):
            s2.setFileAddress(directory=filedir,filename="mystack")
            s=filedir+os.sep+"pcds_data"+os.sep+"mystack.pcds"
            if os.path.isfile(s):            
                self.assertEqual(s,s2.getFileAddress())
        


    # testing isFilePreserved() and setFilePreserve() methods
    def test_setFilePreserved(self):
        s2=stk.Stack()
        self.assertEqual(True,s2.isFilePreserved())
        s2.setFilePreserve(False)
        self.assertEqual(False,s2.isFilePreserved())
        s2.setFilePreserve(True)
        self.assertEqual(True,s2.isFilePreserved())
        


    # testing removeDataFile() method
    # before removing data file, file preserve parameter must be set to False
    def test_removeDataFile(self):
        s2=stk.Stack() 
        filedir=os.path.expanduser('~')+os.sep+"pcds_data"
        filename="stack"
        fileaddr=filedir+os.sep+filename+".pcds"
        s2.setFileAddress()
        if os.path.exists(fileaddr) and os.path.isfile(fileaddr):
            s2.setFilePreserve(False)
            self.assertTrue(s2.removeDataFile())
        filedir="D:"+os.sep+"TEMP"+os.sep+"pcds_data"        
        filename="mystack"
        fileaddr=filedir+os.sep+filename+".pcds"
        s2.setFileAddress(filedir,filename)
        if os.path.exists(fileaddr) and os.path.isfile(fileaddr):
            s2.setFilePreserve(False)
            self.assertTrue(s2.removeDataFile())



    # testing save(self, directory=datadir, filename="stack", enc=True) method
    def test_save(self):
        s1=stk.Stack()        
        s1.push(10)
        s1.push(14.78)
        s1.push('hello')
        s1.push('abc')
        s1.push(True)
        s1.push(False)
        s1.push(None)
        s1.push([4,1,8,9.5,('xy','ab','mn','pr',{1:'a',2:'b',3:{'name':'ali'}})])
        s="<Stack[size=8] Bottom:(10, 14.78, 'hello', 'abc', True, False, None, [4, 1, 8, 9.5, ('xy', 'ab', 'mn', 'pr', {1: 'a', 2: 'b', 3: {'name': 'ali'}})]):Top>"
        self.assertEqual(s,str(s1))        #
        self.assertTrue(s1.save())
        self.assertTrue(s1.save(filename="stack2",enc=False))



    # testing loadDataFromFile(self, fileaddr=datadir+os.sep+"stack.pcds")
    def test_loadDataFromFile(self):
        s1=stk.Stack()
        s2=stk.Stack()
        self.test_save()
        fileaddr=os.path.expanduser('~')+os.sep+"pcds_data"+os.sep+"stack.pcds"
        self.assertEqual(0,len(s1))
        self.assertTrue(s1.loadDataFromFile(fileaddr))
        self.assertEqual(8,len(s1))
        fileaddr=os.path.expanduser('~')+os.sep+"pcds_data"+os.sep+"stack2.pcds"
        self.assertEqual(0,len(s2))
        self.assertTrue(s2.loadDataFromFile(fileaddr))
        self.assertEqual(8,len(s2))





# running main() of unittest from this module
if __name__=='__main__':
	unittest.main()


