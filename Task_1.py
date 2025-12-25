stu = {'Alice':85,'Mark':78,'John':90}
name = input("Enter the student's name: ")
if name in stu:
    print(f"{name}'s marks: {stu[name]}")
else:
    #if student not found
    print("Student not found.")
