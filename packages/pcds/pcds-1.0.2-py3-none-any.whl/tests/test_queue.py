'''
Test Module: test_queue.py
Test Module Name: test_queue
Author: A K M Aminul Islam
Author Email: aminul71bd@gmail.com
Last Modified: Friday July 19 2024 10:30 PM
Version:1.0.0
Python Version:3.12.4
'''

version="1.0.0"


import unittest
import os
from pcds import queue as q


class TestQueue(unittest.TestCase):
    # creating queue instances
    q1=q.Queue()
    q2=q.Queue(5)
    q3=q.Queue(maxsize=10)
    q4=q.Queue(maxsize=0)

    # testing the constructor function
    def test___init__(self):        
        self.assertIsInstance(self.q1,q.Queue)
        self.assertIsInstance(self.q2,q.Queue)
        self.assertIsInstance(self.q3,q.Queue)
        self.assertIsInstance(self.q4,q.Queue)


    # testing the enQueue(), __str__()    
    def test_enQueue(self):
        self.q1.enQueue(10)
        self.q1.enQueue(14.78)
        self.q1.enQueue('hello')
        self.q1.enQueue('abc')
        self.q1.enQueue(True)
        self.q1.enQueue(False)
        self.q1.enQueue(None)
        s="<Queue [7/100], Head:(10, 14.78, 'hello', 'abc', True, False, None):Tail>"
        self.assertEqual(s,str(self.q1))

        # Queue of maxsize = 5
        self.q2.enQueue(10)
        self.q2.enQueue(14.78)
        self.q2.enQueue('hello')
        self.q2.enQueue('abc')
        self.q2.enQueue(True)        
        s="<Queue [5/5], Head:(10, 14.78, 'hello', 'abc', True):Tail>"
        self.assertEqual(s,str(self.q2))
        
        self.assertEqual(10,self.q2.enQueue(False))
        s="<Queue [5/5], Head:(14.78, 'hello', 'abc', True, False):Tail>"
        self.assertEqual(s,str(self.q2))

        self.assertEqual(14.78,self.q2.enQueue(None))
        s="<Queue [5/5], Head:('hello', 'abc', True, False, None):Tail>"
        self.assertEqual(s,str(self.q2))



    # testing the deQueue(), __str__()
    def test_deQueue(self):
        self.q1=q.Queue()
        self.q2=q.Queue(5)
        self.test_enQueue()
        self.assertEqual(10,self.q1.deQueue())
        self.assertEqual(14.78,self.q1.deQueue())
        self.assertEqual('hello',self.q1.deQueue())
        s="<Queue [4/100], Head:('abc', True, False, None):Tail>"
        self.assertEqual(s,str(self.q1))

        self.assertEqual('abc',self.q1.deQueue())
        self.assertEqual(True,self.q1.deQueue())
        self.assertEqual(False,self.q1.deQueue())
        s="<Queue [1/100], Head:(None):Tail>"
        self.assertEqual(s,str(self.q1))

        self.assertEqual(None,self.q1.deQueue())
        s="<Queue [0/100], Head:():Tail>"
        self.assertEqual(s,str(self.q1))

        self.assertEqual(None,self.q1.deQueue())
        s="<Queue [0/100], Head:():Tail>"
        self.assertEqual(s,str(self.q1))

        self.assertEqual(None,self.q1.deQueue())
        s="<Queue [0/100], Head:():Tail>"
        self.assertEqual(s,str(self.q1))

        self.assertEqual('hello',self.q2.deQueue())
        s="<Queue [4/5], Head:('abc', True, False, None):Tail>"
        self.assertEqual(s,str(self.q2))

        self.assertEqual('abc',self.q2.deQueue())
        s="<Queue [3/5], Head:(True, False, None):Tail>"
        self.assertEqual(s,str(self.q2))



    # testing getMaxSize(), changeMaxSize() methods
    def test_changeMaxSize(self):
        self.assertEqual(None,self.q4.getMaxSize())
        self.q4=q.Queue(5)
        self.assertEqual(5,self.q4.getMaxSize())
        self.q4.enQueue(15)
        self.q4.enQueue('hi')
        self.q4.enQueue([1,2,3,'hello',(4,7,8)])
        self.q4.enQueue({1:'ali',2:'khan',3:'haque'})
        s="<Queue [4/5], Head:(15, 'hi', [1, 2, 3, 'hello', (4, 7, 8)], {1: 'ali', 2: 'khan', 3: 'haque'}):Tail>"
        self.assertEqual(s,str(self.q4))



    # testing getSize(), __len__() method
    def test_getSize(self):
        self.q1=q.Queue()
        self.q2=q.Queue(5)
        self.test_enQueue()        
        self.assertEqual(7,self.q1.getSize())
        self.assertEqual(5,self.q2.getSize())
        self.assertEqual(7,len(self.q1))
        self.assertEqual(5,len(self.q2))



    # testing setFileAddress(self, directory=datadir, filename="queue", enc=True) 
    # and getFileAddress() methods
    def test_setFileAddress(self):
        q1=q.Queue()        
        q1.setFileAddress()
        s=os.path.expanduser('~')+os.sep+"pcds_data"+os.sep+"queue.pcds"
        self.assertEqual(s,q1.getFileAddress())
        q1.setFileAddress(filename="queue2")
        s=os.path.expanduser('~')+os.sep+"pcds_data"+os.sep+"queue2.pcds"
        self.assertEqual(s,q1.getFileAddress())



    # testing isFilePreserved() and setFilePreserve() methods
    def test_setFilePreserved(self):
        q1=q.Queue()
        q2=q.Queue(0)
        self.assertEqual(True,q1.isFilePreserved())
        self.assertEqual(None,q2.isFilePreserved())
        q1.setFilePreserve(False)
        self.assertEqual(False,q1.isFilePreserved())
        


    # testing clear() method
    def test_clear(self):
        self.q1=q.Queue()
        self.q2=q.Queue(5)
        self.test_enQueue()        
        self.assertEqual(7,self.q1.getSize())
        self.assertEqual(5,self.q2.getSize())
        self.q1.clear()
        self.assertEqual(0,self.q1.getSize())
        self.assertEqual(100,self.q1.getMaxSize())
        self.q2.clear()
        self.assertEqual(0,self.q2.getSize())
        self.assertEqual(5,self.q2.getMaxSize())



    # testing removeDataFile() method
    # before removing data file, file preserve parameter must be set to False
    def test_removeDataFile(self):
        q1=q.Queue()
        directory=os.path.expanduser('~')+os.sep+"data"+os.sep+"pcds_data"
        q1.setFileAddress(directory,"myqueue")
        fileaddr=os.path.expanduser('~')+os.sep+"data"+os.sep+"pcds_data"+os.sep+"myqueue.pcds"
        self.assertEqual(fileaddr,q1.getFileAddress())
        q1.setFilePreserve(False)
        if os.path.exists(fileaddr) and os.path.isfile(fileaddr):
            self.assertTrue(q1.removeDataFile())



    # testing data file I/O operations
    # testing save() method
    def test_save(self):
        q1=q.Queue()        
        q1.enQueue(10)
        q1.enQueue([1,2,3,(4,7,9)])
        q1.enQueue('hello')
        q1.enQueue('world')
        q1.enQueue({1:10,2:15,3:[40,50]})
        q1.enQueue(14.78)
        q1.enQueue(True)
        q1.enQueue(False)
        q1.enQueue(None)
        self.assertEqual(9,len(q1))
        self.assertTrue(q1.save())
        dirstr=os.path.expanduser('~')+os.sep+"pcds_data"
        self.assertTrue(q1.save(directory=dirstr,filename="queue2",enc=False))
    


    # testing loadDataFromFile() method
    def test_loadDataFromFile(self):
        q1=q.Queue()
        self.assertEqual(0,len(q1))
        self.assertTrue(q1.loadDataFromFile())
        self.assertEqual(9,len(q1))
        q1.clear()
        fileaddr=os.path.expanduser('~')+os.sep+"pcds_data"+os.sep+"queue2.pcds"
        self.assertTrue(q1.loadDataFromFile(fileaddr))
        self.assertEqual(9,len(q1))



# running the main() of unittest
if __name__=='__main__':
	unittest.main()













