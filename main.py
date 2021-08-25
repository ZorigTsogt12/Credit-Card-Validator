# Dictionaries that perform either basic addition on strings or basic times 2
multiple_dic = {'10': '1', '12': '3', '14': '5', '16': '7', '18': '9'}
times_two = {'0': '0', '1': '2', '2': '4', '3': '6', '4': '8', '5': '10', '6': '12', '7': '14', '8': '16', '9': '18'}
normal = {'0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9'}


def times(card_num):
    # First number and every second number afterwards is multiplied by two.
    # Each input is processed and append to a list
    count = 0
    times_two_num = []
    for number in card_num[:15]:
        if count % 2 == 0:
            times_two_num.append(times_two[number])
        else:
            times_two_num.append(normal[number])

        count += 1
    # The list is made in order with the card numbers
    return times_two_num


def multiple(card_list):
    # Checks for number greater than 9 and adds the two digits together
    # If the digit is above 9, adds the digits using a dictionary and
    new_list = []

    for number in card_list:
        if len(number) > 1:
            new_list.append(multiple_dic[number])
        else:
            new_list.append(number)

    return new_list


def add_all(card_list):
    # Adds all the numbers in the given list
    total = 0

    for num in card_list:
        total += int(num)

    return total


while True:
    try:
        card_number = input('Please enter the 16-digit card number: ')
        card_number = card_number.replace(' ', '')
        if len(card_number) == 16:
            times_two_res = times(card_number)
            multiple_list = multiple(times_two_res)
            break
        else:
            print('Please enter 16 digits')
            continue

    except:
        print('Invalid entry')
        continue

total_add = add_all(multiple_list)

total_new = total_add + int(card_number[15])

if total_new % 10 == 0:
    print('The credit card detail is valid')
else:
    print('The credit card detail is invalid')
