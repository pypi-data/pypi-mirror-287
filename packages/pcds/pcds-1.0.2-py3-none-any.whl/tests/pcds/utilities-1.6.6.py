'''
Module Description
--------------------
module filename: utilities.py
module name: utilities
Author: A K M Aminul Islam
Author Email: aminul71bd@gmail.com
Last Modified: Sunday July 14 2024 05:10 AM
Version:1.6.6

Description: This module converts list, tuple and dictionary data
    structures into string and retrieves the corresponding data
    structure from the string data
Content: dataType(arg), str2type(strarg), str2data(strdata), data2str(data),
    hashable2str(variable), list2str(listvar=None), str2list(strvar=None),
    tuple2str(tupvar=None), str2tuple(tupstr=None), dict2str(dictvar=None),
    str2dict(dictstr=None), createDataFileAddr(directory, filename),
    checkDataFileAddr(fileaddr), createDataFile(directory, filename),
    removeDataFile(directory, filename), getHashCode(datastr, algorithm="md5"),
    getFileDetails(fileaddr), char(code=0), charCode(c=' '), str2int(s=""), 
    int2str(strint=0), min(datalist=[]), max(datalist=[])
Supported Data Types: int, float, str, bool, NoneType, list, tuple, dict
Dependencies: os
'''

version="1.6.6"
import os
import hashlib
import datetime



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





# str2type(variable) returns data type of a string type data
# >>> str2type('-105.23')
# 'float'
# >>> str2type('105')
# 'int'
# >>> str2type('["name","hello"]')
# 'list'
# >>> str2type('{"name":"hello"}')
# 'dict'
# >>> str2type('(1,"name","hello")')
# 'tuple'
# >>> str2type('None')
# 'NoneType'
# >>> str2type('True')
# 'bool'
def str2type(strarg=None):
    try:
        if strarg == None:
            raise ValueError("String argument of str2type() is missing.")
        if dataType(strarg) != 'str':
            raise ValueError("Argument of str2type() must be a string.")
    except ValueError as e: print(e); return None
    strarg=strarg.strip()
    if strarg == "": return 'str'
    elif strarg == '': return 'str'
    elif strarg[0] == '(': return 'tuple'
    elif strarg[0] == '[': return 'list'
    elif strarg[0] == '{': return 'dict'
    elif strarg in ['True','False']: return 'bool'
    elif strarg == 'None': return 'NoneType'
    elif '.' in strarg: return 'float'
    elif strarg[0] == '"': return 'str'
    elif strarg[0] == "'": return 'str'
    else:
        try:
            if int(strarg)*1 == int(strarg): return 'int'
        except: pass  # Exception as e: print(e) 
    return 'str'






# str2data(strdata) converts basic string data into data
# >>> u.str2data('[45,7.89,"hello A",True,False,None,(1,5,"abc"),{1:"a",2:47}]')
# [45, 7.89, 'hello A', True, False, None, (1, 5, 'abc'), {1: 'a', 2: 47}]
def str2data(strdata=None):
    try:
        if strdata == None:
            raise ValueError("String argument of str2data() is missing.")
        if dataType(strdata) != 'str':
            raise ValueError("Argument of str2data() must be a string.")
    except ValueError as e: print(e); return None
    try:
        strdata=strdata.strip()
        if str2type(strdata) == 'int': return int(strdata)
        elif str2type(strdata) == 'float': return float(strdata)
        elif strdata == 'True': return True
        elif strdata == 'False': return False
        elif str2type(strdata) == 'NoneType': return None
        elif str2type(strdata) == 'list': return str2list(strdata)
        elif str2type(strdata) == 'tuple': return str2tuple(strdata)
        elif str2type(strdata) == 'dict': return str2dict(strdata)
        elif str2type(strdata) == 'str':
            if strdata[0] in ['"',"'"]: 
                return strdata[1:len(strdata)-1] # ' or " removed
            else: return strdata
        else:
            raise Exception("Exception: Unsupported string data type.")
    except Exception as e: print(e); return None






