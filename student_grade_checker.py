#student Grade Checker

student_name= input("Enter Student Name:-")
student_mark = int(input("Enter Student Marks:-"))

def student_grade_checker(student_name,student_mark):

    
     if student_mark < 0 or student_mark > 100:
            return "Invalid Marks"
    

     if student_mark >= 75:
        grade = "Distinction"
        elif student_mark >= 60:
        grade = "First Class"
        elif student_mark >= 50:
        grade = "Second Class"
        elif student_mark >= 35:
        grade = "Third Class"
    else:
        grade = "Fail"



    return {
            "Student_name": student_name,
            "Student_mark": student_mark,
            "student_grade": grade
        }


student_result= student_grade_checker(student_name,student_mark)
print(student_result)


              
