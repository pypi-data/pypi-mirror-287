'''
Module Description
--------------------
module filename: bstree.py
module name: bstree (Binary Search Tree)
Content: Functions: dataType(data), sort(datalist=[],asc=True), 
        search(data, datalist=[])

        Class: Node, BinarySearchTree (Binary Search Tree)

Description: This module creates a binary search tree that can be used to sort data,
    to find the maximum and minimum and to search for a data or key etc. It can
    handle only integer, float and string type data. Since it removes the duplicate
    data, it can be used in set data structure. It can be used in database management.

    Steps to use this tree:
        1) Load data by append function or by list or by tuple of data
        2) Build the tree by buildTree() function
        3) Now, printTree(), sortTree(), searchTree(data) can be used for
           printing, sorting and searching operations.

    Node Class:
        Constructor: Node(data)
        getValue(), getOriginalData(), printData(), setData(data), getParentNode(), 
        getLeftNode(), getRightNode(), isString(), __str__(), __repr__()

    BinarySearchTree (Binary Search Tree) Class:
        Constructor: BinarySearchTree()
        Class Methods: append(data), loadDataFromList(datalist), getOriginalData(),
        loadDataFromTuple(tuple), getOriginalSize(), min(), getMinNode(), max(),
        getMaxNode(), findRootNode(), getRootData(), getRootNode(), buildTree(), 
        __placeNode(self,node1,newnode), isBuilt(), printTree(), __printNode(self,node),
        sortTree(asc=True), __sortNodes(node), __sortNodesDesc(node), isSorted(),
        getSortOrder(), getSortedData(), getSortedSize(), searchTree(), 
        __search(self,node,data), __len__(), __str__(), __repr__(), clear(),

        setDataFileAddress(directory=datadir, filename="bstree"), getDataFileAddress(),        
        isFilePreserved(), setFilePreserve(preserve=True),
        save(directory="", filename="bstree", enc=True),
        loadDataFromFile(fileaddr=datadir+os.sep+"bstree.pdsf"), removeDataFile()
        
    
    Module level functions:
        sort(datalist=[],asc=True), search(data, datalist=[]), min(datalist=[])
        max(datalist=[])

    Suported Data Types: int, float, str

    Data are saved in a binary file with extension .pcds (python common data structure file)
    Data encryption is supported for security of data.
Author: A K M Aminul Islam
Last Modified: Monday July 22 2024 03:30 PM
Version:1.1.2
Dependencies: utilities, encrypt, os


'''


from pcds import utilities as u
from pcds import encrypt
import os


import pcds
datadir=pcds.getDataDirectory()
version='1.1.2'



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




# ------------------------ Node class ----------------------------
# Node instances retain data or key of the nodes of the tree
class Node:
    __data=None
    __isstr=False
    left=None
    right=None
    parent=None


    # constructor function
    # string data is stored as integer
    def __init__(self,data=None):
        try:
            if dataType(data) not in ['int','float','str']:
                raise TypeError("Unsupported data type. Valid types are 'int','float','str'.")
            if dataType(data) == 'str':
                self.__data=int(u.str2int(data))
                self.__isstr=True
            else:
                self.__data=data
                self.__isstr=False
        except TypeError as e: print(e); return None       
        self.left=None
        self.right=None
        self.parent=None


    # ----------------------- getter and setter methods ----------------------
    # getValue(self) returns only the numeric data of the node
    def getValue(self):
        return self.__data
        

    # getOriginalData(self) returns numeric data into numeric form and string 
    # data into string form
    def getOriginalData(self):
        if not self.__isstr:
            return self.__data
        else:
            return u.int2str(self.__data)



    # printData(self) returns both the numeric and string data of the node
    # in the string form
    def printData(self):
        if not self.__isstr:
            return str(self.__data)
        else:
            return u.int2str(self.__data)


    # setData(self, data) sets data in the node
    def setData(self, data):
        try:
            if dataType(data) not in ['int','float','str']:
                    raise TypeError("Unsupported data type. Valid types are 'int','float','str'.")
            if dataType(data) == 'str':
                self.__data=int(u.str2int(data))
                self.__isstr=True
            else:
                self.__data=data
                self.__isstr=False
        except TypeError as e: print(e); return None



    # getParentNode(self) returns the parent of the current node
    def getParentNode(self):
        return self.parent



    # getLeftNode(self) returns the left node of the current node
    def getLeftNode(self):
        return self.left



    # getRightNode(self) returns the right node of the current node
    def getRightNode(self):
        return self.right



    # isString(self) returns true if a node carries a string type data
    def isString(self):
        return self.__isstr



    # __str__(self) stringifies the node instance when called by str(node)
    def __str__(self):
        if self.__isstr:
            return "<Binary Tree Node: data='"+self.printData()+"'>"
        else: return "<Binary Tree Node: data="+self.printData()+">"



    # __repr__(self) returns the output when called by print(node) 
    def __repr__(self):
        return self.printData()






