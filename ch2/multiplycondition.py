eng_marks = int(input("enter the marks in eng:"))
math_marks = int(input("enter the marks in math:"))

#if both marks are more than 80 , print A grade
if eng_marks > 80 and math_marks < 80:
    print("a grade")
#if either of marks are more than 80
elif eng_marks > 80 or math_marks > 80:
    print("B grade")
# if neither of m9arks are more than 80
else:
    print("C grade")

