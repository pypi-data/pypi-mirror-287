'''
Test Module: test_linkedlist.py
Test Module Name: test_linkedlist
Author: A K M Aminul Islam
Author Email: aminul71bd@gmail.com
Last Modified: Friday July 19 2024 10:30 PM
Version:1.0.0
Python Version:3.12.4
'''

version="1.0.0"


import unittest
import os
from pcds import linkedlist as lnkl



# testing Node class
class TestNode(unittest.TestCase):
    # testing the constructor of Node class
    # Node constructor requires data and index
    def test___init__(self):
        self.assertIsNotNone(lnkl.Node())
        self.assertIsNotNone(lnkl.Node(index=0))
        self.assertIsNotNone(lnkl.Node(data=10,index=0))
        n1=lnkl.Node(100,4)
        self.assertEqual(100,n1.getData())
        self.assertEqual(4,n1.getIndex())
        self.assertEqual(None,n1.next)        


    # testing setData(), getData() method
    def test_setData(self):
        n1=lnkl.Node(index=0)
        n1.setData('hello')
        self.assertEqual('hello',n1.getData())


    # testing setIndex(), getIndex() method
    def test_setIndex(self):
        n1=lnkl.Node()
        n1.setIndex(5)
        self.assertEqual(5,n1.getIndex())
        self.assertEqual(None,n1.setIndex(5.5))


    # testing __str__(), __repr__() method
    def test_str_repr(self):
        n1=lnkl.Node('hello world',2)
        s='<Node: hello world at index 2>'
        self.assertEqual(s,str(n1))
        self.assertEqual(s,repr(n1))







