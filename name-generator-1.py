import random
list_vowels = ['a','e','i','o']
list_consonants = ['b','d','f','g','h','j','k','l','m','n','p','r','s','t']
list_vowels_rare = ['y','u']
list_consonants_rare = ['q','w','x','z','c','v']
list_name = [] #resets name to 0 letters
var_letter_type = random.randrange(0,2) #variable for use in determining the next type of letter; 0=vowel 1=consonant
var_letter_position = 0
var_name_length = random.randrange(4,11) #length of the name
var_letter_event = 0
def letter_new(): #adds a letter to current name
    if(var_letter_type == 0 and random.randrange(0,20) != 0):
        list_name.append(list_vowels[var_vowels]) #adds a vowel to current name
    elif(var_letter_type == 0):
        list_name.append(list_vowels_rare[var_vowels_rare]) #adds a rare vowel to current name
    elif(var_letter_type == 1 and random.randrange(0,20) != 0):
        list_name.append(list_consonants[var_consonants]) #adds a consonant to current name
    else:
        list_name.append(list_consonants_rare[var_consonants_rare]) #adds a rare consonant to current name
while(var_letter_position <var_name_length): #adds letters until the limit is met
    var_vowels = random.randrange(0,len(list_vowels))
    var_consonants = random.randrange(0,len(list_consonants))
    var_vowels_rare = random.randrange(0,len(list_vowels_rare))
    var_consonants_rare = random.randrange(0,len(list_consonants_rare))
    letter_new() #adds a letter to current name
    var_letter_position += 1
    if(random.randrange(0,6) != 0): #chance that the letter type will not change
        if(random.randrange(0,6) == 0 and var_letter_type == 1 and var_letter_position != 1): #chance that the next letter is a duplicate of the previous consonant
            list_name.append(list_consonants[var_consonants])
            var_letter_position += 1
            var_letter_type = 0
        elif(var_letter_type == 0): #changes the letter type
            var_letter_type = 1
        else:
            var_letter_type = 0
str_name = ''.join(list_name).capitalize()
print str_name
