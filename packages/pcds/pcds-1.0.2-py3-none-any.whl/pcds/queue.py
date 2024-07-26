'''
Module Description
--------------------
module filename: queue.py
module name: queue
Content: dataType() function, Queue class
Description: Queue class creates queue data structure
    Queue class public properties and methods
    -----------------------------------------
    Queue(maxsize), getSize(), getMaxSize(), setMaxSize(), getDataString(),
    __len__(), __str__(), 
    __repr__(), __del__(), enQueue(data), deQueue(), clear(),  
    
    setFileAddress(directory="data", filename="queue"), getFileAddress(),
    setFilePreserve(preserve=True), isFilePreserved(), removeDataFile(),
    save(directory="data", filename="queue", enc=True), 
    loadDataFile(fileaddr=packroot+"os.sep"+"pcds_data"+os.sep+"queue.pcds"),
  
    Suported Data Types: int, float, str, bool, tuple, list, dictionary

    Data are saved in a binary file with extension .pcds (python data structure file)

Author: A K M Aminul Islam
Email: aminul71bd@gmail.com

Last Modified: Thursday July 18 2024 4:55 AM

Version:1.1.2

Dependencies: utilities, encrypt, os
'''
from pcds import utilities as u
from pcds import encrypt
import os



version='1.1.2'
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





# Queue class creates an instance of a queue datastructure
#
class Queue:
	
    __data=None     # a private list holding data of the queue
    __maxsize=None  # Maximum size of the queue. If length > size, data dequeued
    __size=None     # holds the current length of the queue (read only)
    __fileaddr=None # string holds the data file path with name
    __preserve=None # keeps data file in the disk when the Queue object is deleted

	
    # constructor function	
    def __init__(self, maxsize=100):
        try:
            # checking inputs
            if dataType(maxsize) != 'int': 
                raise TypeError("Error: Maxsize must be an integer data.")
            if maxsize < 1: 
                raise ValueError("Error: Maxsize must be a positive whole number.")
        except Exception as e: print(e); return None
        self.__maxsize=maxsize
        self.__data=[]
        self.__size=0
        self.__fileaddr=datadir+os.sep+"queue.pdsf"
        self.__preserve=True


    # -------------------------- setter and getter methods --------------------------
    # getSize(self) returns the current size (number of data) of the queue
    def getSize(self):
        if self.__maxsize==None: return None
        return self.__size





    # getMaxSize(self) returns the maximum size of the queue
    def getMaxSize(self):
        if self.__maxsize==None: return None
        return self.__maxsize




    # changeMaxSize(self) changes the current maximum size of the queue
    # to the new given size
    def changeMaxSize(self, maxsize=100):
        try:
            # checking inputs
            if dataType(maxsize) != 'int': 
                raise TypeError("Error: Maxsize must be an integer data.")
            if maxsize < 1: 
                raise ValueError("Error: Maxsize must be a positive whole number..")
            if maxsize < self.__size:
                raise ValueError("Warning! The length of the queue cannot be less than the current size.")
        except Exception as e: print(e); return None
        self.__maxsize=maxsize



    
    # getDataString(self) shows current data in the queue in tuple-string form
    # problem: tuple([1])=(1,), but tuple([1,2])=(1,2)
    def getDataString(self):
        if self.__maxsize==None: return None
        if len(self.__data)==1: return "("+str(self.__data[0])+")"
        return str(tuple(self.__data))




   # __len__(self) returns the number of data in the queue
    def __len__(self):
        if self.__maxsize==None: return None
        return self.__size




    # __str__(self) returns a string of the queue instance with data
    def __str__(self):
        if self.__maxsize:
            return "<Queue ["+str(self.getSize())+"/"+str(self.getMaxSize())+"], Head:" + self.getDataString() + ":Tail>"
        else: return ""




    # __repr__(self) returns queue data in printable form
    def __repr__(self):        
        return self.__str__()



    # -------------------- main functions of the queue ----------------------
    # enQueue() function stores data at the tail of the queue and 
    # returns True. If queue becomes full, the head data is returned.
    def enQueue(self,data):
        if self.__maxsize==None: return None
        try:
            if dataType(data) not in ['str','int','float','bool','NoneType','tuple','list','dict']:
                raise Exception("Error: Queue does not support the datatype given here.")                         
        except Exception as e: print(e); return None
        self.__data.append(data)
        self.__size = self.__size + 1       
        if self.__size > self.__maxsize:
            print("Queue is already full. So, head is dequeued.")
            return self.deQueue()
        



	
    # deQueue() function removes data from the head of the queue
    def deQueue(self):
        if self.__maxsize==None: return None
        if self.__size > 0:            
            head=self.__data[0]
            del(self.__data[0])
            self.__size = self.__size - 1        
            return head
        else:
            print("Queue is empty.") 
            return None
            



    # clear() function removes all data from the queue
    def clear(self):
        if self.__maxsize==None: return None
        self.__init__(self.__maxsize)
        
        




