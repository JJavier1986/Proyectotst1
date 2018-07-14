Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> ###Imprimir los numeros pares desde el 40 hasta el 60, ambos inclusive
n = 40
h = ''
while n <= 60:
    if n%2 == 0:
        h += ' %i' % n
    n += 1
print h
 
