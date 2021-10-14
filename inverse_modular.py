def inverse_modular(n,mod):
    reminder = n%mod
    multiple = n//mod
    return n,mod,reminder,multiple

if __name__=='__main__':
    print(inverse_modular(27,392))
    print(inverse_modular(17,15))

"""
1/27 (mod 392)
392 = 27*14 + 14
27 = 14*1 + 13
14 = 13*1 + 1

14 + 13(-1) = 1
27 + 14(-1) = 13
392 + 27(-14) = 14

(392 + 27(-14)) + (27 + 14(-1))(-1) = 1
392 + 27(-15) + 14 = 1
392(1) + 27(-15) + (392(1) + 27(-14)) = 1
392(2) + 27(-29) = 1
0 + 27(392-29) = 1 (mod 392)
27(363) = 1 (mod 392)
"""
