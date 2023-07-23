
for i in range(2,10,3):
  print('what? ke -',i)

tupleBuah = ('Mangga', 'Jeruk', 'Apel', 'Pepaya')

for buah in tupleBuah:
  print(buah)

for karakter in "Indonesia🇮🇩":
  print(karakter)


for i in range(10,20):
  if(i==17):
    break
  print('apa? - ',i)


liskot = [ 'Jakarta', 'Surabaya', 'Depok', 'Bekasi', 'Solo','Jogjakarta', 'Semarang', 'Makassar']

cariya = input('masukin bro:')

for i, namekota in enumerate(liskot):

  if(namekota.lower() == cariya.lower()):
    print('index ke',i,'nama kotamu ini:',namekota)
    break
else:
  print('Renek BRo')
