def process_user_input(input_value, flag1, flag2, flag3):
    result = 0
    if input_value > 0:
        if flag1:
            if flag2:
                result = input_value * 2
            else:
                if flag3:
                    result = input_value + 3
                else:
                    result = input_value - 1
        else:
            if flag2 and flag3:
                result = input_value / 2
            elif flag2:
                result = input_value * 3
            else:
                result = input_value + 1
    else:
        if flag1 or flag2:
            if flag3:
                result = -input_value
            else:
                result = input_value
        else:
            result = 0
    return result