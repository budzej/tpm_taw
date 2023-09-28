'''
Sprawdzian 01 liczby, listy, krotki
Błażej Rudnik
3TPM
28.09.2023
'''

lista1=[2,4,6,'Anna','Zenon']
print(f"Lista wyglada tak: {lista1}")

#3
lista1.remove(4)


#4
lista1.append(99)


#5
lista2=[100,200,300]

#6
lista1.extend(lista2)

#7
print(f"Polaczone listy ze soba: {lista1+lista2}")

#8
lista2.reverse()

#9
print(f"Odwrocona lista2 wyglada tak: {lista2}")

#10
#lista1.sort()

#11
#print()


#12
moja_tupla=('A','B','C')

#13
lista=list(moja_tupla)
lista.append('D')
moja_tupla=tuple(lista)

#14
print(f"Tupla wyglada teraz w nastepujacy sposob: {moja_tupla}")



#BONUS
start=int(input("Podaj poczatek zakresu: "))
end=int(input("Podaj koniec zakresu: "))
listaX =[x for x in range(start, end + 1)if x % 2!=0]

print(f"Lista z liczbami nieparzystymi: {listaX}")