# ----------------------------- Binary Tree class ------------------------------
class BinarySearchTree:
    # private properties    
    __rootNode=None     # root node which is calculated at the beginning
    __nodeList=[]       # a list that contains all data nodes entered into the tree    
    __treeBuilt=False   # boolean to store tree built info
    __sortedData=[]     # list contains the final sorted data
    __sindx=-1          # holds search index
    __sresult=-1        # holds search result
    __sortAsc=None


    # BinaryTree constructor
    def __init__(self):
        self.__rootNode=None
        self.__nodeList=[]
        self.__sortedData=[]



    # append(self,data=None) adds data at the end of the list
    def append(self,data=None):
        try:
            if data==None:
                raise ValueError("Data or key not given.")
            if dataType(data) not in ['int','float','str']:
                raise Exception("Unsupported data type. Valid types are 'int','float','str'.")
        except Exception as e: print(e); return None        
        self.__nodeList.append(Node(data))
        



    # loadDataFromList(self,data) adds list data into the tree
    def loadDataFromList(self,listdata):
        try:
            if dataType(listdata) == 'list':
                for item in listdata:
                    if dataType(item) not in ['int','float','str']:
                        raise Exception("Unsupported data type. Valid types are 'int','float','str'.")
            else:
                raise ValueError("Data argument is not a list.")
        except Exception as e: print(e); return None
        for item in listdata:
            self.__nodeList.append(Node(item))




    # loadDataFromTuple(self,tupledata) adds data in the tuple into the tree
    def loadDataFromTuple(self,tupledata):
        try:
            if dataType(tupledata) == 'tuple':
                for item in tupledata:
                    if dataType(item) not in ['int','float','str']:
                        raise Exception("Unsupported data type. Valid types are 'int','float','str'.")
            else:
                raise ValueError("Data argument is not a tuple.")
        except Exception as e: print(e); return None
        for item in tupledata:
            self.__nodeList.append(Node(item))
        



    # getOriginalData(self) returns the original data entered in the tree in tuple form
    def getOriginalData(self):
        tmplist=[]
        for datanode in self.__nodeList:
            tmplist.append(datanode.getOriginalData())
        return tuple(tmplist)




    
    # getOriginalSize(self) returns the number of original data entered in the tree
    def getOriginalSize(self):
        return len(self.__nodeList)




    # min() returns the minimum data in the raw tree
    def min(self):
        minnode=self.__nodeList[0]
        for nodeitem in self.__nodeList:
            if nodeitem.getValue() < minnode.getValue():
                minnode=nodeitem
        return minnode.getOriginalData()




    # getMinNode() returns the minimum data in the raw tree
    def getMinNode(self):
        minnode=self.__nodeList[0]
        for nodeitem in self.__nodeList:
            if nodeitem.getValue() < minnode.getValue():
                minnode=nodeitem
        return minnode




    # max() returns the maximum data in the raw tree
    def max(self):
        maxnode=self.__nodeList[0]
        for nodeitem in self.__nodeList:
            if nodeitem.getValue() > maxnode.getValue():
                maxnode=nodeitem
        return maxnode.getOriginalData()




    # getMaxNode() returns the maximum data in the raw tree
    def getMaxNode(self):
        maxnode=self.__nodeList[0]
        for nodeitem in self.__nodeList:
            if nodeitem.getValue() > maxnode.getValue():
                maxnode=nodeitem
        return maxnode




    # findRootNode(self) calculates the root node of the tree 
    # Root Node = Closest node to the mean data ((min+max)//2)
    def findRootNode(self):
        # find the average
        mindata=self.getMinNode().getValue()
        maxdata=self.getMaxNode().getValue()
        avg=(mindata+maxdata)//2       
        # get the closest node to the average
        root=self.__nodeList[0]
        diff=avg-self.__nodeList[0].getValue(); 
        minDiff=abs(diff); 
        for item in self.__nodeList:
            diff=avg-item.getValue()            
            if diff<0: diff=-1*diff            
            if diff<minDiff: 
                minDiff=diff
                root=item            
        # remove the duplicate root nodes
        freq=0; i=0; rootindices=[]
        for item in self.__nodeList:
            if item.getValue()==root.getValue():
                freq=freq+1
                if freq>1:rootindices.append(i)
            i=i+1        
        rootindices.reverse()
        for indx in rootindices:
            del(self.__nodeList[indx]) 
        self.__rootNode=root

        


    # getRootData(self) returns the calculated root node value of the tree
    def getRootData(self):
        if self.__rootNode:
            return self.__rootNode.getOriginalData()




    # getRootNode(self) returns the calculated root node value of the tree
    def getRootNode(self):
        if self.__rootNode:
            return self.__rootNode




    # buildTree(self,asc=True) builds the binary tree and sets the __treebuilt 
    # boolean to True 
    def buildTree(self):
        try:            
            if len(self.__nodeList) == 0:
                raise Exception("The binary tree has no data.")
        except ValueError as e: print(e); return None
        # find the root node first
        self.findRootNode()
        # build tree
        for nodeItem in self.__nodeList:            
            if nodeItem.getValue() == self.__rootNode.getValue():                
                continue
            else:                
                self.__placeNode(self.__rootNode,nodeItem)
        self.__treeBuilt=True



    # __placeNode(self,node1,newnode,asc=True) helps buildTree() function 
    # to build the tree
    def __placeNode(self,node1,newnode):
        tmpnode=None        
        # arrange nodes in ascending order; place smaller data to left node
        if newnode.getValue() > node1.getValue():
            if node1.right==None: # no right node
                node1.right=newnode
                newnode.parent=node1
            else:
                self.__placeNode(node1.right,newnode)
        elif newnode.getValue() < node1.getValue():
            if node1.left==None: # no left node
                node1.left=newnode
                newnode.parent=node1
            else:
                self.__placeNode(node1.left,newnode)
        elif newnode.getValue() == node1.getValue():
            pass #del(newnode)




    # isBuilt() returns True if tree is built
    def isBuilt(self):
        return self.__treeBuilt




    # printTree(self) prints the final sorted data in the tree
    # >>> t1.getDataList()
    # [20, 50, 4, 7, 8, 12, 15, 30, 35, 40, -5]
    # >>> t1.printTree()
    # -5
    # 4
    # 7
    # 8
    # 12
    # 15
    # 20
    # 30
    # 35
    # 40
    # 50
    # >>>
    def printTree(self):
        if not self.__treeBuilt:
            print("Tree not built yet. Use buildTree() first."); return None
        self.__printNode(self.__rootNode)


    # __printNode(self,node) helps to print the final sorted tree
    def __printNode(self,node):        
        if node.left:
            self.__printNode(node.left)        
        print(node.getOriginalData())
        if node.right:
            self.__printNode(node.right)
        




    # sortTree(self,asc=True) stores the sorted data in the list self.__sortedData
    # in ascending order if asc=True or in descending order if asc=False
    # >>> t1.getDataList()
    # [20, 50, 4, 7, 8, 12, 15, 30, 35, 40, -5, 20, 50, 4, 7, 8, 12, 15, 30, a, 35, 40, b, ab, c, bc, cb, -10, -5, 100]
    # >>> t1.sortTree()
    # [-10, -5, 4, 7, 8, 12, 15, 20, 30, 35, 40, 50, 'a', 'b', 'c', 100, 'ab', 'bc', 'cb']
    def sortTree(self,asc=True):
        try:            
            if dataType(asc) != 'bool':
                raise ValueError("Argument must be boolean (True/False).")
            
            if len(self.__nodeList) == 0:
                raise Exception("The binary tree has no data.")
        except ValueError as e: print(e); return None
        if not self.__treeBuilt:
            print("Tree is not built yet, but is going to be built.");
            self.buildTree()
        self.__sortedData=[]
        if asc: 
            self.__sortNodes(self.__rootNode)
            self.__sortAsc=True
        else: 
            self.__sortNodesDesc(self.__rootNode)
            self.__sortAsc=False




    # __sortNodes(self,node) helps sortTree() function to store the tree data
    # in ascending order (left to right)
    def __sortNodes(self,node):        
        if node.left:
            self.__sortNodes(node.left)
        #if node.isString(): self.__sortedData.append(node.printData())
        #else: self.__sortedData.append(node.getValue())
        self.__sortedData.append(node.getOriginalData())
        if node.right:
            self.__sortNodes(node.right)




    # __sortNodesDesc(self,node) helps sortTree() function to store the tree data
    # in descending order (right to left)
    def __sortNodesDesc(self,node): 
        if node.right:
            self.__sortNodesDesc(node.right)
        #if node.isString(): self.__sortedData.append(node.printData())
        #else: self.__sortedData.append(node.getValue())
        self.__sortedData.append(node.getOriginalData())
        if node.left:
            self.__sortNodesDesc(node.left)
        



    # isSorted() returns True if the tree data are sorted
    def isSorted(self):
        if self.__sortedData: return True
        else: return False




    # getSortOrder(self) returns the current sort order: 'ascending',
    # 'descending' or None
    def getSortOrder(self):
        if self.__sortAsc==True: return 'ascending'
        elif self.__sortAsc==False: return 'descending'
        else: return None




    # getSortedData(self) returns the sorted data entered in the tree in tuple form
    def getSortedData(self):
        return tuple(self.__sortedData)




    # getSortedSize(self) returns the number of sorted data in the tree
    def getSortedSize(self):
        if len(self.__nodeList) == 0: return 0
        if len(self.__sortedData) == 0:            
            if not self.__treeBuilt:
                self.buildTree()
            self.sortTree()
        return len(self.__sortedData)



    # searchTree(self, data=None) searches the tree for exact match and returns the 
    # index value of the sorted data list (in ascending order) where the search data 
    # is found. If data is not present in the sorted tree, None is returned
    # >>> t1.getDataList()
    # [20, 50, 4, 7, 8, 12, 15, 30, 35, 40, -5, 20, 50, 4, 7, 8, 12, 15, 30, a, 35, 40, b, ab, c, bc, cb, -10, -5, 100, 14.78, 20, 80.95]
    # >>> t1.sortTree()
    # [-10, -5, 4, 7, 8, 12, 14.78, 15, 20, 30, 35, 40, 50, 'a', 'b', 'c', 80.95, 100, 'ab', 'bc', 'cb']
    # >>> t1.searchTree(14.78)
    # 6
    # >>> t1.searchTree('a')
    # 13
    # >>> t1.searchTree('cb')
    # 20
    # >>> t1.searchTree(-10)
    # 0
    # >>> t1.searchTree(10)
    # False
    def searchTree(self, data=None):
        try:
            if data==None:
                raise ValueError("Data or key not given.")
            if dataType(data) not in ['int','float','str']:
                raise Exception("Unsupported data type. Valid types are 'int','float','str'.")
        except Exception as e: print(e); return None
        if not self.__treeBuilt:
            print("Tree is not built yet, but is going to be built.");
            self.buildTree()
        if dataType(data) == 'str':
            data=data.strip(); data=u.str2int(data)
        self.__sindx=-1
        self.__sresult=-1
        self.__search(self.__rootNode,data)
        if self.__sresult>=0: return self.__sresult
        else: return None


    # __search(self,node,data) helper function used in searching
    def __search(self,node,data):
        if node.left:
            self.__search(node.left,data)
        self.__sindx=self.__sindx+1
        if node.getValue() == data:
            self.__sresult=self.__sindx        
        if node.right:
            self.__search(node.right,data)




    # __len__(self) returns the number of data in the tree
    # If not sorted, it returns the number of original data, and if sorted
    # it returns the number of sorted data
    def __len__(self):
        if self.__sortedData: return len(self.__sortedData)
        else: return len(self.__nodeList)




    # __str__(self) stringifies data list when called by str(tree)
    def __str__(self):
        if self.__sortedData:
            return "<Binary Search Tree(sorted): no. of nodes="+str(len(self.__sortedData))+", data="+str(tuple(self.__sortedData))+">"
        elif self.__nodeList:
            return "<Binary Search Tree(not sorted): no. of nodes="+str(len(self.__nodeList))+", data="+str(self.getOriginalData())+">"
        else: 
            return "<Binary Search Tree: no. of nodes=0, data=()>"




    # __repr__(self) prints data list when called by print(tree)
    def __repr__(self):
        if self.__sortedData:
            return str(tuple(self.__sortedData))
        elif self.__nodeList:
            return str(self.getOriginalData())
        else: return "()"




    # clear(self) removes all data from the tree 
    def clear(self):
        self.__init__()
        

    # ------------------------- disk I/O functions -----------------------



    __preserve=True
    __fileaddr=""



    # setDataFileAddress(self, directory=datadir, filename="bstree") sets 
    # the absolute address of the .pcds data file in the private variable __fileaddr
    def setDataFileAddress(self, directory=datadir, filename="bstree"):
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
            self.__fileaddr=os.path.abspath(fileaddr)
        except Exception as e: print(e); return None
        


    
    # getDataFileAddress(self) returns the absolute address of the .ndsf data file
    def getDataFileAddress(self):
        if self.__fileaddr:
            return self.__fileaddr



 
    # isFilePreserved(self) returns True if 'preserve' parameter is set to True
    def isFilePreserved(self):
        return self.__preserve




    # setFilePreserve(self, preserve=True) sets the 'preserve' parameter 
    # True or False. If preserved, data file will not be deleted by 
    # removeDataFile() function.
    def setFilePreserve(self, preserve=True):
        try:
            if dataType(preserve) != 'bool': 
                raise TypeError("Data type of preserve should be boolean.")
        except TypeError as e: print (e); return None
        self.__preserve=preserve




    # save(self, directory=datadir, filename="dlinkedlist", enc=True) saves all data 
    # in the data file newly created
    # 8 steps: (1) checking inputs (2) data to string conversion 
    # (3) adding file header (4) encryption of data string (5) adding MD5 hash
    # (6) final encryption and encription tagging (7) encoding with 'utf-8'   
    # (8) writing to data file
    # >>> t1=bst.BinarySearchTree()
    # >>> t1
    # (10, 20, 3.478, ab, c, 100, 5, 78, 150, 6.78, a, b)
    # >>> t1.buildTree()
    # >>> t1.sortTree()
    # [3.478, 5, 6.78, 10, 20, 'a', 'b', 'c', 78, 100, 150, 'ab']
    # >>> t1.save()
    # Data Saved Successfully.
    def save(self, directory=datadir, filename="bstree", enc=True):
        try:
            # checking inputs (Part 1) 
            if dataType(directory) != 'str': 
                raise TypeError("Data type of file directory should be string.") 
            if dataType(filename) != 'str': 
                raise TypeError("Data type of file name should be string.")
            if dataType(enc) != 'bool': 
                raise TypeError("Data type of enc (encrypt) should be boolean.")
        except TypeError as e: print(e); return False
        # Tree will be built and sorted if not done previously
        if not self.__treeBuilt:
            self.buildTree()
        if self.__sortedData==[]:
            self.sortTree()        
        # convert all the current data into string (Part 2)        
        s=""
        for data in self.__sortedData:        
            s=s+u.data2str(data)+"\n" # '\n' is the data separator
        s=s[0:len(s)-1]     # the last '\n' is removed
        # adding file header (Part 3)        
        # adding file header (35 character (24+10+1)long string)
        # of which the last 10 digits are integer; the last digit is the keyindx
        fileheader='BINARY TREE FILE HEADER:' + str(encrypt.randomInteger(10))
        # encrypt the data string (Part 4)
        if enc:            
            s=encrypt.encrypt(s,int(fileheader[33]))
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
        except Exception as e: print(e);  return False        
        # creating or opening .pds data file and writing to the file (Part 8)
        directory=directory.strip(); filename=filename.strip(); fileaddr=""
        try:
            fileaddr=u.createDataFile(directory, filename)
            fileaddr=os.path.abspath(fileaddr)
        except Exception as e: 
            print(e); print("Tree data are not saved."); return False
        fo=None
        try:
            fo=open(fileaddr,'wb')
            if not fo:
                print("Data file cannot be opened. Saving not successful.")
                self.__fileaddr=""
                return False
            fo.write(ba)
            fo.close()
            self.__fileaddr=fileaddr            
        except IOError as e: print(e); return False
        except Exception as e: print(e); return False
        if enc:
            print("Encrypted Data Saved Successfully into '"+self.__fileaddr+"'")
        else:
            print("Plain Data Saved Successfully into '"+self.__fileaddr+"'")
        return True



    # loadDataFromFile() function loads stack data in memory from the data file
    # File loading also occurs in 8 steps, but in reverse order of file saving
    # 8 steps: (1) checking inputs (2) reading the binary data file 
    # (3) decoding the data file with utf-8 (4) check the file encryption tag
    # (5) first phase decryption using keyid=10 (6) checking MD5 hash
    # (7) removing file header (8) loading string data into a list after conversion
    # >>> t1.clear()
    # >>> t1.load()
    # Data Loaded Successfully.
    # >>> t1
    # (3.478, 5, 6.78, 10, 20, 'a', 'b', 'c', 78, 100, 150, 'ab')
    def loadDataFromFile(self, fileaddr=datadir+os.sep+"bstree.pcds"):
        # checking inputs (Part 1)        
        if not u.checkDataFileAddr(fileaddr): return False           
        # opening data file in read mode (Part 2)
        fileaddr=os.path.abspath(fileaddr)
        self.__fileaddr=fileaddr
        fo=None; s=""; bs=""        
        try:
            fo=open(fileaddr,'rb')
            # if file is blank
            fo.seek(0,2)
            filesize=fo.tell()
            if filesize==0:
                print("Data File is empty")                    
                return None
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
            # Length of File Header = 35 (24 char+10 digits+'\n')
            if len(s) < 36:
                print("File has no data. Loading is failed")
                return False
            if s[0:24] == 'BINARY TREE FILE HEADER:':
                keyid=int(s[33])
                s=s[35:]  # leave the header part 
                if encrypted:                                 
                    s=encrypt.decrypt(s,keyid)
            else: raise Exception("Data file is corrupt.")
        except Exception as e: print(e); return False
        # loading data into the binary search tree (Part 8)        
        sl=s.split('\n') # sl=string list        
        try:
            self.clear() # head delinking, setting size to zero             
            for strdata in sl:                
                self.__nodeList.append(Node(u.str2data(strdata)))
        except Exception as e: 
            print(e); print("Data loading failed."); return False
        print("Data Loaded Successfully.")
        # Post loading work
        self.buildTree()
        self.sortTree()
        return True



    # removeDataFile(self) deletes the data file when the preserve parameter is False.
    # If preserve is True, the data file will not be deleted    
    def removeDataFile(self):        
        if not self.__preserve:
            try:            
                os.remove(self.__fileaddr); return True
            except Exception as e: print(e); return False
        else:            
            print("BSTree data file is preserved and cannot be deleted.")
            return False


# ------------------------- End of BinarySearchTree -----------------------------

# ------------- Extra Functions: sort(), search(), min(), max() ----------------
#
# sort(datalist=[],asc=True) sorts the datalist either in ascending or
# in descending order using binary search tree. If asc=True sort operation 
# will be done in ascending order or asc=False, sorting will be done in 
# descending order
def sort(datalist=[],asc=True):    
    bst=BinarySearchTree()
    bst.loadDataFromList(datalist)
    bst.buildTree()
    bst.sortTree(asc)
    return bst.getSortedData()




# search(data, datalist=[]) searches the given data in the given data list.
# If data is present, it returns the index position in the sorted tree (in
# ascending order) where the data is found. If the data is not found,
# False is returned.
def search(data, datalist=[]):    
    bst=BinarySearchTree()
    bst.loadDataFromList(datalist)
    bst.buildTree()
    return bst.searchTree(data)




# min() returns the minimum data present in the data list
def min(datalist=[]):
    return u.min(datalist)




# max() returns the minimum data present in the data list
def max(datalist=[]):
    return u.max(datalist)



