class BitcoinKeys:
    #Curve Parameters
    # y**2 = x**3 + ax + b
    a = 0
    b = 7
    G = (55066263022277343669578718895168534326250603453777594175500187360389116729240,
        32670510020758816978083085130507043184471273380659243275938904335757337482424)
    P = 17

    def __init__(self):
        self.private_key = None
        self.public_key = None

    def sum_data_point(self,times):
        pass

    def set_private_key(self,prk):
        self.private_key = prk
        return self.private_key

    def gen_public_key(self):
        prk = self.private_key
        self.public_key = self.sum_data_point(prk)
        return self.public_key

    def get_public_key(self):
        return self.public_key


if __name__=='__main__':
    print('Start point at:', BitcoinKeys.G)

