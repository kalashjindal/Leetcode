def isPowerOfFour(n): 
    s=bin(n)[2:]  # convert decimal to binary representation
    return s.count("1")==1 and len(s)%2!=0 and n!=1 
  
# Driver code 
test_no = 64
if(isPowerOfFour(64)): 
    print(test_no, 'is a power of 4') 
else: 
    print(test_no, 'is not a power of 4') 
