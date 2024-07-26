'''
Test Module: test_dlinkedlist.py
Test Module Name: test_dlinkedlist
Author: A K M Aminul Islam
Author Email: aminul71bd@gmail.com
Last Modified: Saturday July 20 2024 8:30 PM
Version:1.0.0
Python Version:3.12.4
'''

version="1.0.0"


import unittest
import os
from pcds import dlinkedlist as dlnkl



# testing Node class
class TestNode(unittest.TestCase):
    # testing the constructor of Node class
    # Node constructor requires data and index
    def test___init__(self):
        self.assertIsNotNone(dlnkl.Node())
        self.assertIsNotNone(dlnkl.Node(index=0))
        self.assertIsNotNone(dlnkl.Node(data=10,index=0))
        n1=dlnkl.Node(100,4)
        self.assertEqual(100,n1.getData())
        self.assertEqual(4,n1.getIndex())
        self.assertEqual(None,n1.next) 
        self.assertEqual(None,n1.prev)       


    # testing setData(), getData() method
    def test_setData(self):
        n1=dlnkl.Node(index=0)
        n1.setData('hello')
        self.assertEqual('hello',n1.getData())


    # testing setIndex(), getIndex() method
    def test_setIndex(self):
        n1=dlnkl.Node()
        n1.setIndex(5)
        self.assertEqual(5,n1.getIndex())
        self.assertEqual(None,n1.setIndex(5.5))


    # testing __str__(), __repr__() method
    def test_str_repr(self):
        n1=dlnkl.Node('hello world',2)
        s='<Node: hello world at index 2>'
        self.assertEqual(s,str(n1))
        self.assertEqual(s,repr(n1))




