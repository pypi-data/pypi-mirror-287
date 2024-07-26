'''
Test Module: test_utilities.py
Test Module Name: test_utilities
Author: A K M Aminul Islam
Author Email: aminul71bd@gmail.com
Last Modified: Sunday July 14 2024 05:10 AM
Version:1.0.0
'''

version="1.0.0"


import unittest
import os
from pcds import utilities as u


import pcds
datadir=pcds.getDataDirectory()
homedir=os.path.expanduser('~')


# dataType(variable) returns the data type of the given variable
def dataType(arg):
    return str(type(arg)).split("'")[1]






class TestUtilities(unittest.TestCase):
    # testing u.dataType() function
    def test_dataType(self):
        self.assertEqual(u.dataType('abs'),'str')
        self.assertEqual(u.dataType(11258),'int')
        self.assertEqual(u.dataType(-14.0),'float')
        self.assertEqual(u.dataType(-14.89),'float')
        self.assertEqual(u.dataType(-14.89e5),'float')        
        self.assertEqual(u.dataType(True),'bool')
        self.assertEqual(u.dataType(False),'bool')
        self.assertEqual(u.dataType(None),'NoneType')
        self.assertEqual(u.dataType([]),'list')
        self.assertEqual(u.dataType([1,4,[3,6],{'age':14.5}]),'list')
        self.assertEqual(u.dataType(()),'tuple')
        self.assertEqual(u.dataType((1,4,[3,6],{'age':14.5})),'tuple')
        self.assertEqual(u.dataType({}),'dict')
        self.assertEqual(u.dataType({1:'abc',2:15,'name':'john'}),'dict')




# ------------------- Data Conversion Utiliyy Functions -------------------
    # testing u.str2type(strarg) function
    def test_str2type(self):
        #self.assertRaises(ValueError,u.str2type,14.5)
        self.assertEqual(u.str2type('-105.23'),'float')
        self.assertEqual(u.str2type('1.0'),'float')
        self.assertEqual(u.str2type('-10523'),'int')
        self.assertEqual(u.str2type('["name","hello"]'),'list')
        self.assertEqual(u.str2type('{"name":"hello"}'),'dict')
        self.assertEqual(u.str2type('(1,"name","hello")'),'tuple')
        self.assertEqual(u.str2type('None'),'NoneType')
        self.assertEqual(u.str2type('True'),'bool')
        self.assertEqual(u.str2type('False'),'bool')
        self.assertEqual(u.str2type('{}'),'dict')
        self.assertEqual(u.str2type('()'),'tuple')
        self.assertEqual(u.str2type('[]'),'list')
        self.assertEqual(u.str2type('hello'),'str')
        self.assertEqual(u.str2type("hello"),'str')
        self.assertEqual(u.str2type(''),'str')
        self.assertEqual(u.str2type(""),'str')
        self.assertEqual(u.str2type(),None)
        self.assertEqual(u.str2type(15487),None)
        self.assertEqual(u.str2type(154.87),None)
        self.assertEqual(u.str2type(True),None)
        self.assertEqual(u.str2type(None),None)
        self.assertEqual(u.str2type([]),None)
        self.assertEqual(u.str2type(()),None)
        self.assertEqual(u.str2type({}),None)




    # testing u.str2data(strdata) function
    def test_str2data(self):
        s='[45,7.89,"hello A",True,False,None,(1,5,"abc"),{1:"a",2:47}]'
        l=[45, 7.89, 'hello A', True, False, None, (1, 5, 'abc'), {1: 'a', 2: 47}]
        #self.assertRaises(ValueError,u.str2type,14.5)
        self.assertEqual(u.str2data('-105.23'),-105.23)
        self.assertEqual(u.str2data('1.0'),1.0)
        self.assertEqual(u.str2data('-10523'),-10523)
        self.assertEqual(u.str2data('["name","hello"]'),["name","hello"])
        self.assertEqual(u.str2data('{"name":"hello"}'),{"name":"hello"})
        self.assertEqual(u.str2data('(1,"name","hello")'),(1,"name","hello"))
        self.assertEqual(u.str2data('None'),None)
        self.assertEqual(u.str2data('True'),True)
        self.assertEqual(u.str2data('False'),False)
        self.assertEqual(u.str2data('{}'),{})
        self.assertEqual(u.str2data('()'),())
        self.assertEqual(u.str2data('[]'),[])
        self.assertEqual(u.str2data('hello'),'hello')
        self.assertEqual(u.str2data("hello"),'hello')
        self.assertEqual(u.str2data(''),None)
        self.assertEqual(u.str2data(""),None)
        self.assertEqual(u.str2data(),None)
        self.assertEqual(u.str2data(15487),None)
        self.assertEqual(u.str2data(154.87),None)
        self.assertEqual(u.str2data(True),None)
        self.assertEqual(u.str2data(None),None)
        self.assertEqual(u.str2data([]),None)
        self.assertEqual(u.str2data(()),None)
        self.assertEqual(u.str2data({}),None)
        self.assertEqual(u.str2data(s),l)




    # testing u.data2str(strdata) function
    def test_data2str(self):        
        list1=[45,7.89,'hello A',True,False,None,(1,5,'abc'),{1:'a',2: 47}]
        s1='[45,7.89,"hello A",True,False,None,(1,5,"abc"),{1:"a",2:47}]'
        tuple1=('a',12,4.12,{1:'abc',2:'name',3:[3,6,'hello',(4,6,7)]})
        s2='("a",12,4.12,{1:"abc",2:"name",3:[3,6,"hello",(4,6,7)]})'
        dict1={'id':457, 'subjects':['phy','chem','math','bio']}
        s3='{"id":457,"subjects":["phy","chem","math","bio"]}'
        #self.assertRaises(ValueError,u.str2type,14.5)
        self.assertEqual(u.data2str(list1),s1)
        self.assertEqual(u.data2str(tuple1),s2)
        self.assertEqual(u.data2str(dict1),s3)
        
        
