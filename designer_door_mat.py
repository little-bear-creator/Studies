# Print Designer Door Mat with these specifications :
# Mat size must be NxM (N is and odd natural number and M is 3 times N)
# The design should have 'WELCOME' written in the middle
# The design pattern should only use | . and - characters
if __name__ == '__main__' :

    # n and m are assigned input value
    n, m = input().split()
    symbol = '.|.'
    n = int(n)
    m = int(m)
    # Firsts loop to print lines before middle line
    for i in range(int(n/2)):
        # Get number of symbols needed and add (number*symbol) in copy
        copy = (symbol*(i+1)) + (symbol*i)
        # Print each line with copy in the center
        print(copy.center(m, "-"))

    # Print of "welcome" line
    print("WELCOME".center(m, "-"))

    # Second loop for last lines
    for i in range(int(n/2) -1, -1, -1):
        # Get number of symbols needed and add (number*symbol) in copy
        copy = (symbol*(i+1)) + (symbol*i)
        # Print each line with copy in the center
        print(copy.center(m, "-"))
