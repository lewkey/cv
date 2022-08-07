class color:
   BOLD = '\033[1m'
   END = '\033[0m'
print("test " + " " + color.BOLD + 'underweight' + color.END + " test")


year = int(input("Enter a year! "))
if year % 4 != 0:
   print("Not a leap year!")
elif year % 100 != 0:
   print("It is a leap year!")    
elif year % 400 != 0:
   print("Not a leap year!")
else:
   print("Leap year !") 
