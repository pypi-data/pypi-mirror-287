'''
Test Module: test_bstree.py
Test Module Name: test_bstree
Author: A K M Aminul Islam
Author Email: aminul71bd@gmail.com
Last Modified: Sunday July 21 2024 11:30 AM
Version:1.0.0
Python Version:3.12.4
'''

version="1.0.0"


import unittest
import os
from pcds import bstree as bst
from pcds import utilities as u



# testing Node class
class TestNode(unittest.TestCase):
    # testing the constructor of Node class
    # Node constructor requires only data
    def test___init__(self):        
        self.assertIsNotNone(bst.Node())        
        self.assertIsNotNone(bst.Node(data=10))
        n1=bst.Node(100)
        self.assertEqual(100,n1.getValue())        
        self.assertEqual(None,n1.left) 
        self.assertEqual(None,n1.right)
        self.assertEqual(None,n1.parent)



    # testing setData(), getValue() method
    def test_setData(self):        
        n1=bst.Node('ab')         
        self.assertEqual(6241,n1.getValue())       
        n1.setData('hello')
        self.assertEqual(5924297074,n1.getValue())
        n1.setData(12.89)
        self.assertEqual(12.89,n1.getValue())
        n1.setData(100)
        self.assertEqual(100,n1.getValue())



    # testing printData() method
    def test_printData(self):        
        n1=bst.Node('ab') 
        self.assertEqual('ab',n1.printData())       
        n1.setData('hello')
        self.assertEqual('hello',n1.printData())
        n1.setData(12.89)
        self.assertEqual('12.89',n1.printData())
        n1.setData(100)
        self.assertEqual('100',n1.printData())



    # testing getOriginalData() method
    def test_getOriginalData(self):        
        n1=bst.Node('ab')        
        self.assertEqual('ab',n1.getOriginalData())       
        n1.setData('hello')
        self.assertEqual('hello',n1.getOriginalData())
        n1.setData(12.89)
        self.assertEqual(12.89,n1.getOriginalData())
        n1.setData(100)
        self.assertEqual(100,n1.getOriginalData())



    # testing __str__(), __repr__() method
    def test_str_repr(self):
        n1=bst.Node('hello world')        
        self.assertEqual("<Binary Tree Node: data='hello world'>",str(n1))
        self.assertEqual('hello world',repr(n1))



    # testing isString() method
    def test_isString(self):
        n1=bst.Node(12)
        n2=bst.Node('abc')
        self.assertFalse(n1.isString())
        self.assertTrue(n2.isString())




