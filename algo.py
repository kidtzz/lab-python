# def test(num):
#   i = 0
#   for i in range(i,num):
#     if i % 15 == 0:
#       print("fizzz")
#     elif i % 3 == 0:
#         print ("buzzz")
#     elif i % 5 == 0:
#         print("fizz buzz")
#     print(i)

# def Al_kelulusan():
#   nama = input("nama:")
#   nilai = int(input("nilai :"))

#   if nilai > 60:
#     ket = "lulus"
#   else:
#     ket = "tidak lulus"
#   print("nama km ", nama,"kamu sekarang ", ket, "nilai km ", nilai)


# def tampilkanAngka (batas, i = 1):
#   print(f'Perulangan ke {i}')

#   if (i < batas):
#     # di sini lah rekursifitas itu terjadi
#     tampilkanAngka(batas, i + 1)

# # tampilkanAngka(10)


# hm = 5
# def ini_three():
#   for row in range(hm):
#     for col in range(row, hm):
#       print("",end='')
#     for col in range(row+1):
#       print('*',end='')
#     print()
#   for row in range(hm-1):
#     for col in range(row,hm-1):
#       print('',end='')
#     for col in range(row+1):
#       print("*",end='')
#     print()


# def perulangan():
#   for i in range(1, 6):
#     print('perulangan luar [i]:',i)
#     for j in range(1,6):
#       print('perulangan dalam [i, j]:',i,',',j)


# perulangan()
# ini_three()

 
# --OOP--

# __ untuk privet access modifier
# _ untuk protected

# class player:
#   #attrbute
#   name ="betin"
#   __salary = 1000
#   #method
#   def get_salary( self):
#     return self.__salary

# player = player()

# player.name = 'koe loo'
# print(f'{player.name} ini name baru {player.get_salary()}')

class Player:
  def __init__(self, health=100, energy=100): #constructor
    self.health = health
    self.energy = energy
    print('new player')

  def attack(self, mon_betin, damage=1 ):
    mon_betin.health -= damage
    self.energy -= damage
    print("attack")

class betin:
  def __init__(self, health=500):
    self.health = health
    print('monster created..')

player = Player()
mon_betin = betin(health=100) 

player.attack(mon_betin, damage=10)
print(mon_betin.__dict__)