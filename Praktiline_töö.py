# ülesanne 0
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

# ulesanne 13-2
print("arv", "   ruut ", "    kuup")
i = 1
while i < 11:
    print(f" {i}      {i ** 2}         {i ** 3}")
    i += 1
