import hashlib
def md5_hashing(str):
 hash_obj = hashlib.md5(str.encode())
 print("md5_hashing of ",str,":",hash_obj.hexdigest())
def sha3_512_hashing(str):
 hash_obj = hashlib.sha3_512(str.encode())
 print("sha3_512_hashing of",str,":",hash_obj.hexdigest())
def sha256(str):
    hash_obj=hashlib.sha256(str.encode())
    print("sha256 of",str,":",hash_obj.hexdigest())
print("choose the format of hashing")
print("1:md5_hashing\n2:sha3_512_hashing\n3:sha256")
n = int (input("enter the no of the above format:"))
mystring = input("Enter string to hash: ")
if n == 1:
    md5_hashing(mystring)
elif n == 2:
    sha3_512_hashing(mystring)
elif n == 3:
    sha256(mystring)
else:
    print("lol")
    