# data2str(data) converts data into string data
# >>> u.data2str([45,7.89,'hello A',True,False,None,(1,5,'abc'),{1:'a',2:47}])
# '[45,7.89,"hello A",True,False,None,(1,5,"abc"),{1:"a",2:47}]'
def data2str(data):
    try:        
        if dataType(data) not in ['int','float','str','bool','NoneType','list','tuple','dict']:
            raise ValueError("Invalid data types in data2str().\nSupported data types are 'int','float','str','bool','NoneType','list','tuple', and 'dict'.")
    except ValueError as e: print(e); return None    
    if dataType(data) in ['int','float','bool','NoneType']:
        return str(data)
    elif dataType(data) == 'str':
        return '"'+data.strip()+'"'
    elif dataType(data) == 'list':
        return list2str(data)
    elif dataType(data) == 'tuple':
        return tuple2str(data)
    elif dataType(data) == 'dict':
        return dict2str(data)






# Hashable Data Types = INTEGER, FLOAT, STRING, BOOLEAN, TUPLE, NONETYPE
# >>> u.hashable2str(True)
# 'True'
# >>> u.hashable2str(None)
# 'None'
# >>> u.hashable2str(145)
# '145'
# >>> u.hashable2str(145.12)
# '145.12'
# >>> u.hashable2str('hello')
# '"hello"'
# >>> u.hashable2str(('hello',2,3.6,True))
# "('hello', 2, 3.6, True)"
def hashable2str(variable):
    try:
        if dataType(variable) in ['int','float','bool','tuple','NoneType']: 
            return str(variable)
        elif dataType(variable) == 'str': return '"'+variable+'"'
        else:
            raise TypeError("Data Type is not hashable.")
    except TypeError as e: print(e)





# list2str(listvar=None) converts list into string; string data is double quoted
# list2str(['hi John', 2, 3.6, True, [3, 6.8, None], {'name': 'john', 'age': 16}])
# "['hello', 2, 3.6, True, [3, 6.8, None], {'name': 'john', 'age': 16}]"
def list2str(listvar=None):
    try:
        if listvar==None: raise ValueError("List argument required in list2str().")
        if dataType(listvar) != 'list':
            raise TypeError("List argument required in list2str().")        
        s=""
        # changing single quote to double quote and removing blank space
        for listitem in listvar:      
            s=s+data2str(listitem)+','
        return "["+s[0:len(s)-1]+"]"    # last comma is ommitted
    except Exception as e: print(e); return None





# str2list(strvar) converts a list string into a list data type that
# contains basic data types (int,float,str,bool,NoneType,list,tuple)
# >>> s='[2,6,"hello","hi",[3,["a","b","c",True,34],5,7.8],"abc",None,True,False,14.89]'
# >>> str2list(s)
# [2, 6, 'hello', 'hi', [3, ['a', 'b', 'c', True, 34], 5, 7.8], 'abc', None, True, False, 14.89]

