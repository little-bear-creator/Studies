# Function to convert decimal to binary, octal and hexadecimal
# Convert decimal to binary and return a string
def decimal_to_binary(dec):
    decimal = int(dec)
    binary_num = str(bin(decimal))
    # return a string without the useless first characters
    return binary_num[2:] 

# Convert decimal to octal and return a string
def decimal_to_octal(dec):
    decimal = int(dec)
    octal_num = str(oct(decimal))
    # return a string without the useless first characters
    return octal_num[2:]

# Convert decimal to hexadecimal and return a string
def decimal_to_hexadecimal(dec):
    decimal = int(dec)
    hexa_num = str(hex(decimal))
    # return a capitalize string without the useless first characters
    return hexa_num[2:].swapcase()

# Given an integer n, print the following values for each integer from 1 to n :
# 1. Decimal
# 2. Octal
# 3. Hexadecimal
# 4. Binary
def print_formatted(number):
    
    # Width of number in binary
    width = len(decimal_to_binary(number))
    
    for i in range(number):
        num = i+1
        print(str(num).rjust(width)+" "+decimal_to_octal(num).rjust(width)+" "+decimal_to_hexadecimal(num).rjust(width)+" "+decimal_to_binary(num).rjust(width))

    


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
