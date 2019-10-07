def dc_sum(l):
    if len(l) == 1:
        return l[0]
    return l[0] + dc_sum(l[1:])

l = [1,3,5,6,9, 22]
print(dc_sum(l))
print(sum(l))

def dc_count(l):
    if len(l) == 1:
        return 1
    return 1 + dc_count(l[1:])

print(dc_count(l))
print(len(l))

def dc_max(l):
    if len(l) == 1:
        return l[0]
    return l[0] if l[0] > dc_max(l[1:]) else dc_max(l[1:])

print(dc_max(l))
print(max(l))


def bi_search(l, t):
    findex = 0
    lindex = len(l) -1 
    while findex <= lindex:
        guess = int((findex + lindex) / 2)
        if l[guess] == t:
            return guess
        elif l[guess] > t:
            lindex = lindex -1
        else:
            findex = findex + 1

print(bi_search(l, 100))
    