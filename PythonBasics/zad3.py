lista = []
unos = "0"
while str(unos) != "Done": 
    unos = input("unesi broj: ")
    if str(unos)!="Done" and ord(unos)>=48 and ord(unos)<=57:
        lista.append(int(unos))
    else:
        print("unsei broj koji cvalja")
print(len(lista))
zbroj = 0
for number in lista:
    zbroj+=number
print(zbroj/len(lista))
print(min(lista))
print(max(lista))
lista.sort()
print(lista)
