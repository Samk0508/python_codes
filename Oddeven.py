
#program to print the given number is odd or even

num = int(input("Enter a number: "))#input
#logic= if number is complete divisible by 2 then its even else odd
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))
