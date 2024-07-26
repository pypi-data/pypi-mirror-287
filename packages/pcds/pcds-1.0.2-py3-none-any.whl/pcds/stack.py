'''
Module Description
--------------------
module filename: stack.py
module name: stack
Content: dataType() function, Stack class
Description: Stack class creates stack data structure
    Stack class public properties and methods
    -----------------------------------------
    Stack(), push(data), pop(), getSize(), getDataString(), getFileAddress(),
    setFileAddress(directory="data", filename="queue"), isFilePreserved(), 
    setFilePreserve(preserve=True), __len__(), getDataString(), __str__(), 
    __repr__(), clear(), removeDataFile(),
    save(directory="data", filename="queue", enc=True), 
    loadDataFile(fileaddr=packroot+os.sep+"pcds_data"+os.sep+"stack.pcds")

    Suported Data Types: int, float, str, bool, tuple, list, dictionary

    Data are saved in a binary file with extension .pcds (python data structure file)

Author: A K M Aminul Islam
Email: aminul71bd@gmail.com

Last Modified: Thursday July 18 2024 4:30 AM

Version:1.2.2

Dependencies: utilities, encrypt, os
'''
from pcds import utilities as u
from pcds import encrypt
import os


version='1.2.2'

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






# Stack class creates an instance of a stack data structure
#
class Stack:
	
    __data=[] # a private list holding data of the stack
    __size=0 # holds the number of data in the stack (read only)
    __fileaddr="" # string holds the data file address (path with name)
    __preserve=True # keeps data file in the disk if value is True
    

    # constructor function	
    def __init__(self):
        self.__data=[]
        self.__size=0



    # push() function stores data at the top of the stack and returns True.
    def push(self,data):
        try:
            if dataType(data) not in ['str','int','float','bool','NoneType','tuple','list','dict']:
                raise Exception("Invalid Data Type, so not accepted by the stack.") 
        except Exception as e: print(e); return None
        self.__data.append(data)
        self.__size = self.__size + 1        
        



    
    # pop() function removes data from the head of the stack
    def pop(self):
        if len(self.__data) > 0:            
            top=self.__data[len(self.__data)-1]
            del(self.__data[len(self.__data)-1])
            self.__size = self.__size - 1        
            return top
        else:
            self.__size = 0
            return None





    # getSize(self) returns the number of data in the stack
    def getSize(self):
        return self.__size





    # __len__(self) returns the number of data in the stack
    def __len__(self):
        return self.__size




    # getDataString(self) returns the current data in the stack in tuple-string form
    # problem: tuple([1])=(1,), but tuple([1,2])=(1,2)
    def getDataString(self): 
        if len(self.__data)==1: return "("+str(self.__data[0])+")"       
        return str(tuple(self.__data))



    # __str__(self) returns a string of the stack instance with data
    def __str__(self):
        return "<Stack[size="+str(self.__size)+"] Bottom:" + self.getDataString() + ":Top>"




   # __repr__(self) returns stack data in printable form
    def __repr__(self):        
        return self.__str__()




    # clear() function removes all data from the stack
    def clear(self):        
        self.__init__()
        



