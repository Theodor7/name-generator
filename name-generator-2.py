import random
word_type = random.randrange(0,2)
name_length = random.randrange(2,5) #length of name/2 -+2
name = ''
vowels = 'aaaaeeeeiiiooouy'
consonants = 'bbbbccddddffffggghhhjjjkkkkllllmmmmnnnnppppqrrrrssssttttvvvwxz'
consonants_double = 'gklmnprst'
for x in range(0,name_length):
    if(random.randrange(0,2) != 0 or x < 2):
        name += random.choice(vowels) + random.choice(consonants)
    elif(random.randrange(0,3) == 0):
        name += random.choice(vowels) + 2*random.choice(consonants_double)
    else:
        name += random.choice(consonants) + random.choice(vowels)
if(random.randrange(0,2) == 0):
    name += random.choice(vowels)
if(random.randrange(0,2) == 0):
    name = name[1:]
print name.capitalize()
