def test(s):
    lowc=0
    upc=0
    for i in s:
        if i.isupper():
            upc+=1
        elif i.islower():
            lowc+=1
        else: pass
    print('number of upper case letters',upc)
    print('number of lower case letters',lowc)

test('Bungou Stray Dogs')




