#ask user for sentence
sentence = input("Please enter a sentence to translate into pig latin:").strip().lower()

# split sentence into words
split = sentence.split()
vowels = "aeiou"
newWords = []

# loop through words and convert to pig latin
for word in split:
    if word[0] in vowels:
        #if word starts with vowel, just add "yay"
        newWord = word + "yay"
        newWords.append(newWord)
    else:
        vowelPosition = 0
        for letter in word:
            #otherwise move first consonant cluster to end and add "ay"
            if letter not in vowels:
                vowelPosition = vowelPosition + 1
            else:
                break
        cons = word[:vowelPosition]
        remainder = word[vowelPosition:]
        newWord = remainder + cons + "ay"
        newWords.append(newWord)

# stick words back together and capitalize beginning     
output = " ".join(newWords).capitalize()

#output final string
print(output)