def str2list(strvar=None):
    try:
        if strvar==None: raise ValueError("No argument given to str2list().")
        if str2type(strvar) != 'list':
            raise TypeError("List like string required in str2list().")
        s=strvar[1:len(strvar)-1]
        
        # Finding listitems
        comma1Index=-1; comma2Index=-1
        charCount=0
        listvar=[]; 
        locked=False; # locked=True means comma is valid 
        locktype=""
        for i in range(len(s)):
            # locking by list/tuple/dictionary
            if s[i] == '[' and not locked: 
                locked=True; locktype='list'
            elif s[i] == '(' and not locked:
                locked=True; locktype='tuple'
            elif s[i] == '{' and not locked:
                locked=True; locktype='dict'
            # processing list
            if s[i] == '[' and locktype == 'list':
                charCount=charCount+1                
                if i != len(s)-1: continue
            elif s[i] == ']' and locktype == 'list':
                charCount=charCount-1
                if charCount == 0:
                    locked = False; locktype="" 
                if i != len(s)-1: continue
            # processing tuple
            elif s[i] == '(' and locktype == 'tuple':
                charCount=charCount+1;                 
                if i != len(s)-1: continue
            elif s[i] == ')' and locktype == 'tuple':
                charCount=charCount-1 
                if charCount == 0:
                    locked = False; locktype="" 
                if i != len(s)-1: continue
            # processing dictionary
            elif s[i] == '{' and locktype == 'dict':
                charCount=charCount+1                
                if i != len(s)-1: continue
            elif s[i] == '}' and locktype == 'dict':
                charCount=charCount-1 
                if charCount == 0:
                    locked = False; locktype="" 
                if i != len(s)-1: continue
            if s[i] == ',' and not locked:
                comma1Index = comma2Index; comma2Index = i
                s2=s[comma1Index+1:comma2Index]           
                listvar.append(str2data(s2))
                locked=False
            if i==len(s)-1 and not locked:
                s2=s[comma2Index+1:len(s)]
                listvar.append(str2data(s2))                
        return listvar
    except Exception as e: print(e); return None





# tuple2str(tupvar) converts a tuple data into a string data
# >>> t=(2, 6, 'hello world', 'hi', [3, ('a', 'b', 'c', True, 34), 5, 7.8], 'abc', None, True, False, 14.89)
# >>> u.tuple2str(t)
# (2,6,"hello world","hi",[3,("a","b","c",True,34),5,7.8],"abc",None,True,False,14.89)
def tuple2str(tupvar=None):
    try:
        if tupvar==None: raise ValueError("Tuple argument required in tuple2str().")
        if dataType(tupvar) != 'tuple':
            raise TypeError("Tuple argument required in tuple2str().")
        tmplist=list(tupvar)
        s=""
        for listitem in tmplist:      
            s=s+data2str(listitem)+','
        return "("+s[0:len(s)-1]+")"    # last comma is ommitted
    except Exception as e: print(e); return None





# str2tuple(tupstr) converts a tuple string into a tuple data type that
# contains basic data types (int,float,str,bool,NoneType,list,tuple)
# >>> s='(2,6,"hello","hi",[3,("a","b","c",True,34),5,7.8],"abc",None,True,False,14.89)'
# >>> u.str2tuple(s)
# (2, 6, 'hello', 'hi', [3, ('a', 'b', 'c', True, 34), 5, 7.8], 'abc', None, True, False, 14.89)
def str2tuple(tupstr=None):
    try:
        if tupstr==None: raise ValueError("No argument given to str2tuple().")
        if str2type(tupstr) != 'tuple':
            raise TypeError("Tuple like string required in str2tuple().")
        s=tupstr[1:len(tupstr)-1]

        # Finding tuple items
        comma1Index=-1; comma2Index=-1
        charCount=0
        listvar=[]; 
        locked=False; # locked=True means comma is valid 
        locktype=""
        for i in range(len(s)):
            # locking by list/tuple/dictionary
            if s[i] == '[' and not locked: 
                locked=True; locktype='list'
            elif s[i] == '(' and not locked:
                locked=True; locktype='tuple'
            elif s[i] == '{' and not locked:
                locked=True; locktype='dict'
            # processing list
            if s[i] == '[' and locktype == 'list':
                charCount=charCount+1                
                if i != len(s)-1: continue
            elif s[i] == ']' and locktype == 'list':
                charCount=charCount-1
                if charCount == 0:
                    locked = False; locktype="" 
                if i != len(s)-1: continue
            # processing tuple
            elif s[i] == '(' and locktype == 'tuple':
                charCount=charCount+1;                 
                if i != len(s)-1: continue
            elif s[i] == ')' and locktype == 'tuple':
                charCount=charCount-1 
                if charCount == 0:
                    locked = False; locktype="" 
                if i != len(s)-1: continue
            # processing dictionary
            elif s[i] == '{' and locktype == 'dict':
                charCount=charCount+1                
                if i != len(s)-1: continue
            elif s[i] == '}' and locktype == 'dict':
                charCount=charCount-1 
                if charCount == 0:
                    locked = False; locktype="" 
                if i != len(s)-1: continue
            if s[i] == ',' and not locked:
                comma1Index = comma2Index; comma2Index = i
                s2=s[comma1Index+1:comma2Index]           
                listvar.append(str2data(s2))
                locked=False
            if i==len(s)-1 and not locked:
                s2=s[comma2Index+1:len(s)]
                listvar.append(str2data(s2))                
        return tuple(listvar)
    except Exception as e: print(e); return None







