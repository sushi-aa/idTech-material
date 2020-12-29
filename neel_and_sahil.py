


d = dict()
for i in range(0, 10):
    d[i] = i**2

print(d)

d2 = {'Arushi': 18, 'Sahil': 12, 'Neel': 12}
print(d2)

d2.update({'Sally': 20})
print(d2)

print( sorted(d2.items(), reverse=True) )
print(sorted(d2.items(), key=lambda x: x[1], reverse=True))
