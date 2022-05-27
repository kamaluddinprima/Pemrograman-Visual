# untuk memanggil library tkinter
from tkinter import*
# untuk mengimport font agar tampak lebih besar
import tkinter.font

#MENYETING ROOT

root = Tk() #root disini menampung librarynya sekaligus sebagai main window dari aplikasinya
root.title("APLIKASI CARBON FOOTPRINT") #untuk title dari aplikasinya
root.config(bg="gray17") #configurasi warna backgorund
root.geometry("400x600") #ukuran aplikasinya 400x500 px

#WARNA
color={"nero": "#252726", "hijau": "#3f9940",
       "darkorange": "#FE6106"}

#MENGATUR FONT
thefont = tkinter.font.Font(size=15)

#MEMBUAT NAV ATAS
topFrame = Frame(root, bg=color["hijau"]) #membuat frame di root dengan value background color hijau
topFrame.pack(side="top", fill=X) #mengatur posisi dari framenya

# MEMBUAT HEADER
#Membuat Label di dalam topFrame -> Label(topFrame, value...) dengan value text, font, background (bg), warna font (fg), height dan padding sumbu x.
homeLabel = Label(topFrame, text="Carbon Footprint", font="Bahnschrift 15", bg=color["hijau"], fg="gray17", height=2, padx=20)
homeLabel.pack(side="right") #mengatur posisi dari framenya mau di mana dengan pack(side"...")


#MEMBUAT TULISAN UTAMA
#Membuat tulisan dengan Label di dalam root -> Label(root, value...) lihat di bawah ini.  Dengan value-nya text, font, background (bg), warna font (fg).
brandLabel = Label(root, text="Welcome to Carbon Footprint!", font="System 20", bg="gray17", fg="green")
brandLabel.place(x=5, y=100)  #mengatur posisi dari labelnya dengan place(x=.., y=..)

#yg di bawah ini sama dengan yang di atas, hanya saja ini untuk membuat tulsan kedua di bawahnya
brandLabel2 = Label(root, text="Silahkan masukkan angkanya: ", font="Bahnschrift 12", bg="gray17", fg="green")
brandLabel2.place(x=10, y=170) #mengatur posisi dari labelnya dengan place(x=.., y=..)


# MEMBUAT KOTAK FRAME BARU UNTUK TEMPAT KALKULATORNYA
# dengan menggunakan LabelFrame(root, value...), untuk valuenya berisi text, background(bg), warna font(fg), dan padding x, y.
newFrame = LabelFrame(root, text="Penghitung Emisi Karbon",  bg="gray17", fg="white", padx= 10 ,pady=10)
newFrame.place(x=15, y=220) #mengatur posisi dari labelFrame-nya dengan place(x=.., y=..)


# MEMBUAT JUDUL DAN "=" SAMADENGAN
judul = Label(newFrame, text="Carbon Kendaraan",bg="gray17", fg="white").grid(row=0, columnspan=3) #MEMBUAT TULISAN JUDUL KE-1
samde = Label(newFrame, text="=", bg="gray17", fg="white").grid(row=1, column=1) #MEMBUAT TANDA "=" KE-1

judul2 = Label(newFrame, text="Carbon Makanan", bg="gray17", fg="white").grid(row=3, columnspan=3) #MEMBUAT TULISAN JUDUL KE-2
samde2 = Label(newFrame, text="=", bg="gray17", fg="white").grid(row=4, column=1) #MEMBUAT TANDA "=" KE-2

judul3 = Label(newFrame, text="Carbon Elektronik", bg="gray17", fg="white").grid(row=6, columnspan=3) #MEMBUAT TULISAN JUDUL KE-3
samde3 = Label(newFrame, text="=", bg="gray17", fg="white").grid(row=7, column=1) #MEMBUAT TANDA "=" KE-3


#MEMBUAT KOTAK INPUT ANGKA BARIS 1
e1 = Entry(newFrame, width=15) #Kotak input sebelah kiri baris ke-1
e2 = Entry(newFrame, width=15) #Kotak input sebelah kanan baris ke-1
e1["font"] = thefont #untuk mengatur ukuran font inputan kiri
e2["font"] = thefont #untuk mengatur ukuran font inputan kanan
e2.insert(0, "0") #agar ketika default, input bagian kanan bernilai 0
e1.grid(row=1, column=0) #untuk mengatur posisi grid baris dan kolomnya mau di mana
e2.grid(row=1, column=2) #untuk mengatur posisi grid baris dan kolomnya mau di mana
hasil = "0"

#MEMBUAT KOTAK INPUT ANGKA BARIS 2
e3 = Entry(newFrame, width=15) #Kotak input sebelah kiri baris ke-2
e4 = Entry(newFrame, width=15) #Kotak input sebelah kanan baris ke-2
e3["font"] = thefont #untuk mengatur ukuran font inputan kiri
e4["font"] = thefont #untuk mengatur ukuran font inputan kanan
e4.insert(0, "0") #agar ketika default, input bagian kanan bernilai 0
e3.grid(row=4, column=0) #untuk mengatur posisi grid baris dan kolomnya mau di mana
e4.grid(row=4, column=2) #untuk mengatur posisi grid baris dan kolomnya mau di mana

