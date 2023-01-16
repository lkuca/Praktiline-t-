#for x in range (1,101,1):
#   if x%5==0:
#       print(x, end=" ")

# ülesanne 0
from sys import excepthook


õige_vastus = 7
for b in range(0, 5):
    c = (abs(int(input("proovi leida vastus numbrile 0-10,sa saad ainult 5 korda proovida!"))))
    if c == õige_vastus:
        print("tubli")
        break
    elif b < 4:
        print("proovi veel")

# teine variant
while True:
    try:
        a = (abs(int(input("et hakkata cycle vajuta 1 "))))
        if a == 1:
            print("edasi")
        else:
            break
    except ValueError:
        print("ei ole number")
        break

# ulesanne 13
print("arv", "   ruut ", "    kuup")
for i in range(1, 11):
    # print( i , i**2 , i**3 )
    print(f" {i}      {i ** 2}         {i ** 3}")
print("teine variant")
# ulesanne 13-2
print("arv", "   ruut ", "    kuup")
i = 1
while i < 11:
    print(f" {i}      {i ** 2}         {i ** 3}")
    i += 1



# MAKSIMI ÜLESANNE
#ans = random.randit(1, 10)
#while true:
#   g= input ("mis numbri ma arvasin?(1-10, mängu lõpetamiseks kirjutage lõpp")
#   if g.lower()== "lõpp
#       print("mängu on läbi")
#       break
#   if not g. isnumeric():
#       print("vale andmetüüp!")
#       continue
#   g= int(g)
#   if g == ans:
#       print("õige vastus!")
#       break
#   if g>10 or g<1
#       print("Vahemik on vale!")
#       countinue
#   elif g !=ans:
#       print(f"vale!")
#       countinue



# ARTURI ÜLESANNE
#g=1
#TRY:
#   f = int(input("mittu ülesandeid sa tahad?"))
#   for d in range(0,f,1)
#   print(f"ülesanne {g}:")
#   a = randit(1,50)
#   b = randit(1,50)
#   c = a+b
#   for i in range(0,5,1):
#       answer = int(input(f"a+b=?"))
#       if answer == a+b:
#           print("see on õige")
#           break
#       else:
#           print("proovi veel kord")
#           print()
#   g = g+1
#   print(f"õige on c")
#except:
#   print()
#Dilan ülesanne
#print("")
#letter= random.choice(string.ascii_letters)

#while True:
#    answ = str(input(""))
#    if letter == answ:
#        print("")
#        break
#    else: print("Provi uuesti!")



#TIMUR ÜLESANNE
#print()
#print("ülesanne 6 1")
#for i in range (0,5):
#   print("* "*5)
#for i in range(0,10):
#   print("* i")
#for i in range(0,10):
#   print("* "*(10-i))



#SANJA ÜLESANNE
# while true:
#   try:
#       mainnumber = int(input("vali number 1-100:"))
#       break
#   except ValueError:
#       print("see pole täisarv")
#if mainnumber<1 or mainnumber>100:
#       print("vali õige number")
#else:
#   paaritu =0
#   Paaris= 0
#   x= 0
#   while x != mainnumber:
#   printx=x +1...........
#   print(int(x), end= " "
#   if x% 2== 0
#       paaris
#   else:
#       paaritu += 1
