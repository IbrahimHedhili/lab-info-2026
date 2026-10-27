"""Write a program that, given the three sides of a triangle, 
determines whether the triangle is acute-angled,
 rectangular-angled or obtuse-angled."""


sides = [float(input("First side: ")), float(input("Second side: ")), float(input("Third side: "))]

sides.sort(reverse = True)

operation =  sides[0]*sides[0] - sides[1]*sides[1]- sides[2]*sides[2]

if operation == 0: print("The triangle is rectangular-angled")
elif operation > 0: print("The triangle is obtuse-angled")
elif operation < 0: print("The triangle is acute-angled")
