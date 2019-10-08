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

def quick_search(l):
    if len(l) < 2:
        return l
    pivot = l[0]
    less = [i for i in l[1:] if i<=pivot]
    greater = [i for i in l[1:] if i>pivot]
    
    return quick_search(less) + [pivot] + quick_search(greater)

l = [4, 1, 5, 66, 29, 22, 12]
sorted_l = quick_search(l)
print(sorted_l)


def merge_sort(l):
  
    if len(l) < 2:
        return l
    splitter = int(len(l) / 2)
    left = merge_sort(l[0:splitter])
    right = merge_sort(l[splitter:])

    loop_len = max(len(left), len(right))
    i = 0
    j = 0
    arr = []
    for _  in range(loop_len + 1):
        if left[i] >= right[j]:
            arr.append(right[j])
            if j == len(right) -1:
                arr += left[i:]
                return arr
            else:
                j += 1
        else:
            arr.append(left[i])
            if i == len(left) -1:
                arr += right[j:]
                return arr
            else:
                i += 1
    return arr
        

print(merge_sort(l))