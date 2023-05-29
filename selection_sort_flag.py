def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        max_index = i
        for j in range(i+1, n):
            if arr[j] < arr[max_index]:
                max_index = j
        arr[i], arr[max_index] = arr[max_index], arr[i]

arr = [64, 34, 25, 12, 22, 11, 90]
is_sorted = False
while not is_sorted:
    is_sorted = True
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:            
            selection_sort(arr)
            is_sorted = False
            break
print("Hasil pengurutan", arr)