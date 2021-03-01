hex_dict = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}

def hex_to_decimal(lst):
    n = 0
    s = 1
    for num in lst:
        power = len(lst) - s
        if num in hex_dict:
            k = hex_dict.get(num)
            n += (16**power) * k
        else:
            n += (16**power) * num
        s += 1
    return n
