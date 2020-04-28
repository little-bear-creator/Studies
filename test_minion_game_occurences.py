def countOccurences(word, bigword, n):

    # x is a tuple : (char before word, word, char after word)
    x = bigword.partition(word)
    # if I can continue to test occurences
    if(x[2] != ""):
        n = countOccurences(word, x[2], (n+1))
    return n

if __name__ == '__main__':
    string = "BAANANAS"
    print("Occurence de B dans string : "+str(countOccurences("B", string, 0)))

    print("Occurence de BA dans string : "+str(countOccurences("BA", string, 0)))
    print("Occurence de A dans string : "+str(countOccurences("A", string, 0)))
    print("Occurence de AA dans string : "+str(countOccurences("AA", string, 0)))
