class caesarCipher:
    def __init__(self):
        self.__key = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    def encrypt(self, data, shift):
        encrypted = ''
        for i in data:
            
            if i == ' ':
                encrypted += ' '
                continue
            
            encryptedLetter = self.__key.index(i.upper()) + shift
            if encryptedLetter > 25:
                encrypted += self.__key[encryptedLetter - 26]
            else:
                encrypted += self.__key[encryptedLetter]
        
        return encrypted
    
    def decrypt(self, data, shift):
        decrypted = ''
        for i in data:
            
            if i == ' ':
                decrypted += ' '
                continue
            
            decryptedLetter = self.__key.index(i.upper()) - shift
            if decryptedLetter < 0:
                decrypted += self.__key[decryptedLetter + 26]
            else:
                decrypted += self.__key[decryptedLetter]
        
        return decrypted


system = caesarCipher()
print(system.encrypt('Adham Saleh', 3))
print(system.decrypt('DGKDP VDOHK', 3))