def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        
angka_andi = [9, 5, 3, 8, 2]
selection_sort(angka_andi)
print("Hasil pengurutan:", angka_andi)