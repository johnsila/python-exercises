#a program that will take a word
#  and output the pig latin version of the word by following the following rules:
"""a. If the word starts with a consonant or group of consonants, move all letters
before the first vowel to the end of the word then add "ay".
 eg,will=illway,dog= ogday,chatter -> atterchay """
# If the word starts with a vowel, 
# simply add "way" to the end of the word eg electrician – electricianway.

print("PIG LATIN GAME")

ay = 'ay'
way = 'way'
consonant = ('B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','Y','V','X','Z')
vowel = ('A','E','I','O','U')
user_word = input('Enter a word : ')
# getting first letter and making sure its a string and setting it to uppercase
first_letter = user_word[0]
first_letter = str(first_letter)
first_letter=first_letter.upper()
if first_letter in consonant:
   print(first_letter,'is a consonant')
   length_of_word = len(user_word)
   remove_first_letter = user_word[1:length_of_word]
   pig_latin=remove_first_letter+first_letter+ay
   print('The word in Pig Latin is:',pig_latin)
elif first_letter in vowel:
   print(first_letter,'is a vowel')
   pig_latin=user_word+way
   print('The word in Pig Latin is:',pig_latin)
else:
   print("invalid word")
#end of program