# ------------------------- File Handing Utiliyy Functions ----------------------
# 
    # testing createDataFileAddr(directory=datadir, filename="hello") function
    # createDataFileAddr(directory=datadir, filename="hello") generates an absolute file
    # address of a valid .pdsf data file. But it does not create the actual file
    def test_createDataFileAddr(self):
        s1=datadir + '\\hello.pcds'
        s2=homedir + '\\data\\pcds_data\\hello.pcds'
        s3=homedir + '\\data\\pcds_data\\hello2.pcds'
        self.assertEqual(u.createDataFileAddr(),s1)
        self.assertEqual(u.createDataFileAddr(directory=datadir,filename="hello"),s1)
        self.assertEqual(u.createDataFileAddr(directory=homedir+"\\data"),s2)
        self.assertEqual(u.createDataFileAddr(directory=homedir+"\\data",filename="hello2"),s3)




    # checkDataFileAddr(fileaddr=datadir+os.sep+"hello.pcds") checks whether the 
    # input file is a valid .pcds file. It returns True if address is a valid .pcds 
    # file, otherwise False is returned. File should be manually created.
    def test_checkDataFileAddr(self):
        s1=datadir + '\\hello.pcds'
        s2=homedir + '\\data\\pcds_data\\hello.pcds'
        s3=homedir + '\\data\\pcds_data\\hello2.pcds'
        u.createDataFile()
        u.createDataFile(s1)
        self.assertTrue(u.checkDataFileAddr(s1))
        u.createDataFile(s2)
        self.assertTrue(u.checkDataFileAddr(s2))
        u.removeDataFile(directory=homedir + '\\data\\pcds_data',filename="hello2")
        self.assertFalse(u.checkDataFileAddr(s3))



    
    # createDataFile(directory=datadir, filename="hello") creates a .pcds data file 
    # at the given filepath. If file is created successfully, file address is 
    # returned, otherwise error message is displayed and None is returned
    def test_createDataFile(self):
        s1=datadir
        s2=homedir + '\\data\\pcds_data\\hello.pcds'
        s3=homedir + '\\data\\pcds_data\\hello2.pcds'
        self.assertEqual(u.createDataFile(),s1+'\\hello.pcds')
        self.assertEqual(u.createDataFile(directory=homedir+"\\data"),s2)
        self.assertEqual(u.createDataFile(directory=homedir+"\\data",filename="hello2"),s3)
        



    # removeDataFile(directory=datadir, filename="hello") deletes the .pcds data 
    # file and True is returned. If delete operation is failed, None is returned.
    def test_removeDataFile(self):
        s1=datadir
        s2=homedir+"\\data\\pcds_data"
        if os.path.isfile(s1+os.sep+"hello.pcds"):
            self.assertEqual(u.removeDataFile(),True)
        else:
            self.assertEqual(u.removeDataFile(),False)
        if os.path.isfile(s2+os.sep+"hello2.pcds"):
            self.assertEqual(u.removeDataFile(s2,filename="hello2"),True)
        else:
            self.assertEqual(u.removeDataFile(s2,filename="hello2"),False)



    # getHashCode(datastr, algorithm="md5") creates the popular hashcode of the
    # items of the following data types:
    #   str, filestr, buffer_reader, int, float, bool, NoneType
    # Supported Common Hash Algorithm: md5, sha1, sha256, sha512
    def test_getHashCode(self):
        s="hello world"
        md5hash='5eb63bbbe01eeed093cb22bb8f5acdc3'
        sha1hash='2aae6c35c94fcfb415dbe95f408b9ce91ee846ed'
        sha256hash='b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9'
        sha512hash='309ecc489c12d6eb4cc40f50c902f2b4d0ed77ee511a7c7a9bcd3ca86d4cd86f989dd35bc5ff499670da34255b45b0cfd830e81f605dcf7dc5542e93ae9cd76f'
        self.assertEqual(u.getHashCode(s, algorithm="md5"),md5hash)
        self.assertEqual(u.getHashCode(s, algorithm="sha1"),sha1hash)
        self.assertEqual(u.getHashCode(s, algorithm="sha256"),sha256hash)
        self.assertEqual(u.getHashCode(s, algorithm="sha512"),sha512hash)

        s=""
        md5hash='d41d8cd98f00b204e9800998ecf8427e'
        sha1hash='da39a3ee5e6b4b0d3255bfef95601890afd80709'
        sha256hash='e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'
        sha512hash='cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e'
        self.assertEqual(u.getHashCode(s, algorithm="md5"),md5hash)
        self.assertEqual(u.getHashCode(s, algorithm="sha1"),sha1hash)
        self.assertEqual(u.getHashCode(s, algorithm="sha256"),sha256hash)
        self.assertEqual(u.getHashCode(s, algorithm="sha512"),sha512hash)
        
        # testing non-string type data; default algorithm is 'md5'
        self.assertEqual(u.getHashCode(110),'5f93f983524def3dca464469d2cf9f3e')
        self.assertEqual(u.getHashCode(None),'6adf97f83acf6453d4a6a4b1070f3754')
        self.assertEqual(u.getHashCode(14.56),'b27cc392e8521b57cb4bb36f689ed263')
        self.assertEqual(u.getHashCode(True),'f827cf462f62848df37c5e1e94a4da74')
        self.assertEqual(u.getHashCode(False),'f8320b26d30ab433c5a54546d21f414c')


        # testing filetype data; default algorithm is 'md5';
        # files are to be open in binary mode
        filestr=os.getcwd()+os.sep+"sample.txt"    # text="hello world"        
        if os.path.exists(filestr):
            self.assertEqual(u.getHashCode(filestr),'5eb63bbbe01eeed093cb22bb8f5acdc3')
        if os.path.exists(filestr):
            fo=open(filestr,'rb')
            self.assertEqual(u.getHashCode(fo),'5eb63bbbe01eeed093cb22bb8f5acdc3')



    # getFileDetails(fileaddr) returns the file details of the given file address
    def test_getFileDetails(self):
        fileaddr=os.getcwd()+os.sep+"\\pcds\\md5sums.txt"
        #infodict={'file': 'C:\\Users\\admin\\pycodes\\python projects\\pcds-1.0.1\\tests\\pcds\\md5sums.txt', 'md5hash': '778a6d658cbd2967124fefb0a10556a0', 'mode': '33206', 'ino': '1970324837274343', 'dev': '16484973977398432186', 'nlink': '1', 'uid': '0', 'gid': '0', 'size': '1083', 'atime': 'Friday, July 26, 2024 10:47:04', 'mtime': 'Wednesday, July 24, 2024 12:46:58', 'ctime': 'Thursday, July 25, 2024 08:07:07'}
        self.assertEqual(dataType(u.getFileDetails(fileaddr)),'dict')






