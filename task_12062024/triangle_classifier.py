side_1 = int(input("Enter the side 1 length : "))
side_2 = int(input("Enter the side 2 length : "))
side_3 = int(input("Enter the side 3 length : "))
if side_1 == side_2 == side_3:
    print("The triagle is equilateral")
elif (side_1 == side_2) or (side_2 == side_3) or (side_1 == side_3):
    print("The triangle is isosceles")
else:
    print("The triangle is scalene")