# --------------- testing BinarySearchTree class ---------------------
class TestBinarySearchTree(unittest.TestCase):
    # testing constructor function which does not need any argument
    def test___init__(self):
        t1=bst.BinarySearchTree()
        self.assertIsInstance(t1,bst.BinarySearchTree)
        self.assertEqual(0,t1.getOriginalSize())


    # testing append() method that takes a single data
    # only integer, float and string type data are supported
    def test_append(self):
        t1=bst.BinarySearchTree()
        t1.append(100)
        self.assertEqual(1,t1.getOriginalSize())
        t1.append(10.47)
        self.assertEqual(2,t1.getOriginalSize())
        t1.append('hello')
        self.assertEqual(3,t1.getOriginalSize())
        # The following data are not accepted
        self.assertIsNone(t1.append(True))
        self.assertIsNone(t1.append(False))
        self.assertIsNone(t1.append(None))
        self.assertIsNone(t1.append([1,2,3]))
        self.assertIsNone(t1.append((1,2,3)))
        self.assertIsNone(t1.append({1:'a',2:'b'}))
        self.assertEqual(3,t1.getOriginalSize())



    # testing loadDataFromList(self,data) method
    def test_loadDataFromList(self):
        t1=bst.BinarySearchTree()
        l=[2,6.9,1.4,9,'a','b',40.5,2,1.4,'a',2,6.9,34]
        t1.loadDataFromList(l)
        self.assertEqual(13,t1.getOriginalSize())
        t1.clear()
        l=[2,6.9,1.4,9,'a','b',40.5,2,True,1.4,'a',2,6.9,34]
        self.assertIsNone(t1.loadDataFromList(l))
        self.assertEqual(0,t1.getOriginalSize())



    # testing loadDataFromTuple(self,data) method
    def test_loadDataFromTuple(self):
        t1=bst.BinarySearchTree()
        l=(2,6.9,1.4,9,'a','b',40.5,34)
        t1.loadDataFromTuple(l)
        self.assertEqual(8,t1.getOriginalSize())
        t1.clear()
        l=(2,6.9,1.4,9,None,'b',40.5,34)
        self.assertIsNone(t1.loadDataFromTuple(l))
        self.assertEqual(0,t1.getOriginalSize())



    # testing getDataList(self), getOriginalSize(), getOriginalSize() methods
    def test_getDataList(self):
        t1=bst.BinarySearchTree()
        l=[2,6.9,1.4,9,'a','b',40.5,2,1.4,'a',2,6.9,34]
        t1.loadDataFromList(l)
        # data not sorted
        self.assertEqual(tuple(l),t1.getOriginalData())
        self.assertEqual(13,t1.getOriginalSize())



    # testing min() method
    def test_min(self):
        t1=bst.BinarySearchTree()
        l=[2,6.9,1.4,9,10,'a','b',40.5,45,80,2,1.4,'a',2,6.9,55,14.6,34]
        t1.loadDataFromList(l)
        self.assertEqual(1.4,t1.min())        



    # testing getMinNode() method
    def test_getMinNode(self):
        t1=bst.BinarySearchTree()
        l=[2,6.9,1.4,9,10,'a','b',40.5,45,80,2,1.4,'a',2,6.9,55,14.6,34]
        t1.loadDataFromList(l)
        self.assertEqual('1.4',repr(t1.getMinNode()))
        self.assertEqual('<Binary Tree Node: data=1.4>',str(t1.getMinNode()))



    # testing max() method
    def test_max(self):
        t1=bst.BinarySearchTree()
        l=[2,6.9,1.4,9,10,'a','b',40.5,45,80,2,1.4,'a',2,6.9,55,14.6,34]
        t1.loadDataFromList(l)
        self.assertEqual(80,t1.max())



    # testing getRootData(), getRootNode() methods
    def test_getRootData(self):
        t1=bst.BinarySearchTree()
        l=[2,6.9,1.4,9,10,'a','b',40.5,45,80,2,1.4,'a',2,6.9,55,14.6,34]
        t1.loadDataFromList(l)
        t1.findRootNode()
        self.assertEqual(40.5,t1.getRootData())
        self.assertEqual('<Binary Tree Node: data=40.5>',str(t1.getRootNode()))



    # testing buildTree() and isBuilt() methods
    def test_buildTree(self):
        t1=bst.BinarySearchTree()
        l=[2,6.9,1.4,9,10,'a','b',40.5,45,80,2,1.4,'a',2,6.9,55,14.6,34]
        t1.loadDataFromList(l)
        self.assertFalse(t1.isBuilt())
        t1.buildTree()
        self.assertTrue(t1.isBuilt())



    # testing sortTree(), isSorted(), getSortOrder() methods
    def test_sortTree(self):
        t1=bst.BinarySearchTree()
        l=[2,6.9,1.4,9,10,'a','b',40.5,45,80,2,1.4,'a',2,6.9,55,14.6,34]
        t1.loadDataFromList(l)
        t1.buildTree()
        self.assertFalse(t1.isSorted())
        t1.sortTree()
        self.assertTrue(t1.isSorted())
        self.assertEqual('ascending',t1.getSortOrder())
        t1.sortTree(asc=False)
        self.assertTrue(t1.isSorted())
        self.assertEqual('descending',t1.getSortOrder())



    # testing getSortedData(self), getSortedSize() methods
    def test_getSortedData(self):
        t1=bst.BinarySearchTree()
        l=[2,6.9,1.4,9,'a','b',40.5,2,1.4,'a',2,6.9,34]
        t1.loadDataFromList(l)
        # data not sorted
        self.assertEqual((),t1.getSortedData())
        t1.buildTree()
        t1.sortTree(asc=True)
        self.assertEqual((1.4, 2, 6.9, 9, 34, 40.5, 'a', 'b'),t1.getSortedData())
        self.assertEqual(8,t1.getSortedSize())
        t1.sortTree(asc=False)
        self.assertEqual(('b', 'a', 40.5, 34, 9, 6.9, 2, 1.4),t1.getSortedData())
        self.assertEqual(8,t1.getSortedSize())



    # testing searchTree() method
    def test_searchTree(self):
        t1=bst.BinarySearchTree()
        l=[20,50,4,7,8,12,15,30,35,40,-5,20,50,4,7,8,12,15,30,'a',35,40,'b','ab','c','bc','cb',-10,-5,100,14.78,20,80.95]
        t1.loadDataFromList(l)
        # (-10,-5,4,7,8,12,14.78,15,20,30,35,40,50,'a','b','c',80.95,100,'ab','bc','cb')
        self.assertEqual(None,t1.searchTree(18))
        self.assertEqual(11,t1.searchTree(40))
        self.assertEqual(19,t1.searchTree('bc'))
        self.assertEqual(None,t1.searchTree('cd'))



    # testing __str__(), __repr__(), __len__() methods
    def test_str_repr_len(self):
        t1=bst.BinarySearchTree()
        l=[20,50,4,7,8,12,15,30,35,40,-5,20,50,4,7,8,12,15,30,'a',35,40,'b','ab','c','bc','cb',-10,-5,100,14.78,20,80.95]
        t1.loadDataFromList(l)
        # testing on raw data
        self.assertEqual(33,len(t1))
        s="(20, 50, 4, 7, 8, 12, 15, 30, 35, 40, -5, 20, 50, 4, 7, 8, 12, 15, 30, 'a', 35, 40, 'b', 'ab', 'c', 'bc', 'cb', -10, -5, 100, 14.78, 20, 80.95)"
        self.assertEqual(s,repr(t1))
        s="<Binary Search Tree(not sorted): no. of nodes=33, data=(20, 50, 4, 7, 8, 12, 15, 30, 35, 40, -5, 20, 50, 4, 7, 8, 12, 15, 30, 'a', 35, 40, 'b', 'ab', 'c', 'bc', 'cb', -10, -5, 100, 14.78, 20, 80.95)>"
        self.assertEqual(s,str(t1))
        # testing on sorted data
        t1.sortTree()
        self.assertEqual(21,len(t1))
        s="(-10, -5, 4, 7, 8, 12, 14.78, 15, 20, 30, 35, 40, 50, 'a', 'b', 'c', 80.95, 100, 'ab', 'bc', 'cb')"
        self.assertEqual(s,repr(t1))
        s="<Binary Search Tree(sorted): no. of nodes=21, data=(-10, -5, 4, 7, 8, 12, 14.78, 15, 20, 30, 35, 40, 50, 'a', 'b', 'c', 80.95, 100, 'ab', 'bc', 'cb')>"
        self.assertEqual(s,str(t1))




