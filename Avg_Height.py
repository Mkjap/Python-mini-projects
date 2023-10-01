student_heights = input("Input a list of student heights ").split()
for n in range(0,len(student_heights)):
    student_heights[n]= int(student_heights[n])
    #print(student_heights[n])
print(student_heights)
#Total_heights_students = sum(student_heights)
Total_height_students = 0
for height in student_heights:
    Total_height_students += height 
#print(Total_heights_students)

number_students = 0
for student in student_heights:
    number_students += 1
#print(number_students)

average_height_students = float(Total_height_students / number_students)
#count_of_total_students = len(student_heights)
#print(count)
#average_heights_students = float(Total_heights_students / count_of_total_students)
print(f"The average height of the given list of students is {average_height_students:.2f}")
