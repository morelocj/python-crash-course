#6-1.
person = {
    'first_name':'Jared',
    'last_name':'Friedman',
    'age': 41,
    'city':'Brooklyn',
}
print(person)

#6-2.
fav_nums = {
    'Lucy':5.5,
    'Viana':0,
    'Pepe':42,
}
print(fav_nums)

#6-3.
glossary = {
    'print':'show on the computer',
    'float':'a number with a decimal',
}
pr = glossary['print']
fl = glossary['float']
print(f'print: {pr}')
print(f'float: {fl}')

#6-4.
for item in glossary:
    print(item)
    print(glossary[item])

#6-5.
rivers = {
    'nile':'egypt',
    'mississippi':'USA',
    'congo':'DRC'
}
for river in rivers:
    print(f'The {river} runs through {rivers[river]}.')
for river in rivers:
    print(river)
for river in rivers:
    print(rivers[river])

#6-6.
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
should_take = ['jared', 'jen', 'pepe', 'lucy', 'phil']
for name in should_take:
    if name in favorite_languages:
        print(f'Dear {name}, thank you for responding.')
    else:
        print(f'Dear {name}, please take the poll.')

#6-7.
person2 = {
    'first_name':'lucy',
    'last_name':'morelock',
    'age':5.5,
    'city':'woburn'
}
person3 = {
    'first_name':'viana',
    'last_name':'morelock',
    'age':1.5,
    'city':'woburn',
}
people = [person, person2, person3]
for i in people:
    print(i)

#6-8.
pet1 = {
    'animal':'bird',
    'owner':'viana'
}
pet2 = {
    'animal':'cat',
    'owner':'lucy',
}
pet3 = {
    'animal':'dog',
    'owner':'hazel'
}
pets = [pet1, pet2, pet3]
for pet in pets:
    print(pet)

#6-9.
favorite_places = {
    'lucy':'disney world',
    'viana':'baby school',
    'rainer':'berlin'
}
for i in favorite_places:
    print(f'{i}\'s favorite place is {favorite_places[i]}.')

#6-10.
fav_nums2 = {
    'Lucy':[5.5, 1.5],
    'Viana':0,
    'Pepe':[1,2,3,42]
}
for i in fav_nums2:
    print(f'{i}: {fav_nums2[i]}')

#6-11.
cities = {
    'boston':{
        'country':'USA',
        'name backwards':'notsob',
        'accent':'pak the cah in havid yad!',
    },
    'sydney':{
        'country':'australia',
        'name backwards':'yendys',
        'accent':'gdeye mite!',
    },
    'london':{
        'country':'england',
        'name backwards':'nodnol',
        'accent':'jolly good show!'
    },
}
for place, info in cities.items():
    print(f'\n{place.title()}:')
    country = info['country']
    print(f'\tCountry: {country}')
    back = info['name backwards']
    accent = info['accent']
    print(f'\tName backwards: {back}')
    print(f'\tAccent: {accent}')

#6-12.
pets = {
    'Squawkey':{
        'animal':'bird',
        'owner':'viana'
        },
        'Meowsers':{
            'animal':'cat',
            'owner':'lucy',
            },
            'Ruff':{
                'animal':'dog',
                'owner':'hazel'
                },
                }
for pet, info in pets.items():
    species = info['animal']
    owner = info['owner']
    print(f'{pet} is a {species} who belongs to {owner.title()}.')
