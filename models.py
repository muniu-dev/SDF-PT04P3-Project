# models.py

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    grade = Column(String)
    grades = relationship("Grade", back_populates="student")

    def __repr__(self):
        return f"<Student(name='{self.name}', grade='{self.grade}')>"

class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    subject = Column(String)
    classes = relationship("Class", back_populates="teacher")

    def __repr__(self):
        return f"<Teacher(name='{self.name}', subject='{self.subject}')>"

class Class(Base):
    __tablename__ = 'classes'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))

    teacher = relationship("Teacher", back_populates="classes")
    students = relationship("Student", back_populates="grades")

    def __repr__(self):
        return f"<Class(name='{self.name}')>"

class Grade(Base):
    __tablename__ = 'grades'
    id = Column(Integer, primary_key=True)
    grade = Column(Integer)
    student_id = Column(Integer, ForeignKey('students.id'))

    student = relationship("Student", back_populates="grades")

    def __repr__(self):
        return f"<Grade(grade='{self.grade}')>"
