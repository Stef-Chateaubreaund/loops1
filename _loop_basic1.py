
#1 basic 


for i in range(1, 150):
   print(i)


#2 multiple of 5

print(*range(5, 1001, 5))


#3 couting


for n in range(100):
    if n % 5 == 0 and n % 10 == 0:
        print("coding dojo")
        continue
    elif n % 5 == 0:
        print("coding")
        continue
    elif n % 10 == 0:
        print("coding dojo")
        continue
    print(n)


#4 that suckers huge

sumOdd = 0
for number in range(0,500+1):
    if number % 2 != 0:
        print("{0}".format(number))
        sumOdd = sumOdd + number
print("The Sum of Odd Numbers from 1 to {0} = {1}".format(number, sumOdd))



#Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.

for count in range(2018,0,-4):
    print(count)



#Flexible Counter

mult = 3
for i in range(9,0,-1):
    if i % mult==0:
        print(i)







