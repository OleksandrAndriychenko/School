a = b'r\xc3\xa9sum\xc3\xa9'
resul = a.decode()
print(resul)
resul_1 = resul.encode('Latin1')
print(resul_1)
resul_2 = resul_1.decode('Latin1')
print(resul_2)