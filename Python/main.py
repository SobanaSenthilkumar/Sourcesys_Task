print("STUDENT MANAGEMENT SYSTEM")

from student_module import Student

try:
    name = input("Enter Student Name: ")
    marks = int(input("Enter Marks: "))

    s1 = Student(name, marks)

    s1.display()
    print("Grade:", s1.grade())

except ValueError:
    print("Invalid Marks Entered")
except Exception as e:
    print("Error:", e)
finally:
    print("Program Finished")