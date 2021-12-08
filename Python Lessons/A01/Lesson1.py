x = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'

a = x.split()

b = a[1]

b = b.split('@')
print(b[1])