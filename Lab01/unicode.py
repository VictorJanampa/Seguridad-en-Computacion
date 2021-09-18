'''
7. Volver a preprocesar el archivo cambiando cada carácter según UNICODE-8
8. Volver a preprocesar el archivo cambiando cada carácter según UNICODE-8230
'''
s = open("HERALDOSNEGROS_pre.txt",mode="r", encoding='utf-8')
string=s.read()
s.close()
unicode8 = string.encode('utf-8').hex()
unicode8230 = string.encode('utf-16be').hex()
print('Unicode-8')
print('0x'+unicode8)
print('Unicode-8230')
print('0x'+unicode8230)
