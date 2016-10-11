import random
vowels = 'aaaaaaaaaaaaaeeeeeeeeeeeeeiiiiiiiiioooooooooouuuuyy'
consonants = 'bbbbbbbbcccddddddffffffggghhhjjkkkkkkkllllllmmmmmmmmnnnnnnnppppppqrrrrrrsssssssssstttttttvvvvwxz'
name = ''
pattern = random.randint(0,1)
for x in range(0,random.randint(3,10)):
    if x %2 == pattern:
        name += random.choice(vowels)
        if random.randint(0,8) == 0:
            pattern = -(pattern-1)
    else:
        name += random.choice(consonants)
        if random.randint(0,4) == 0:
            pattern = -(pattern-1)
print name.capitalize()