# testing DLinkedList class
class TestDLinkedList(unittest.TestCase):
    # testing the constructor of LinkedList class
    # LinkedList constructor requires only a name
    def test___init__(self):
        dll=dlnkl.DLinkedList()
        s='<DLNKList[DLinkedList]: size=0, Data=()>'
        self.assertEqual(s,str(dll))
        dll2=dlnkl.DLinkedList('mydlinkedlist')
        s='<mydlinkedlist[DLinkedList]: size=0, Data=()>'
        self.assertEqual(s,str(dll2))
        self.assertEqual('<Head Node at index -1>',str(dll2.getHead()))
        self.assertEqual('mydlinkedlist',dll2.getName())


    # testing getCurrentIndex() method
    def test_getCurrentIndex(self):
        dll=dlnkl.DLinkedList('mydlinkedlist')
        self.assertEqual(-1,dll.getCurrentIndex())
        dll.append("hello")
        dll.append(12.56)
        self.assertEqual(1,dll.getCurrentIndex())


    # testing tell() method which is as same as getCurrentIndex() method 
    def test_tell(self):
        dll=dlnkl.DLinkedList('mydlinkedlist')
        self.assertEqual(-1,dll.tell())
        dll.append("hello")
        dll.append(12.56)
        self.assertEqual(1,dll.tell())




    # testing getCurrentNode() method 
    def test_getCurrentNode(self):
        dll=dlnkl.DLinkedList('mydlinkedlist')
        self.assertEqual('<Head Node at index -1>',str(dll.getCurrentNode()))
        dll.append("hello")
        dll.append(12.56)
        self.assertEqual('<Node: 12.56 at index 1>',str(dll.getCurrentNode()))




    # testing getCurrentData() method 
    def test_getCurrentData(self):
        dll=dlnkl.DLinkedList('mydlinkedlist')
        self.assertEqual('mydlinkedlist',dll.getCurrentData())
        dll.append("hello")
        dll.append(12.56)
        self.assertEqual(12.56,dll.getCurrentData())




    # testing getSize() method 
    def test_getSize(self):
        dll=dlnkl.DLinkedList('mydlinkedlist')
        self.assertEqual(0,dll.getSize())
        dll.append("hello")
        dll.append(12.56)
        self.assertEqual(2,dll.getSize())




    # testing append() method
    def test_append(self):
        n1=dlnkl.Node(10,2)
        dll=dlnkl.DLinkedList('mydlinkedlist')
        self.assertIsNone(dll.append(n1))
        dll.append("hello")
        dll.append(12.56)
        self.assertEqual(2,dll.getSize())




    # testing addDataFromList() method
    def test_addDataFromList(self):
        dll=dlnkl.DLinkedList('mydlinkedlist')
        l=[1,3,'hello',True,None,False,(7,8,9)]
        dll.addDataFromList(l)
        s="<mydlinkedlist[DLinkedList]: size=7, Data=(1, 3, 'hello', True, None, False, (7, 8, 9))>"
        self.assertEqual(s,str(dll))




    # testing addDataFromTuple() method
    def test_addDataFromTuple(self):
        dll=dlnkl.DLinkedList('mydlinkedlist')
        t=(1,3,'hello',True,None,False,[7,8,9])
        dll.addDataFromTuple(t)
        s="<mydlinkedlist[DLinkedList]: size=7, Data=(1, 3, 'hello', True, None, False, [7, 8, 9])>"
        self.assertEqual(s,str(dll))





    # testing moveNext(), moveLast(), movePrev(), moveFirst(), moveToHead() methods
    def test_move(self):
        dll=dlnkl.DLinkedList('mydlinkedlist')
        l=[1,3,'hello',True,None,False,(7,8,9)]
        dll.addDataFromList(l)
        self.assertEqual(6,dll.tell())
        self.assertEqual((7,8,9),dll.getCurrentData())
        dll.moveFirst()
        self.assertEqual(0,dll.tell())
        self.assertEqual(1,dll.getCurrentData())
        dll.moveNext()
        self.assertEqual(1,dll.tell())
        self.assertEqual(3,dll.getCurrentData())
        dll.moveNext()
        self.assertEqual(2,dll.tell())
        self.assertEqual('hello',dll.getCurrentData())
        dll.moveNext()
        self.assertEqual(True,dll.getCurrentData())
        dll.moveLast()
        self.assertEqual(6,dll.tell())
        self.assertEqual((7,8,9),dll.getCurrentData())
        dll.movePrev()
        self.assertEqual(5,dll.tell())
        self.assertEqual(False,dll.getCurrentData())
        dll.movePrev()
        self.assertEqual(4,dll.tell())
        self.assertEqual(None,dll.getCurrentData())
        dll.moveToHead()
        self.assertEqual(-1,dll.tell())
        self.assertEqual('mydlinkedlist',dll.getCurrentData())






    # testing seek(offset,ref) method
    def test_seek(self): 
        dll=dlnkl.DLinkedList('mydlinkedlist')
        l=[1,3,'hello',True,None,False,(7,8,9)]
        dll.addDataFromList(l)
        self.assertIsNone(dll.seek(2.5))
        self.assertIsNone(dll.seek('0'))
       
        dll.seek(0,0)
        self.assertEqual(0,dll.tell())
        self.assertEqual(1,dll.getCurrentData())
        dll.seek(1,0)
        self.assertEqual(1,dll.tell())
        self.assertEqual(3,dll.getCurrentData())
        dll.seek(1,1)
        self.assertEqual(2,dll.tell())
        self.assertEqual('hello',dll.getCurrentData())
        dll.seek(1,1)
        self.assertEqual(3,dll.tell())
        self.assertEqual(True,dll.getCurrentData())
        dll.seek(1,1)
        self.assertEqual(4,dll.tell())
        self.assertEqual(None,dll.getCurrentData())
        dll.seek(-1,1)
        self.assertEqual(3,dll.tell())
        self.assertEqual(True,dll.getCurrentData())
        dll.seek(0,2)
        self.assertEqual(6,dll.tell())
        self.assertEqual((7,8,9),dll.getCurrentData())
        dll.seek(-1,2)
        self.assertEqual(5,dll.tell())
        self.assertEqual(False,dll.getCurrentData())
        dll.seek(-2,2)
        self.assertEqual(4,dll.tell())
        self.assertEqual(None,dll.getCurrentData())
        # seek() can move to head
        dll.seek(-1,0)
        self.assertEqual(-1,dll.tell())
        self.assertEqual('mydlinkedlist',dll.getCurrentData())
        dll.seek(-2,0)
        self.assertEqual(-1,dll.tell())






    # testing getAllData() method
    def test_getAllData(self):
        dll=dlnkl.DLinkedList('mydlinkedlist')
        l=[1,3,'hello',True,14.5,False,(7,8,9)]
        dll.addDataFromList(l)
        t=(1, 3, 'hello', True, 14.5, False, (7, 8, 9))
        self.assertEqual(t,dll.getAllData())





    # testing convert2dict() method
    def test_convert2dict(self):
        dll=dlnkl.DLinkedList('mydlinkedlist')
        l=[1,3,'hello',True,14.5,False,(7,8,9)]
        dll.addDataFromList(l)
        d={'name':'mydlinkedlist','class':'DLinkedList','size':7,0:1,1:3,2:'hello',3:True,4:14.5,5:False,6:(7,8,9)}
        self.assertEqual(d,dll.convert2dict())






    # testing getNodeAt(self,index=0) method
    def test_getNodeAt(self):
        dll=dlnkl.DLinkedList('mydlinkedlist')
        l=[1,3,'hello',True,14.5,False,(7,8,9)]
        dll.addDataFromList(l)        
        self.assertEqual('<Node: 1 at index 0>',str(dll.getNodeAt()))
        self.assertEqual('<Node: hello at index 2>',str(dll.getNodeAt(2)))





    # testing getDataAt(self,index=0) method
    def test_getDataAt(self):
        dll=dlnkl.DLinkedList('mydlinkedlist')
        l=[1,3,'hello',True,14.5,False,(7,8,9)]
        dll.addDataFromList(l)        
        self.assertEqual(1,dll.getDataAt())
        self.assertEqual('hello',dll.getDataAt(2))





    # testing editDataAt(self,data,index=0) method
    def test_editDataAt(self):
        dll=dlnkl.DLinkedList('mydlinkedlist')
        l=[1,3,'hello',True,14.5,False,(7,8,9)]
        dll.addDataFromList(l)
        dll.editDataAt(data=10,index=0)
        self.assertEqual(10,dll.getDataAt())
        dll.editDataAt('hello world',2)
        self.assertEqual('hello world',dll.getDataAt(2))





    # testing insertDataAt(self,data,index=0) method
    def test_insertDataAt(self):
        dll=dlnkl.DLinkedList('mydlinkedlist')
        l=[1,3,'hello',True,14.5,False,(7,8,9)]
        dll.addDataFromList(l)
        # default insert index=0
        dll.insertDataAt(data=10);
        t=(10, 1, 3, 'hello', True, 14.5, False, (7, 8, 9))
        self.assertEqual(t,dll.getAllData())
        self.assertEqual(8,len(dll))

        dll.insertDataAt('world',4); 
        t=(10, 1, 3, 'hello', 'world', True, 14.5, False, (7, 8, 9))
        self.assertEqual(t,dll.getAllData())
        self.assertEqual(9,len(dll))

        dll.insertDataAt('end',9); 
        t=(10, 1, 3, 'hello', 'world', True, 14.5, False, (7, 8, 9), 'end')
        self.assertEqual(t,dll.getAllData())
        self.assertEqual(10,len(dll))





    # testing deleteDataAt(self,index=0) method
    def test_deleteDataAt(self):
        dll=dlnkl.DLinkedList('mydlinkedlist')
        l=[1,3,'hello',True,14.5,False,(7,8,9)]
        dll.addDataFromList(l)
        # default index=0
        dll.deleteDataAt();
        t=(3, 'hello', True, 14.5, False, (7, 8, 9))
        self.assertEqual(t,dll.getAllData())
        self.assertEqual(6,len(dll))

        dll.deleteDataAt(4); 
        t=(3, 'hello', True, 14.5, (7, 8, 9))
        self.assertEqual(t,dll.getAllData())
        self.assertEqual(5,len(dll))

        dll.deleteDataAt(4); 
        t=(3, 'hello', True, 14.5)
        self.assertEqual(t,dll.getAllData())
        self.assertEqual(4,len(dll))




    # testing searchData(self, searchdata) method
    def test_searchData(self):
        dll=dlnkl.DLinkedList('mydlinkedlist')
        l=[('jaon', 'john', 'ali', 'karim'), 10, 20, 30, 'hello', 'john', 'ali', 'karim ali', 100, 10, 20, 30, 40, True, False, None]
        dll.addDataFromList(l)        
        d={0: ('jaon', 'john', 'ali', 'karim'), 6: 'ali', 7: 'karim ali'}
        self.assertEqual(d,dll.searchData('ali'))




    # testing clear() method
    def test_clear(self):
        dll=dlnkl.DLinkedList('mydlinkedlist')
        l=[('jaon', 'john', 'ali', 'karim'), 10, 20, 30, 'hello', 'john', 'ali', 'karim ali', 100, 10, 20, 30, 40, True, False, None]
        dll.addDataFromList(l)        
        self.assertEqual(16,dll.getSize())
        dll.clear()
        self.assertEqual(0,dll.getSize())