# testing LinkedList class
class TestLinkedList(unittest.TestCase):
    # testing the constructor of LinkedList class
    # LinkedList constructor requires only a name
    def test___init__(self):
        ll=lnkl.LinkedList()
        s='<LNKList[LinkedList]: size=0, Data=()>'
        self.assertEqual(s,str(ll))
        myll=lnkl.LinkedList('mylinkedlist')
        s='<mylinkedlist[LinkedList]: size=0, Data=()>'
        self.assertEqual(s,str(myll))
        self.assertEqual('<Head Node at index -1>',str(myll.getHead()))
        self.assertEqual('mylinkedlist',myll.getName())


    # testing getCurrentIndex() method
    def test_getCurrentIndex(self):
        myll=lnkl.LinkedList('mylinkedlist')
        self.assertEqual(-1,myll.getCurrentIndex())
        myll.append("hello")
        myll.append(12.56)
        self.assertEqual(1,myll.getCurrentIndex())


    # testing tell() method which is as same as getCurrentIndex() method 
    def test_tell(self):
        myll=lnkl.LinkedList('mylinkedlist')
        self.assertEqual(-1,myll.tell())
        myll.append("hello")
        myll.append(12.56)
        self.assertEqual(1,myll.tell())




    # testing getCurrentNode() method 
    def test_getCurrentNode(self):
        myll=lnkl.LinkedList('mylinkedlist')
        self.assertEqual('<Head Node at index -1>',str(myll.getCurrentNode()))
        myll.append("hello")
        myll.append(12.56)
        self.assertEqual('<Node: 12.56 at index 1>',str(myll.getCurrentNode()))




    # testing getCurrentData() method 
    def test_getCurrentData(self):
        myll=lnkl.LinkedList('mylinkedlist')
        self.assertEqual('mylinkedlist',myll.getCurrentData())
        myll.append("hello")
        myll.append(12.56)
        self.assertEqual(12.56,myll.getCurrentData())




    # testing getSize() method 
    def test_getSize(self):
        myll=lnkl.LinkedList('mylinkedlist')
        self.assertEqual(0,myll.getSize())
        myll.append("hello")
        myll.append(12.56)
        self.assertEqual(2,myll.getSize())



    # testing append() method
    def test_append(self):
        n1=lnkl.Node(10,2)
        myll=lnkl.LinkedList('mylinkedlist')
        self.assertIsNone(myll.append(n1))
        myll.append("hello")
        myll.append(12.56)
        self.assertEqual(2,myll.getSize())




    # testing addDataFromList() method
    def test_addDataFromList(self):
        myll=lnkl.LinkedList('mylinkedlist')
        l=[1,3,'hello',True,None,False,(7,8,9)]
        myll.addDataFromList(l)
        s="<mylinkedlist[LinkedList]: size=7, Data=(1, 3, 'hello', True, None, False, (7, 8, 9))>"
        self.assertEqual(s,str(myll))




    # testing addDataFromTuple() method
    def test_addDataFromTuple(self):
        myll=lnkl.LinkedList('mylinkedlist')
        t=(1,3,'hello',True,None,False,[7,8,9])
        myll.addDataFromTuple(t)
        s="<mylinkedlist[LinkedList]: size=7, Data=(1, 3, 'hello', True, None, False, [7, 8, 9])>"
        self.assertEqual(s,str(myll))




    # testing moveNext(), moveLast(), movePrev(), moveFirst(), moveToHead() methods
    def test_move(self):
        myll=lnkl.LinkedList('mylinkedlist')
        l=[1,3,'hello',True,None,False,(7,8,9)]
        myll.addDataFromList(l)
        self.assertEqual(6,myll.tell())
        self.assertEqual((7,8,9),myll.getCurrentData())
        myll.moveFirst()
        self.assertEqual(0,myll.tell())
        self.assertEqual(1,myll.getCurrentData())
        myll.moveNext()
        self.assertEqual(1,myll.tell())
        self.assertEqual(3,myll.getCurrentData())
        myll.moveNext()
        self.assertEqual(2,myll.tell())
        self.assertEqual('hello',myll.getCurrentData())
        myll.moveNext()
        self.assertEqual(True,myll.getCurrentData())
        myll.moveLast()
        self.assertEqual(6,myll.tell())
        self.assertEqual((7,8,9),myll.getCurrentData())
        myll.movePrev()
        self.assertEqual(5,myll.tell())
        self.assertEqual(False,myll.getCurrentData())
        myll.movePrev()
        self.assertEqual(4,myll.tell())
        self.assertEqual(None,myll.getCurrentData())
        myll.moveToHead()
        self.assertEqual(-1,myll.tell())
        self.assertEqual('mylinkedlist',myll.getCurrentData())




    # testing seek(offset,ref) method
    def test_seek(self): 
        myll=lnkl.LinkedList('mylinkedlist')
        l=[1,3,'hello',True,None,False,(7,8,9)]
        myll.addDataFromList(l)
        self.assertIsNone(myll.seek(2.5))
        self.assertIsNone(myll.seek('0'))
       
        myll.seek(0,0)
        self.assertEqual(0,myll.tell())
        self.assertEqual(1,myll.getCurrentData())
        myll.seek(1,0)
        self.assertEqual(1,myll.tell())
        self.assertEqual(3,myll.getCurrentData())
        myll.seek(1,1)
        self.assertEqual(2,myll.tell())
        self.assertEqual('hello',myll.getCurrentData())
        myll.seek(1,1)
        self.assertEqual(3,myll.tell())
        self.assertEqual(True,myll.getCurrentData())
        myll.seek(1,1)
        self.assertEqual(4,myll.tell())
        self.assertEqual(None,myll.getCurrentData())
        myll.seek(-1,1)
        self.assertEqual(3,myll.tell())
        self.assertEqual(True,myll.getCurrentData())
        myll.seek(0,2)
        self.assertEqual(6,myll.tell())
        self.assertEqual((7,8,9),myll.getCurrentData())
        myll.seek(-1,2)
        self.assertEqual(5,myll.tell())
        self.assertEqual(False,myll.getCurrentData())
        myll.seek(-2,2)
        self.assertEqual(4,myll.tell())
        self.assertEqual(None,myll.getCurrentData())
        # seek() cannot move to head
        myll.seek(-1,0)
        self.assertEqual(4,myll.tell())
        self.assertEqual(None,myll.getCurrentData())




    # testing getAllData() method
    def test_getAllData(self):
        myll=lnkl.LinkedList('mylinkedlist')
        l=[1,3,'hello',True,14.5,False,(7,8,9)]
        myll.addDataFromList(l)
        t=(1, 3, 'hello', True, 14.5, False, (7, 8, 9))
        self.assertEqual(t,myll.getAllData())





    # testing convert2dict() method
    def test_convert2dict(self):
        myll=lnkl.LinkedList('mylinkedlist')
        l=[1,3,'hello',True,14.5,False,(7,8,9)]
        myll.addDataFromList(l)
        d={'name':'mylinkedlist','class':'LinkedList','size':7,0:1,1:3,2:'hello',3:True,4:14.5,5:False,6:(7,8,9)}
        self.assertEqual(d,myll.convert2dict())




    # testing getNodeAt(self,index=0) method
    def test_getNodeAt(self):
        myll=lnkl.LinkedList('mylinkedlist')
        l=[1,3,'hello',True,14.5,False,(7,8,9)]
        myll.addDataFromList(l)        
        self.assertEqual('<Node: 1 at index 0>',str(myll.getNodeAt()))
        self.assertEqual('<Node: hello at index 2>',str(myll.getNodeAt(2)))




    # testing getDataAt(self,index=0) method
    def test_getDataAt(self):
        myll=lnkl.LinkedList('mylinkedlist')
        l=[1,3,'hello',True,14.5,False,(7,8,9)]
        myll.addDataFromList(l)        
        self.assertEqual(1,myll.getDataAt())
        self.assertEqual('hello',myll.getDataAt(2))




    # testing editDataAt(self,data,index=0) method
    def test_editDataAt(self):
        myll=lnkl.LinkedList('mylinkedlist')
        l=[1,3,'hello',True,14.5,False,(7,8,9)]
        myll.addDataFromList(l)
        myll.editDataAt(data=10,index=0)
        self.assertEqual(10,myll.getDataAt())
        myll.editDataAt('hello world',2)
        self.assertEqual('hello world',myll.getDataAt(2))




    # testing insertDataAt(self,data,index=0) method
    def test_insertDataAt(self):
        myll=lnkl.LinkedList('mylinkedlist')
        l=[1,3,'hello',True,14.5,False,(7,8,9)]
        myll.addDataFromList(l)
        # default insert index=0
        myll.insertDataAt(data=10);
        t=(10, 1, 3, 'hello', True, 14.5, False, (7, 8, 9))
        self.assertEqual(t,myll.getAllData())
        self.assertEqual(8,len(myll))

        myll.insertDataAt('world',4); 
        t=(10, 1, 3, 'hello', 'world', True, 14.5, False, (7, 8, 9))
        self.assertEqual(t,myll.getAllData())
        self.assertEqual(9,len(myll))

        myll.insertDataAt('end',9); 
        t=(10, 1, 3, 'hello', 'world', True, 14.5, False, (7, 8, 9), 'end')
        self.assertEqual(t,myll.getAllData())
        self.assertEqual(10,len(myll))




    # testing deleteDataAt(self,index=0) method
    def test_deleteDataAt(self):
        myll=lnkl.LinkedList('mylinkedlist')
        l=[1,3,'hello',True,14.5,False,(7,8,9)]
        myll.addDataFromList(l)
        # default index=0
        myll.deleteDataAt();
        t=(3, 'hello', True, 14.5, False, (7, 8, 9))
        self.assertEqual(t,myll.getAllData())
        self.assertEqual(6,len(myll))

        myll.deleteDataAt(4); 
        t=(3, 'hello', True, 14.5, (7, 8, 9))
        self.assertEqual(t,myll.getAllData())
        self.assertEqual(5,len(myll))

        myll.deleteDataAt(4); 
        t=(3, 'hello', True, 14.5)
        self.assertEqual(t,myll.getAllData())
        self.assertEqual(4,len(myll))




    # testing searchData(self, searchdata) method
    def test_searchData(self):
        myll=lnkl.LinkedList('mylinkedlist')
        l=[('jaon', 'john', 'ali', 'karim'), 10, 20, 30, 'hello', 'john', 'ali', 'karim ali', 100, 10, 20, 30, 40, True, False, None]
        myll.addDataFromList(l)        
        d={0: ('jaon', 'john', 'ali', 'karim'), 6: 'ali', 7: 'karim ali'}
        self.assertEqual(d,myll.searchData('ali'))




    # testing clear() method
    def test_clear(self):
        myll=lnkl.LinkedList('mylinkedlist')
        l=[('jaon', 'john', 'ali', 'karim'), 10, 20, 30, 'hello', 'john', 'ali', 'karim ali', 100, 10, 20, 30, 40, True, False, None]
        myll.addDataFromList(l)        
        self.assertEqual(16,myll.getSize())
        myll.clear()
        self.assertEqual(0,myll.getSize())




    
    # ----------------------- Data File related methods -----------------------
    #
    # testing setFilePreserve(self, preserve=True), isFilePreserved() methods
    def test_setFilePreserve(self):
        myll=lnkl.LinkedList('mylinkedlist')
        self.assertTrue(myll.isFilePreserved())
        myll.setFilePreserve(False)
        self.assertFalse(myll.isFilePreserved())




    # testing setFileAddress(self, directory=datadir, filename="linkedlist")
    # and getFileAddress() methods
    def test_setFileAddress(self):
        myll=lnkl.LinkedList('mylinkedlist')
        filedir=os.path.expanduser('~')+os.sep+"pcds_data"
        filename="linkedlist"
        fileaddr=filedir+os.sep+filename+".pcds"
        myll.setFileAddress(filedir,filename)
        self.assertEqual(fileaddr, myll.getFileAddress())
        filedir=os.path.expanduser('~')+os.sep+"pcds_data"
        filename="linkedlist2"
        fileaddr=filedir+os.sep+filename+".pcds"        
        myll.setFileAddress(filedir,filename)
        self.assertEqual(fileaddr, myll.getFileAddress())




    # testing save(self, directory=datadir, filename="linkedlist", enc=True) method
    def test_save(self):
        myll=lnkl.LinkedList('mylinkedlist')
        l=[('jaon', 'john', 'ali', 'karim'), 10, 20, 30, 'hello', 'john', 'ali', 'karim ali', 100, 10, 20, 30, 40, True, False, None]
        myll.addDataFromList(l)        
        self.assertEqual(16,myll.getSize())
        self.assertTrue(myll.save())
        # msg: Encrypted Data Saved Successfully into 'C:\Users\admin\pcds_data\linkedlist.pcds'
        self.assertTrue(myll.save(filename="linkedlist2",enc=False))
        # msg: Plain Data Saved Successfully into 'C:\Users\admin\pcds_data\linkedlist2.pcds'




    # testing loadDataFromFile(self, fileaddr=datadir+os.sep+"linkedlist.pcds") method
    def test_loadDataFromFile(self):
        self.test_save()
        myll=lnkl.LinkedList('mylinkedlist')
        self.assertEqual(0,myll.getSize())
        myll.loadDataFromFile()
        # msg: Data Loaded Successfully from the file: 'C:\Users\admin\pcds_data\linkedlist.pcds'
        self.assertEqual(16,myll.getSize())
        fileaddr=os.path.expanduser('~')+"\\pcds_data\\linkedlist2.pcds"
        myll.clear()
        self.assertEqual(0,myll.getSize())
        myll.loadDataFromFile(fileaddr)
        # msg: Data Loaded Successfully from the file: 'C:\Users\admin\pcds_data\linkedlist2.pcds'
        self.assertEqual(16,myll.getSize())




    # testing removeDataFile() method
    # before removing data file, file preserve parameter must be set to False
    def test_removeDataFile(self):
        myll=lnkl.LinkedList('mylinkedlist')
        filedir=os.path.expanduser('~')+os.sep+"pcds_data"
        filename="linkedlist"
        fileaddr=filedir+os.sep+filename+".pcds"
        myll.setFileAddress()
        if os.path.exists(fileaddr) and os.path.isfile(fileaddr):
            myll.setFilePreserve(False)
            self.assertTrue(myll.removeDataFile())
        filename="linkedlist2"
        fileaddr=filedir+os.sep+filename+".pcds"
        myll.setFileAddress()
        if os.path.exists(fileaddr) and os.path.isfile(fileaddr):
            myll.setFilePreserve(False)
            self.assertTrue(myll.removeDataFile())



if __name__ == '__main__':
    unittest.main()



