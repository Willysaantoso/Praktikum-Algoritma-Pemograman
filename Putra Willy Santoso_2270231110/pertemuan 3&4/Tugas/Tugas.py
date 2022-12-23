print("----------------- WILLY WARKOP -----------------")
nama = input("MASUKKAN NAMA ANDA : ")
Alamat = "JL. AJA DULU"
No_telp = int(input("MASUKKAN NO TELP "))

#buat waktu
import time
tanggal = time.strftime("%D %H:%M:%S")
print(tanggal)

def fungsimakanan():
   global totalmkn
   global porsi
   global mkn
   print ("\n----------------- Menu Makanan -----------------")
   print("1. Roti bakar - Rp 15000")
   print("2. Bubur kacang hijau - Rp 10000")
   print("3. Mie nyemek - Rp 13000")
   nomor=int(input("Masukan Pilihan: "))
   porsi= int(input("Berapa Porsi: "))

   if nomor==1:
       totalmkn=porsi*15000
       print (porsi," Porsi Roti bakar = Rp", totalmkn)
       mkn=("Roti bakar")
   elif nomor==2:
       totalmkn=porsi*10000
       print (porsi," Porsi Bubur kacang hijau = Rp", totalmkn)
       mkn=("Bubur kacang hijau")
   elif nomor==3:
       totalmkn=porsi*13000
       print (porsi, " Porsi Mie nyemek = Rp", totalmkn)
       mkn=("Mie nyemek")
   else:
      print("Pilihan tidak ada, silahkan masukan lagi!!!")
      fungsimakanan()

def fungsiminuman():
   global totalmnm
   global mnm
   global gelas
   print("\n----------------- Menu Minuman -----------------")
   print("1. Es Teh manis - Rp 5000")
   print("2. Es Jeruk - Rp 10000")
   print("3. Es Milo susu - Rp 12000")
   nomor=int(input("Masukan Pilihan: "))
   gelas= int(input("Berapa Gelas: "))

   if nomor==1:
       totalmnm=gelas*5000
       print (gelas," Es Teh manis = Rp", totalmnm)
       mnm=("Es Teh manis")
   elif nomor==2:
       totalmnm=gelas*10000
       print (gelas, " Gelas Es Jeruk = Rp", totalmnm)
       mnm=("Es Jeruk")
   elif nomor==3:
       totalmnm=gelas*10000
       print (gelas, " Gelas Es Milo susu = Rp", totalmnm)
       mnm=("es Milo susu")
   else:
      print("Pilihan tidak ada, silahkan masukan lagi!!")
      fungsiminuman()

fungsimakanan()
fungsiminuman()
totalsemua=totalmkn+totalmnm

print("\nTotal harus Dibayar: Rp",totalsemua)
uang=int(input("Uang Tunai Pembeli: Rp "))
kembalian=int(uang-totalsemua)
print("Kembalian :",kembalian)

print("\n==================================")
print("========== STRUK PEMBELIAN =========")
print("==================================")
print ("Nama\t\t:",nama)
print ("Alamat\t\t:",Alamat)
print ("No telp\t\t:",No_telp)
print ("Tanggal\t\t:",tanggal)

print ("Beli\t\t:",porsi,mkn,"( Rp", totalmkn,")")
print ("\t\t ",gelas,mnm,"( Rp", totalmnm,")")
print ("Tagihan\t\t: Rp",totalsemua)
print ("Dibayar\t\t: Rp",uang)
print ("Kembalian\t: Rp",kembalian)
print("==================================")
print("==================================")