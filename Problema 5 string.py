cnp=str(input('Introduceti CNP-ul persoanei: '))
if cnp.isnumeric() and len(cnp) == 13:
    print('CNP-ul este corect')
else:
    print('CNP-ul este gresit')
