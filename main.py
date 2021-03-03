class EllipticCurve:

    def __init__(self,a,b):
        self.a = a
        self.b = b
        self.g = None
        self.modulus = None

    def show_equation(self):
        e = f'y**2 = X**3 + {self.a}*x + {self.b}'
        print('The equation is:', e)
        pass

    def set_generator_point(self,x,y):
        self.g = (x,y)
        return self.g

    def set_modulus(self,n):
        self.modulus = n
        return self.modulus

    def get_modulus(self,n,inverse=False):
        if not self.modulus:
            raise Exception('Modulus parameter must by defined\n'+
                            'use set_modulus(n) to set it')
        if not inverse:
            result = n%self.modulus
        else:
            result = None
            loop = range(1000000000)
            for i in loop:
                print(i, 'of', loop, end='\r')
                if n*i%self.modulus == 1:
                    result = i
                    break
        return result

    def get_next_gslope(self,point,is_double=False):
        x,y = point
        xg,yg = self.g
        if is_double:
            nominator = 3*(x**2)+self.a
            denominator = 2*y
        else:
            nominator = y-yg
            denominator = x-xg
        if self.modulus:
            nominator = self.get_modulus(nominator)
            denominator = self.get_modulus(denominator,inverse=True)
            if (nominator is None) or (denominator is None):
                result = None
            else:
                result = (nominator*denominator)%self.modulus
        else:
            result = nominator/denominator
        return result

    def get_next_gpoint(self,point,is_double=False):
        if not self.g:
            raise Exception('Generator point must be set\n'+
                            'use set_generator_point(x,y) to set it')
        x,y = point
        xg,yg = self.g
        slope = self.get_next_gslope(point,is_double)
        if slope is None:
            x2 = None
            y2 = None
        else:
            x2 = (slope**2)-(x+xg)
            if self.modulus:
                x2 = x2%self.modulus
            y2 = (slope*(x-x2))-y
            if self.modulus:
                y2 = y2%self.modulus
        return (x2,y2)

    def get_gtimes_point(self,n):
        if n<=0:
            raise Exception('N must be greater than 0')
        else:
            result = self.g
            for _ in range(1,n):
                if _ == 1: 
                    result = self.get_next_gpoint(result,is_double=True)
                else: 
                    result = self.get_next_gpoint(result)
                if result == (None, None):
                    result = 'Reached infinity point'
                    break
        return result


class BitcoinKeys(EllipticCurve):
    a = 0
    b = 7
    G = (0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798,
       0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8)
    P = 2**256 - 2**32 - 2**9 - 2**8 - 2**7 - 2**6 - 2**4 - 1

    def __init__(self):
        self.private_key = None
        self.public_key = None
        super().__init__(self.a, self.b)
        super().set_generator_point(self.G[0],self.G[1])
        super().set_modulus(self.P)

    def set_private_key(self,prk):
        self.private_key = prk
        return self.private_key

    def gen_public_key(self):
        prk = self.private_key
        self.public_key = self.get_gtimes_point(prk)
        return self.public_key

    def get_public_key(self):
        return self.public_key


        

if __name__=='__main__':
    a = BitcoinKeys()
    a.set_private_key(100)
    print(a.gen_public_key())
    print(a.get_public_key())
