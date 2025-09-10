def input_student() -> dict:
    name = input("Enter the name of the student: ")
    rollno = int(input("Enter the rollno of the student: "))
    marks = int(input("Enter the marks of the student: "))
    
    return {"name": name, "rollno": rollno, "marks": marks}

def student_with_max_marks(students: list):
    max_marks = students[0]["marks"]
    ind = 0
    
    for i in range(len(students)):
        if students[i]["marks"] > max_marks:
            max_marks = students[i]["marks"]
            ind = i
            
    print(f"{students[ind]['name']} has secured the highest marks")

def students_with_more_marks(students: list):
    print("Students who secured more than 75 marks are:")
    for student in students:
        if student["marks"] > 75:
            print(student["name"])
        
if __name__ == "main":
    students = []

    for i in range(5):
        students.append(input_student())

    students = tuple(students)
        
    student_with_max_marks(students)
    students_with_more_marks(students)
