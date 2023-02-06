#get the sentence from the user

original = input("What would you like to translate to pig latin?: ").lower().strip()


#split the sentence into words

words = original.split(" ")
print(words)

#loop through words and translate to pig latin

new_words = []

# if it starts with a vowel just add "yay"
vowels = 'aeiou'

for word in words:
    print(word)
    if word[0] in vowels:
        new_word = word+'yay'
        new_words.append(new_word)
        print(new_word)

#otherwise, move the first consonant cluster to the end and add "ay"
    else:
        vowel_pos = 0
        for letter in word:
            if letter not in vowels:
                vowel_pos += 1
            else:
                break
        cons = word[:vowel_pos]
        the_rest = word[vowel_pos:]
        new_word = the_rest + cons +'ay'
        print(new_word)
        new_words.append(new_word)

print(new_words)
#stick words back together

output = " ".join(new_words)

#output final string

print(output)