# tuple2str(tupvar) converts a tuple data into a string data
# >>> dict2str({1:47,2:"hi A",3:4.78,'a':None,'b':[47,'hello',(15.4,'ab')]})
# '{1:47,2:"hi A",3:4.78,"a":None,"b":[47,"hello",(15.4,"ab")]}'
def dict2str(dictvar=None):
    try:
        if dictvar==None: 
            raise ValueError("Dictionary argument required in dict2str().")
        if dataType(dictvar) != 'dict':
            raise TypeError("Dictionary argument required in dict2str().")
        s=""        
        for key in dictvar.keys():
            s=s+data2str(key)+':'     
            s=s+data2str(dictvar[key])+','
        return "{"+s[0:len(s)-1]+"}"    # last comma is ommitted
    except Exception as e: print(e); return None






# str2dict(dictstr=None) converts dictionary string to dictionary data type
# >>> d={'name':'john','marks':(15,17,12,15.4),'age':16.5,'sub':['a','b','c']}
# >>> s=dict2str(d)
# >>> s
# '{"name":"john","marks":(15,17,12,15.4),"age":16.5,"sub":["a","b","c"]}'
# >>> str2dict(s)
# {'name': 'john', 'marks': (15, 17, 12, 15.4), 'age': 16.5, 'sub': ['a', 'b', 'c']}
def str2dict(dictstr=None):
    try:
        if dictstr==None: raise ValueError("No argument given to str2dict().")
        if str2type(dictstr) != 'dict':
            raise TypeError("Dictionary like string required in str2dict().")
        s=dictstr[1:len(dictstr)-1]

        # keys are hashable single data types (str,int,float,bool,NoneType)
        keystartindex=0; key=None
        datastartindex=-1; 
        locked=False; keypart=True; tmpdict={}
        lockChar=""; unlockChar=""; charCount=0
        for i in range(len(s)):
            if s[i] == ':' and keypart and not locked:
                key=s[keystartindex:i]
                key=str2data(key)
                datastartindex=i+1; keypart=False; locked=False
            # processing normal data
            if s[i] == ',' and not locked and not keypart:            
                datastr=s[datastartindex:i];
                data=str2data(datastr)
                tmpdict[key]=data
                keystartindex = i + 1
                locked=False; keypart=True
            # processing list, tuple and dictionary type data
            if i==datastartindex:
                if s[datastartindex] == '[':
                    lockChar='['; unlockChar=']';locked=True;
                elif s[datastartindex] == '(':
                    lockChar='('; unlockChar=')';locked=True;
                elif s[datastartindex] == '{':
                    lockChar='{'; unlockChar='}';locked=True;                
                else: 
                    locked=False
                #keypart=False
                
            if locked:
                if s[i] == lockChar: charCount=charCount+1 
                elif s[i] == unlockChar: charCount=charCount-1            
                if charCount == 0:
                    datastr=s[datastartindex:i+1];
                    data=str2data(datastr)
                    tmpdict[key]=data            
                    locked=False; keypart=True; 
                    keystartindex=i+2 # current position=']/)/}' + 1 for ','
            if i==len(s)-1:
                datastr=s[datastartindex:i+1]
                data=str2data(datastr)
                tmpdict[key]=data
        return tmpdict
    except Exception as e: print(e); return None








