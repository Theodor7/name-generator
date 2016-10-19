from random import randint, choice
vowels, consonants, name, pattern = 'aaaaaaaaaaaaaeeeeeeeeeeeeeiiiiiiiiioooooooooouuuuyy', 'bbbbbbbbcccddddddffffffggghhhjjkkkkkkkllllllmmmmmmmmnnnnnnnppppppqrrrrrrsssssssssstttttttvvvvwxz', '', randint(0,1)
suffixes = ['town','ville','field','ton','bury','ford','ham','thorp','bourne','inver','beck','burgh','chester','chipping','dale','gate','halm','ing','ington','ness','pool','stead','ster','tilly','combe','wood','burn','bridge','lock','church']
word_start = ['Greater ','Small ','Long ','Market ','New ','Old ','North ','East ','West ','South ','Woods ']
word_end = [' Hill',' Dale',' Heath',' End',' Cross',' Woods',' Sands',' Green']

for x in range(0,randint(2,6)):
    if x %2 == pattern:
        name += choice(vowels)
    else:
        name += choice(consonants)

name += choice(suffixes)
town_name = name.capitalize()
if randint(0,4) == 0 :
    if randint(0,3) == 0 :
        town_name += choice(word_end)
    else:
        town_name = choice(word_start) + town_name
print town_name
