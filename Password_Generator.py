import random
import array
import pyperclip

def passwordGenerator() :
    print("================================")
    print("||     Password Generator     ||")
    print("================================")

    # maximum length of password needed
    max_len = int(input("Enter the length of password you want (at least 8): "))

    while max_len < 8:
        print("\n*** Please enter at least 8 or above!")
        max_len = int(
            input("Enter the length of password you want (at least 8): "))

    # declare arrays of the character that we need in out password
    # Represented as chars to enable easy string concatenation
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    lowercase_letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p',
        'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]

    uppercase_letters = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'p',
        'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]

    symbols = [
        '@', '#', '$', '%', '=', ':', '?', '.', '/', '>', '*', '(', ')', '<'
    ]

    # combining all the character arrays above to form one array
    combined_list = digits + uppercase_letters + lowercase_letters + symbols

    # randomly select at least one character from each character set above
    rand_digit = random.choice(digits)
    rand_upper = random.choice(uppercase_letters)
    rand_lower = random.choice(lowercase_letters)
    rand_symbol = random.choice(symbols)

    # combine the character randomly selected above
    # at this stage, the password contains only 4 characters but
    # we want a {max_len}-character password
    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

    # now that we are sure we have at least one character from each
    # set of characters, we fill the rest of
    # the password length by selecting randomly from the combined
    # list of character above.
    for x in range(max_len - 4):
        temp_pass = temp_pass + random.choice(combined_list)

        # convert temporary password into array and shuffle to
        # prevent it from having a consistent pattern
        # where the beginning of the password is predictable
        temp_pass_list = array.array('u', temp_pass)
        random.shuffle(temp_pass_list)

    # traverse the temporary password array and append the chars
    # to form the password
    password = ""
    for x in temp_pass_list:
        password = password + x

    # print out password
    print("----------------------------------------------------------------")
    print("Here's your password:- " + password)
    print("----------------------------------------------------------------");
    # Copy password to Clipboard
    pyperclip.copy(password)
    print("-> Note: No need to copy, your password has been copied! <-\n")