# ------------------------- File Handing Utiliyy Functions ----------------------

# createDataFileAddr(directory="", filename="hello") generates an absolute file
# address of a valid .pcds data file. But it does not create the actual file
def createDataFileAddr(directory=datadir, filename="hello"):
    try:
        # checking inputs            
        if dataType(directory) != 'str': 
            raise TypeError("Data type of file directory should be string.") 
        if dataType(filename) != 'str': 
            raise TypeError("Data type of file name should be string.") 
    except TypeError as e: print(e); return None
    directory=directory.strip(); filename=filename.strip()
    fileaddr=""
    try:        
        if directory != datadir:            
            if os.path.isdir(directory):
                if os.path.basename(directory) != "pcds_data":
                    directory=directory+os.sep+"pcds_data";
                    if not os.path.exists(directory):
                        os.makedirs(directory)
            else:
                raise ValueError("Given file directory is not found.")    
    except ValueError as e: print(e); return None 
    fileaddr=directory+os.sep+filename+".pcds"
    return fileaddr





# checkDataFileAddr(fileaddr) checks whether the input file is a valid .pdsf file
# It returns True if address is a valid .pdsf file, otherwise False is returned 
def checkDataFileAddr(fileaddr=datadir+os.sep+"hello.pcds"):    
    try:
        # checking inputs            
        if dataType(fileaddr) != 'str': 
            raise TypeError("Data type of file address should be string.")             
    except TypeError as e: print(e); return
    fileaddr=fileaddr.strip()
    try:
        if not os.path.exists(fileaddr):
            raise ValueError("Given file address does not exist.")
        else:
            if not os.path.isfile(fileaddr):
                raise ValueError("Given file address is not a file.")
            else:
                basename=os.path.basename(fileaddr)
                if basename[len(basename)-5:len(basename)] != ".pcds":
                    raise ValueError("File is not a .pcds file.")
                return True
    except Exception as e: print(e); return False
        





# createDataFile() creates a .pcds data file at the given filepath
# If file is created successfully, file address is returned, otherwise
# error message is displayed and None is returned
def createDataFile(directory=datadir, filename="hello"):
    fileaddr=createDataFileAddr(directory,filename)
    fo=None
    try:            
        fo=open(fileaddr,'wb')
        if not fo:
            raise IOError("Data file is not created.")            
        else:
            fo.close()
            return fileaddr
    except Exception as e: print(e); return None
    





# removeDataFile(directory="", filename="hello") deletes the .pcds data file
# True is returned. If delete operation is failed, False is returned
def removeDataFile(directory=datadir, filename="hello"):
    try:
        fileaddr=createDataFileAddr(directory,filename)
        if os.path.isfile(fileaddr):
            os.remove(fileaddr)
            print("File removed.")
            return True
        else:
            raise Exception("Data file not found.")
    except Exception as e: print(e); return False
    
        




