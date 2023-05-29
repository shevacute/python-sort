def bubble_sort_books(books):
    n = len(books)
    for i in range(n-1):
        for j in range(n-i-1):
            if books[j]['Jumlah Halaman'] > books[j+1]['Jumlah Halaman']:
                books[j], books[j+1] = books[j+1], books[j]
    return books    
books = [
    {
        'No.': 1,
        'Judul Buku': "Harry Potter and the Sorcerer's Stone",
        'Penulis': 'J.K. Rowling',
        'Jumlah Halaman': 320
    },
    {
        'No.': 2,
        'Judul Buku': 'To Kill a Mockingbird',
        'Penulis': 'Harper Lee',
        'Jumlah Halaman': 281
    },
    {
        'No.': 3,
        'Judul Buku': 'The Great Gatsby',
        'Penulis': 'F. Scott Fitzgerald',
        'Jumlah Halaman': 180
    },
    {
        'No.': 4,
        'Judul Buku': 'Pride and Prejudice',
        'Penulis': 'Jane Austen',
        'Jumlah Halaman': 432
    },
    {
        'No.': 5,
        'Judul Buku': '1984',
        'Penulis': 'George Orwell',
        'Jumlah Halaman': 328
    }
    ]
hasil = bubble_sort_books(books)
print("Daftar buku setelah diurutkan berdasarkan jumlah halaman secara ascending:")
for buku in hasil:
    print(f"No. {buku['No.']}: {buku['Judul Buku']} oleh {buku['Penulis']} ({buku['Jumlah Halaman']} halaman)")