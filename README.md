# Wiener_Theorem
Takes as input an RSA public key vulnerable to Wiener's Attack and outputs its corresponding RSA private key. 

i.e., for for public keys with `d < 1/3 * N ^(1/4)` 
where `d = RSA decryption exponent` and `N = RSA modulus`
`d` can be efficiently recovered, allowing construction of the RSA private key. 