# getHashCode(datastr, algorithm="md5") creates the popular hashcode of the
# files are to be open in binary mode
# items of the following data types:
#   str, filestr, buffer_reader, int, float, bool, NoneType
# Supported Common Hash Algorithm: md5, sha1, sha256, sha512
# >>> u.getHashCode("hello world")
# '5eb63bbbe01eeed093cb22bb8f5acdc3'
# >>> u.getHashCode("hello world",'sha1')
# '2aae6c35c94fcfb415dbe95f408b9ce91ee846ed'
# >>> u.getHashCode("hello world",'sha256')
# 'b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9'
# >>> u.getHashCode("hello world",'sha512')
#'309ecc489c12d6eb4cc40f50c902f2b4d0ed77ee511a7c7a9bcd3ca86d4cd86f989dd35bc5ff499670da34255b45b0cfd830e81f605dcf7dc5542e93ae9cd76f'
# >>>
# >>> u.getHashCode(12345)
# '827ccb0eea8a706c4c34a16891f84e7b'
# >>> u.getHashCode(1234.5)
# '3c80e9adacfdeab38845f2790aca3294'
# >>> u.getHashCode(True)
# 'f827cf462f62848df37c5e1e94a4da74'
# >>> u.getHashCode(False)
# 'f8320b26d30ab433c5a54546d21f414c'
# >>>
# >>> filestr='md5sums.txt'
# >>> fo=open(filestr,'rb')
# >>> u.getHashCode(fo)
# '0fb9cbc05d937fff428f7de759eb0021'
# >>> fo.close()
# >>> u.getHashCode(filestr)
# '0fb9cbc05d937fff428f7de759eb0021'
# >>>
def getHashCode(datastr, algorithm="md5"):
    buffreader=False; isfile=False; fileaddr=""; fo=None
    try:
        # checking inputs 
        if dataType(datastr) in ['int','float','bool','NoneType']:
            datastr=str(datastr)           
        elif dataType(datastr) == '_io.BufferedReader' and datastr: 
            buffreader=True; fo=datastr
        elif dataType(datastr) == 'str': 
            datastr=datastr.strip()
            if os.path.isfile(datastr):
                isfile=True; fileaddr=datastr
        else: raise TypeError("Unsupported data type to create hash code.")        
        if dataType(algorithm) != 'str': 
            raise TypeError("'algorithm' is a string type argument.")
        algorithm=algorithm.strip()
        if algorithm.upper() not in ['MD5','SHA1','SHA256','SHA512']: 
            raise ValueError("'algorithm' value must be in ['md5','sha1','sha256','sha512'].")
    except TypeError as e: print(e); return               
    except ValueError as e: print(e); return
    ba=None     # ba=bytearray
    if buffreader:
        try:            
            ba=fo.read()            
        except Exception as e: print(e); return None
    elif isfile:
        fo=open(fileaddr,'rb')
        ba=fo.read()
        fo.close()
    else:
        ba=datastr.encode('utf-8')
    result=None
    if algorithm.upper() == 'MD5':
        result=hashlib.md5(ba)
    elif algorithm.upper() == 'SHA1':
        result=hashlib.sha1(ba)
    elif algorithm.upper() == 'SHA256':
        result=hashlib.sha256(ba)
    elif algorithm.upper() == 'SHA512':
        result=hashlib.sha512(ba)
    return result.hexdigest()






# getFileDetails(fileaddr) returns the file details of the given file address
# >>> u.getFileDetails('md5sums.txt')
# {'file': 'C:\\Users\\admin\\pycodes\\pcds\\md5sums.txt', 
# 'md5hash': '0fb9cbc05d937fff428f7de759eb0021', 'mode': '33206', 
# 'ino': '15199648742451859', 'dev': '16484973977398432186', 'nlink': '1', 
# 'uid': '0', 'gid': '0', 'size': '1085', 'atime': '1719184029', 
# 'mtime': '1719116616', 'ctime': '1718702639'}
# ctime=file creation time in s(windows), last meta data change time (linux)
# mtime=lastmodified time in s, atime=last access time in s
# mode=file type and file permission mode; dev=device identifier
# ino=file inode (linux), file index(windows); uid=user id; gid=group id
# nlink=No of hard links attached to the file; size=file size in bytes
# >>>
# >>> u.getFileDetails('md5sum.txt')
# Argument of getFileDetails() is not a file.
# >>>
# >>> u.getFileDetails('md5sums.txt')
# {'file': 'C:\\Users\\admin\\pycodes\\pds\\md5sums.txt', 'mode': '33206',
# 'md5hash': '0fb9cbc05d937fff428f7de759eb0021', 'ino': '15199648742451859', 
# 'dev': '16484973977398432186', 'nlink': '1', 'uid': '0', 'gid': '0', 
# 'atime': 'Monday, June 24, 2024 06:48:46', 'size': '1085',
# 'mtime': 'Sunday, June 23, 2024 10:23:36', 'ctime': 'Tuesday, June 18, 2024 03:23:59'}
# >>>
def getFileDetails(fileaddr):
    try:
        # checking inputs 
        if dataType(fileaddr) != 'str': 
            raise TypeError("getFileDetails() needs string type file address.") 
        fileaddr=fileaddr.strip()
        if not os.path.isfile(fileaddr):
            raise ValueError("Argument of getFileDetails() is not a file.")
    except TypeError as e: print(e); return None
    except ValueError as e: print(e); return None
    fileaddr=os.path.abspath(fileaddr)
    md5hashstr=getHashCode(fileaddr)
    s=str(os.stat(fileaddr))
    s=(s.split('(')[1]).split(')')[0]    # get data part
    datalist=s.split(',')
    templist=[]
    # removing st_ from the beginning of each data item
    for item in datalist:
        item=item.split('_')[1]
        templist.append(item)
    tempdict={'file':fileaddr,'md5hash':md5hashstr}
    for item in templist:
        l=item.split('=')
        key=l[0]; value=l[1]
        tempdict[key]=value
    tempdict['ctime']=datetime.datetime.fromtimestamp(int(tempdict['ctime'])).strftime("%A, %B %d, %Y %I:%M:%S")
    tempdict['mtime']=datetime.datetime.fromtimestamp(int(tempdict['mtime'])).strftime("%A, %B %d, %Y %I:%M:%S")
    tempdict['atime']=datetime.datetime.fromtimestamp(int(tempdict['atime'])).strftime("%A, %B %d, %Y %I:%M:%S")
    return tempdict



