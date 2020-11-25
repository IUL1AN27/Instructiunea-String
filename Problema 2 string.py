a=str(input('Caracterele sunt:'))
MAJUSCULE=0
cifre=0
speciale=0
for n in a:
    if ord(n) in range(65 , 91):
        MAJUSCULE+=1
    if ord(n) in range (48 , 58):
        cifre+=1
    if ord(n) in range (33 , 48) or ord(n) in range (58 , 65) or ord(n) in range (123 , 127): 
        speciale+=1
print(f'numarul de majuscule este {MAJUSCULE}')
print(f'numarul de cifre este {cifre}')
print(f'numarul de caractere speciale este {speciale}')
