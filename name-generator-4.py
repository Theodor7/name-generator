from random import randint, choice
vowels, consonants, name, pattern = 'aaaaaaaaaaaaaeeeeeeeeeeeeeiiiiiiiiioooooooooouuuuyy', 'bbbbbbbbcccddddddffffffggghhhjjkkkkkkkllllllmmmmmmmmnnnnnnnppppppqrrrrrrsssssssssstttttttvvvvwxz', '', randint(0,1)
for x in range(0,randint(3,10)):
    if x %2 == pattern:
        name += choice(vowels)
        if randint(0,7) == 0:
            pattern = -(pattern-1)
    else:
        name += choice(consonants)
        if randint(0,4) == 0:
            pattern = -(pattern-1)
print name.capitalize()