# -------------------------- string vs integer ----------------------------

# char(code=0) converts code into character (code=ascii code-32)
# There are 95 printable characters
# >>> char(1)
# '!'
# >>> char(32)
# '@'
# >>> char(33)
# 'A'
# >>> char(94)
# '~'
def char(code=0):
    try:
        if dataType(code) != 'int' or code<0 or code>94:
            raise ValueError("Invalid character code. It must be between 0 and 94.")
    except ValueError as e: print(e); return
    return chr(code+32)





# charCode(c=' ') returns (ascii code - 32)
# There are 95 printable characters
# >>> charCode('A')
# 33
# >>> charCode('a')
# 65
# >>> charCode('~')
# 94
def charCode(c=' '):
    try:
        if dataType(c) != 'str' or len(c) != 1:
            raise ValueError("Only a single character is valid.")
    except ValueError as e: print(e); return
    return ord(c)-32



from upmath import lib


# str2int(s="") converts a string into an integer
# >>> u.str2int('Bangladesh')
# b10:21865203026835110307
# >>> u.str2int('Hello! How are you? Are you okay?')
# b10:78908037017201105521911845578186691963140629150393989397259497611
def str2int(s=""):
    try:
        if dataType(s) != 'str':
            raise ValueError("Only string argument is required.")
    except ValueError as e: print(e); return
    s=s.strip(); strlen=len(s)
    total=lib.Number(0); i=0
    for i in range(strlen):   
        total=total + lib.Number(charCode(s[strlen-1-i]))*lib.Number((95**i))
    return int(total)





# int2str(strint=0) converts a string-integer to corresponding string
# large integer value provide as string (enclose by single quote)
# >>> u.int2str('21865203026835110307')
# 'Bangladesh'
# >>> u.int2str('78908037017201105521911845578186691963140629150393989397259497611')
# 'Hello! How are you? Are you okay?'
def int2str(strint=0):
    if strint==0: return chr(32)          
    try:
        if dataType(strint) not in ['str','int','upmath.src.upnumber.Number']:
            raise ValueError("Only an integer is required.")
        if dataType(strint) in ['str','int']: strint=lib.Number(strint)
    except ValueError as e: print(e); return  
    s=""; rem=lib.Number(-1); quotient=lib.Number(-1); # rem=remainder
    divisor=lib.Number('95');divident=strint
    quotient=int(divident/divisor); s=char(int(strint-quotient*divisor));
    divident=quotient    
    while quotient>0:
        quotient = int(divident/divisor)
        s=char(int(divident-quotient*divisor))+s 
        divident=quotient       
    return s





