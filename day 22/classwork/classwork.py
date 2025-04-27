for i in range(2, 100, 2):
    print(i)

for i in range(1, 100, 2):
    print(i)

total = sum(range(1, 100))
print(total)

even_total = sum(range(2, 101, 2))
print(even_total)

odd_total = sum(range(1, 101, 2))
print(odd_total)

seats = 50
while seats > 0:
    print(seats)
    seats = seats - 1

    count = 1
while count < 5:
    print(count)
    count = count + 1

    num = int(input("enter the number: "))
count = 0
while count < num:
    print(count)
    count = count + 1

    password = 1234
    new_password = int(input("seiyvanet 4 cifriani paroli"))
    while password != new_password:
        print("password isnt correcct")
        new_password = int(input("try again")) 
        print("password is correct")

        number = 6
        new_num = int(input("enter the number:"))
        while new_num !=