# ------------------- string vs integer utility functions ----------------------

    # char(code=0) converts code into character (code=ascii code-32)
    # There are 95 printable characters
    def test_char(self):
        self.assertEqual(u.char(),' ') # space character
        self.assertEqual(u.char(16),'0')
        self.assertEqual(u.char(33),'A')
        self.assertEqual(u.char(65),'a')
        self.assertEqual(u.char(90),'z')
        self.assertEqual(u.char(94),'~')



    # charCode(c=' ') returns (ascii code - 32)
    # There are 95 printable characters
    def test_charCode(self):
        self.assertEqual(u.charCode(' '),0) # space character
        self.assertEqual(u.charCode('0'),16)
        self.assertEqual(u.charCode('A'),33)
        self.assertEqual(u.charCode('a'),65)
        self.assertEqual(u.charCode('z'),90)
        self.assertEqual(u.charCode('~'),94)




    # str2int(s="") converts a string into an integer
    def test_str2int(self):
        self.assertEqual(u.str2int('Bangladesh'),21865203026835110307)
        n=78908037017201105521911845578186691963140629150393989397259497611
        self.assertEqual(u.str2int('Hello! How are you? Are you okay?'),n)
        self.assertEqual(u.str2int(),0)
        self.assertEqual(u.str2int(''),0)




    # int2str(strint=0) converts a string-integer to corresponding string
    # large integer value provide as string (enclose by single quote)
    def test_int2str(self):
        self.assertEqual(u.int2str(21865203026835110307),'Bangladesh')
        n=78908037017201105521911845578186691963140629150393989397259497611
        self.assertEqual(u.int2str(n),'Hello! How are you? Are you okay?')
        self.assertEqual(u.int2str(),' ')
        self.assertEqual(u.int2str(0),' ')