# ------------------------------ min() and max() ------------------------------------

# min(datalist=[]) returns the minimum data in the datalist
# from pds import utilities as u
# >>> l
# [10, 15, 48, 74, 5, 0, -5, -15, 100, 18, 45, 26, 85, 99, 1, 2, 6, 7, 8, 12]
# >>>
# >>> u.min(l)
# -15
# >>>
# >>> slist
# ['xyz', 'abc', 'ab', 'mn', 'pq', 'z', 'a', 'f', 'db', 'bd', 'com', 'len', 'pqr', 'abc', 'xyz', 'not', 'hot', 'hat', 'mat', 'cat', 'dog', 'fog', 'jag']
# >>>
# >>> u.min(slist)
# 'a'
# >>>
# >>> l2
# [10, 15, 48, 74, 5, 'a', 0, -5, -15, 100, 18, 45, 'm', 26, 85, 'z', 99, 1, 2, 6, 7, 8, 12, 'ab']
# >>> u.min(l2)
# -15
# >>>
def min(datalist=[]):
    try:
        if dataType(datalist) != 'list':
            raise ValueError("Data argumend is a list structure.")
        for data in datalist:
            if dataType(data) not in ['int','float','str']:
                raise ValueError("Invalid data type. Only integer, float and string types are supported.")
    except ValueError as e: print(e); return
    isstr=False
    if dataType(datalist[0]) in ['int','float']:
        mindata=datalist[0]
    elif dataType(datalist[0]) == 'str':
        mindata=int(str2int(datalist[0])); isstr=True
    for data in datalist:        
        if dataType(data) in ['int','float']:
            if data<mindata: 
                mindata=data; isstr=False
        elif dataType(data) == 'str':
            if int(str2int(data))<mindata: 
                mindata=int(str2int(data)); isstr=True
    if not isstr:return mindata
    else: return int2str(mindata)






# max(datalist=[]) returns the maximum data in the datalist
# from pds import utilities as u
# >>> l
# [10, 15, 48, 74, 5, 0, -5, -15, 100, 18, 45, 26, 85, 99, 1, 2, 6, 7, 8, 12]
# >>>
# >>> u.max(l)
# 100
# >>>
# >>> slist
# ['xyz', 'abc', 'ab', 'mn', 'pq', 'z', 'a', 'f', 'db', 'bd', 'com', 'len', 'pqr', 'abc', 'xyz', 'not', 'hot', 'hat', 'mat', 'cat', 'dog', 'fog', 'jag']
# >>>
# >>> u.max(slist)
# 'xyz'
# >>>
# >>> l2
# [10, 15, 48, 74, 5, 'a', 0, -5, -15, 100, 18, 45, 'm', 26, 85, 'z', 99, 1, 2, 6, 7, 8, 12, 'ab']
# >>> u.max(l2)
# 'ab'
# >>>
def max(datalist=[]):
    try:
        if dataType(datalist) != 'list':
            raise ValueError("Data argumend is a list structure.")
        for data in datalist:
            if dataType(data) not in ['int','float','str']:
                raise ValueError("Invalid data type. Only integer, float and string types are supported.")
    except ValueError as e: print(e); return
    isstr=False
    if dataType(datalist[0]) in ['int','float']:
        maxdata=datalist[0]
    elif dataType(datalist[0]) == 'str':
        maxdata=int(str2int(datalist[0])); isstr=True
    for data in datalist:
        #print(data,dataType(data),maxdata)
        if dataType(data) in ['int','float']:
            if data>maxdata: 
                maxdata=data; isstr=False
        elif dataType(data) == 'str':
            if int(str2int(data))>maxdata: 
                maxdata=int(str2int(data)); isstr=True
    if not isstr:return maxdata
    else: return int2str(maxdata)







