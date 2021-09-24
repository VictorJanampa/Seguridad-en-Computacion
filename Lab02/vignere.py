alpha=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string)-len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))

def cifrar(text,key):
    cText = []
    for i in range(len(text)):
        x = (alpha.index(text[i])+alpha.index(key[i])) % 27
        cText.append(alpha[x])
    return("" . join(cText))

def descifrar(text, key):
    oText = []
    for i in range(len(text)):
        x = (alpha.index(text[i])- alpha.index(key[i])+ 27) % 27
        oText.append(alpha[x])
    return("" . join(oText))


s = "WPIXHVYYOSRTECSZBEEGHUUFWRWTZGRWUFSRIWESSXVOHAIHOHWWHCWHUZOBOZEAOYBMCRLTEYOTI"
key = "HIELO"
key = generateKey(s, key)
print('Original :',s)
print("Descifrado :",descifrar(s, key))