# ----------------------- Data File related methods -----------------------
    #
    # testing setFilePreserve(self, preserve=True), isFilePreserved() methods
    # Default value of file preserve is True.
    def test_setFilePreserve(self):
        t1=bst.BinarySearchTree()
        self.assertTrue(t1.isFilePreserved())
        t1.setFilePreserve(False)
        self.assertFalse(t1.isFilePreserved())





    # testing setDataFileAddress(self, directory=datadir, filename="bstree")
    # and getDataFileAddress() methods
    def test_setDataFileAddress(self):
        t1=bst.BinarySearchTree()
        filedir=os.path.expanduser('~')+os.sep+"pcds_data"
        filename="bstree"
        fileaddr=filedir+os.sep+filename+".pcds"
        t1.setDataFileAddress(filedir,filename)
        self.assertEqual(fileaddr, t1.getDataFileAddress())
        filename="bstree2"
        fileaddr=filedir+os.sep+filename+".pcds"        
        t1.setDataFileAddress(filedir,filename)
        self.assertEqual(fileaddr, t1.getDataFileAddress())





    # testing save(self, directory=datadir, filename="dlinkedlist", enc=True) method
    # If tree is not built and sorted, it will be done automatically.
    def test_save(self):
        t1=bst.BinarySearchTree()
        l=[20,50,4,7,8,12,15,30,35,40,-5,20,50,4,7,8,12,15,30,'a',35,40,'b','ab','c','bc','cb',-10,-5,100,14.78,20,80.95]
        t1.loadDataFromList(l)        
        self.assertEqual(33,len(t1))
        self.assertTrue(t1.save())
        # msg: Encrypted Data Saved Successfully into 'C:\Users\admin\pcds_data\bstree.pcds'
        self.assertTrue(t1.save(filename="bstree2",enc=False))
        # msg: Plain Data Saved Successfully into 'C:\Users\admin\pcds_data\bstree2.pcds'





    # testing loadDataFromFile(self, fileaddr=datadir+os.sep+"linkedlist.pcds") method
    def test_loadDataFromFile(self):
        t1=bst.BinarySearchTree()
        self.assertEqual(0,len(t1))
        self.test_save()
        t1.loadDataFromFile()        
        # msg: Data Loaded Successfully from the file: 'C:\Users\admin\pcds_data\bstree.pcds'
        self.assertEqual(21,len(t1))
        s="(-10, -5, 4, 7, 8, 12, 14.78, 15, 20, 30, 35, 40, 50, 'a', 'b', 'c', 80.95, 100, 'ab', 'bc', 'cb')"
        self.assertEqual(s,repr(t1))
        t1.clear()
        fileaddr=os.path.expanduser('~')+"\\pcds_data\\bstree2.pcds"        
        self.assertEqual(0,len(t1))
        t1.loadDataFromFile(fileaddr)
        # msg: Data Loaded Successfully from the file: 'C:\Users\admin\pcds_data\bstree2.pcds'
        self.assertEqual(21,len(t1))
        s="(-10, -5, 4, 7, 8, 12, 14.78, 15, 20, 30, 35, 40, 50, 'a', 'b', 'c', 80.95, 100, 'ab', 'bc', 'cb')"
        self.assertEqual(s,repr(t1))




    # testing removeDataFile() method
    # before removing data file, file preserve parameter must be set to False
    def test_removeDataFile(self):
        t1=bst.BinarySearchTree()
        filedir=os.path.expanduser('~')+os.sep+"pcds_data"
        filename="bstree"
        fileaddr=filedir+os.sep+filename+".pcds"
        t1.setDataFileAddress()
        if os.path.exists(fileaddr) and os.path.isfile(fileaddr):
            t1.setFilePreserve(False)
            self.assertTrue(t1.removeDataFile())
        filename="bstree2"
        fileaddr=filedir+os.sep+filename+".pcds"
        t1.setDataFileAddress(filedir,filename)
        if os.path.exists(fileaddr) and os.path.isfile(fileaddr):
            t1.setFilePreserve(False)
            self.assertTrue(t1.removeDataFile())





if __name__ == '__main__':
    unittest.main()


# ----------------------------- END of TEST -----------------------------






