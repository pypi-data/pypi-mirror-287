# defining our dictionary of Unicode Maya numerals
numeral_dict = {
    '\u1D2E0': 0,
    '\u1D2E1': 1,
    '\u1D2E2': 2,
    '\u1D2E3': 3,
    '\u1D2E4': 4,
    '\u1D2E5': 5,
    '\u1D2E6': 6,
    '\u1D2E7': 7,
    '\u1D2E8': 8,
    '\u1D2E9': 9,
    '\u1D2EA': 10,
    '\u1D2EB': 11,
    '\u1D2EC': 12,
    '\u1D2ED': 13,
    '\u1D2EE': 14,
    '\u1D2EF': 15,
    '\u1D2F0': 16,
    '\u1D2F1': 17,
    '\u1D2F2': 18,
    '\u1D2F3': 19
}

# setting global variables
place_counter = 1
numeral_stack = []
glyph_list = []

# the function that checks whether to stop dividing or continue the loop
def divide_num_input(input_num):
    global numeral_stack
    # get length of input_num
    input_as_str = str(input_num)
    length_of_input = len(input_as_str)
    
    # check inputs to know when to stop dividing
    if input_num % 20 == 0:
        if (input_num / 20) % 20 == 0:
            new_num = input_num // 20
            numeral_stack.append(0)
            final_num = new_num // 20
            numeral_stack.append(final_num)
            nums_to_glyphs(numeral_stack)
        elif (input_num / 20) <= 19:
            divided_num = input_num // 20
            numeral_stack.append(divided_num)
            nums_to_glyphs(numeral_stack)
        else:
            divide_number_loop(input_num)
    else:
        divide_number_loop(input_num)

# popping the number in the ones place and continuing the loop
def first_pass(num_to_divide):
    # clearing the glyph list from previous runs of the loop
    global glyph_list
    glyph_list.clear()
    
    # resetting the place counter
    global place_counter
    place_counter = 1
    
    # clearing the numeral stack
    global numeral_stack
    numeral_stack.clear()

    stringed_num_to_divide = str(num_to_divide)
    next_num, popped_ones_place = stringed_num_to_divide[:-place_counter], stringed_num_to_divide[-place_counter]
    place_remainder = int(popped_ones_place)
    numeral_stack.append(place_remainder)
    place_counter += 1
    num_to_divide = int(str(next_num) + "0")
    divide_num_input(num_to_divide)

# the main loop for dividing our numbers
def divide_number_loop(num_to_divide):
    global place_counter
    # if not divisible by 20, we move the last digit to the appropriate place and divide the remaining number by 20
    divided_num = num_to_divide // 20
    stringed_divided_num = str(divided_num)
    next_num, divided_string = stringed_divided_num[:-place_counter], stringed_divided_num[-place_counter:]
    # getting our place number to turn into a Maya numeral later; the place is tracked by the place_counter variable
    place_remainder = int(divided_string)
    if place_remainder > 0:
        global numeral_stack
        numeral_stack.append(place_remainder)
    # getting our new number to divide
        zero_string = ("0" * place_counter)
        num_to_divide = int(str(next_num) + zero_string)
        place_counter += 1
        if num_to_divide > 0:
            divide_num_input(num_to_divide)
        else:
            nums_to_glyphs(numeral_stack)
    else:
        nums_to_glyphs(numeral_stack)

# convert our numerals to Maya glyphs
def nums_to_glyphs(input_list):
    global glyph_list
    for num in input_list:
        glyph_value = list(numeral_dict.keys())[list(numeral_dict.values()).index(num)]
        glyph_list.append(glyph_value)
    
    return glyph_list

# call the main loop and print our list of glyphs
def convert(num_to_convert):
    first_pass(num_to_convert)
    return glyph_list
