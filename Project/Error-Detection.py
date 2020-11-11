# Alex Chen
# ET 574 - Project # 1
# Prof. Sun

# Turn 16 digit number into single digits
def extract_digits(credit_card):
    digits = [int(d) for d in str(credit_card)]
    return digits


# Take the even indexs and perform doubling and if needed -9, append to list and
# return sum of list
def even_indexes(digits):
    even_doubling = []
    for x in range(len(digits)):
        if x % 2 == 0:
            doubling = digits[x] * 2
            if doubling > 9:
                doubling -= 9
                even_doubling.append(doubling)
            else:
                even_doubling.append(doubling)
    return sum(even_doubling)


# Take the odd indexs and append to list and return sum of list
def odd_index(digits):
    odd_values = []
    for x in range(len(digits)):
        if x % 2 == 1:
            odd_values.append(digits[x])
    return sum(odd_values)


# Check if credit card input is an int
def check_int_string(credit_card):
    try:  # Try to place input into an int values
        value = int(credit_card)
        return value
    except ValueError:  # If unable to, a Value Error is shown, but will instead redo main
        print("Credit card cannot be a string value\n")
        exit()


def main():
    credit_card = input("Enter a credit card number: ")
    # Check if input is a string or int value
    check_int_string(credit_card)
    if len(credit_card) != 16:  # Check length of credit card
        print(f"{credit_card} is an invalid length")
    else:  # If all passes, use functions above
        digits = extract_digits(credit_card)
        even_sum = even_indexes(digits)
        odd_sum = odd_index(digits)
        if (odd_sum + even_sum) % 10 == 0:  # Final step, make sure the sums are divisiable by 10
            print(f"{credit_card} is a valid card")
        else:  # Else invalid card
            print(f"{credit_card} is INVALID")


main()
