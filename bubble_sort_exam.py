def bubble_sort (nilai_ujian):
    n = len(nilai_ujian)
    for i in range(n-1):
        for j in range(n-i-1):
            if nilai_ujian[j] > nilai_ujian[j+1]:
                nilai_ujian[j], nilai_ujian[j+1] = nilai_ujian[j+1], nilai_ujian[j]
                
nilai_ujian = [78, 65, 90, 82,70]
bubble_sort(nilai_ujian)
print("Hasil pengurutan:", nilai_ujian)