'''
9. Volver a preprocesar el archivo insertando la cadena AQUÍ cada 20 caracteres, el texto resultante
deberá contener un número de caracteres que sea múltiplo de 4, si es necesario rellenar al final con
caracteres X según se necesite
'''
s = open("HERALDOSNEGROS_pre.txt",mode="r", encoding='utf-8')
string=s.read()
s.close()
def insertEvery20(s):
    aqui='AQUI'
    i=19
    size=len(s)
    while(i<size):
        s = s[:i] + aqui + s[i:]
        i+=(19+len(aqui))
        size+=len(aqui)
    if(len(s)%4!=0):
        s=s+'X'*(4-len(s)%4)        
    return s
final=insertEvery20(string)
print(final)
