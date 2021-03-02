import sys
from Crypto.PublicKey import RSA
'''
-------------- Function Definitions --------------------
'''

'''
Input: (Int) numerator and (Int) denominator
Output: (List of Ints) Continuing fractions
'''
def cf(n, d):
    if d == 0: return []
    q = n//d
    r = n - q*d
    return [q] + cf(d, r)

'''
Input: (List of Ints) Continuing fractions
Output: (List of tuples) Convergents of input
'''
def cf_convergents(cf):
    convergents = [[1,0]]
    for i in range(len(cf)):
        if i == 0:
            convergents.append([cf[i], 1])
        else:
            n = cf[i] * convergents[i][0] + convergents[i-1][0]
            d = cf[i] * convergents[i][1] + convergents[i-1][1]
            convergents.append([n, d])
    return convergents

'''
-------------- End Function Definitions ---------------
'''


pub_key_file = sys.argv[1]

with open(pub_key_file) as f:
    key = RSA.importKey(f.read())

modulus = key.n
exponent = key.e
continued_fraction = cf(exponent, modulus)
convergents = cf_convergents(continued_fraction)

'''
Iterate over the convergents using each denominator as the private exponent to construct a private key. 

If the construct method fails, it can be assumed that factors p and q can't be computed, so d is not the private exponent.
'''
for i in range(len(convergents)):
    try:
        new_key = RSA.construct([modulus, exponent, convergents[i][1]])
        decryption_exponent = convergents[i][1]
        break
    except:
        pass

try:
    with open("private_key.pem", "wb") as f:
        f.write(new_key.exportKey(format='PEM', pkcs=8))
        print("Valid private key found with decryption exponent %s"%(decryption_exponent))
        print("Printing private key to file 'private_key.pem'")
except:
    print("No valid private key could be generated from the given inputs.")
    

