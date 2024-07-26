'''
Test Module: test_encrypt.py
Test Module Name: test_encrypt
Author: A K M Aminul Islam
Author Email: aminul71bd@gmail.com
Last Modified: Sunday July 14 2024 12:42 PM
Version:1.0.0
'''

version="1.0.0"

import unittest
from pcds import encrypt as enc



class TestEncrypt(unittest.TestCase):


    # testing createRandomKey() function
    # >>> enc.createRandomKey()
    # 'FY,rK%#eE6cd7`./*x2C9VXO(Q=;A\'v"&IBjTbtfwJNlyZ5R!-)L 3P<S@u[>m~_Ma:+4Wn{gkG1]Diz0qos8p^HU$h\\|}?'
    def test_createRandomKey(self):
        self.assertEqual(len(enc.createRandomKey()),95)
        self.assertEqual(len(enc.createRandomKey()),95)
        self.assertEqual(len(enc.createRandomKey()),95)




    # randomInteger(size=10) creates a random integer of the given size
    # >>> enc.randomInteger(25)
    # 4898935591547556468622300
    # >>> enc.randomInteger(25)
	# 3853398123461720477916201
    def test_randomInteger(self):
        n1=15; n2=20; n3=50
        self.assertEqual(len(str(enc.randomInteger())),10)
        self.assertEqual(len(str(enc.randomInteger(n1))),n1)
        self.assertEqual(len(str(enc.randomInteger(n2))),n2)
        self.assertEqual(len(str(enc.randomInteger(n3))),n3)
        self.assertEqual(enc.randomInteger(0),None)
        self.assertEqual(enc.randomInteger('ab'),None)
        self.assertEqual(enc.randomInteger('2.5'),None)
        



    # encrypt(rawstr,keyid=5) creates an encrypted string from the given raw string.
    # keyid is an integer from 0 to 10. 0-9 key ids for initial encription that
    # does not have newline('\n') character. key id=10 for final encryption where
    # newline character is converted to vtab('\v') character.
    def test_encrypt(self):
        self.assertEqual(enc.encrypt(),None)
        self.assertEqual(enc.encrypt("hello \n world."),'ue55~>\n>%~o5[U')
        self.assertEqual(enc.encrypt("hello \n world.",0),'I{ff-Y\nYt-8fE[')
        self.assertEqual(enc.encrypt("hello \n world.",2),"U388Hu\nu'H/8db")
        self.assertEqual(enc.encrypt("hello \n world.",9),'9[;;JR\nR^J ;O*')
        self.assertEqual(enc.encrypt("hello \n world.",10),';A~~bK\x0bKcb2~qe')



    # decrypt(encstr,keyid=5) converts the encrypted string into normal string.
    # keyid is an integer from 0 to 10. 10 for initial decryption and 0-9 key ids 
    # for final decription. In initial level, all vtab '\v' characters are
    # converted to newline character first.
    def test_decrypt(self):
        self.assertEqual(enc.decrypt(),None)
        self.assertEqual(enc.decrypt('ue55~>\n>%~o5[U'),'hello \n world.')
        self.assertEqual(enc.decrypt('I{ff-Y\nYt-8fE[',0),'hello \n world.')
        self.assertEqual(enc.decrypt("U388Hu\nu'H/8db",2),'hello \n world.')
        self.assertEqual(enc.decrypt('9[;;JR\nR^J ;O*',9),'hello \n world.')
        self.assertEqual(enc.decrypt(';A~~bK\x0bKcb2~qe',10),'hello \n world.')    





if __name__ == '__main__':
    unittest.main()

