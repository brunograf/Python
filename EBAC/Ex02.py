def gen (n):
   n = 1
   print ('Primeiro print')
   yield n
   
   n += 1
   print ('Segundo print')
   yield n
   
   n += 1
   print ('Terceiro print')
   yield n

g = gen (1)
print (next(g))
print (next(g))
print (next(g))