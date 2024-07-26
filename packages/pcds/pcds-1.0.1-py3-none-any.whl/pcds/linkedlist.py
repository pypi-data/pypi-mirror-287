'''
Module Description
--------------------
module filename: linkedlist.py
module name: linkedlist (Singly Linked List)
Content: Functions: dataType() 
        Class: Node, DLinkedList (Doubly Linked List)
Description: This module creates singly linked list which can be traversed in forward
    direction only. The list is made of node objects. Each Node object holds data and 
    has a forward link and one unique indix. Nodes are linked by the next attribute.

    Node Class:
        Constructor: Node(data,index)
        setData(data), getData(), setIndex(index), getIndex(), __str__(), __repr__()

    LinkedList (singly linked list) Class:
        Constructor: LinkedList()
        Class Methods: getCurrentIndex(), tell(),  getCurrentNode(), getCurrentData(), 
        changeCurrentData(data), getDataFile(), getSize(),  
        append(), addDataFromList(self, listobj=[]), addDataFromTuple(self, tupleobj=[])
        moveNext(), moveLast(), movePrev(), moveFirst(), seek(offset,location),
        getAllData(), getAllIndices(), convert2dict(), getNodeAt(), getDataAt(), 
        editDataAt(data,index=0), insertDataAt(data, index=0), deleteDataAt(index=0), 
        searchData(searchdata), clear(), __len__(), __str__(), __repr__() 
        isFilePreserved(), setFilePreserve(bool), getFileAddress(), 
        setFileAddress(directory=datadir, filename="linkedlist"),
        save(directory="", filename="dlinkedlist", enc=True), 
        loadDataFromFile(fileaddr="pcds_data\\linkedlist.pcds"), removeDataFile()

    Suported Data Types: int, float, str, bool, tuple, list, dictionary

    Data are saved in a binary file with extension .pcds (python data structure file)
    Data encryption is supported for the security of data.
Author: A K M Aminul Islam
Last Modified: Saturday July 20 2024 04:45 AM
Version:1.2.3
Dependencies: utilities, encrypt, os
'''

version="1.2.3"

import os
from pcds import utilities as u
from pcds import encrypt


import pcds
datadir=pcds.getDataDirectory()




# dataType(variable) returns the data type of the given variable
# >>> dataType(34)
# 'int'
# >>> dataType([])
# 'list'
# >>> dataType({})
# 'dict'
# >>> dataType(None)
# 'NoneType'
def dataType(arg):
    return str(type(arg)).split("'")[1]



