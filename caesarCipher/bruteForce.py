def attack(encrypted):
    key = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    keyLimit = 1

    probability = []
    while keyLimit < 27:
        randomState = ''
        for i in encrypted:
            
            if i == ' ':
                randomState += ' '
                continue
            
            
            letter = key.index(i.upper()) - keyLimit
            if letter < 0:
                    randomState += key[letter + 26]
            else:
                randomState += key[letter]
        
        probability.append(randomState)
        keyLimit+=1
    
    return probability

print(attack('DGKDP VDOHK'))
