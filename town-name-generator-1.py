from random import randint, choice
vowels, consonants, name, pattern = 'aaaaaaaaaaaaaeeeeeeeeeeeeeiiiiiiiiioooooooooouuuuyy', 'bbbbbbbbcccddddddffffffggghhhjjkkkkkkkllllllmmmmmmmmnnnnnnnppppppqrrrrrrsssssssssstttttttvvvvwxz', '', randint(0,1)
suffixes = ['town','ville','field','ton','bury','ford','ham','thorp','bourne','inver','beck','burgh','chester','chipping','dale','gate','halm','ing','ington','ness','pool','stead','ster','tilly','combe','wood','burn','bridge','lock','church','polis']
word_start = ['Greater ','Small ','Long ','New ','Old ','North ','East ','West ','South ']
word_end = [' Hill',' Heath',' End',' Cross',' Woods',' Sands',' Green',' City']

for x in range(0,randint(2,6)):
    if x %2 == pattern:
        name += choice(vowels)
        if randint(0,7) == 0:
            pattern = -(pattern-1)
    else:
        name += choice(consonants)
        if randint(0,4) == 0:
            pattern = -(pattern-1)

name += choice(suffixes)
town_name = name.capitalize()

if randint(0,6) == 0 :
    if randint(0,2) == 0 :
        town_name += choice(word_end)
    else:
        town_name = choice(word_start) + town_name
print town_name
