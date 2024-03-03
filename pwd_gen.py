import string 
import random
s1=string.ascii_uppercase
s2=string.ascii_lowercase
s3=string.digits
s4=string.punctuation
pwd_length = int(input("enter the lenght of the password needed:\n"))
s=[]
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))
print("".join(random.sample(s,pwd_length)))