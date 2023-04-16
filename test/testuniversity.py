
grade11 = float(input("Enter the grade for term 1 of subject 1: "))
grade12 = float(input("Enter the grade for term 2 of subject 1: "))
grade21 = float(input("Enter the grade for term 1 of subject 2: "))
grade22 = float(input("Enter the grade for term 2 of subject 2: "))

sum_term1 = grade11 + grade21
sum_term2 = grade12 + grade22

if sum_term1 > sum_term2:
    print("The student had a higher average in term 1")
    print("The student had a lower average in term 2")
elif sum_term2 > sum_term1:
    print("The student had a higher average in term 2")
    print("The student had a lower average in term 1")
else:
    print("The student had the same average in both terms")