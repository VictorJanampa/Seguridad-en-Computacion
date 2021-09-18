'''
1.	Realizar las siguientes sustituciones: j x i, h x i, ñ x n, k x l, u x v, w x v, y x z
2.	Elimine las tildes
3.	Convierta todas las letras a mayúsculas
4.	Elimine los espacios en blanco y los signos de puntuación
5.	Guarde el resultado en el archivo “HERALDOSNEGROS_pre.txt”
'''
import string
def replacement(s):
    a = ["j","h","ñ","k","u","w","y","á","é","í","ó","ú"]
    b = ["i","i","n","l","v","v","z","a","e","i","o","u"]
    for i in range(len(a)):
        s = s.replace(a[i], b[i]).replace(a[i].upper(), b[i].upper())
    return s

def removePunctuation(s):
    punctuation = string.punctuation+"¿¡\n\t "
    
    for i in range(len(punctuation)):
       s = s.replace(punctuation[i], "")
    return s

file = open("HERALDOSNEGROS.txt",mode="r", encoding='utf-8')
s=replacement(removePunctuation(str(file.read())).upper())
string = open("HERALDOSNEGROS_pre.txt",'w',encoding = 'utf-8')
string.write(s)
print(s)
file.close()
string.close()


