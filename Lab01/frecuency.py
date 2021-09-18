import operator
import string
'''
5. Abra el archivo generado e implementar una función que calcule una tabla de frecuencias para
cada letra de la ’A’ a ’Z’. La función deberá definirse como frecuencias(archivo) deberá devolver un
diccionario cuyos índices son las letras analizadas y cuyos valores son las frecuencias de las mismas
en el texto (número de veces que aparecen). Reconozca en el resultado obtenido los cinco caracteres
de mayor frecuencia
'''
s = open("HERALDOSNEGROS_pre.txt",mode="r", encoding='utf-8')
def frecuency(s):
    text=s.read()
    alpha = string.ascii_uppercase
    d=dict()
    for i in alpha:
        d[i] = text.count(i)
    sortedDict = sorted(d.items(), key=operator.itemgetter(1), reverse=True)
    return sortedDict
d=frecuency(s)
s.close()
print(d[0:5])

    