# ----------------------------- class Node ---------------------------------
class Node:
    __data=None
    __index=-2


    # constructor function of Node class. A node needs data and index.
    # Supported Data Types:'int','float','str','bool','NoneType','list','tuple','dict'.")
    # Index value is either -1, zero, or a positive integer.
    # Only the head node has index -1.
    # >>> import linkedList as lnkl
    # >>> n1=lnkl.Node(20,2)
    # >>> n1
    # <Node: 20 at index 2>
    def __init__(self,data=None,index=-2):
        try:
            if dataType(data) not in ['int','float','str','bool','NoneType','list','tuple','dict']:
                raise TypeError("Invalid Data Type.\nSupported Data Types:'int','float','str','bool','NoneType','list','tuple','dict'.")
            if dataType(index) != 'int':
                raise TypeError("Index is an integer type data.")            
            if index<-1:
                raise ValueError("Index must be a positive integer, zero or -1.")
        except ValueError as e: print(e); return None        
        if data==None:
            print("Warning! None type data is entered.")
        self.__data=data
        self.next=None        
        self.__index=index



    # setter and getter methods
    # getData() returns data of the node object
    # >>> n1.getData()
    # 'hello'
    def getData(self):
        return self.__data



    # setData(self,data=None) sets or changes the current node data
    # >>> n1.setData('hello')
    # >>> n1
    # <Node: hello at index 4>
    def setData(self,data=None):
        try:
            if dataType(data) not in ['int','float','str','bool','NoneType','list','tuple','dict']:
                raise TypeError("Invalid Data Type.\nSupported Data Types:'int','float','str','bool','NoneType','list','tuple','dict'.")
        except TypeError as e: print(e); return None
        if data==None:
            print("Warning! None type data is entered.")
        self.__data=data



    # setIndex(self,index=0) sets the index of the node. Index value is either zero,
    # -1 or a positive integer. Only the head node has index -1.
    # >>> n1.setIndex(4)
    # >>> n1
    # <Node: 20 at index 4>
    def setIndex(self,index=-1):
        try:
            if dataType(index) != 'int':
                raise TypeError("Index is an integer type data.")            
            if index<-1:
                raise ValueError("Index must be a positive integer, zero or -1.")
        except Exception as e: print(e); return None
        self.__index=index



    # getIndex(self) returns the index of the node
    # >>> n1.setIndex(4); n1.getIndex()
    # 4
    def getIndex(self):
        if self.__index>=-1:
            return self.__index
        else:
            print("Warning! Index is not set.")



    # __str__(self) returns the string representation of the node instance
    # when str(node) function is used
    # >>> str(n1)
    # <Node: 20 at index 2>
    def __str__(self):
        if self.__index==-1:
            return "<Head Node at index -1>"
        elif self.__index>-1:
            if self.__data==None:
                return "<Node: None at index "+str(self.__index)+">"
            else:
                return "<Node: "+str(self.__data)+" at index "+str(self.__index)+">"
        else:
            return ""



    # __repr__(self) returns the printable version of the 
    # node instance when repr(node) or print(node) function is used
    # >>> n1
    # <Node: 20 at index 2>
    def __repr__(self):
        return self.__str__()

    

