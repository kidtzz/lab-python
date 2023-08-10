

def test(num):
  i = 0
  for i in range(i,num):
    if i % 15 == 0:
      print("fizzz")
    elif i % 3 == 0:
        print ("buzzz")
    elif i % 5 == 0:
        print("fizz buzz")
    print(i)


def Al_kelulusan():
  nama = input("nama:")
  nilai = int(input("nilai :"))

  if nilai > 60:
    ket = "lulus"
  else:
    ket = "tidak lulus"
  print("nama km ", nama,"kamu sekarang ", ket, "nilai km ", nilai)
  

def tampilkanAngka (batas, i = 1):
  print(f'Perulangan ke {i}')

  if (i < batas):
    # di sini lah rekursifitas itu terjadi
    tampilkanAngka(batas, i + 1)

# memanggil fungsi tampilkanAngka
# untuk pertama  kali
tampilkanAngka(10)

def tampilkanAngka (batas, i = 1):
  if (i < batas):
    # di sini lah rekursifitas itu terjadi
    tampilkanAngka(batas, i + 1)

  print(f'Perulangan ke {i}')

# memanggil fungsi tampilanAngka
# untuk pertama  kali
tampilkanAngka(10)
