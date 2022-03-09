# Nama  : Muhammad Kamaluddin Primajaya
# NIM   : 20051397035
# Kelas : Manajemen Informatika 2020A

abjad = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
kalimat = input('Masukkan Kalimat : ')
key = int(input('Masukkan Kunci: '))

def encode(kalimat,cipher_key):
    kalimat = kalimat.lower()
    hasil_encode = ''
    for karakter in kalimat:
        if karakter in abjad:
            index_lama = abjad.index(karakter)
            index_baru = (index_lama + cipher_key ) % len(abjad)
            abjad_baru = abjad[index_baru]
            hasil_encode = hasil_encode + abjad_baru 
        else:
            hasil_encode = hasil_encode + ' ' 
    return hasil_encode

# ENKRIPSI
kalimat_hasil = encode(kalimat,key)
print('Hasilnya adalah', kalimat_hasil)