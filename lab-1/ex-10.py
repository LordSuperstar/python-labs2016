s=input()
a=s.find('h')
b=s.rfind('h')
c=s.replace('h', 'H')
d=c[:a]+'h'+c[a+1:]
f=d[:b]+'h'+d[b+1:]
print(f)