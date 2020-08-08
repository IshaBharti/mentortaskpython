day=input('enter the day')
meal=input('enter the meal')
if day=='monday':
    if meal=='breakfast':
        print('roti')
    elif meal=='lunch':
        print('sabji')
    else:
        print('gobhi')
if day=='tuesday':
    if meal=="breakfast":
        print("dalia")
    elif meal=="lunch":
        print('roti sabji')
    else:
        print('dal')
elif day=='wednesday':
    if meal=="breakfast":
        print('dal')
    elif meal=='lunch':
        print('idli')
    else:
        print('dalia')
elif day=='thursday':
    if meal=='breakfast':
        print('gulab jamun')
    elif lunch=='lunch':
        print('roti sabji')
    else:
        print("kadi")
elif day=='friday':
    if meal=='breakfast':
        print('roti anf dal')
    elif meal=='lunch':
        print('chai')
    else:
        print('pakora')
elif day=="saturday":
    print('juice')
    if meal=='breakfast':
        print('sabu dana')
    elif meal=='lunch':
        print('gulab jamun')
    else:
        print('dal')
else:
    print('juice all day')        


