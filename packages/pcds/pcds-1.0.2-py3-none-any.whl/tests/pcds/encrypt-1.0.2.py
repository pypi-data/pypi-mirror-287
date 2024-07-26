'''
Module Description
--------------------
module filename: encrypt.py
module name: encrypt
Author: A K M Aminul Islam
Last Modified: Sunday July 14 2024 12:45 PM
Version:1.0.2

Description: This module can encrypt a raw string and can decrypt the encrypted
    string using a selected key symmetrically. The key is 95 character long and
    it is made of randomly arranged printable characters (ascii codes:32-126).
Content: 
    Functions: dataType(arg), createRandomKey(), randomInteger(), encrypt(), decrypt()
    Others: ascii printable characters, 10 random keys (trk10)
Dependencies: random

'''

version="1.0.2"

import random




# list of printable characters (lpc)
# range of ascii codes=32-126, Total 95 characters
# ascii code=lpc[index]+32
lpc=[' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~']
tpc=(' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~')
lpcString=' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'



finalkey='K0N/G3J.#):]gdeaV,I=45n7D9B`^>@?O&mslo*1j%TZ8C+WrQR|-uHYLFMy"iX h({}qAwU;$f!~xtbSE26_[\'c<\\zPpvk'



# tuple of 10 random keys (trk10)
trk10=('YyCk$9R&qLz`)B[+\\O~34HDsl\'*m/(N#de=^PU?>7jAKh5,np!]b:SVxW;XM|w%_gJZrE{6FIQc1f"o- G8ivu.t@a0T<}2', \
'8o"A?x|%`\'VTe)\\Hmt~JI5[F]R9;<k(NpYMCSEy6qZhKW@71bB0* iu=Xn4:}z!U{^Lcv/Ql>aj_O2,+Gr-sf$gwD3&#P.d', \
'u!A#n\\yWT}0&z-b)*N^?QB"Dl%Rt<{+r9IcJ7[vSpoP6hME>(1Gs~KO`XYZ];4$@g5.Ld3fkUV:w8meH_q/,aF2\'x C=|ji', \
'R*"#vu3ykqs5BO$F/\\KDG9S.J]%Q =,>U-n?xb;4YT[hac\'MA~2<_0PN8pZ!}X^gl1t:deIm6rj(z@C+&{W)EL7woV`f|iH', \
'aof#SI%r(T,?i;D4s1[Qj5n7^l82K3_$HAphyWFG*\\O`LVu\'B!X.9Yw"J:Z-}~Uxgqbc{&6R@|]kC/+dPM> t)E=e<zvmN0', \
'>Y<=^EfK(&x-,7U.ZGmCOrF?\'9:t4JlDWj1bN6)B{I#L\\g0T"v$3|;h A/@cSzdM`!PV[e+Hui]w58n~p*oaRXk%qysQ_}2', \
'I>N* f&;0hR4/#.JuiHw\'5jMAd8^G<DFlpmCsv@)P7WKzTZg\\+Q,k"[n1x$e|Y]E`_BS9:%2yq!c3U-}~=rat(bX?LV{Oo6', \
'Eg#:=^nH(iJBk\'X%/123rv~SV9Uf$7ZYD}qo.-F+CQsTPM46_p8AwLN)jaOb\\"I<`R*>lztdGmW,&Kuh@ {!;c50xye]|[?', \
'W\\|@w2jg{c*hP-~/l]aJp&>)$}:8o=m?#A6(DEF^eI!s3;Vv[b7SHRzMtU9d LnZ<0xXNQ`,1%+TG"CK4q.kru5\'ByY_Oif', \
'R~qL$z]s<i{Xd-*2BN+?4vG},/"w(Y53uC=Aj1M7nlEb&.gpPe%#WU0Tk\'8yDK@:\\!f6O[Ht9|_Z;)FJ`r IoQc^mx>ahSV', \
)





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





# createRandomKey() creates a 95 character long random key string
# rearranging the printable characters randomly
# >>> key=enc.createRandomKey()
# >>> key
# 'Q!"#r~RAh%s$Jl./0`>5436H8XxP<=\'?@v+aDE2G71uKLMnz)g&\\TSV }YO[f]^_*CbcIeUw-i9k(mNopqd,tF|W:yj{B;Z'
# >>> len(key)
# 95
def createRandomKey():
    mylpc=lpc.copy()
    for i in range(100):
        i=int(random.random()*95)
        j=int(random.random()*95)
        while i==j:
            i=int(random.random()*95)
            j=int(random.random()*95)
        # exchanging characters   
        temp=mylpc[i]
        mylpc[i]=mylpc[j]
        mylpc[j]=temp
    return "".join(mylpc)




