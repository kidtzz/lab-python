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

# tampilkanAngka(10)


hm = 5
def ini_three():
  for row in range(hm):
    for col in range(row, hm):
      print("",end='')
    for col in range(row+1):
      print('*',end='')
    print()
  for row in range(hm-1):
    for col in range(row,hm-1):
      print('*',end='')
    for col in range(row+1):
      print("",end='')
    print()


def perulangan():
  for i in range(1, 6):
    print('perulangan luar [i]:',i)
    for j in range(1,6):
      print('perulangan dalam [i, j]:',i,',',j)


perulangan()
ini_three()