# ----------------------- Data File related methods -----------------------
    #
    # testing setFilePreserve(self, preserve=True), isFilePreserved() methods
    def test_setFilePreserve(self):
        dll=dlnkl.DLinkedList('mydlinkedlist')
        self.assertTrue(dll.isFilePreserved())
        dll.setFilePreserve(False)
        self.assertFalse(dll.isFilePreserved())





    # testing setFileAddress(self, directory=datadir, filename="linkedlist")
    # and getFileAddress() methods
    def test_setFileAddress(self):
        dll=dlnkl.DLinkedList('mydlinkedlist')
        filedir=os.path.expanduser('~')+os.sep+"pcds_data"
        filename="dlinkedlist"
        fileaddr=filedir+os.sep+filename+".pcds"
        dll.setFileAddress(filedir,filename)
        self.assertEqual(fileaddr, dll.getFileAddress())
        filedir=os.path.expanduser('~')+os.sep+"pcds_data"
        filename="dlinkedlist2"
        fileaddr=filedir+os.sep+filename+".pcds"        
        dll.setFileAddress(filedir,filename)
        self.assertEqual(fileaddr, dll.getFileAddress())





    # testing save(self, directory=datadir, filename="dlinkedlist", enc=True) method
    def test_save(self):
        dll=dlnkl.DLinkedList('mydlinkedlist')
        l=[('jaon', 'john', 'ali', 'karim'), 10, 20, 30, 'hello', 'john', 'ali', 'karim ali', 100, 10, 20, 30, 40, True, False, None]
        dll.addDataFromList(l)        
        self.assertEqual(16,dll.getSize())
        self.assertTrue(dll.save())
        # msg: Encrypted Data Saved Successfully into 'C:\Users\admin\pcds_data\dlinkedlist.pcds'
        self.assertTrue(dll.save(filename="dlinkedlist2",enc=False))
        # msg: Plain Data Saved Successfully into 'C:\Users\admin\pcds_data\dlinkedlist2.pcds'





    # testing loadDataFromFile(self, fileaddr=datadir+os.sep+"linkedlist.pcds") method
    def test_loadDataFromFile(self):
        self.test_save()
        dll=dlnkl.DLinkedList('mydlinkedlist')
        self.assertEqual(0,dll.getSize())
        dll.loadDataFromFile()
        # msg: Data Loaded Successfully from the file: 'C:\Users\admin\pcds_data\dlinkedlist.pcds'
        self.assertEqual(16,dll.getSize())
        fileaddr=os.path.expanduser('~')+"\\pcds_data\\dlinkedlist2.pcds"
        dll.clear()
        self.assertEqual(0,dll.getSize())
        dll.loadDataFromFile(fileaddr)
        # msg: Data Loaded Successfully from the file: 'C:\Users\admin\pcds_data\dlinkedlist2.pcds'
        self.assertEqual(16,dll.getSize())





    # testing removeDataFile() method
    # before removing data file, file preserve parameter must be set to False
    def test_removeDataFile(self):
        dll=dlnkl.DLinkedList('mydlinkedlist')
        filedir=os.path.expanduser('~')+os.sep+"pcds_data"
        filename="dlinkedlist"
        fileaddr=filedir+os.sep+filename+".pcds"
        dll.setFileAddress()
        if os.path.exists(fileaddr) and os.path.isfile(fileaddr):
            dll.setFilePreserve(False)
            self.assertTrue(dll.removeDataFile())
        filename="dlinkedlist2"
        fileaddr=filedir+os.sep+filename+".pcds"
        dll.setFileAddress()
        if os.path.exists(fileaddr) and os.path.isfile(fileaddr):
            dll.setFilePreserve(False)
            self.assertTrue(dll.removeDataFile())








if __name__ == '__main__':
    unittest.main()