# ------------------------- File I/O Operations -----------------------------
#

    # setFileAddress(self, directory="data", filename="queue") sets 
    # the absolute address of the .pcds data file in the private variable __fileaddr
    # But, the file is not created physically
    def setFileAddress(self, directory=datadir, filename="queue"):
        if self.__maxsize==None: return None
        try:
            # checking inputs (Part 1) 
            if dataType(directory) != 'str': 
                raise TypeError("Error: Data type of file directory should be string.") 
            if dataType(filename) != 'str': 
                raise TypeError("Error: Data type of file name should be string.")            
        except TypeError as e: print(e); return None
        directory=directory.strip(); filename=filename.strip(); fileaddr=""
        try:            
            fileaddr=u.createDataFileAddr(directory, filename)
            self.__fileaddr=os.path.abspath(fileaddr)
        except Exception as e: print(e); return None





    # getDataFile(self) returns the absolute address of the .pdsf data file
    def getFileAddress(self):
        if self.__fileaddr:
            if self.__maxsize==None: return None
            return self.__fileaddr





    # isFilePreserved(self) returns True if 'preserve' parameter is set to True
    def isFilePreserved(self):
        if self.__maxsize==None: return None
        return self.__preserve




    # setFilePreserve(self, preserve=True) sets the 'preserve' parameter 
    # True or False. If preserved, data file will not be deleted by 
    # removeDataFile() function
    def setFilePreserve(self, preserve=True):
        if self.__maxsize==None: return None
        try:
            if dataType(preserve) != 'bool': 
                raise TypeError("Error: Data type of preserve should be boolean.")
        except TypeError as e: print (e); return None
        self.__preserve=preserve





    # delete(self) deletes the data file. If preserve is True, the
    # data file will not be deleted    
    def removeDataFile(self):
        if self.__maxsize==None: return None
        if not self.__preserve:
            try: 
                if os.path.exists(self.__fileaddr) and os.path.isfile(self.__fileaddr):
                    os.remove(self.__fileaddr)
                    self.__fileaddr=None
                    return True
                else:
                    raise Exception("Data file does not exist.")
            except Exception as e: print(e); return False
        else:            
            print("Queue data file is preserved and cannot be deleted.")
            return False
         




    # save() saves all data in the data file newly created
    # 8 steps: (1) checking inputs (2) data to string conversion 
    # (3) adding file header (4) encryption of data string (5) adding MD5 hash
    # (6) final encryption and encription tagging (7) encoding with 'utf-8'   
    # (8) writing to data file
    # >>> q1=q.Queue()
    # >>> q1.enQueue(10)
    # >>> q1.enQueue([1,2,3,(4,7,9)])
    # >>> q1.enQueue('hello')
    # >>> q1.enQueue('world')
    # >>> q1.enQueue({1:10,2:15,3:[40,50]})
    # >>> q1.enQueue(14.78)
    # >>> q1.enQueue(True)
    # >>> q1.enQueue(False)
    # >>> q1
    # <Queue of size 8, Head:(10, [1, 2, 3, (4, 7, 9)], 'hello', 'world', {1: 10, 2: 15, 3: [40, 50]}, 14.78, True, False):Tail>
    # >>> q1.save()
    # Data Saved Successfully into 'C:\Users\admin\pycodes\pds\data\queue.pdsf'
    # >>>
    def save(self, directory=datadir, filename="queue", enc=True):
        if self.__maxsize==None: return None
        try:
            # checking inputs (Part 1) 
            if dataType(directory) != 'str': 
                raise TypeError("Error: Data type of file directory should be string.") 
            if dataType(filename) != 'str': 
                raise TypeError("Error: Data type of file name should be string.")
            if dataType(enc) != 'bool': 
                raise TypeError("Error: Data type of enc (encrypt) should be boolean.")
        except TypeError as e: print(e); return False                       
        # convert all the current data into string (Part 2)        
        s="";i=0
        for item in self.__data:
            if i<self.__size-1:
                s=s+u.data2str(item)+"\n" # '\n' is the data separator
            else: 
                s=s+u.data2str(item) # '\n' not present
        # adding file header (Part 3)        
        # adding file header (28 character (18+10)long string)
        # of which the last 10 digits are integer; the last digit is the keyindx
        fileheader='QUEUE FILE HEADER:' + str(encrypt.randomInteger(10))
        # encrypt the data string (Part 4)
        if enc:            
            s=encrypt.encrypt(s,int(fileheader[27]))
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
        # creating or opening .pdsf data file and writing to the file (Part 8)
        directory=directory.strip(); filename=filename.strip(); fileaddr=""
        try:            
            fileaddr=u.createDataFile(directory, filename)            
            self.__fileaddr=os.path.abspath(fileaddr)
        except Exception as e: 
            print(e); print("Error: List data are not saved."); return False
        fo=None
        try:
            fo=open(self.__fileaddr,'wb')
            if not fo:
                print("Error: Data file cannot be opened. Saving operation is failed.")
                self.__fileaddr=""
                return False
            fo.write(ba)
            fo.close()
            self.__fileaddr=fileaddr        
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
    # >>> q1.clear()
    # >>> q1
    # <Queue of size 0, Head:():Tail>
    # >>> q1.load()
    # Data Loaded Successfully.
    # >>> q1
    # <Queue of size 8, Head:(10, [1, 2, 3, (4, 7, 9)], 'hello', 'world', {1: 10, 2: 15, 3: [40, 50]}, 14.78, True, False):Tail>
    def loadDataFromFile(self, fileaddr=datadir+os.sep+"queue.pcds"):
        if self.__maxsize==None: return False
        # checking inputs (Part 1)
        if not u.checkDataFileAddr(fileaddr):
            return False
        # opening the binary data file to read data (Part 2)
        self.__fileaddr=os.path.abspath(fileaddr)        
        fo=None; s=""; bs=""        
        try:
            fo=open(self.__fileaddr,'rb')
            # if file is blank
            fo.seek(0,2)
            filesize=fo.tell()
            if filesize==0:
                print("Data File is empty")                    
                return False            
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
            print("File has no data. Loading is stopped.")
            return False
        fileMD5=s[4:36]
        hdstr=s[37:len(s)] # hdstr=header+data string
        newMD5=u.getHashCode(hdstr,"md5")        
        try:            
            if newMD5 != fileMD5:
                raise Exception("Error: Data file is corrupt as hash missmatch. Loading is failed.")
        except Exception as e: print(e); return False
        s=hdstr
        # decrypting the encrypted data string into readable string(Part 7)
        try:
            # In the File Header, the last character is the keyid
            # Length of File Header = 29 (18 char+10 digits+'\n')
            if len(s) < 30:
                print("File has no data. Loading is failed")
                return False
            if s[0:18] == 'QUEUE FILE HEADER:':
                keyid=int(s[27])
                s=s[29:]  # leave the header part
                if encrypted:
                    s=encrypt.decrypt(s,keyid)                
            else: raise Exception("Data file is corrupt as file header is missing.")
        except Exception as e: print(e); return False
        # loading data into the data list (Part 8)        
        sl=s.split('\n') # sl=string list 
        sl=sl[0:len(sl)-1] # removing the last empty part    
        try:
            self.clear() # removing data            
            i=0
            for sdata in sl:
                self.__data.append(u.str2data(sdata))                
                i=i+1 
            self.__size = i
            # set the maxsize to the next tens (if size=25, maxsize=30)
            if self.__maxsize < self.__size: self.__maxsize = 10*(1+self.__size//10)
        except Exception as e:
            print(e); print("Error: Data not loaded successfully."); return False
        print("Data Loaded Successfully from the file: '"+self.__fileaddr+"'")
        return True







