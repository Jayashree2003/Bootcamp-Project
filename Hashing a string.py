#Name: Jayashree S
#E-Mail ID: jaya20116.ad@rmkec.ac.in

import hashlib

str2hash = input("enter a string: ")

result = hashlib.md5(str2hash.encode())

print("The hash is : ", end ="")
print(result.digest())
print("size of the hash",len(result.digest()))