#MEMBUAT KOTAK INPUT ANGKA BARIS 3
e5 = Entry(newFrame, width=15) #Kotak input sebelah kiri baris ke-2
e6 = Entry(newFrame, width=15) #Kotak input sebelah kanan baris ke-2
e5["font"] = thefont #untuk mengatur ukuran font inputan kiri
e6["font"] = thefont #untuk mengatur ukuran font inputan kanan
e6.insert(0, "0") #agar ketika default, input bagian kanan bernilai 0
e5.grid(row=7, column=0) #untuk mengatur posisi grid baris dan kolomnya mau di mana
e6.grid(row=7, column=2) #untuk mengatur posisi grid baris dan kolomnya mau di mana



def rumusKendaraan(rk): #Kalkulator Kategori Kendaraan

    e2.delete(0, END)   #Menghapus output pada kotak 2

    kategori = clicked1.get()   #Mendapatkan nilai dari kotak input
    input = int(e1.get())

    #Menentukan kategori dan membuat rumus hitungan
    if kategori == "Motor":
        hasil = (input * 86.5)      #Rumus carbon footprint motor per km dalam satu hari
    elif kategori == "Mobil":
        hasil = (input * 246)       #Rumus carbon footprint mobil per km dalam satu hari

    #Mendefinisikan hasil operasi bilangan
    hasilkendaraan = hasil
    e2.insert(0, hasilkendaraan)    #Menampilan hasil operasi bilangan pada kotak output (e2)



def rumusMakanan(rm):   #Kalkulator Kategori Makanan

    e4.delete(0, END)   #Menghapus output pada kotak 4

    kategori = clicked2.get()   #Mendapatkan nilai dari kotak input
    input = int(e3.get())

    if kategori == "Daging ayam":
        hasil = (input * 246)       #Rumus carbon footprint daging sapi per porsi dalam satu hari
    elif kategori == "Daging sapi":
        hasil = (input * 388)       #Rumus carbon footprint daging sapi per porsi dalam satu hari
    elif kategori == "Tahu":
        hasil = (input * 292)       #Rumus carbon footprint tahu per porsi dalam satu hari
    elif kategori == "Tempe":
        hasil = (input * 115)       #Rumus carbon footprint tempe per porsi dalam satu hari
    elif kategori == "Nasi putih":
        hasil = (input * 140)       #Rumus carbon footprint nasi putih per porsi dalam satu hari

    #Mendefinisikan hasil operasi bilangan
    hasilmakanan = hasil
    e4.insert(0, hasilmakanan)  #Menampilan hasil operasi bilangan pada kotak output (e4)



def rumusElektronik(re):    #Kalkulator Kategori Makanan

    e6.delete(0, END)       #Menghapus output pada kotak 4

    kategori = clicked3.get()   #Mendapatkan nilai dari kotak input
    input = int(e5.get())

    global hasil

    if kategori == "Smartphone":
        hasil = (input * 90)        #Rumus carbon footprint smartphone per jam dalam satu hari
    elif kategori == "Laptop/PC":
        hasil = (input * 47)        #Rumus carbon footprint laptop perjam dalam satu hari
    elif kategori == "AC":
        hasil = (input * 244)       #Rumus carbon footprint AC perjam dalam satu hari
    elif kategori == "TV":
        hasil = (input * 46)        #Rumus carbon footprint kulkas perjam dalam satu hari

    #Mendefinisikan hasil operasi bilangan
    hasilelektronik = hasil
    e6.insert(0, hasilelektronik)   #Menampilan hasil operasi bilangan pada kotak output (e4)



#Membuat pilihan kategori kendaraan dan menjalankan program berdasarkan kategori yang telah dipilih 1
option = ["Motor", "Mobil"] #menyetting isi dari menu optionnya
clicked1 = StringVar() #membuat variable untuk menampung StringVar()
clicked1.set(option[0]) #menyetting agar secara default menampilkan option index ke-0
drop1 = OptionMenu(newFrame, clicked1, *option, command=rumusKendaraan) #disini barulah membuat menu option dengan OptionMenu(), command di sini agar terhubung dengan rumusnya
drop1.config(width=20) #menyetting lebar dari menu optionnya ketika saat dropdown
drop1.grid(row=2, column=0) #menyetting posisi grid nya

#Membuat pilihan kategori makanan dan menjalankan program berdasarkan kategori yang telah dipilih 2
option = ["Daging ayam", "Daging sapi", "Tahu", "Tempe", "Nasi putih"]
clicked2 = StringVar()
clicked2.set(option[0])
drop2 = OptionMenu(newFrame, clicked2, *option, command=rumusMakanan)
drop2.config(width=20)
drop2.grid(row=5, column=0)

#Membuat pilihan kategori barang elektronik dan menjalankan program berdasarkan kategori yang telah dipilih 3
option = ["Smartphone", "Laptop/PC", "AC", "TV"]
clicked3 = StringVar()
clicked3.set(option[0])
drop3 = OptionMenu(newFrame, clicked3, *option, command=rumusElektronik)
drop3.config(width=20)
drop3.grid(row=8, column=0)



#Tombol hitung
btn = Button(newFrame, text="Count", bg=color['darkorange'], command=lambda: rumusKendaraan) #Tombol hitung kendaraan
btn.grid(row=2, column=2) #mengatur posisi gridnya

btn2 = Button(newFrame, text="Count", bg=color['darkorange'], command=lambda: rumusMakanan)  #Tombol hitung makanan
btn2.grid(row=5, column=2) #mengatur posisi gridnya

btn3 = Button(newFrame, text="Count", bg=color['darkorange'], command=lambda: rumusElektronik)   #Tombol hitung elektronik
btn3.grid(row=8, column=2) #mengatur posisi gridnya



root.mainloop() #agar aplikasinya tidak langsung close, maka harus dideklarasikan mainloop() agar terus berputar dan mengulang