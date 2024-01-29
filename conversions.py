# Converts base 10 decimal number to given base
def decimal_to_base(num, base):
    decimal = decimal_conversion(num, base)
    remainder_list = []
    quotient = int(num)
    while quotient > 0:
        remainder_list.append(quotient % base)
        quotient = quotient // base

    # Converts base 16 to hex
    if base == 16:
        for i in range(len(remainder_list)):
            if remainder_list[i] > 9:
                remainder_list[i] = chr(remainder_list[i] + 55)
        final = ''
        for num in remainder_list:
            final = str(num) + final

        # Combine with decimal
        final = final + decimal

        return final

    final = ''
    for num in remainder_list:
        final = str(num) + final

    # Combine with decimal
    final = final + decimal
    return final


# Helper function for "decimal_to_base"
def decimal_conversion(num, base):
    if '.' in str(num):
        divider = str(num).index('.')
        num = str(num)
        decimal = float(num[divider:])

        remainder_list = []
        i = 0
        while not decimal.is_integer() and i < 20:
            decimal = decimal * base
            if int(decimal) > 9:
                remainder_list.append(chr(int(decimal) + 55))
                decimal -= int(decimal)
            else:
                remainder_list.append(str(int(decimal)))
                decimal -= int(decimal)
            i += 1

        return '.' + ''.join(remainder_list)

    else:
        return ''


# if __name__ == '__main__':


def base_to_decimal(num, base):
    if '.' in str(num):
        num = str(num)
        divider = num.index('.')
        integer = num[:divider]
        decimal = num[divider+1:]
        int_list = list(integer)
        deci_list = list(decimal)

        total = 0
        for i in range(len(int_list)):
            total += int(int_list[i]) * (base ** (len(int_list)-1 - i))
        integer = str(total)

        total = 0
        for i in range(len(deci_list)):
            total += int(deci_list[i]) * (base ** -(i+1))
        decimal = total

        return float(integer) + decimal

    else:
        int_list = list(str(num))
        total = 0
        for i in range(len(int_list)):
            total += int(int_list[i]) * (base ** (len(int_list)-1 - i))
        return int(total)


def ones_complement(num):
    pass


if __name__ == '__main__':
    print("decimal_to_base:")
    print(decimal_to_base(78, 8))  # 116
    print(decimal_to_base(78, 16))  # 4E
    print(decimal_to_base(10203049, 16))  # 9BAFA9
    print(decimal_to_base(53, 2))  # 110101
    print(decimal_to_base(53.5, 2))  # 110101.1

    print("\ndecimal_conversion:")
    print(decimal_conversion(.8, 16))  # 0.CCCCCCCCCCCC
    print(decimal_conversion(.1745, 16))  # 0.2CAC083126E978D4FDF4
    print(decimal_conversion(.28934, 8))  # 0.2241105753266265152

    print("\nbase_to_decimal:")
    print(base_to_decimal(116, 8))  # 78
    print(base_to_decimal(111.1, 2))  # 7.5
    print(base_to_decimal(1101010101.100111, 2))  # 853.61767578125
    print(decimal_to_base(base_to_decimal(001001101.010111, 2), 8))  # 115.27


# # (Made more general through "decimal_to_base") Base 10 decimal or integers to binary
# def decimal_to_binary(num):
#     integer_list = []
#     if '.' in str(num):
#         divider = str(num).index('.')
#         num = str(num)
#         decimal = float(num[divider:])
#         integer = int(num[:divider])
#
#         # Calculates Decimal part if applicable
#         i = 0
#         while decimal < 1 and i != 8:
#             decimal *= 2
#             if decimal > 1:
#                 decimal -= 1
#                 integer_list.append(str(1))
#             elif decimal < 1:
#                 integer_list.append(str(0))
#             elif decimal == 1:
#                 integer_list.append(str(1))
#                 break
#             i += 1
#         final_decimal = ''.join(integer_list)
#
#     else:
#         integer = num
#
#     quotient = 1
#     remainders = []
#
#     # Calculates integer part
#     while quotient > 0:
#         quotient = integer // 2
#         remainders.append(integer % 2)
#         integer = quotient
#
#     final = ''
#     for binary in remainders:
#         final = str(binary) + final
#
#     if not integer_list:
#         return int(final)
#
#     else:
#         return float(final + '.' + final_decimal)
#
#
# # if __name__ == '__main__':
# #     print(decimal_to_binary(53.45))
# #     print(decimal_to_binary(101.56))
# #     print(decimal_to_binary(.625))
#
#
