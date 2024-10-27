import string

class monoAlphabetic:
    def __init__(self):
        self.__alphabet = string.ascii_uppercase #ABCDEFGHIJKLMNOPQRSTUVWXYZ

    def encrypt(self, data, key):
        encrypted = ''
        for i in data:
            if i == ' ':
                encrypted += ' '
            else:
                encrypted += key[self.__alphabet.index(i.upper())]
        
        return encrypted
    
    def decrypt(self, data, key):
        decrypted = ''
        for i in data:
            if i == ' ':
                decrypted += ' '
            else:
                decrypted += self.__alphabet[key.index(i.upper())]
        
        return decrypted
    

system = monoAlphabetic()
print(system.encrypt('Adham saleh', 'HWQRZXAPLTIDSBCOMVFKYNEGUJ'))
print(system.decrypt('HRPHS FHDZP', 'HWQRZXAPLTIDSBCOMVFKYNEGUJ'))

