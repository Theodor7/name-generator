import random

def name():
    vowels = 'aaaaaaaaaaaaaeeeeeeeeeeeeeiiiiiiiiioooooooooouuuuyy'
    consonants = 'bbbbbbbbcccddddddffffffggghhhjjkkkkkkkllllllmmmmmmmmnnnnnnnppppppqrrrrrrsssssssssstttttttvvvvwxz'

    name = ''
    vowels_saturation = 0
    consonants_saturation = 0

    while(len(name) < random.randrange(3,12)):
        if(random.randrange(-3*vowels_saturation - 1, 3*consonants_saturation + 1) >= 0):
            name += random.choice(vowels)
            vowels_saturation += 1
            consonants_saturation = 0
        else:
            name += random.choice(consonants)
            consonants_saturation += 1
            vowels_saturation = 0
    return name.capitalize()

print
name = name()

print(name)
