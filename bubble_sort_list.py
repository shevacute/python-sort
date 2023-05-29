def bubble_sort(angka_ahmad):
    n = len(angka_ahmad)
    for i in range(n-1):
        for j in range(n-i-1):
            if angka_ahmad[j] < angka_ahmad[j+1]:
                angka_ahmad[j], angka_ahmad[j+1] = angka_ahmad[j+1], angka_ahmad[j]
                
angka_ahmad = [42, 19, 33, 8, 55]
bubble_sort(angka_ahmad)
print("Hasil pengurutan:", angka_ahmad)