# grades_management.py

class Student:
    def __init__(self, roll_no, name, course, grade):
        self.roll_no = roll_no
        self.name = name
        self.course = course
        self.grade = grade

    def __str__(self):
        return f"Roll No: {self.roll_no}, Name: {self.name}, Course: {self.course}, Grade: {self.grade}"

class GradesManager:
    def __init__(self):
        self.students = []

    def add_student(self, roll_no, name, course, grade):
        for s in self.students:
            if s.roll_no == roll_no:
                print("Student with this roll number already exists.")
                return
        self.students.append(Student(roll_no, name, course, grade))
        print(f"Student '{name}' added successfully.")

    def search_student(self, keyword):
        found = False
        for s in self.students:
            if keyword.lower() in s.name.lower() or keyword.lower() == s.roll_no.lower():
                print(s)
                found = True
        if not found:
            print("No student found matching the keyword.")

    def update_grade(self, roll_no, new_grade):
        for s in self.students:
            if s.roll_no == roll_no:
                s.grade = new_grade
                print(f"Grade updated for {s.name}.")
                return
        print("Student not found.")

    def view_all_students(self):
        if not self.students:
            print("No student records yet.")
            return
        print("\nList of all students:")
        for s in self.students:
            print(s)

    def calculate_average(self):
        if not self.students:
            print("No student records to calculate average.")
            return
        grades = []
        for s in self.students:
            try:
                grades.append(float(s.grade))
            except ValueError:
                continue
        if grades:
            avg = sum(grades) / len(grades)
            print(f"Average Grade: {avg:.2f}")
        else:
            print("No numeric grades found for calculation.")

def main():
    gm = GradesManager()
    while True:
        print("\n--- Student Grades Management ---")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Update Student Grade")
        print("4. View All Students")
        print("5. Calculate Average Grade")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            roll_no = input("Enter Roll Number: ")
            name = input("Enter Student Name: ")
            course = input("Enter Course: ")
            grade = input("Enter Grade: ")
            gm.add_student(roll_no, name, course, grade)
        elif choice == '2':
            keyword = input("Enter student name or roll number to search: ")
            gm.search_student(keyword)
        elif choice == '3':
            roll_no = input("Enter Roll Number to update: ")
            new_grade = input("Enter new Grade: ")
            gm.update_grade(roll_no, new_grade)
        elif choice == '4':
            gm.view_all_students()
        elif choice == '5':
            gm.calculate_average()
        elif choice == '6':
            print("Exiting Student Grades Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
