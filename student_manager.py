import csv

class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average_grade(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

class StudentManager:
    def __init__(self):
        self.students = []
        self.file = "students.csv"

    def add_student(self, student):
        self.students.append(student)
        print(f"Student '{student.name}' has been added successfully.")

    def remove_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                print(f"Student '{student.name}' has been removed successfully.")
                return True
        print("No student found with the provided ID.")
        return False

    def save_to_file(self):
        with open(self.file, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["student_id", "name", "grades"])
            writer.writeheader()
            for student in self.students:
                grades_str = ",".join(map(str, student.grades))
                writer.writerow({
                    "student_id": student.student_id,
                    "name": student.name,
                    "grades": grades_str
                })
        print("All student data has been saved to file.")

def main():
    manager = StudentManager()

    while True:
        print("\n--- Student Management ---")
        print("1. Add Student")
        print("2. Add Grade")
        print("3. Show Student Average Grade")
        print("4. Remove Student")
        print("5. Save to File")
        print("6. Exit")

        choice = input("Please enter your choice (1-6): ")

        if choice == '1':
            student_id = int(input("Enter Student ID: "))
            name = input("Enter Student Name: ")
            student = Student(student_id, name)
            manager.add_student(student)

        elif choice == '2':
            student_id = int(input("Enter Student ID to add grade: "))
            for student in manager.students:
                if student.student_id == student_id:
                    grade = float(input("Enter grade: "))
                    student.add_grade(grade)
                    print(f"Grade {grade} added successfully for {student.name}.")
                    break
            else:
                print("No student found with that ID.")

        elif choice == '3':
            student_id = int(input("Enter Student ID to calculate average grade: "))
            for student in manager.students:
                if student.student_id == student_id:
                    avg = student.average_grade()
                    print(f"Average grade for '{student.name}' is: {avg:.2f}")
                    break
            else:
                print("No student found with that ID.")

        elif choice == '4':
            student_id = int(input("Enter Student ID to remove: "))
            manager.remove_student(student_id)

        elif choice == '5':
            manager.save_to_file()

        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