# ------------------------------ min() and max() ------------------------------------
    # min(datalist=[]) returns the minimum data in the datalist
    def test_min(self):
        l=[10,15,48,74,5,0,-5,-15,100,18,45,26,85,99,1,2,6,7,8,12]
        self.assertEqual(u.min(l),-15)
        l=['xyz','abc','ab','mn','pq','z','a','f','db','bd','com','len','pqr','A','abc','xyz','not','hot','hat','mat','cat','dog','fog','jag']
        self.assertEqual(u.min(l),'A')
        l=[10,15,48,74,5,'a',0,-5,-15,100,18,45,'m',26,85,'z',99,1,2,6,7,8,-25,12,'ab']
        self.assertEqual(u.min(l),-25)




    # max(datalist=[]) returns the maximun data in the datalist
    def test_max(self):
        l=[10,15,48,74,5,0,-5,-15,100,18,45,26,85,99,1,2,6,7,8,12]
        self.assertEqual(u.max(l),100)
        l=['xyz','abc','ab','mn','pq','z','a','f','db','bd','com','len','pqr','A','abc','xyz','not','hot','hat','mat','cat','dog','fog','jag']
        self.assertEqual(u.max(l),'xyz')
        l=[10,15,48,74,5,'a',0,-5,-15,100,18,45,'m',26,85,'z',99,1,2,6,7,8,-25,12,'ab']
        self.assertEqual(u.max(l),'ab')

# -------------------------- END of TestUtilities class -------------------------



if __name__ == '__main__':
    unittest.main()


