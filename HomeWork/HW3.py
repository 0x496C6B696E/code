# HW1: Write a Python script to read the contents of the file 'task1_fruits.txt', which contains various fruit names, each on a new line.
# Your goal is to count the frequency of each word (fruit name) and store this information in a dictionary.
# Output: { 'apple': 10, 'banana': 8, 'cherry': 5, # ... and so on for other fruits }
fruit_counts = {}
 
with open("fruits.txt", "r") as fr:
    for line in fr:
        fruit = line.strip()
        if fruit:
            if fruit in fruit_counts:
                fruit_counts[fruit] += 1
            else:
                fruit_counts[fruit] = 1

print(fruit_counts)
 


# HW2: Using the dictionary created in Task 1, identify the word(s) that occur most frequently in the file
# If there is a tie for the most frequent word, include all words that share the highest frequency.
# Write these words and their counts to a new text file: top_words.txt
# Output: Most Frequent Word(s): banana,grape\nFrequency: 15
max_count = 0
for count in fruit_counts.values():
    if count > max_count:
        max_count = count
 
top_words = []
for fruit, count in fruit_counts.items():
    if count == max_count:
        top_words.append(fruit)
 
with open("top_words.txt", "w") as fw:
    fw.write("Most Frequent Word(s): " + ",".join(top_words) + "\n")
    fw.write("Frequency: " + str(max_count) + "\n")
 
print("Most Frequent Word(s): " + ",".join(top_words))
print("Frequency: " + str(max_count))


# HW3: Create a dictionary where keys are numbers (1-10) and values are their squares.
# Write this dictionary to a CSV file (squares.csv) with two columns: Number and Square.
# Output: Number,Square\n1,1\n2,4\n3,9\n4,16 (Don’t forget this is csv, “,” means different column)
squares = {}
for n in range(1, 11):
    squares[n] = n * n
 
with open("squares.csv", "w") as csvfile:
    csvfile.write("Number,Square\n")
    for number, square in squares.items():
        csvfile.write(str(number) + "," + str(square) + "\n")

for n, s in squares.items():
    print(str(n) + "," + str(s))
 


# HW4: Determine the winner of the Vowel-Consonant Game. The game is played with a given string S, and two players, Mirza and Turan
# String: Both players are given the same string, S.
# Substrings: Players create substrings using the letters of S.
# Conditions:
# Mirza's substrings must start and end with consonants.
# Turan's substrings must start and end with vowels.
# End Condition: The game ends when all possible substrings conforming to the rules have been created.
# Scoring: Players score points based on the length of each unique substring they create.
# Output: The name of the winner and their score, or "Draw" if the game ends in a tie.
# Example: Apple -> Mirza: p,pp,ppl,pl,l; Turan: a,apple,e

def vowel_consonant_game(S):
    vowels = "aeiouAEIOU"
 
    def is_vowel(ch):
        return ch in vowels
 
    def is_consonant(ch):
        return ch.isalpha() and ch not in vowels
 
    mirza_score = 0
    turan_score = 0
    mirza_subs = []
    turan_subs = []
    seen = []
 
    n = len(S)
    for i in range(n):
        for j in range(i + 1, n + 1):
            sub = S[i:j]
 
            if sub in seen:
                continue
            seen.append(sub)
 
            first = sub[0]
            last  = sub[-1]
 
            if is_consonant(first) and is_consonant(last):
                mirza_score += len(sub)
                mirza_subs.append(sub)
 
            elif is_vowel(first) and is_vowel(last):
                turan_score += len(sub)
                turan_subs.append(sub)
 
    if mirza_score > turan_score:
        result = "Mirza wins! Score: " + str(mirza_score)
    elif turan_score > mirza_score:
        result = "Turan wins! Score: " + str(turan_score)
    else:
        result = "Draw! Both scored: " + str(mirza_score)
        
    print("Mirza substrings : " + str(mirza_subs))
    print("Mirza score      : " + str(mirza_score))
    print("Turan substrings : " + str(turan_subs))
    print("Turan score      : " + str(turan_score))
    print("Result           : " + result)
 
 
vowel_consonant_game("Apple")
vowel_consonant_game("programming")
