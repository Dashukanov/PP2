import re
with open("row.txt", 'r', encoding='utf-8') as file:
    str = file.readlines()
a = ''.join(str)

#1
tx = re.compile("a{1}b*")
m = tx.findall(a)
print(m)

#2
tx = re.compile("a{1}b{2,3}")
m = tx.findall(a)
print(m)

#3
tx = re.compile("[a-z]*_[a-z]*")
m = tx.findall(a)
print(m)

#4
tx = re.compile("[A-Z][a-z]+")
m = tx.findall(a)
print(m)

#5
tx = re.compile("a\w.+b")
m = tx.findall(a)
print(m)

#6
a = ''.join(str)
tx = re.sub('[ ,.]', ':', a)
print(tx)

#7
tx = re.sub('_',' ', a)
tx = tx.title()
tx = re.sub(' ', '', tx)
print(tx)

#8
tx = re.findall(r"[A-Z][a-z]*", a)
print(tx)

#9
tx = re.sub(r"(\w)([A-Z])", r"\1 \2 ", a)
print(tx)

#10
tx = re.sub('(.)([A-Z][a-z]+)', r'\1_\2 ', a)
tx = tx.lower()
tx = re.sub('([a-z0-9])([A-Z])', r'\1_\2', tx)
print(tx)