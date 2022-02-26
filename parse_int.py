def parse_int(string):
    string_number = string.split(' ')
    int_dict = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eigth': 8,
        'nine': 9,
        'ten': 10,
        'eleven': 11,
        'twelve': 12,
        'thirteen': 13,
        'fourteen': 14,
        'fifteen': 15,
        'sixteen': 16,
        'seventeen': 17,
        'eighteen': 18,
        'nineteen': 19,
        'twenty': 20,
        'thirty': 30,
        'forty': 40,
        'fifty': 50,
        'sixty': 60,
        'seventy': 70,
        'eighty': 80,
        'ninety': 90,
        'hundred': 100,
        'thousand': 1000,
        'million': 1000000,
        'and': 0,
    }
    int_value = 0
    if string:

        if len(string_number) <= 3:
            for num in string_number:
                if num.find('-') < 0 and num != 'hundred' and num != 'thousand' and num != 'million':
                    int_value += int_dict.get(num)
                elif 'hundred' == num or 'thousand' == num or 'million' == num:
                    int_value *= int_dict.get(num)
                elif num.find('-') > 0:
                    int_value += sum([int_dict.get(x) for x in num.split('-')])
        else:
            i, l = 0, len(string_number)
            while i < l:

                if (i + 1) < l:
                    if string_number[i + 1] in ['hundred', 'thousand', 'million']:
                        if string_number[i + 1] == 'hundred':
                            int_value += int_dict.get(
                                string_number[i]) * int_dict.get(string_number[i + 1])
                        else:
                            int_value += sum([int_dict.get(x)
                                             for x in string_number[i].split('-')])
                            int_value = int_value * \
                                int_dict.get(string_number[i + 1])
                        i += 2
                        continue
                    elif string_number[i] == 'thousand':
                        int_value = int_value * int_dict.get(string_number[i])
                    else:
                        int_value += sum([int_dict.get(x)
                                         for x in string_number[i].split('-')])
                else:
                    int_value += sum([int_dict.get(x)
                                     for x in string_number[i].split('-')])

                i += 1

    return int_value


# test
print(parse_int('seven hundred eighty-three thousand nine hundred and nineteen'))
print(parse_int('two hundred forty-six'))
print(parse_int('forty-one thousand two hundred and nineteen'))