# ----------------------------- class LinkedList ---------------------------------
class LinkedList:
    __head=None     # head of the linked list
    __size=-1       # read-only private property
    __curNode=None  # holds the current node of the doubly linked list
    __file=None     # holds the file address (path+'\\'+filename) string
    __preserve=True # data file will not be deleted when the list variable is deleted
        

    # constructor of the doubly linked list    
    def __init__(self,name="LNKList"):
        try:
            if dataType(name) != 'str':
                raise TypeError("LinkedList name is a string type data.")
        except TypeError as e: print(e); return None
        # setting private variables        
        self.__head=Node(name,-1)        
        self.__size=0
        self.__curNode=self.__head
        



    # ------------------ setter and getter methods --------------------
    # getHead(self) returns the head node of the linked list
    def getHead(self):
        return self.__head





    # getName(self) returns the name of the linked list
    def getName(self):
        return self.__head.getData()





    # getCurrentIndex(self) returns the current location of the list pointer
    def getCurrentIndex(self):
        if self.__curNode:
            return self.__curNode.getIndex()





    # tell(self) returns also the current location of the list pointer
    def tell(self):
        if self.__curNode:
            return self.__curNode.getIndex()





    # getCurrentNode(self) returns the current node object of the list pointer
    def getCurrentNode(self):
        if self.__curNode:
            return self.__curNode




    # getCurrentData(self) returns the current data of the list
    def getCurrentData(self):
        if self.__curNode:
            return self.__curNode.getData()




    # changeCurrentData(self) changes the current data of the list
    def changeCurrentData(self,data):
        if self.__curNode:
            self.__curNode.setData(data)




    # getSize(self) returns size (number of nodes) of the linked list
    def getSize(self):
        if self.__size>=0:
            return self.__size
    # -------------- End of setter and getter methods ---------------

    # append(self,data) adds the given data at the end of the list.
    # List size and index of the last node are updated accordingly.
    def append(self,data):
        try:
            if dataType(data) not in ['int','float','str','bool','NoneType','list','tuple','dict']:
                raise TypeError("Invalid Data Type.\nSupported Data Types:'int','float','str','bool','NoneType','list','tuple','dict'.")
        except TypeError as e: print(e); return None
        # moving to the last node and adding the new node with new data
        new_node=Node(data,self.__size)
        if self.__size==0:
            self.__head.next=new_node
            self.__size=1
            self.__curNode=self.__head.next
        else:
            self.moveLast()
            tmpnode=self.__curNode
            tmpnode.next=new_node
            self.__curNode=new_node
            self.__size=self.__size+1
        



    # addDataFromList(listobj=[]) appends data from the list
    def addDataFromList(self, listobj=[]):
        try:
            if dataType(listobj) != "list":
                raise TypeError("Argument is not a list data type.")
            if len(listobj)==0:
                raise ValueError("List is empty.")
        except Exception as e: print(e); return None
        # Move the list pointer at the end
        if self.__size==0:
            self.__curNode=self.__head
        else:
            self.moveLast()            
        for data in listobj:
            new_node=Node(data,self.__size)
            self.__curNode.next=new_node
            self.__size=self.__size+1
            self.__curNode=new_node
            



    # addDataFromTuple(listobj=()) appends data from the tuple given
    def addDataFromTuple(self, tupleobj=()):
        try:
            if dataType(tupleobj) != "tuple":
                raise TypeError("Argument is not a tuple data type.")
            if len(tupleobj)==0:
                raise ValueError("Tuple is empty.")
        except Exception as e: print(e); return None
        # Move the list pointer at the end
        if self.__size==0:
            self.__curNode=self.__head
        else:
            self.moveLast()            
        for data in tupleobj:
            new_node=Node(data,self.__size)
            self.__curNode.next=new_node
            self.__size=self.__size+1
            self.__curNode=new_node





    # moveNext(self) moves the list pointer to the next available node
    def moveNext(self):
        if self.__curNode.next:
            self.__curNode = self.__curNode.next        




    # moveLast(self) moves the list pointer to the end of the list
    def moveLast(self):
        while self.__curNode.next:
            self.__curNode = self.__curNode.next        
        



    # movePrev(self) moves the list pointer to the previous node
    def movePrev(self):
        curIndex=self.__curNode.getIndex()
        if curIndex==0:return
        self.__curNode=self.__head
        i=0
        while i<=curIndex-1 and self.__curNode:
            self.__curNode = self.__curNode.next
            i=i+1




    # moveFirst(self) moves the list pointer to the beginning of the list
    def moveFirst(self):
        if self.__head.next:
            self.__curNode=self.__head.next




    # moveToHead(self) moves the list pointer to the beginning of the list
    def moveToHead(self):
        self.__curNode = self.__head




    # seek(self,offset=0,location=0) moves the list pointer by the offset value
    # from the reference location (0=from begining, 1=from current, 2=from end)
    # seek(0,0)=beginning; seek(0,1)=current position; seek(0,2)=end position
    def seek(self,offset=0,location=0):
        try:
            if dataType(offset) != 'int':
                raise TypeError("Argument offset is an integer type data.")
            if dataType(location) != 'int':
                raise TypeError("Argument location is an integer type data.")
            if location not in [0,1,2]:
                raise ValueError("Argument location has value either 0, 1 or 2 only.")
        except TypeError as e: print(e); return None
        except ValueError as e: print(e); return None
        curIndex=self.__curNode.getIndex()
        moveright=-1; frombeginning=True
        # offset from the beginning of the list
        try:
            if location==0:
                if offset<0:                    
                    raise ValueError("Index out of range.")
                elif curIndex > offset:
                    moveright=offset; frombeginning=True
                elif curIndex == offset: return
                elif offset>=self.__size :
                    raise ValueError("Index out of range.")
                elif offset>curIndex and offset<self.__size:
                    moveright=offset-curIndex; frombeginning=False
            elif location==1:
                if offset==0: return None
                elif offset<0:
                    if -offset>curIndex:  # left of the beginning
                        raise ValueError("Index out of range.")
                    if -offset==curIndex:  # at the beginning
                        moveright=0;frombeginning=True
                    elif -offset<curIndex:  # between beginning and current position
                        moveright=curIndex+offset;frombeginning=True
                elif offset>0:
                    if curIndex+offset>=self.__size :
                        raise ValueError("Index out of range.")                    
                    elif curIndex+offset<self.__size :
                        moveright=offset; frombeginning=False
            elif location==2:
                if offset>0:
                    raise ValueError("Index out of range.")
                elif offset==0:
                    moveright=self.__size-1-curIndex; frombeginning=False
                elif offset<0:
                    if -offset>self.__size-1:  # left of the beginning
                        raise ValueError("Index out of range.")
                    elif -offset==self.__size-1:  # left of the beginning
                        moveright=0;frombeginning=True
                    elif curIndex<self.__size-1+offset: # between current position and end 
                        moveright=self.__size-1+offset-curIndex;frombeginning=False
                    elif curIndex==self.__size-1+offset: return
                    elif curIndex>self.__size-1+offset: # between beginning and current position
                        moveright=self.__size-1+offset;frombeginning=True
        except ValueError as e: print(e); return None
        # moving to the right position
        if frombeginning==True:
            i=0
            self.__curNode=self.__head
            while i<=moveright and self.__curNode.next: 
                self.__curNode=self.__curNode.next
                i=i+1
        else:
            i=0
            while i<moveright and self.__curNode.next: 
                self.__curNode=self.__curNode.next
                i=i+1





    # getAllData(self) returns all data of the linked list in tuple form
    def getAllData(self):
        cur_node=self.__head
        tmplist=[]
        while cur_node.next:
            cur_node = cur_node.next
            tmplist.append(cur_node.getData())
        return tuple(tmplist)



   

    # convert2dict(self) returns linked list data in dictionary form 
    def convert2dict(self):
        cur_node=self.__head
        tmpdict={'name':self.getName(),'class':'LinkedList','size':self.__size}
        while cur_node.next:
            cur_node = cur_node.next
            tmpdict[cur_node.getIndex()]=cur_node.getData()
        return tmpdict





    # getNodeAt(self,index=0) returns the node at the specific index position
    def getNodeAt(self,index=0):
        try:
            if dataType(index) != 'int':
                raise TypeError("Index must be a positive integer.")
            if index<0 or index >= self.__size: 
                raise ValueError("Index out of the range.")
        except Exception as e: print(e); return None
        self.seek(index,0)
        return self.__curNode
        




    # getDataAt(self,index=0) returns data of the node at the given index 
    def getDataAt(self,index=0):
        try:
            if dataType(index) != 'int':
                raise TypeError("Index must be a positive integer.")
            if index<0 or index >= self.__size: 
                raise ValueError("Index out of the range.")
        except Exception as e: print(e); return None
        self.seek(index,0)
        return self.__curNode.getData()
        




    # editDataAt(self,data,index=0) edits data at the given index
    def editDataAt(self,data,index=0):        
        try:
            if dataType(index) != 'int':
                raise TypeError("Index must be a positive integer.")
            if index<0 or index >= self.__size: 
                raise ValueError("Index out of the range.")
            if dataType(data) not in ['int','float','str','bool','NoneType','list','tuple','dict']:
                raise TypeError("Invalid Data Type.\nSupported Data Types:'int','float','str','bool','NoneType','list','tuple','dict'.")
        except Exception as e: print(e); return None
        self.seek(index,0)
        self.__curNode.setData(data)




    # insertDataAt(self,data,index=0) inserts new data at the given index position
    # following the necessary updates
    def insertDataAt(self,data,index=0):
        try:
            if dataType(index) != 'int':
                raise TypeError("Index must be a positive integer.")
            if index<0 or index > self.__size: 
                raise ValueError("Index out of the range.")
            if dataType(data) not in ['int','float','str','bool','NoneType','list','tuple','dict']:
                raise TypeError("Invalid Data Type.\nSupported Data Types:'int','float','str','bool','NoneType','list','tuple','dict'.")
        except Exception as e: print(e); return None
        # inserting and creating bidirectional links
        new_node=Node(data, index)
        if index==self.__size:
            self.append(data)
            return
        elif index==0:
            self.seek(0,0)
            self.__head.next=new_node
            new_node.next=self.__curNode
        else:
            self.seek(index-1,0)
            prevnode=self.__curNode
            curnode=self.__curNode.next
            prevnode.next=new_node
            new_node.next=curnode            
        self.__curNode=new_node 
        #self.__curNode.setIndex(index)         
        # updating indices
        i=0
        while self.__curNode.next:
            self.__curNode.setIndex(index+i)
            i=i+1
            self.__curNode=self.__curNode.next
        self.__curNode.setIndex(index+i)
        self.__size = self.__size + 1
        




    # deleteDataAt(self,index=0) deletes the node at the given index and updates
    # the other indices
    def deleteDataAt(self,index=0):
        try:
            if dataType(index) != 'int':
                raise TypeError("Index must be a positive integer.")
            if index<0 or index > self.__size-1: 
                raise ValueError("Index out of the range.")
        except Exception as e: print(e); return None
        # moving to the current index, cutting and rejoining the links
        if index==0:
            self.seek(0,0)
            if self.__curNode.next:
                self.__head.next=self.__curNode.next
            self.__curNode=self.__curNode.next
        elif index==self.__size-1:
            self.seek(index-1,0)            
            self.__curNode.next=None
            self.__size = self.__size - 1
            return            
        elif index<=self.__size-1:
            self.seek(index-1,0)
            nextnode=self.__curNode.next.next
            self.__curNode.next=nextnode
            if nextnode: self.__curNode=nextnode        
        # updating indices        
        i=0
        while self.__curNode.next:
            self.__curNode.setIndex(index+i)
            i=i+1
            self.__curNode=self.__curNode.next
        self.__curNode.setIndex(index+i)
        self.__size = self.__size - 1





    # searchData(self, searchdata) returns the indices and data of the linkedlist
    # where the searchdata is found. It returns a dictionary {index:data, ...}
    # Supported search data type: str, int, float, bool, NoneType
    # >>> myll
    # <Linked List: size=16, Data=(['jaon', 'john', 'ali', 'karim'], 10, 20, 30, 'hello', 'john', 'ali', 'karim ali', 100, 10, 20, 30, 40, True, False, None) >
    # >>> myll.searchData('ali')
    # {0: ['jaon', 'john', 'ali', 'karim'], 6: 'ali', 7: 'karim ali'}
    # >>> myll.searchData(10)
    # {1: 10, 9: 10}
    # >>> myll.searchData(True)
    # {13: True}
    # >>> myll.searchData([1,2,3])
    # Search data type is unsupported.
    # {}
    def searchData(self, searchdata):
        try:
            if dataType(searchdata) not in ['int','float','str','bool','NoneType','list','tuple','dict']:
                raise TypeError("Invalid Data Type.\nSupported Data Types:'int','float','str','bool','NoneType','list','tuple','dict'.")
        except Exception as e: print(e); return None
        # come to the beginning of the list and start searching
        s=""; foundDict={}
        self.seek(0,0)         
        curnode=self.__curNode
        try:
            while curnode:                
                listdata=curnode.getData()
                index=curnode.getIndex()
                if dataType(searchdata) == 'str':
                    if dataType(listdata) in ['int','float','bool','NoneType']:
                        curnode=curnode.next
                        continue
                    elif dataType(listdata) in ['str','list','tuple']:
                        if searchdata in listdata:
                            foundDict[index]=listdata
                    elif dataType(listdata) == 'dict':
                        if searchdata in listdata.keys() or searchdata in listdata.values():
                            foundDict[index]=listdata
                elif dataType(searchdata) in ['int','float','bool','NoneType']:                    
                    if searchdata == listdata: foundDict[index]=listdata
                    elif dataType(listdata) in ['list','tuple']:
                        if searchdata in listdata:
                            foundDict[index]=listdata
                    elif dataType(listdata) == 'dict':                        
                        if searchdata in listdata.keys() or searchdata in listdata.values():
                            foundDict[index]=listdata
                else:
                    raise ValueError("Search data type is unsupported.")
                curnode=curnode.next
        except ValueError as e: print(e); return None
        except Exception as e: print(e); return None
        return foundDict




    
    # clear(self) delinks all nodes from the head of the linked list
    # by initializing the link list
    # >>> myll=lnkl.LinkedList()
    # >>> myll
    # <Linked List: size=9, Data=(10, 20, 30, 40, 50, 'a', 'b', 'c', 'd') >
    # >>> myll.clear()
    # >>> myll
    # <Linked List: size=0, Data=() >
    def clear(self):
        self.__init__()     # data file loses all data
        



    # __len__(self) returns the size of the linked list when len(linkedlist) used
    def __len__(self):
        return self.__size



    # __str__(self) stringify the linked list data when str(linkedlist) used
    def __str__(self):
        return "<"+self.getName()+"[LinkedList]: size="+str(self.__size)+", Data="+str(self.getAllData())+">"




    # __repr__(self) converts linked list into a printable representation
    # when repr(linkedlist) or print(linkedlist) is used
    # >>> myll=lnkl.LinkedList()
    # >>> myll.append(125)
    # >>> myll.append(1.25)
    # >>> myll.append('hello world')
    # >>> myll.append(['hello',' world',74.12])
    # >>> myll.append(('hello',[4,8,7.2,None],' world',74.12))
    # >>> myll.append({2:45,'a':'abc','rolls':[12,14,13]})    
    # >>> myll
    # <DLinked List: size=6, Data=(125, 1.25, 'hello world', ['hello', ' world', 74.12], ('hello', [4, 8, 7.2, None], ' world', 74.12), {2: 45, 'a': 'abc', 'rolls': [12, 14, 13]}) >
    def __repr__(self):
        return self.__str__()



