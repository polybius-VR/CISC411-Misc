import random, time

def bubbleSort(sequence):
    length = len(sequence)
    start = time.time()
    for i in range(0, length - 1, 1):
        for j in range(0, length - i - 1, 1):
            if sequence[j] > sequence[j + 1]:
                sequence[j], sequence[j+1] = sequence[j+1], sequence[j]
    elapsedTime = time.time()-start
    return sequence, elapsedTime

def selectionSort(sequence):
    length = len(sequence)
    start = time.time()
    for i in range(0, length - 1, 1):
        min = i
        for j in range(i+1, length, 1):
            if sequence[j] < sequence[min]:
                min = j
        sequence[i], sequence[min] = sequence[min], sequence[i]
    elapsedTime = time.time()-start
    return sequence, elapsedTime

def insertionSort(sequence):
    length = len(sequence)
    start = time.time()
    for i in range(1, length, 1):
        marked = sequence[i]
        j = i
        while j >= 1 and sequence[j-1] > marked:
            sequence[j] = sequence[j-1]
            j -= 1
        sequence[j] = marked
    elapsedTime = time.time()-start
    return sequence, elapsedTime

def quick(sequence, start, end):
    if start >= end:
        return sequence
    sequence, left, right = partition(sequence, start, end)
    quick(sequence, start, left-1)
    quick(sequence, left+1, end)
    return sequence

def quickSort(sequence):
    sorted = quick(sequence, 0, len(sequence) - 1)
    return sorted

def partition(sequence, start, end):
    if start >= end:
        return
    pivot = sequence[end]
    left, right = start, end-1
    while left <= right:
        while sequence[left] <= pivot and left <= right:
            left += 1
        while sequence[right] >= pivot and left <= right:
            right -= 1
        if left <= right:
            sequence[left], sequence[right] = sequence[right], sequence[left]
            left -= 1
            right -= 1
    sequence[left], sequence[end] = sequence[end], sequence[left]
    return sequence, left, right

def mergeSort(sequence):
    length = len(sequence)
    if length < 2:
        return sequence
    mid = length // 2 #middle index
    #divide the sequence into two sub-lists
    seqLeft = sequence[:mid]
    seqRight = sequence[mid:]
    #merge sort recursively
    mergeSort(seqLeft)
    mergeSort(seqRight)
    return sequence

def merge(left, right, whole):
    i = 0
    j = 0
    while i + j < len(whole):
        if left[i] < right[j] and j == len(right) or i < len(left):
            whole[i+j] = left[i]
            i += 1
        else:
            whole[i+j] = right[j]
            j += 1
    return whole


def heapify(seq, n, i):
    m = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and seq[i] < seq[l]:
        m = l
    if r < n and seq[i] < seq[r]:
        m = r
    if m != i:
        seq[i], seq[m] = seq[m], seq[i]
        heapify(seq, n, m)

#Heap Sort
def heapSort(seq):
    n = len(seq)
    for i in range(n, -1, -1):
        heapify(seq, n, i)
    for j in range(n-1, 0, -1):
        seq[j], seq[0] - seq[0], seq[j]
        heapify(seq, j, 0)
    return seq


# generate 300 random integerers
# in the range 
unsortedsequence = list(random.randint(-150,150) for x in range(300))
bubble = bubbleSort(unsortedsequence)
select = selectionSort(unsortedsequence)
insert = insertionSort(unsortedsequence)
quick = quickSort(unsortedsequence)
heap = heapSort(unsortedsequence)

print("bubble sort: ", bubble )
print("selection sort: ", select)
print("insertion sort: ", insert)
print("quick sort: ", quick)
print("heap sort: ", heap)