# -----------------------------------
# ------------------------- File I/O Operations -----------------------------
#
    # setFileAddress(self, directory=datadir, filename="stack") sets 
    # the absolute address of the .pcds data file in the private variable __fileaddr
    # It creates a blank data file
    def setFileAddress(self, directory=datadir, filename="stack"):
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





    # getDataFile(self) returns the absolute address of the .pcds data file
    def getFileAddress(self):
        if self.__fileaddr:
            return self.__fileaddr



 
    # isFilePreserved(self) returns True if 'preserve' parameter is set to True
    def isFilePreserved(self):
        return self.__preserve




    # setFilePreserve(self, preserve=True) sets the 'preserve' parameter 
    # True or False. If preserved, data file will not be deleted by 
    # removeDataFile()
    def setFilePreserve(self, preserve=True):
        try:
            if dataType(preserve) != 'bool': 
                raise TypeError("Data type of preserve should be boolean.")
        except TypeError as e: print (e); return None
        self.__preserve=preserve
        




    # removeDataFile(self) deletes the data file. If preserve is True, the
    # data file will not be deleted    
    def removeDataFile(self):        
        if not self.__preserve:
            try:
                if os.path.exists(self.__fileaddr) and os.path.isfile(self.__fileaddr):            
                    os.remove(self.__fileaddr)
                    self.__fileaddr=""
                    return True
                else:
                    raise Exception("Data file does not exist.")
            except Exception as e: print(e); return False
        else:            
            print("Stack data file is preserved and cannot be deleted.")
            return False





    # save() saves all data in the data file newly created
    # 8 steps: (1) checking inputs (2) data to string conversion 
    # (3) adding file header (4) encryption of data string (5) adding MD5 hash
    # (6) final encryption and encription tagging (7) encoding with 'utf-8'   
    # (8) writing to data file
    # >>> import stack as stk
    # >>> s1=stk.Stack()
    # >>> s1.push(10)
    # >>> s1.push(20)
    # >>> s1.push('hello')
    # >>> s1.push('world')
    # >>> s1.push(True)
    # >>> s1.push(False)
    # >>> s1.push(None)
    # >>> s1.save()
    # Data Saved Successfully into 'C:\Users\admin\pycodes\pcds\data\stack.pcds'
    # >>> s1
    # <Stack Bottom:(10, 20, 'hello', 'world', True, False, None):Top>
    def save(self, directory=datadir, filename="stack", enc=True):       
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
        s="";i=0
        for item in self.__data:
            if i<self.__size-1:
                s=s+u.data2str(item)+"\n" # '\n' is the data separator
            else: 
                s=s+u.data2str(item) # '\n' not present
        # adding file header (Part 3)        
        # adding file header (28 character (18+10)long string)
        # of which the last 10 digits are integer; the last digit is the keyindx
        fileheader='STACK FILE HEADER:' + str(encrypt.randomInteger(10))      
        # encrypt only the data string (Part 4)
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
            print(e); print("List data are not saved."); return False
        fo=None
        try:
            fo=open(self.__fileaddr,'wb')
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
    # >>> s1.clear()
    # >>> s1.load()
    # Data Loaded Successfully.
    # >>> s1
    # <Stack Bottom:(10, 20, 'hello', 'world', True, False, None):Top>
    def loadDataFromFile(self, fileaddr=datadir+os.sep+"stack.pcds"):
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
        # extracting and checking md5hash code (Part 6)
        if len(s) < 38:
            print("File has no data. Loading is stopped.")
            return False
        fileMD5=s[4:36]
        hdstr=s[37:len(s)] # hdstr=header+[enctag]+data string        
        newMD5=u.getHashCode(hdstr,"md5")        
        try:            
            if newMD5 != fileMD5:
                raise Exception("Data file is corrupt as hash missmatch. Loading is failed.")
        except Exception as e: print(e); return False
        s=hdstr
        # decrypting the encrypted data string into readable string(Part 7)
        try:
            # In the File Header, the last character is the keyid
            # Length of File Header = 29 (18 char+10 digits+'\n')
            if len(s) < 30:
                print("File has no data. Loading is failed")
                return False
            if s[0:18] == 'STACK FILE HEADER:':
                keyid=int(s[27])
                s=s[29:]  # leave the header part
                if encrypted:
                    s=encrypt.decrypt(s,keyid)                
            else: raise Exception("Data file is corrupt as file header is missing.")
        except Exception as e: print(e); return False
        # loading data into the data list after conversion (Part 8)        
        sl=s.split('\n') # sl=string list 
        sl=sl[0:len(sl)-1] # removing the last empty part    
        try:
            self.clear() # removing data            
            i=0
            for sdata in sl:
                self.__data.append(u.str2data(sdata))                
                i=i+1 
            self.__size = i                                           
        except Exception as e: 
            print(e); print("Data not loaded successfully."); return False
        print("Data Loaded Successfully from the file: '"+self.__fileaddr+"'")
        return True





