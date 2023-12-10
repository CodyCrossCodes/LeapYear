year = int(input())

year_string = str(year)


if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
  print("Leap year")
elif year % 4 == 0 and year % 100 != 0:
  print ("Leap year")
else:
  print("Not leap year")