# randomInteger(size=10) creates a random integer of the given size
# >>> enc.randomInteger(5)
# 29420
# >>> enc.randomInteger()
# 9593015503
# >>> enc.randomInteger()
# 7482870104
def randomInteger(size=10):
    try:
        if dataType(size) != 'int':
            raise TypeError("Argument of randomInteger() must be an integer.")
        if size < 1:
            raise ValueError("Digits of integer must be a positive whole number.")
    except Exception as e: print(e); return None
    s=""
    for i in range(size): 
        n=int(random.random()*10)
        if i==0:
            while n==0:
                n=int(random.random()*10)
        s=s+chr(48+n)
    return int(s)    
    




# encrypt(rawstr,keyid=5) creates an encrypted string from the given raw string.
# keyid is an integer from 0 to 10. 0-9 key ids for initial encription that
# does not have newline('\n') character. key id=10 for final encryption where
# newline character is converted to vtab('\v') character.
# >>> enc.encrypt("hello \n world.",2)
# "U388Hu\nu'H/8db"
# >>> enc.encrypt("hello \n world.",0)
# 'I{ff-Y\nYt-8fE['
# >>> enc.encrypt("hello \n world.")
# 'ue55~>\n>%~o5[U'
# >>> enc.encrypt("hello \n world.",10)
# ';A~~bK\x0bKcb2~qe'
def encrypt(rawstr=None,keyid=5):
    try:
        if rawstr == None:
            raise ValueError("String argument required for encryption.")
        if dataType(rawstr) != 'str':
            raise TypeError("String argument required for encryption.")
        if dataType(keyid) != 'int':
            raise TypeError("Integer keyid (0-10) argument required in encrypt(). ")
        if keyid<0 or keyid>10:
            raise ValueError("Integer keyid (0-10) argument required in encrypt().")
    except Exception as e: print(e); return None
    key=""
    if keyid==10: key=finalkey
    else: key=trk10[keyid]    
    if len(key) != 95:
        raise ValueError("Invalid Key (Key length is not 95).")
    s=""
    for c in rawstr:        
        if ord(c)==10 and keyid==10:
            # in final encryption, newline character is converted to vtab character
            c='\v'
            s=s+c
        elif ord(c) < 32 or ord(c) > 126: s=s+c
        else:
            s=s+key[ord(c)-32]
    return s
    




# decrypt(encstr,keyid=5) converts the encrypted string into normal string.
# keyid is an integer from 0 to 10. 10 for initial decryption and 0-9 key ids 
# for final decription. In initial level, all vtab '\v' characters are
# converted to newline character first.
# >>> enc.decrypt(';A~~bK\x0bKcb2~qe',10)
# 'hello \n world.'
# >>> enc.decrypt('ue55~>\n>%~o5[U')
# 'hello \n world.'
# >>> enc.decrypt("U388Hu\nu'H/8db",2)
# 'hello \n world.'
# >>> enc.decrypt('I{ff-Y\nYt-8fE[',0)
# 'hello \n world.'
# >>>
def decrypt(encstr=None,keyid=5):
    try:
        if encstr == None:
            raise ValueError("String argument required in decrypt().")
        if dataType(encstr) != 'str':
            raise ValueError("String argument required in decrypt().")
        if dataType(keyid) != 'int':
            raise ValueError("Integer keyid (0-10) argument required in decrypt().")
        if keyid<0 or keyid>10:
                raise ValueError("Integer keyid (0-10) argument required in decrypt().")
    except Exception as e: print(e); return None
    key=""
    if keyid==10: key=finalkey
    else: key=trk10[keyid]    
    if len(key) != 95:
        raise ValueError("Invalid Key (Key length is not 95).")
    s=""
    for c in encstr:
        if ord(c)==11 and keyid==10:
            # initially, vtab character is converted to newline character
            s=s+'\n'
        elif ord(c) < 32 or ord(c) > 126: s=s+c        
        else:
            for i in range(95):
                if c==key[i]:
                    s=s+chr(i+32)
                    break
    return s
    
  