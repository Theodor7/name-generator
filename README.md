# Random Name Generator
Generates random names.
Experimenting by making different versions to try and get the best results.

name-generator-1
  My first attempt.
  Letters divided into 4 lists: vowels, consonants, and a list for each with the rare letters.
  While loop (while name is less than name length, add new letter).
  In-built higher chance two of the same consonants in a row.

name-generator-2
  Letters divided into 3 strings: vowels, consonants, and consonants of which there can two of in a row.
  For loop (3 to 5 times it adds a vowel, then a consonant, with a chance of either doing the opposite or adding a vowel then two of the same consonant).
  Then is has a chance of removing the first letter, and a chance of removing the last.
  In-built higher chance two of the same consonants in a row (only some consonants).

name-generator-3
  Letters divided into 2 strings: vowels, and consonants.
  While loop (while name is less than name length, add new letter).
  NO in-built higher chance two of the same consonants in a row.
  A new letter becomes less likely to be a vowel, the more of them there are in a row. Same with consonants.

name-generator-4
  Letters divided into 2 strings: vowels, and consonants.
  NO in-built higher chance two of the same consonants in a row.
  For loop (Adds a new letter a random amount of times).
  Pro: Very easy to adjust chances of vowels appearing 2 times in a row, independently of consonants.
