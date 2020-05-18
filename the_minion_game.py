import string
# TO DO : find another algorithm to count occurences of word in bigword
# TO DO : find another algorithm for this game... Look at the exemple on HackerRank
# Return "True" if char is a vowel
def isVowel(char):
    vowels = "AEIOU"
    # Find() returns index of char in vowels
    if(vowels.find(char) != -1):
        return "True"
    else:
        return "False"

# Count how many occurences of "word" in "bigword" exist, return an int
# When calling the function write 0 for argument 'n'
# Specification : argument word has to be built with string extracted from bigword
def countOccurences(word, bigword, n):

    # x is a tuple : (char before word, word, char after word)
    x = bigword.partition(word)
    # If word == bigword, we still have one occurence
    if(word == bigword):
        n += 1
    # if I can continue to test occurences
    elif(x[2] != ""):
        n = countOccurences(word, x[2], (n+1))
    # In this case x[2] == "" so I can't conitnue to count occurences
    # But word can still be a part of bigword, if word represent the last part of BANANA 
    # For exemple : NANA with word BANANA
    # wrong, count everything in double
    #elif(x[0] != ""):
        #n += 1
    return n

def minion_game(string):
    # Results of Stuart and Kevin
    result_stuart = 0
    result_kevin = 0

    # List of words each player can make
    result_list_stuart = []
    result_list_kevin = []


    # Test if string has empty space, return "DRAW" if it is the case
    if((len(string) == 0) or (len(string.split()) > 1)):
        print("DRAW")
    else:
        # ERROR : Résultat beaucoup trop grand, j'ai une mauvaise méthode de calcul : séparer les deux joueurs ?
        # ERROR : implémentation différnte dans la loop kevin, le résultat est plus petit que prévu dorénavant, continuer de tester
        # TEST : countOccurences à l'air de fonctionner et donne de bon résultats
        
        # Big loop to find kevin and stuart results according to the rules
        # for each letter of word "string"
        for index in range(len(string)):
            # Save the rest of string starting at index
            #bigword = string[index::]

            # Test if char is a Vowel, then Kevin can play
            if(isVowel(string[index]) == "True"):

                for i in range(len(string)):
                    # iterate through string by taking a word more and more bigger
                    # if i != 0 we have already searched and counted string[index] in string
                    if(i != 0):
                        word = string[index:index+i]
                    # Case where i == 0 and we just have to search string[index]
                    else:
                        word = string[index]
                    # check if word hasn't been used before
                    if(result_list_kevin.count(word) == 0):
                        result_kevin += countOccurences(word, string, 0)
                        result_list_kevin.append(word)
            else:
                # Stuart can play

                for i in range(len(string)):
                    
                    # Case where i == index and we just have to search string[index]
                    if(i == index):
                        word = string[index]
                    # We start searching new words at index
                    elif(i > index):
                        # TO DO : BANANA doesn't appear
                        word = string[index:(index+i)]
                    # In this case, i != 0 and i <= index, we don't search for new words
                    else:
                        word = ""
                    print("Word before test is : "+word+", value of i and index are :"+str(index)+" "+str(i))

                    # check if word hasn't been used before
                    if((word != "") and (result_list_stuart.count(word) == 0)):
                        print("Word found is "+word+" for Stuart")
                        result_stuart += countOccurences(word, string, 0)
                        print("result for Stuart is "+str(result_stuart))
                        result_list_stuart.append(word)
                        print("")

        #Print results to debug calcul
        print("----- "+"Stuart a "+str(result_stuart))
        
        print("----- "+"Kevin a "+str(result_kevin))
        
        # Test who wins
        if(result_kevin > result_stuart):
            print("Kevin "+str(result_kevin))
        elif(result_stuart > result_kevin):
            print("Stuart "+str(result_stuart))
        else:
            print("Draw")

        #End of result
        print("------- END of calcul -----------")
    

if __name__ == '__main__':
    #s = "BAANANAS"
    #minion_game(s)
    #s = "BANANANAAAS"
    #minion_game(s)
    s = "BANANA"
    minion_game(s)
