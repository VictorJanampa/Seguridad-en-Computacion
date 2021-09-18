import pprint
'''
6. Aplicar el método Kasiski, que recorre el texto preprocesado y halla los trigramas en el mismo
(sucesión de tres letras seguidas que se repiten) y las distancias (número de caracteres entre ellos)
entre los trigramas
'''
f = open("HERALDOSNEGROS_pre.txt",mode="r", encoding='utf-8')
s=f.read()
f.close()
def kasiski(s):
    trigrams = dict()
    for i in range(0,len(s)-2):
        act = s[i:i+3]
        count = [i for i in range(len(s)) if s.startswith(act, i)]
        if(len(count)>1):
            res=[]
            for j in range(len(count)-1):
                res.append(count[j+1]-count[j]-3)
            trigrams.update(dict({act:res}))
    return trigrams
pprint.pprint(kasiski(s))
