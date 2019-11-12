T = int(input())
for k in range(T):
    w = list(map(ord, list(input())))
    concat = []
    for k in range(len(w) - 2, -1, -1):
        if w[k] < w[k + 1]:
            # find pivot
            pivot = k + 1
            for i in range(k + 1, len(w)):
                if w[i] > w[k]:
                    pivot = i
                else:
                    break
            concat = w[:k]
            concat.append(w[pivot])
            w[pivot] = w[k]
            concat += sorted(w[k + 1:])
            break
    if len(concat) == 0:
        print("no answer")
    else:
        print(''.join(map(chr, concat))) 
