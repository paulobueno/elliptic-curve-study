class EllipticCurve:

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.g = None
        self.modulus = None

    def show_equation(self):
        e = f'y**2 = X**3 + {self.a}*x + {self.b}'
        print('The equation is:', e)
        pass

    def set_generator_point(self, x, y):
        self.g = (x, y)
        return self.g

    def set_modulus(self, n):
        self.modulus = n
        self.g = (self.g[0] % n, self.g[1] % n)
        return self.modulus

    def get_modulus(self, n, inverse=False):
        result = None
        if not self.modulus:
            raise Exception('Modulus parameter must by defined\n' +
                            'use set_modulus(n) to set it')
        if not inverse:
            result = n % self.modulus
        else:
            loop = range(self.modulus - 1)
            for i in loop:
                print(i, 'of', loop, end='\r')
                if (n * i) % self.modulus == 1:
                    result = i
                    break
        return result

    def get_next_slope(self, xy1, xy2, is_double=False):
        x1, y1 = xy1
        x2, y2 = xy2
        result = None
        if is_double or (xy1 == xy2):
            nominator = 3 * (x1 ** 2) + self.a
            denominator = 2 * y1
        else:
            nominator = y1 - y2
            denominator = x1 - x2
        if self.modulus:
            nominator = self.get_modulus(nominator)
            denominator = self.get_modulus(denominator, inverse=True)
            if denominator is not None:
                result = (nominator * denominator) % self.modulus
            else:
                result = None
        else:
            result = nominator / denominator
        return result

    def get_next_point(self, xy1, xy2, is_double=False):
        if not self.g:
            raise Exception('Generator point must be set\n' +
                            'use set_generator_point(x,y) to set it')
        result = None
        x1, y1 = xy1
        x2, y2 = xy2
        slope = self.get_next_slope(xy1, xy2, is_double)
        if slope is not None:
            x3 = (slope ** 2) - (x1 + x2)
            if self.modulus:
                x3 = x3 % self.modulus
            y3 = (slope * (x2 - x3)) - y2
            if self.modulus:
                y3 = y3 % self.modulus
            result = (x3, y3)
        else:
            x3 = - (x1 + x2)
            if self.modulus:
                x3 = x3 % self.modulus
            result = (x3, 0)
        return result

    def get_gtimes_points(self, n):
        results_list = [self.g]
        for _ in range(n):
            print(_, ' of ',n,end='\r')
            point = results_list[-1]
            if point is not None:
                next_point = self.get_next_point(point, self.g)
                results_list.append(next_point)
            else:
                point = results_list[-2]
                next_point = self.get_next_point(point, results_list[2])
                results_list.append(next_point)
            results_list = results_list[-2:]
        return results_list


class BitcoinKeys(EllipticCurve):
    a = 0
    b = 7
    G = (0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798,
         0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8)
    P = 2 ** 256 - 2 ** 32 - 2 ** 9 - 2 ** 8 - 2 ** 7 - 2 ** 6 - 2 ** 4 - 1

    def __init__(self):
        self.private_key = None
        self.public_key = None
        super().__init__(self.a, self.b)
        super().set_generator_point(self.G[0], self.G[1])
        super().set_modulus(self.P)

    def set_private_key(self, prk):
        self.private_key = prk
        return self.private_key

    def gen_public_key(self):
        prk = self.private_key
        self.public_key = self.get_gtimes_points(prk)
        return self.public_key

    def get_public_key(self):
        return self.public_key


if __name__ == '__main__':
    # a = EllipticCurve(0,7)
    # a.set_generator_point(5,1)
    # a.set_modulus(17)
    # print(a.get_gtimes_points(25))
    a = BitcoinKeys()
    # a.set_generator_point(15, 4)
    # a.set_modulus(17)
    pk = '1E99423A4ED27608A15A2616A2B0E9E52CED330AC530EDCC32C8FFC6A526AEDD'
    print(a.get_gtimes_points(int(pk,16)))
