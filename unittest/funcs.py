def is_odd_even(su):
    if su % 2 == 0:
        return True
    else:
        return False

def make_sum(suli):
    sum = 0
    for i in suli:
        sum += i
    return sum

def give_max(suli):
    max = 0
    for i in suli:
        if max < i:
            max = i
    return max

def give_min(suli):
    min = suli[0]
    for i in suli:
        if min > i:
            min = i
    return min
