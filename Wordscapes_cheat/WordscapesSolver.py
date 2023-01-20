from urllib.request import urlopen
import urllib.error


#Function to find all possible combinations of [word_size] characters, given a set of characters [letters].
#[current_combination] must be input as an empty string, since the function work recursively
def Combinator(letters, word_size, current_combination):
    all_combinations = []
    if(len(current_combination)+1 == word_size):
        for i in range(0, len(letters)):
            all_combinations.append((current_combination + letters[i]))
        return(all_combinations)
    else:
        for i in range(0, len(letters)):
            new_letters = letters.copy()
            new_letters.pop(i)
            all_combinations = all_combinations + Combinator(new_letters, word_size, current_combination + letters[i])
        return(all_combinations)

    return 0


#function to look up the word online. I just need to know if a specific word exists or not,
#and so the function just returns an error code (404 if the word doesn't exist, 200 if the word does exist, and 500 if there is no internet connection).
#Wordscapes uses words from Wiktionary.org, but Woktionary contains words for all languages, not just English
#so if I look up a word on there and it exists, I won't know if it's acutally an English word, or a word in some other language.
#Instead, I use this api.dictionaryapi that i found.
#Looking up all the combinations online one by one takes a very long time (and probably works as some sort of DDoS attack),
#so i found it way more convenient to just use a pre-downloaded list of english words instead.
def check_real_word_online(word):
    try:
        page_response = urlopen(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
    #Page not found
    except urllib.error.HTTPError as e:
        response_code = 404
    #Could not connect
    except urllib.error.URLError as e:
        response_code = 500
    else:
        response_code = page_response.getcode()

    return(response_code)

#This is the part where we input the letters, one at a time. Can be input as lower case or upper case.
#Other characters than letters in the English alphabet (or Roman alphabet i guess) can be input, but probably no words will be found containing that character
inputting_letters = 1
letters = []
print("Input letters, one letter at a time, for a maximum of 8 letters.")
print("Input \"cancel\" to remove last input letter.")
print("Input \"end\" to signal that you have finished inputting:")

while(inputting_letters):
    current_letter = input()
    current_letter = current_letter.upper()

    if(current_letter == "END"):
        inputting_letters = 0
        break
    elif(current_letter == "CANCEL"):
        print("Removing letter: " + letters.pop())
    elif(len(current_letter) > 1):
        print("Please input only one letter at a time\n")
    elif(len(current_letter) == 0):
        print("Please input a valid letter\n")
    else:
        letters.append(current_letter)

    if(len(letters) == 8):
        print("Maximum number of characters has been inputted")
        inputting_letters = 0
        break

print("\nInputted letters are:")
for x in letters:
    print(x)

#Input if three-letters words are allowed on this level. If not, we won't wase time finding all possible three letter combinations
three_letter_words_allowed = ''
while(three_letter_words_allowed != 'Y') and (three_letter_words_allowed != 'N'):
    three_letter_words_allowed = input("\nAre three letter words allowed? (y/n)\n")
    three_letter_words_allowed = three_letter_words_allowed.upper()
    if(three_letter_words_allowed != 'Y') and (three_letter_words_allowed != 'N'):
        print("Invalid input. Please input \"y\" for Yes, or \"n\" for No")
if(three_letter_words_allowed == 'Y'):
    start_number = 3
else:
    start_number = 4


#We find all possible combinations, by running the Combinator function once for each combination size
all_combinations = []

for i in range(start_number, len(letters)+1):
    all_combinations = all_combinations + Combinator(letters, i, "")


#I downloaded a list of all english words in a txt document  from http://www.mieliestronk.com/wordlist.html
#Sometimes, a word that appear in a Wordscapes level does not appear in this list, and thus the word will not be found.
#(and this works the other way around too, so some words on this list might not count as words in Wordscapes).
#Wordscapes use English words from Wiktionary, but i have not been able to find a full list of English Wiktionary words yet.
#The list "English_Words.txt" must be in the same file as the python file.
#I search for words occuring in this list
real_word_combinations = []
file = open('English_Words.txt', 'r')
word_list = file.read().split()

#Here I search for the words, as well as getrid of duplicates
for i in all_combinations:
    if (i in word_list) and (i not in real_word_combinations):
        real_word_combinations.append(i)


#This part searches using the online dictionary. It is very slow.
#for i in all_combinations:
#    response_code = check_real_word_online(i)
#    if(response_code == 200):
#        real_word_combinations.append(i)
#    elif(response_code == 500):
#        print("Connection lost. Ending Search.")
#        break
#    elif(response_code != 404):
#        print("Something else went wrong lmao.")
#        break


#Print all found words
print("\n")
for i in real_word_combinations:
    print(i)
