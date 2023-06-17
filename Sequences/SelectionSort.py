def select(seq, start):
    minIndex = start

    for j in range(start,+1, len(seq)):
        if seq[minIndex] > seq[j]:
            minIndex = j
    return minIndex

def selSort(seq):
    for i in range(len(seq) - 1):
        minIndex = select(seq, i)
        tmp = seq[i]
        seq[i] = seq[minIndex]
        seq[minIndex] = tmp