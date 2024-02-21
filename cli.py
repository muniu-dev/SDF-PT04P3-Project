from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Student, Teacher, Class

# Database connection
DATABASE_URL = 'mysql+mysqlconnector://root:12345@localhost/school'
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def main():
    print("Welcome to School Management System!")
    while True:
        print_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            student_management()
        elif choice == '2':
            teacher_management()
        elif choice == '3':
            class_management()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

def print_menu():
    print("1. Student Management")
    print("2. Teacher Management")
    print("3. Class Management")
    print("4. Exit")

def student_management():
    print("\nStudent Management:")
    while True:
        print_student_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            edit_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def print_student_menu():
    print("1. Add Student")
    print("2. View Students")
    print("3. Edit Student")
    print("4. Delete Student")
    print("5. Back")

def add_student():
    name = input("Enter student name: ")
    grade = input("Enter student grade: ")
    student = Student(name=name, grade=grade)
    session.add(student)
    session.commit()
    print("Student added successfully!")

def view_students():
    students = session.query(Student).all()
    print("\nList of Students:")
    for student in students:
        print(f"ID: {student.id}, Name: {student.name}, Grade: {student.grade}")

def edit_student():
    student_id = input("Enter student ID to edit: ")
    student = session.query(Student).filter_by(id=student_id).first()
    if student:
        new_name = input("Enter new name (leave empty to keep current): ")
        new_grade = input("Enter new grade (leave empty to keep current): ")
        if new_name:
            student.name = new_name
        if new_grade:
            student.grade = new_grade
        session.commit()
        print("Student details updated successfully!")
    else:
        print("Student not found.")

def delete_student():
    student_id = input("Enter student ID to delete: ")
    student = session.query(Student).filter_by(id=student_id).first()
    if student:
        session.delete(student)
        session.commit()
        print("Student deleted successfully!")
    else:
        print("Student not found.")

def teacher_management():
    print("\nTeacher Management:")
    while True:
        print_teacher_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_teacher()
        elif choice == '2':
            view_teachers()
        elif choice == '3':
            edit_teacher()
        elif choice == '4':
            delete_teacher()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def print_teacher_menu():
    print("1. Add Teacher")
    print("2. View Teachers")
    print("3. Edit Teacher")
    print("4. Delete Teacher")
    print("5. Back")

def add_teacher():
    name = input("Enter teacher name: ")
    subject = input("Enter subject taught: ")
    teacher = Teacher(name=name, subject=subject)
    session.add(teacher)
    session.commit()
    print("Teacher added successfully!")

def view_teachers():
    teachers = session.query(Teacher).all()
    print("\nList of Teachers:")
    for teacher in teachers:
        print(f"ID: {teacher.id}, Name: {teacher.name}, Subject: {teacher.subject}")

def edit_teacher():
    teacher_id = input("Enter teacher ID to edit: ")
    teacher = session.query(Teacher).filter_by(id=teacher_id).first()
    if teacher:
        new_name = input("Enter new name (leave empty to keep current): ")
        new_subject = input("Enter new subject (leave empty to keep current): ")
        if new_name:
            teacher.name = new_name
        if new_subject:
            teacher.subject = new_subject
        session.commit()
        print("Teacher details updated successfully!")
    else:
        print("Teacher not found.")

def delete_teacher():
    teacher_id = input("Enter teacher ID to delete: ")
    teacher = session.query(Teacher).filter_by(id=teacher_id).first()
    if teacher:
        session.delete(teacher)
        session.commit()
        print("Teacher deleted successfully!")
    else:
        print("Teacher not found.")

def class_management():
    print("\nClass Management:")
    while True:
        print_class_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_class()
        elif choice == '2':
            view_classes()
        elif choice == '3':
            edit_class()
        elif choice == '4':
            delete_class()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def print_class_menu():
    print("1. Add Class")
    print("2. View Classes")
    print("3. Edit Class")
    print("4. Delete Class")
    print("5. Back")

def add_class():
    name = input("Enter class name: ")
    teacher_id = input("Enter teacher ID for this class: ")
    class_obj = Class(name=name, teacher_id=teacher_id)
    session.add(class_obj)
    session.commit()
    print("Class added successfully!")

def view_classes():
    classes = session.query(Class).all()
    print("\nList of Classes:")
    for class_obj in classes:
        print(f"ID: {class_obj.id}, Name: {class_obj.name}, Teacher ID: {class_obj.teacher_id}")

def edit_class():
    class_id = input("Enter class ID to edit: ")
    class_obj = session.query(Class).filter_by(id=class_id).first()
    if class_obj:
        new_name = input("Enter new name (leave empty to keep current): ")
        new_teacher_id = input("Enter new teacher ID (leave empty to keep current): ")
        if new_name:
            class_obj.name = new_name
        if new_teacher_id:
            class_obj.teacher_id = new_teacher_id
        session.commit()
        print("Class details updated successfully!")
    else:
        print("Class not found.")

def delete_class():
    class_id = input("Enter class ID to delete: ")
    class_obj = session.query(Class).filter_by(id=class_id).first()
    if class_obj:
        session.delete(class_obj)
        session.commit()
        print("Class deleted successfully!")
    else:
        print("Class not found.")

if __name__ == "__main__":
    main()