# ------------------------- File I/O Operations -----------------------------
#
     
    # isFilePreserved(self) returns True if 'preserve' parameter is set to True
    def isFilePreserved(self):
        return self.__preserve




    # setFilePreserve(self, preserve=True) sets the 'preserve' parameter 
    # True or False. If preserved, data file will not be deleted when the
    # data file is tried to be deleted by removeDataFile(self) function
    def setFilePreserve(self, preserve=True):
        try:
            if dataType(preserve) != 'bool': 
                raise TypeError("Data type of preserve should be boolean.")
        except TypeError as e: print (e); return None
        self.__preserve=preserve




    # setFileAddress(self, directory=datadir, filename="linkedlist", enc=True) sets 
    # the absolute address of the .pdsf data file in the private variable __file
    def setFileAddress(self, directory=datadir, filename="linkedlist"):
        try:
            # checking inputs (Part 1) 
            if dataType(directory) != 'str': 
                raise TypeError("Data type of file directory should be string.") 
            if dataType(filename) != 'str': 
                raise TypeError("Data type of file name should be string.")            
        except TypeError as e: print(e); return None
        directory=directory.strip(); filename=filename.strip(); fileaddr=""
        try:            
            fileaddr=u.createDataFile(directory, filename)
            self.__file=os.path.abspath(fileaddr)
        except Exception as e: print(e); return None
        


    
    # getDataFile(self) returns the absolute address of the .pcds data file
    def getFileAddress(self):
        if self.__file:
            return self.__file




    # save(self, directory=datadir, filename="linkedlist", enc=True) saves all data 
    # in the data file newly created
    # 8 steps: (1) checking inputs (2) data to string conversion 
    # (3) adding file header (4) encryption of data string (5) adding MD5 hash
    # (6) final encryption and encription tagging (7) encoding with 'utf-8'   
    # (8) writing to data file
    def save(self, directory=datadir, filename="linkedlist", enc=True):
        try:
            # checking inputs (Part 1) 
            if dataType(directory) != 'str': 
                raise TypeError("Data type of file directory should be string.") 
            if dataType(filename) != 'str': 
                raise TypeError("Data type of file name should be string.")
            if dataType(enc) != 'bool': 
                raise TypeError("Data type of enc (encrypt) should be boolean.")
        except TypeError as e: print(e); return False        
        # convert all the current data into string (Part 2)
        cur_node=self.__head
        s=""
        while cur_node.next:
            cur_node = cur_node.next
            data=cur_node.getData()
            s=s+u.data2str(data)+"\n" # '\n' is the data separator
        s=s[0:len(s)-1]     # the last '\n' is removed
        # adding file header (Part 3)        
        # adding file header (34 character (23+10+1)long string)
        # of which the last 10 digits are integer; the last digit is the keyindx
        fileheader='LINKEDLIST FILE HEADER:' + str(encrypt.randomInteger(10))
        # encrypt the data string (Part 4)
        if enc:
            s=encrypt.encrypt(s,int(fileheader[32]))
        s=fileheader+'\n'+s
        # adding md5 hash at the beginning of the file (Part 5)
        md5hashstr=u.getHashCode(s,"md5")
        s="MD5:"+md5hashstr+"\n"+s    # Newly 37(4+32+1) characters are added
        # second phase (final) encryption and encryption tagging (Part 6)
        if enc:
            s="[ENCRYPTED]"+'\n'+s
            s=encrypt.encrypt(s,10)
        else:
            s="[NOT ENCRYPTED]"+'\n'+s
        # convert string into byte array using 'utf-8' encoding (Part 7)
        ba=None # byte array
        try:
            ba=s.encode('utf-8') # converting string to bytearray 
        except Exception as e: print(e); return False    
        # creating or opening .pds data file and writing to the file (Part 8)
        directory=directory.strip(); filename=filename.strip(); fileaddr=""
        try:
            fileaddr=u.createDataFile(directory, filename)
            fileaddr=os.path.abspath(fileaddr)
        except Exception as e: 
            print(e); print("List data are not saved."); return False
        fo=None
        try:
            fo=open(fileaddr,'wb')
            if not fo:
                print("Data file cannot be opened. Saving not successful.")
                self.__file=""
                return False
            fo.write(ba)
            fo.close()
            self.__file=fileaddr            
        except IOError as e: print(e); return False
        except Exception as e: print(e); return False
        if enc:
            print("Encrypted Data Saved Successfully into '"+self.__file+"'")
        else:
            print("Plain Data Saved Successfully into '"+self.__file+"'")
        return True




    # loadDataFromFile() function loads stack data in memory from the data file
    # File loading also occurs in 8 steps, but in reverse order of file saving
    # 8 steps: (1) checking inputs (2) reading the binary data file 
    # (3) decoding the data file with utf-8 (4) check the file encryption tag
    # (5) first phase decryption using keyid=10 (6) checking MD5 hash
    # (7) removing file header (8) loading string data into a list after conversion
    # >>> myll=lnkl.LinkedList()
    # >>> myll
    # <Linked List: size=0, Data=() >
    # >>> myll.loadDataFile()
    # ['125', '1.25', '"hello world"', '["hello","world",74.12]', '("hello",[4,8,7.2,None],"world",74.12)', '{2:45,"a":"abc","rolls":[12,14,13]}', '148.25', '"hello"']
    # >>> myll
    # <DLinked List: size=8, Data=(125, 1.25, 'hello world', ['hello', 'world', 74.12], ('hello', [4, 8, 7.2, None], 'world', 74.12), {2: 45, 'a': 'abc', 'rolls': [12, 14, 13]}, 148.25, 'hello') >
    def loadDataFromFile(self, fileaddr=datadir+os.sep+"linkedlist.pcds"):
        # checking inputs (Part 1)
        if not u.checkDataFileAddr(fileaddr):
            return False
        # opening data file in read mode (Part 2)
        fileaddr=os.path.abspath(fileaddr)
        self.__file=fileaddr
        fo=None; s=""; bs=""        
        try:
            fo=open(fileaddr,'rb')
            # if file is blank
            fo.seek(0,2)
            filesize=fo.tell()
            if filesize==0:
                print("Data File is empty")                    
                return False
            # reading bytes from the data file in byte array
            fo.seek(0,0)            # come to the beginning of the file
            bs=fo.read(filesize)    # bs=binary byte string
            fo.close()
        except Exception as e: print(e); return False
        # decoding byte array into string (Part 3)
        try:            
            s=bs.decode('utf-8')                
        except Exception as e: print(e); return False
        # checking the encryption tag (Part 4)
        encrypted=False
        if '\v' in s:
            encflagstr=s.split('\v')[0]
        elif '\n' in s:
            encflagstr=s.split('\n')[0]
        if encflagstr=="[NOT ENCRYPTED]":
            encrypted=False; s=s[16:len(s)]
        elif encflagstr=="yo+sRFr-oli":
            encrypted=True; s=s[12:len(s)]
        # first phase decryption using keyid=10 (Part 5)
        if encrypted: s=encrypt.decrypt(s,10)
        # extracting and checking md5hash strings(Part 6)
        if len(s) < 38:
            print("File has no data. Loading is failed.")
            return False
        fileMD5=s[4:36]
        hdstr=s[37:len(s)] # hdstr=header+data string
        newMD5=u.getHashCode(hdstr,"md5")        
        try:            
            if newMD5 != fileMD5:
                raise Exception("Data file is corrupt as hash missmatch. Loading is failed.")
        except Exception as e: print(e); return False
        s=hdstr
        # decrypting the data string into readable string(Part 7)         
        try:
            # In the File Header, the last character is the keyid
            # Length of File Header = 34 (23 char+10 digits+'\n')
            if len(s) < 35:
                print("File has no data. Loading is failed")
                return False
            if s[0:23] == 'LINKEDLIST FILE HEADER:':
                keyid=int(s[32])
                s=s[34:len(s)]  # leave the header part 
                if encrypted:                                 
                    s=encrypt.decrypt(s,keyid)
            else: raise Exception("Data file is corrupt.")
        except Exception as e: print(e); return False
        # loading data into the linked list (Part 8)        
        sl=s.split('\n') # sl=string list        
        try:
            self.clear() # head delinking, setting size to zero 
            cur_node=self.__head
            cur_node.setIndex(-1)
            i=0
            while cur_node:
                if i==len(sl): break
                cur_node.next=Node(u.str2data(sl[i]),i)
                #cur_node.next.setIndex(i)
                cur_node = cur_node.next
                i=i+1 
            self.__size = i                                           
        except Exception as e: 
            print(e); print("Data not loaded successfully."); return False
        print("Data Loaded Successfully from the file: '"+self.__file+"'")
        return True




    # removeDataFile(self) deletes the data file. If preserve is True, the
    # data file will not be deleted    
    def removeDataFile(self):        
        if not self.__preserve:
            try:            
                os.remove(self.__file)
                return True
            except Exception as e: print(e); return False
        else:            
            print("LinkList data file is preserved and cannot be deleted.")
            return False

# ------------------------ END of linkedlist.py file --------------------------

