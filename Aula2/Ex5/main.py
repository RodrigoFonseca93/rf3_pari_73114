#!/usr/bin/env python

from copy import deepcopy


def countNumbersUpTo(stop_char):

    inputs = []
    while True:
        char = raw_input('Enter a char (press ' + stop_char + ' to finish):')
        if char == 'X':
            break
        else:
            inputs.append(char)
    print('here is the list of all your inputs: ' + str(inputs))

    total_numerics = 0
    for input in inputs:
        if input.isdigit():
            total_numerics += 1

    print('Total numeric inputs is ' + str(total_numerics))

    ####### Ex 5b #######

    numeric_inputs = []
    for input in inputs:
        if input.isdigit():
            numeric_inputs.append(int(input))

    print('Numeric inputs:' + str(numeric_inputs))

    ###### Ex 5c ######

    dict_other = {}
    for idx, input in enumerate(inputs): ##enumerate returns the index of the input
        if not input.isdigit():
            #add key value to dict
            dict_other[1] = input

    print('dict_other:' +str(dict_other))


    #### Ex 5d ####

    sorted_numeric_inputs = deepcopy(numeric_inputs)

    sorted_numeric_inputs = numeric_inputs
    sorted_numeric_inputs.sort()
    print('sorted numeric inputs: ' + str(numeric_inputs))

    print('numeric inputs (again): ' + str(numeric_inputs))