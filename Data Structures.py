classmates = ["Alice", "Bob", "Charlie", "David"]
print("classmates", classmates)
print("Total students:", len(classmates))
print("First student:", classmates[0])
print("Last student:", classmates[-1])
classmates.append("Eve")
print("Updated classmates:", classmates)
classmates.remove("Charlie")
print("After removing Charlie:", classmates)
classmates.sort()
print("Sorted classmates:", classmates)
classmates.reverse()
print("Reversed classmates:", classmates)
Teachers = {"Math": "Mr. Smith", "Science": "Ms. Johnson", "History": "Mr. Lee"}
print("Teachers:", Teachers)
print("Math teacher:", Teachers["Math"])
Teachers["experience"] = 6
print("Updated Teachers:", Teachers)
role_number = [1, 2, 3, 4, 5]
name = ["Alice", "Bob", "Charlie", "David", "Eve"]
student_info = dict(zip(role_number, name))
print("Student Info:", student_info)