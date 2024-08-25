def check_palindrome(str):

    #cleaning str
    clean_string = (str.replace(" ","")).lower()
    reverse_string = clean_string[::-1]
    return clean_string ==reverse_string

str = input("enter the string:")
if check_palindrome(str):
    print("it is a palindrome")
else:
    print("not a palindrome")